import uuid
from typing import Generic, TypeVar

import gel
from gel.models.pydantic import GelModel

from app.models.utils import CursorPagination

T = TypeVar("T", bound=GelModel)


class BaseService(Generic[T]):
    def __init__(self, client: gel.AsyncIOClient, model_class: type[T]):
        self.client = client
        self.model_class = model_class

    async def create(self, obj: T) -> T:
        await self.client.save(obj)
        return obj

    async def update(self, obj: T) -> T:
        if obj.id is None:
            raise ValueError(
                f"Cannot update a {self.model_class.__name__} object without an ID"
            )
        await self.client.save(obj)
        return obj

    async def get_by_id(self, obj_id: uuid.UUID) -> T | None:
        return await self.client.query_single(
            self.model_class.select().filter(id=obj_id)
        )

    async def delete(self, obj_id: uuid.UUID) -> None:
        await self.client.query_single(self.model_class.filter(id=obj_id).delete())

    async def list_all(
        self, cursor_pagination: CursorPagination
    ) -> tuple[list[T], bool]:
        # Common pagination logic
        has_more: bool = await self.client.query_required_single(
            f"""
            with
              starting_after := <uuid>$starting_after,
              NEXT_OBJ := (select {self.model_class.__name__} filter .id > starting_after limit 1),
            select exists NEXT_OBJ;
            """,
            starting_after=cursor_pagination.starting_after,
        )
        result = await self.client.query(
            self.model_class.select()
            .filter(
                lambda obj: (
                    obj.id > cursor_pagination.starting_after
                    if cursor_pagination.starting_after is not None
                    else True
                ),
                lambda obj: (
                    obj.id < cursor_pagination.ending_before
                    if cursor_pagination.ending_before is not None
                    else True
                ),
            )
            .limit(cursor_pagination.limit)
        )
        return result, has_more
