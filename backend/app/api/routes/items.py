import uuid

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from app.api.deps import CurrentUser
from app.main import g
from app.models.data import Item
from app.models.utils import Collection, LimitOffsetPaginationDep
from app.services.item import ItemServiceDep

router = APIRouter(
    prefix="/items", tags=["items"], dependencies=[g.auth.maybe_auth_token]
)


@router.get("/")
async def read_items(
    limit_offset_pagination: LimitOffsetPaginationDep,
    item_service: ItemServiceDep,
) -> Collection[Item]:
    """
    Retrieve items.
    """

    return await item_service.list_all(limit_offset_pagination)


@router.get("/{id}")
async def read_item(
    item_service: ItemServiceDep,
    id: uuid.UUID,
) -> Item | None:
    """
    Get item by ID.
    """

    item = await item_service.get_by_id(id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return item


class ItemCreate(BaseModel):
    title: str | None = None
    description: str | None = None


@router.post("/")
async def create_item(
    *, item_in: ItemCreate, item_service: ItemServiceDep, current_user: CurrentUser
) -> Item:
    """
    Create new item.
    """

    new_item = Item(
        **item_in.model_dump(),
        owner=current_user,
    )
    item = await item_service.create(new_item)
    return item


class ItemUpdate(Item.__variants__.Base):
    pass


@router.put("/{id}")
async def update_item(
    *,
    id: uuid.UUID,
    item_in: ItemUpdate,
    item_service: ItemServiceDep,
) -> Item:
    """
    Update an item.
    """

    existing_item = await item_service.get_by_id(id)
    if existing_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    item = existing_item.model_copy(
        update=item_in.model_dump(exclude_unset=True, exclude={"id"})
    )
    item = await item_service.update(item)
    return item


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(
    item_service: ItemServiceDep,
    id: uuid.UUID,
) -> None:
    """
    Delete an item.
    """

    await item_service.delete(id)
