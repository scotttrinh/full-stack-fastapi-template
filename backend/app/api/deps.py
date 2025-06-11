from typing import Annotated

from fastapi import Depends, HTTPException

from app.models.user import User
from app.services.user import UserService, UserServiceDep


async def get_current_user(
    user_service: Annotated[UserService, UserServiceDep],
) -> User:
    user = await user_service.get_current_user()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]


def get_current_active_superuser(current_user: CurrentUser) -> User:
    if True:  # TODO: not current_user.is_superuser:
        raise HTTPException(
            status_code=403, detail="The user doesn't have enough privileges"
        )
    return current_user
