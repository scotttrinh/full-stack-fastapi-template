#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from . import std
from .. import std as ___std_1__

from gel.models.pydantic import (
    Cardinality,
    DEFAULT_VALUE,
    DefaultValue,
    Direction,
    EmptyDirection,
    ExprCompatible,
    GelModelMeta,
    GelPointerReflection,
    LazyClassProperty,
    OptionalProperty,
    PathAlias,
    PointerKind,
    PyConstType,
    SchemaPath,
    Unspecified,
    UnspecifiedType
)

import builtins as ___builtins_2__
import builtins as ___builtins__
import builtins as ___builtins_1__
from builtins import tuple, type
from collections.abc import Callable
from typing import Literal, TYPE_CHECKING, TypeVar
from typing_extensions import Self, TypeAliasType
from uuid import UUID

if TYPE_CHECKING:

    from .. import default, schema, std as ___std__
    from ..ext import auth as ___ext_auth__

    from builtins import dict, str




#
# type default::Item
#
class __Item_typeof_base__(std.__Object_typeof_base__):
    class __gel_reflection__(std.__Object_typeof_base__.__gel_reflection__):
        id = UUID(int=90631249492997644026455057663680268687)
        name = SchemaPath('default', 'Item')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'description': GelPointerReflection(
                    name='description',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'title': GelPointerReflection(
                    name='title',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'owner': GelPointerReflection(
                    name='owner',
                    type=SchemaPath('default', 'User'),
                    typexpr='default::User',
                    kind=PointerKind('Link'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | std.__Object_typeof_base__.__gel_reflection__.pointers
            )

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

class __Item_typeof__(std.__Object_typeof__, __Item_typeof_base__):
    class __typeof__(std.__Object_typeof__.__typeof__):
        description = TypeAliasType('description', 'OptionalProperty[std.str, builtins.str]')
        title = TypeAliasType('title', 'OptionalProperty[std.str, builtins.str]')
        owner = TypeAliasType('owner', 'User')


class __Item_typeof_partial__(
    std.__Object_typeof_partial__,
    __Item_typeof_base__,
):
    class __typeof__(std.__Object_typeof_partial__.__typeof__):
        description = TypeAliasType('description', 'OptionalProperty[std.str, builtins.str]')
        title = TypeAliasType('title', 'OptionalProperty[std.str, builtins.str]')
        owner = TypeAliasType('owner', 'User | User.__variants__.Partial')


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
            description: builtins.str | None = None,
            title: builtins.str | None = None,
            owner: User | None = None,
        ) -> None:
            """Create a new default::Item instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            description: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            title: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            owner: type[default.User] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update default::Item instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            description: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            title: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            owner: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[default.User] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch default::Item instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            description: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            title: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            owner: type[default.User] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch default::Item instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            description: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            title: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(std.Object.__variants__):
        class Base(
            __Item_typeof__,
            std.Object.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    description: builtins.str | None = None,
                    title: builtins.str | None = None,
                    owner: User | None = None,
                ) -> None:
                    """Create a new default::Item instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    description: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    title: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    owner: type[default.User] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update default::Item instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    description: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    title: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    owner: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[default.User] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch default::Item instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    description: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    title: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    owner: type[default.User] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch default::Item instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    description: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    title: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            std.Object.__variants__.Required,
            __gel_variant__="Required",
        ):
            owner: ___default__.User

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __Item_typeof_partial__,
            Base,
            std.Object.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            std.Object.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            description: OptionalProperty[___std_1__.str, builtins.str]
            title: OptionalProperty[___std_1__.str, builtins.str]
            owner: ___default__.User | ___default__.User.__variants__.Partial


        Any = TypeVar("Any", bound="Item | Base | Required | Partial")
    class __links__(std.Object.__links__):
        pass
    class __links_partial__(std.Object.__links_partial__):
        pass

if not TYPE_CHECKING:
    Item.__variants__.Base = Item



#
# type default::User
#
class __User_typeof_base__(std.__Object_typeof_base__):
    class __gel_reflection__(std.__Object_typeof_base__.__gel_reflection__):
        id = UUID(int=90621163747909578176093817614167176215)
        name = SchemaPath('default', 'User')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'email': GelPointerReflection(
                    name='email',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'full_name': GelPointerReflection(
                    name='full_name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'is_superuser': GelPointerReflection(
                    name='is_superuser',
                    type=SchemaPath('std', 'bool'),
                    typexpr='std::bool',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'identity': GelPointerReflection(
                    name='identity',
                    type=SchemaPath('ext', 'auth', 'Identity'),
                    typexpr='ext::auth::Identity',
                    kind=PointerKind('Link'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | std.__Object_typeof_base__.__gel_reflection__.pointers
            )

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

class __User_typeof__(std.__Object_typeof__, __User_typeof_base__):
    class __typeof__(std.__Object_typeof__.__typeof__):
        email = TypeAliasType('email', 'OptionalProperty[std.str, builtins.str]')
        full_name = TypeAliasType('full_name', 'OptionalProperty[std.str, builtins.str]')
        is_superuser = TypeAliasType('is_superuser', 'std.bool')
        identity = TypeAliasType('identity', 'ext_auth.Identity')


class __User_typeof_partial__(
    std.__Object_typeof_partial__,
    __User_typeof_base__,
):
    class __typeof__(std.__Object_typeof_partial__.__typeof__):
        email = TypeAliasType('email', 'OptionalProperty[std.str, builtins.str]')
        full_name = TypeAliasType('full_name', 'OptionalProperty[std.str, builtins.str]')
        is_superuser = TypeAliasType('is_superuser', 'OptionalProperty[std.bool, bool]')
        identity = TypeAliasType('identity', 'ext_auth.Identity | ext_auth.Identity.__variants__.Partial')


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
            email: builtins.str | None = None,
            full_name: builtins.str | None = None,
            is_superuser: bool | DefaultValue = DEFAULT_VALUE,
            identity: ext_auth.Identity | None = None,
        ) -> None:
            """Create a new default::User instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            full_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            is_superuser: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            identity: type[___ext_auth__.Identity] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update default::User instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            email: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            full_name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            is_superuser: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            identity: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___ext_auth__.Identity] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch default::User instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            full_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            is_superuser: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
            identity: type[___ext_auth__.Identity] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch default::User instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
            id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            email: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            full_name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
            is_superuser: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(std.Object.__variants__):
        class Base(
            __User_typeof__,
            std.Object.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    email: builtins.str | None = None,
                    full_name: builtins.str | None = None,
                    is_superuser: bool | DefaultValue = DEFAULT_VALUE,
                    identity: ext_auth.Identity | None = None,
                ) -> None:
                    """Create a new default::User instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    full_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    is_superuser: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    identity: type[___ext_auth__.Identity] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update default::User instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    email: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    full_name: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    is_superuser: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    identity: ___builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___ext_auth__.Identity] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch default::User instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    full_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    is_superuser: ___builtins_2__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                    identity: type[___ext_auth__.Identity] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch default::User instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | ___builtins__.str, EmptyDirection | ___builtins__.str],
                    id: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    email: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    full_name: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                    is_superuser: Direction | ___builtins__.str | ___builtins__.str | ___builtins__.bool | tuple[Direction | ___builtins__.str, EmptyDirection | ___builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            std.Object.__variants__.Required,
            __gel_variant__="Required",
        ):
            is_superuser: ___std_1__.bool
            identity: ___ext_auth_1__.Identity

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __User_typeof_partial__,
            Base,
            std.Object.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            std.Object.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            email: OptionalProperty[___std_1__.str, builtins.str]
            full_name: OptionalProperty[___std_1__.str, builtins.str]
            is_superuser: OptionalProperty[___std_1__.bool, bool]
            identity: ___ext_auth_1__.Identity | ___ext_auth_1__.Identity.__variants__.Partial


        Any = TypeVar("Any", bound="User | Base | Required | Partial")
    class __links__(std.Object.__links__):
        pass
    class __links_partial__(std.Object.__links_partial__):
        pass

if not TYPE_CHECKING:
    User.__variants__.Base = User



from .. import default as ___default__  # noqa: E402 F403
from ..ext import auth as ___ext_auth_1__  # noqa: E402 F403
from .ext import auth as ext_auth  # noqa: E402 F403

import builtins as builtins  # noqa: E402 F403
from builtins import bool  # noqa: E402 F403
