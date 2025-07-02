import uuid
from typing import Generic, TypeVar

import gel
from gel.models.pydantic import GelModel

from app.models.utils import Collection, LimitOffsetPagination, QueryModel

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
            self.model_class.filter(id=obj_id)
        )


    async def delete(self, obj_id: uuid.UUID) -> None:
        await self.client.query_single(self.model_class.filter(id=obj_id).delete())

    async def list_all(
        self, limit_offset_pagination: LimitOffsetPagination
    ) -> Collection[T]:
        # Common pagination logic
        count: int = await self.client.query_required_single(
            f"""
            select count((select {self.model_class.__name__}))
            """
        )
        q = QueryModel(
            self.model_class,
            f"""
            select {self.model_class.__name__} {{ ** }}
            offset <int64>$offset
            limit <int64>$limit
            """,
        )
        result = await self.client.query(
            q,  # type: ignore
            offset=limit_offset_pagination.offset,
            limit=limit_offset_pagination.limit,
        )
        return Collection(data=result, count=count)
