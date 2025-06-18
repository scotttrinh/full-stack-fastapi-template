import dataclasses
import uuid
from typing import Annotated, Generic, TypeVar

from fastapi import Query
from pydantic import BaseModel

T = TypeVar("T")


class Collection(BaseModel, Generic[T]):
    data: list[T]
    count: int


class CursorPagination(BaseModel):
    starting_after: uuid.UUID | None = None
    ending_before: uuid.UUID | None = None
    limit: int = 100


CursorPaginationDep = Annotated[CursorPagination, Query()]


class LimitOffsetPagination(BaseModel):
    limit: int = 100
    offset: int = 0


LimitOffsetPaginationDep = Annotated[LimitOffsetPagination, Query()]


@dataclasses.dataclass
class QueryModel:
    type: type
    query: str

    def __edgeql__(self):
        return (self.type, self.query)
