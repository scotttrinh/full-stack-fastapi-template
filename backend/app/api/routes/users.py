import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import (
    CurrentUser,
    get_current_active_superuser,
)
from app.main import g
from app.models.data import User
from app.models.utils import Collection, LimitOffsetPaginationDep
from app.services.user import UserServiceDep

router = APIRouter(prefix="/users", tags=["users"], dependencies=[g.auth.maybe_auth_token])


@router.get("/", dependencies=[Depends(get_current_active_superuser)])
async def read_users(
    user_service: UserServiceDep, limit_offset_pagination: LimitOffsetPaginationDep
) -> Collection[User]:
    """
    Retrieve users.
    """

    return await user_service.list_all(limit_offset_pagination)


@router.post(
    "/",
    dependencies=[Depends(get_current_active_superuser)],
)
async def create_user(*, user_service: UserServiceDep, user_in: User):
    """
    Create new user.
    """

    user = await user_service.create(user_in)
    return user


class UserUpdate(User.__variants__.Base):
    pass


@router.patch("/me", dependencies=[g.auth.maybe_auth_token])
async def update_user_me(
    *,
    user_service: UserServiceDep,
    user_in: UserUpdate,
    current_user: CurrentUser,
) -> User:
    """
    Update own user.
    """

    current_user = current_user.model_copy(
        update=user_in.model_dump(exclude_unset=True, exclude={"id"})
    )
    await user_service.update(current_user)
    return current_user


@router.get("/me")
def read_user_me(current_user: CurrentUser) -> User:
    """
    Get current user.
    """
    return current_user


@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_me(
    user_service: UserServiceDep, current_user: CurrentUser
) -> None:
    """
    Delete own user.
    """
    if current_user.is_superuser:
        raise HTTPException(
            status_code=403, detail="Super users are not allowed to delete themselves"
        )
    await user_service.delete(current_user.id)


@router.get("/{user_id}")
async def read_user_by_id(
    user_service: UserServiceDep, user_id: uuid.UUID, current_user: CurrentUser
) -> Any:
    """
    Get a specific user by id.
    """
    if user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="The user doesn't have enough privileges",
        )

    user = await user_service.get_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.patch(
    "/{user_id}",
    dependencies=[Depends(get_current_active_superuser)],
    response_model=User,
)
async def update_user(
    *,
    user_service: UserServiceDep,
    user_id: uuid.UUID,
    user_in: User.__variants__.Base,
) -> Any:
    """
    Update a user.
    """

    user = await user_service.get_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this id does not exist in the system",
        )

    user = user.model_copy(
        update=user_in.model_dump(exclude_unset=True, exclude={"id"})
    )
    await user_service.update(user)
    return user


@router.delete("/{user_id}", dependencies=[Depends(get_current_active_superuser)])
async def delete_user(
    user_service: UserServiceDep, current_user: CurrentUser, user_id: uuid.UUID
) -> Any:
    """
    Delete a user.
    """
    if user_id == current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Super users are not allowed to delete themselves",
        )

    await user_service.delete(user_id)
