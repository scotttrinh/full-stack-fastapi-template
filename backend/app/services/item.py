import uuid

import gel

from app.models.data import default


class ItemService:
    def __init__(self, client: gel.AsyncIOClient):
        self.client = client

    async def create(self, item_create: default.Item) -> default.Item:
        return await self.client.query_required_single()

    async def update(self, item_update: default.Item) -> default.Item:
        return await self.client.query_required_single()

    async def get_by_id(self, item_id: uuid.UUID) -> default.Item:
        return await self.client.query_required_single()

    async def delete(self, item_id: uuid.UUID) -> None:
        return await self.client.query_required_single()