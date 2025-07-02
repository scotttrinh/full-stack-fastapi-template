import dataclasses
from typing import Annotated, Type

import gel
import gel.fastapi
from fastapi import Depends

from app.models.data import User
from app.models.utils import QueryModel
from app.services.base import BaseService


class UserService(BaseService[User]):
    def __init__(self, client: gel.AsyncIOClient):
        super().__init__(client, User)

    async def get_by_email(self, email: str) -> User | None:
        return await self.client.query_single(User.select("*").filter(email=email))

    async def get_current_user(self) -> User | None:
        try:
            auth_token = await self.client.query_single(
                "select global ext::auth::client_token"
            )
            print("auth_token: ", auth_token)
            return await self.client.query_single(
                QueryModel(User, """select (global current_user) { ** }""")
            )
        except gel.errors.QueryAssertionError as e:
            if "JWT signature mismatch" in str(e):
                print("JWT signature mismatch error from the server: ", e)
                return None
            raise e


def make_user_service(
    client: gel.fastapi.Client,
) -> UserService:
    return UserService(client)


UserServiceDep = Annotated[UserService, Depends(make_user_service)]
