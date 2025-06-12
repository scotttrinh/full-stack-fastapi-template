import uuid

from fastapi import APIRouter, HTTPException, status

from app.models.data import Item
from app.models.utils import Collection, CursorPaginationDep
from app.services.item import ItemServiceDep

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
async def read_items(
    cursor_pagination: CursorPaginationDep,
    item_service: ItemServiceDep,
) -> Collection[Item]:
    """
    Retrieve items.
    """

    items, has_more = await item_service.list_all(cursor_pagination)
    return Collection(data=items, has_more=has_more)


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


@router.post("/")
async def create_item(*, item_in: Item, item_service: ItemServiceDep) -> Item:
    """
    Create new item.
    """

    item = await item_service.create(item_in)
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
