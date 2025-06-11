#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from . import std

from gel.models.pydantic import (
    Direction,
    EmptyDirection,
    ExprCompatible,
    LazyClassProperty,
    OptionalLink,
    OptionalProperty,
    PathAlias,
    PyConstType,
    SchemaPath,
    Unspecified,
    UnspecifiedType
)

import builtins as builtins
import builtins as __builtins__
from builtins import tuple, type
from collections.abc import Callable
from typing import TYPE_CHECKING, TypeVar
from typing_extensions import Self, TypeAliasType
from uuid import UUID

if TYPE_CHECKING:

    from .. import default, schema, std as __std__
    from ..ext import auth as __ext_auth__




#
# type default::Item
#
class __Item_typeof__(std.__Object_typeof__):
    class __gel_reflection__(std.__Object_typeof__.__gel_reflection__):
        id = UUID(int=90631249492997644026455057663680268687)
        name = SchemaPath('default', 'Item')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ..schema import ObjectType
            return ObjectType(
                id=UUID(int=90631249492997644026455057663680268687),
                name='default::Item',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(std.__Object_typeof__.__typeof__):
        description = TypeAliasType('description', 'OptionalProperty[std.str, str]')
        title = TypeAliasType('title', 'OptionalProperty[std.str, str]')
        owner = TypeAliasType('owner', 'OptionalLink[User]')


class Item(
    __Item_typeof__,
    std.Object,
    __gel_type_id__=UUID(int=90631249492997644026455057663680268687),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            description: str | None = None,
            title: str | None = None,
            owner: User | None = None,
        ) -> None:
            """Create a new default::Item instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            description: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            title: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            owner: type[default.User] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update default::Item instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            description: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            title: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            owner: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[default.User] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch default::Item instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            description: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            title: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            owner: type[default.User] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch default::Item instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            description: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            title: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(std.Object.__variants__):
        class Base(__Item_typeof__, std.Object.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    description: str | None = None,
                    title: str | None = None,
                    owner: User | None = None,
                ) -> None:
                    """Create a new default::Item instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    description: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    title: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    owner: type[default.User] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update default::Item instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    description: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    title: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    owner: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[default.User] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch default::Item instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    description: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    title: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    owner: type[default.User] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch default::Item instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    description: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    title: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Item | Base")
    class __links__(std.Object.__links__):
        pass

if not TYPE_CHECKING:
    Item.__variants__.Base = Item



#
# type default::User
#
class __User_typeof__(std.__Object_typeof__):
    class __gel_reflection__(std.__Object_typeof__.__gel_reflection__):
        id = UUID(int=90621163747909578176093817614167176215)
        name = SchemaPath('default', 'User')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ..schema import ObjectType
            return ObjectType(
                id=UUID(int=90621163747909578176093817614167176215),
                name='default::User',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(std.__Object_typeof__.__typeof__):
        email = TypeAliasType('email', 'OptionalProperty[std.str, str]')
        full_name = TypeAliasType('full_name', 'OptionalProperty[std.str, str]')
        identity = TypeAliasType('identity', 'OptionalLink[ext_auth.Identity]')


class User(
    __User_typeof__,
    std.Object,
    __gel_type_id__=UUID(int=90621163747909578176093817614167176215),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            email: str | None = None,
            full_name: str | None = None,
            identity: ext_auth.Identity | None = None,
        ) -> None:
            """Create a new default::User instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            full_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            identity: type[__ext_auth__.Identity] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update default::User instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            full_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__ext_auth__.Identity] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch default::User instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            full_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            identity: type[__ext_auth__.Identity] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch default::User instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            email: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            full_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(std.Object.__variants__):
        class Base(__User_typeof__, std.Object.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    email: str | None = None,
                    full_name: str | None = None,
                    identity: ext_auth.Identity | None = None,
                ) -> None:
                    """Create a new default::User instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    full_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    identity: type[__ext_auth__.Identity] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update default::User instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    full_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__ext_auth__.Identity] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch default::User instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    full_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    identity: type[__ext_auth__.Identity] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch default::User instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    email: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    full_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="User | Base")
    class __links__(std.Object.__links__):
        pass

if not TYPE_CHECKING:
    User.__variants__.Base = User



from .ext import auth as ext_auth  # noqa: E402 F403

from builtins import str  # noqa: E402 F403
