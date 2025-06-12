from typing import Annotated

import gel
import gel.fastapi
from fastapi import Depends

from app.models.data.default import Item
from app.services.base import BaseService


class ItemService(BaseService[Item]):
    def __init__(self, client: gel.AsyncIOClient):
        super().__init__(client, Item)


def make_item_service(client: gel.fastapi.Client) -> ItemService:
    return ItemService(client)


ItemServiceDep = Annotated[ItemService, Depends(make_item_service)]
