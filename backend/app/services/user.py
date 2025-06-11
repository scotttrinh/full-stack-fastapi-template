import uuid
from typing import Annotated

import gel
import gel.fastapi
from fastapi import Depends

from app.main import gel_auth
from app.models.data import User
from app.models.data.std import uuid


class UserService:
    def __init__(self, client: gel.AsyncIOClient):
        self.client = client

    async def create(self, user_create: User) -> User:
        await self.client.save(user_create)
        return user_create

    async def update(self, user_update: User) -> User:
        if user_update.id is None:
            raise ValueError("Cannot update a User object without an ID")

        await self.client.save(user_update)
        return user_update

    async def list_all(self, skip: int = 0, limit: int = 100) -> list[User]:
        return await self.client.query(
            User.select().offset(skip).limit(limit)
        )

    async def get_by_id(self, user_id: uuid) -> User | None:
        return await self.client.query_single(
            User.select().filter(lambda user: user.id == user_id)
        )

    async def get_by_email(self, email: str) -> User | None:
        return await self.client.query_single(
            User.select().filter(lambda user: user.email == email)
        )

    async def delete(self, user_id: uuid) -> None:
        await self.client.query_single(
            User.filter(lambda user: user.id == user_id).delete()
        )

    async def get_current_user(self) -> User | None:
        result = await self.client.query_single(
            """
            select global current_user {
                id,
                full_name,
                email,
                is_superuser,
                identity: {
                    id,
                }
            }
            """
        )
        if result is None:
            return None

        return User(**result)


def make_user_service(
    client: Annotated[gel.fastapi.Client, gel_auth.maybe_auth_token],
) -> UserService:
    return UserService(client)


UserServiceDep = Annotated[UserService, Depends(make_user_service)]
