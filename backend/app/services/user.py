from typing import Annotated

import gel
import gel.fastapi
from fastapi import Depends

from app.models.data import User
from app.services.base import BaseService


class UserService(BaseService[User]):
    def __init__(self, client: gel.AsyncIOClient):
        super().__init__(client, User)

    async def get_by_email(self, email: str) -> User | None:
        return await self.client.query_single(User.select().filter(email=email))

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
    client: gel.fastapi.Client,
) -> UserService:
    return UserService(client)


UserServiceDep = Annotated[UserService, Depends(make_user_service)]
