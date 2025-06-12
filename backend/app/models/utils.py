import uuid
from typing import Annotated, Generic, TypeVar

from fastapi import Query
from pydantic import BaseModel

T = TypeVar("T")


class Collection(BaseModel, Generic[T]):
    data: list[T]
    has_more: bool


class CursorPagination(BaseModel):
    starting_after: uuid.UUID | None = None
    ending_before: uuid.UUID | None = None
    limit: int = 100


CursorPaginationDep = Annotated[CursorPagination, Query()]
