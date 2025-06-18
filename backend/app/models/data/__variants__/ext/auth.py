#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from .. import cfg, std
from ... import std as ___std_1__

from gel.models.pydantic import (
    AnyEnum,
    Cardinality,
    DEFAULT_VALUE,
    DefaultValue,
    Direction,
    EmptyDirection,
    ExprCompatible,
    GelModelMeta,
    GelPointerReflection,
    LazyClassProperty,
    MultiLink,
    MultiProperty,
    OptionalLink,
    OptionalProperty,
    PathAlias,
    PointerKind,
    PyConstType,
    RequiredMultiLink,
    SchemaPath,
    Unspecified,
    UnspecifiedType
)

import builtins as ___builtins_2__
import builtins as ___builtins_3__
import builtins as builtins
import builtins as ___builtins_1__
import datetime as ___datetime_1__
import datetime as ___datetime__
from builtins import tuple, type
from collections.abc import Callable, Iterable
from typing import Literal, TYPE_CHECKING, TypeVar
from typing_extensions import Self, TypeAliasType
from uuid import UUID

if TYPE_CHECKING:

    from ... import cfg as ___cfg__, schema, std as ___std__
    from ...ext import auth as ext_auth

    from builtins import dict, str


class FlowType(AnyEnum):
    PKCE = 'PKCE'
    Implicit = 'Implicit'


class JWTAlgo(AnyEnum):
    RS256 = 'RS256'
    HS256 = 'HS256'


class WebhookEvent(AnyEnum):
    IdentityCreated = 'IdentityCreated'
    IdentityAuthenticated = 'IdentityAuthenticated'
    EmailFactorCreated = 'EmailFactorCreated'
    EmailVerified = 'EmailVerified'
    EmailVerificationRequested = 'EmailVerificationRequested'
    PasswordResetRequested = 'PasswordResetRequested'
    MagicLinkRequested = 'MagicLinkRequested'




#
# type ext::auth::Auditable
#
class __Auditable_typeof_base__(std.__BaseObject_typeof_base__):
    class __gel_reflection__(
        std.__BaseObject_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=89170665678168121361218419839485559093)
        name = SchemaPath('ext', 'auth', 'Auditable')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'created_at': GelPointerReflection(
                    name='created_at',
                    type=SchemaPath('std', 'datetime'),
                    typexpr='std::datetime',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'modified_at': GelPointerReflection(
                    name='modified_at',
                    type=SchemaPath('std', 'datetime'),
                    typexpr='std::datetime',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | std.__BaseObject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=89170665678168121361218419839485559093),
                name='ext::auth::Auditable',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __Auditable_typeof__(
    std.__BaseObject_typeof__,
    __Auditable_typeof_base__,
):
    class __typeof__(std.__BaseObject_typeof__.__typeof__):
        created_at = TypeAliasType('created_at', 'std.datetime')
        modified_at = TypeAliasType('modified_at', 'std.datetime')


class __Auditable_typeof_partial__(
    std.__BaseObject_typeof_partial__,
    __Auditable_typeof_base__,
):
    class __typeof__(std.__BaseObject_typeof_partial__.__typeof__):
        created_at = TypeAliasType('created_at', 'OptionalProperty[std.datetime, datetime]')
        modified_at = TypeAliasType('modified_at', 'OptionalProperty[std.datetime, datetime]')


class Auditable(
    __Auditable_typeof__,
    std.BaseObject,
    __gel_type_id__=UUID(int=89170665678168121361218419839485559093),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            created_at: datetime | DefaultValue = DEFAULT_VALUE,
            modified_at: datetime,
        ) -> None:
            """Create a new ext::auth::Auditable instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::Auditable instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::Auditable instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::Auditable instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(std.BaseObject.__variants__):
        class Base(
            __Auditable_typeof__,
            std.BaseObject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime | DefaultValue = DEFAULT_VALUE,
                    modified_at: datetime,
                ) -> None:
                    """Create a new ext::auth::Auditable instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::Auditable instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::Auditable instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::Auditable instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            std.BaseObject.__variants__.Required,
            __gel_variant__="Required",
        ):
            created_at: ___std_1__.datetime
            modified_at: ___std_1__.datetime

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __Auditable_typeof_partial__,
            Base,
            std.BaseObject.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            std.BaseObject.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            created_at: OptionalProperty[___std_1__.datetime, datetime]
            modified_at: OptionalProperty[___std_1__.datetime, datetime]


        Any = TypeVar("Any", bound="Auditable | Base | Required | Partial")
    class __links__(std.BaseObject.__links__):
        pass
    class __links_partial__(std.BaseObject.__links_partial__):
        pass

if not TYPE_CHECKING:
    Auditable.__variants__.Base = Auditable



#
# type ext::auth::AuthConfig
#
class __AuthConfig_typeof_base__(cfg.__ExtensionConfig_typeof_base__):
    class __gel_reflection__(
        cfg.__ExtensionConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=82556222219052082021678686650866392229)
        name = SchemaPath('ext', 'auth', 'AuthConfig')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'app_name': GelPointerReflection(
                    name='app_name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'logo_url': GelPointerReflection(
                    name='logo_url',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'dark_logo_url': GelPointerReflection(
                    name='dark_logo_url',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'brand_color': GelPointerReflection(
                    name='brand_color',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'auth_signing_key': GelPointerReflection(
                    name='auth_signing_key',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'token_time_to_live': GelPointerReflection(
                    name='token_time_to_live',
                    type=SchemaPath('std', 'duration'),
                    typexpr='std::duration',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'allowed_redirect_urls': GelPointerReflection(
                    name='allowed_redirect_urls',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('Many'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'providers': GelPointerReflection(
                    name='providers',
                    type=SchemaPath('ext', 'auth', 'ProviderConfig'),
                    typexpr='ext::auth::ProviderConfig',
                    kind=PointerKind('Link'),
                    cardinality=Cardinality('Many'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'ui': GelPointerReflection(
                    name='ui',
                    type=SchemaPath('ext', 'auth', 'UIConfig'),
                    typexpr='ext::auth::UIConfig',
                    kind=PointerKind('Link'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'webhooks': GelPointerReflection(
                    name='webhooks',
                    type=SchemaPath('ext', 'auth', 'WebhookConfig'),
                    typexpr='ext::auth::WebhookConfig',
                    kind=PointerKind('Link'),
                    cardinality=Cardinality('Many'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | cfg.__ExtensionConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=82556222219052082021678686650866392229),
                name='ext::auth::AuthConfig',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __AuthConfig_typeof__(
    cfg.__ExtensionConfig_typeof__,
    __AuthConfig_typeof_base__,
):
    class __typeof__(cfg.__ExtensionConfig_typeof__.__typeof__):
        app_name = TypeAliasType('app_name', 'OptionalProperty[std.str, ___builtins__.str]')
        logo_url = TypeAliasType('logo_url', 'OptionalProperty[std.str, ___builtins__.str]')
        dark_logo_url = TypeAliasType('dark_logo_url', 'OptionalProperty[std.str, ___builtins__.str]')
        brand_color = TypeAliasType('brand_color', 'OptionalProperty[std.str, ___builtins__.str]')
        auth_signing_key = TypeAliasType('auth_signing_key', 'OptionalProperty[std.str, ___builtins__.str]')
        token_time_to_live = TypeAliasType('token_time_to_live', 'OptionalProperty[std.duration, timedelta]')
        allowed_redirect_urls = TypeAliasType('allowed_redirect_urls', 'MultiProperty[std.str, ___builtins__.str]')
        providers = TypeAliasType('providers', 'MultiLink[ProviderConfig]')
        ui = TypeAliasType('ui', 'OptionalLink[UIConfig]')
        webhooks = TypeAliasType('webhooks', 'MultiLink[WebhookConfig]')


class __AuthConfig_typeof_partial__(
    cfg.__ExtensionConfig_typeof_partial__,
    __AuthConfig_typeof_base__,
):
    class __typeof__(cfg.__ExtensionConfig_typeof_partial__.__typeof__):
        app_name = TypeAliasType('app_name', 'OptionalProperty[std.str, ___builtins__.str]')
        logo_url = TypeAliasType('logo_url', 'OptionalProperty[std.str, ___builtins__.str]')
        dark_logo_url = TypeAliasType('dark_logo_url', 'OptionalProperty[std.str, ___builtins__.str]')
        brand_color = TypeAliasType('brand_color', 'OptionalProperty[std.str, ___builtins__.str]')
        auth_signing_key = TypeAliasType('auth_signing_key', 'OptionalProperty[std.str, ___builtins__.str]')
        token_time_to_live = TypeAliasType('token_time_to_live', 'OptionalProperty[std.duration, timedelta]')
        allowed_redirect_urls = TypeAliasType('allowed_redirect_urls', 'MultiProperty[std.str, ___builtins__.str]')
        providers = TypeAliasType('providers', 'MultiLink[ProviderConfig | ProviderConfig.__variants__.Partial]')
        ui = TypeAliasType('ui', 'OptionalLink[UIConfig | UIConfig.__variants__.Partial]')
        webhooks = TypeAliasType('webhooks', 'MultiLink[WebhookConfig | WebhookConfig.__variants__.Partial]')


class AuthConfig(
    __AuthConfig_typeof__,
    cfg.ExtensionConfig,
    __gel_type_id__=UUID(int=82556222219052082021678686650866392229),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            cfg: cfg.AbstractConfig | None = None,
            app_name: ___builtins__.str | None = None,
            logo_url: ___builtins__.str | None = None,
            dark_logo_url: ___builtins__.str | None = None,
            brand_color: ___builtins__.str | None = None,
            auth_signing_key: ___builtins__.str | None = None,
            token_time_to_live: timedelta | None | DefaultValue = DEFAULT_VALUE,
            allowed_redirect_urls: Iterable[___builtins__.str] = [],
            providers: Iterable[ProviderConfig] = [],
            ui: UIConfig | None = None,
            webhooks: Iterable[WebhookConfig] = [],
        ) -> None:
            """Create a new ext::auth::AuthConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            cfg: type[___cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
            app_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            logo_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            dark_logo_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            brand_color: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            auth_signing_key: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            token_time_to_live: ___datetime_1__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            allowed_redirect_urls: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            providers: type[ext_auth.ProviderConfig] | UnspecifiedType = Unspecified,
            ui: type[ext_auth.UIConfig] | UnspecifiedType = Unspecified,
            webhooks: type[ext_auth.WebhookConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::AuthConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            cfg: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
            app_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            logo_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            dark_logo_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            brand_color: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            auth_signing_key: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            token_time_to_live: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            allowed_redirect_urls: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            providers: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.ProviderConfig] | UnspecifiedType = Unspecified,
            ui: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.UIConfig] | UnspecifiedType = Unspecified,
            webhooks: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.WebhookConfig] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::AuthConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            cfg: type[___cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
            app_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            logo_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            dark_logo_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            brand_color: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            auth_signing_key: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            token_time_to_live: ___datetime_1__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
            allowed_redirect_urls: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            providers: type[ext_auth.ProviderConfig] | UnspecifiedType = Unspecified,
            ui: type[ext_auth.UIConfig] | UnspecifiedType = Unspecified,
            webhooks: type[ext_auth.WebhookConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::AuthConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            app_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            logo_url: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            dark_logo_url: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            brand_color: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            auth_signing_key: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            token_time_to_live: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            allowed_redirect_urls: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(cfg.ExtensionConfig.__variants__):
        class Base(
            __AuthConfig_typeof__,
            cfg.ExtensionConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    cfg: cfg.AbstractConfig | None = None,
                    app_name: ___builtins__.str | None = None,
                    logo_url: ___builtins__.str | None = None,
                    dark_logo_url: ___builtins__.str | None = None,
                    brand_color: ___builtins__.str | None = None,
                    auth_signing_key: ___builtins__.str | None = None,
                    token_time_to_live: timedelta | None | DefaultValue = DEFAULT_VALUE,
                    allowed_redirect_urls: Iterable[___builtins__.str] = [],
                    providers: Iterable[ProviderConfig] = [],
                    ui: UIConfig | None = None,
                    webhooks: Iterable[WebhookConfig] = [],
                ) -> None:
                    """Create a new ext::auth::AuthConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    cfg: type[___cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
                    app_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    logo_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    dark_logo_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    brand_color: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    auth_signing_key: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    token_time_to_live: ___datetime_1__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    allowed_redirect_urls: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    providers: type[ext_auth.ProviderConfig] | UnspecifiedType = Unspecified,
                    ui: type[ext_auth.UIConfig] | UnspecifiedType = Unspecified,
                    webhooks: type[ext_auth.WebhookConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::AuthConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    cfg: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
                    app_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    logo_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    dark_logo_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    brand_color: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    auth_signing_key: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    token_time_to_live: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    allowed_redirect_urls: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    providers: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.ProviderConfig] | UnspecifiedType = Unspecified,
                    ui: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.UIConfig] | UnspecifiedType = Unspecified,
                    webhooks: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.WebhookConfig] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::AuthConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    cfg: type[___cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
                    app_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    logo_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    dark_logo_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    brand_color: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    auth_signing_key: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    token_time_to_live: ___datetime_1__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                    allowed_redirect_urls: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    providers: type[ext_auth.ProviderConfig] | UnspecifiedType = Unspecified,
                    ui: type[ext_auth.UIConfig] | UnspecifiedType = Unspecified,
                    webhooks: type[ext_auth.WebhookConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::AuthConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    app_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    logo_url: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    dark_logo_url: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    brand_color: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    auth_signing_key: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    token_time_to_live: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    allowed_redirect_urls: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            cfg.ExtensionConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            pass

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __AuthConfig_typeof_partial__,
            Base,
            cfg.ExtensionConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            cfg.ExtensionConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            app_name: OptionalProperty[___std_1__.str, ___builtins__.str]
            logo_url: OptionalProperty[___std_1__.str, ___builtins__.str]
            dark_logo_url: OptionalProperty[___std_1__.str, ___builtins__.str]
            brand_color: OptionalProperty[___std_1__.str, ___builtins__.str]
            auth_signing_key: OptionalProperty[___std_1__.str, ___builtins__.str]
            token_time_to_live: OptionalProperty[___std_1__.duration, timedelta]
            allowed_redirect_urls: MultiProperty[___std_1__.str, ___builtins__.str]
            providers: MultiLink[___ext_auth__.ProviderConfig | ___ext_auth__.ProviderConfig.__variants__.Partial]
            ui: OptionalLink[___ext_auth__.UIConfig | ___ext_auth__.UIConfig.__variants__.Partial]
            webhooks: MultiLink[___ext_auth__.WebhookConfig | ___ext_auth__.WebhookConfig.__variants__.Partial]


        Any = TypeVar("Any", bound="AuthConfig | Base | Required | Partial")
    class __links__(cfg.ExtensionConfig.__links__):
        pass
    class __links_partial__(cfg.ExtensionConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    AuthConfig.__variants__.Base = AuthConfig



#
# type ext::auth::ProviderConfig
#
class __ProviderConfig_typeof_base__(cfg.__ConfigObject_typeof_base__):
    class __gel_reflection__(
        cfg.__ConfigObject_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=118712192702193322452317409393620995308)
        name = SchemaPath('ext', 'auth', 'ProviderConfig')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'name': GelPointerReflection(
                    name='name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | cfg.__ConfigObject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=118712192702193322452317409393620995308),
                name='ext::auth::ProviderConfig',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __ProviderConfig_typeof__(
    cfg.__ConfigObject_typeof__,
    __ProviderConfig_typeof_base__,
):
    class __typeof__(cfg.__ConfigObject_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')


class __ProviderConfig_typeof_partial__(
    cfg.__ConfigObject_typeof_partial__,
    __ProviderConfig_typeof_base__,
):
    class __typeof__(cfg.__ConfigObject_typeof_partial__.__typeof__):
        name = TypeAliasType('name', 'OptionalProperty[std.str, ___builtins__.str]')


class ProviderConfig(
    __ProviderConfig_typeof__,
    cfg.ConfigObject,
    __gel_type_id__=UUID(int=118712192702193322452317409393620995308),
):
    if TYPE_CHECKING:
        def __init__(self, /, *, name: ___builtins__.str) -> None:
            """Create a new ext::auth::ProviderConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::auth::ProviderConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::ProviderConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::ProviderConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(cfg.ConfigObject.__variants__):
        class Base(
            __ProviderConfig_typeof__,
            cfg.ConfigObject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(self, /, *, name: ___builtins__.str) -> None:
                    """Create a new ext::auth::ProviderConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::auth::ProviderConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::ProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::ProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            cfg.ConfigObject.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: ___std_1__.str

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __ProviderConfig_typeof_partial__,
            Base,
            cfg.ConfigObject.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            cfg.ConfigObject.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            name: OptionalProperty[___std_1__.str, ___builtins__.str]


        Any = TypeVar("Any", bound="ProviderConfig | Base | Required | Partial")
    class __links__(cfg.ConfigObject.__links__):
        pass
    class __links_partial__(cfg.ConfigObject.__links_partial__):
        pass

if not TYPE_CHECKING:
    ProviderConfig.__variants__.Base = ProviderConfig



#
# type ext::auth::UIConfig
#
class __UIConfig_typeof_base__(cfg.__ConfigObject_typeof_base__):
    class __gel_reflection__(
        cfg.__ConfigObject_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=118696617643017006394314869111520389176)
        name = SchemaPath('ext', 'auth', 'UIConfig')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'redirect_to': GelPointerReflection(
                    name='redirect_to',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'redirect_to_on_signup': GelPointerReflection(
                    name='redirect_to_on_signup',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'flow_type': GelPointerReflection(
                    name='flow_type',
                    type=SchemaPath('ext', 'auth', 'FlowType'),
                    typexpr='ext::auth::FlowType',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
                'app_name': GelPointerReflection(
                    name='app_name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'logo_url': GelPointerReflection(
                    name='logo_url',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'dark_logo_url': GelPointerReflection(
                    name='dark_logo_url',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'brand_color': GelPointerReflection(
                    name='brand_color',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | cfg.__ConfigObject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=118696617643017006394314869111520389176),
                name='ext::auth::UIConfig',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __UIConfig_typeof__(
    cfg.__ConfigObject_typeof__,
    __UIConfig_typeof_base__,
):
    class __typeof__(cfg.__ConfigObject_typeof__.__typeof__):
        redirect_to = TypeAliasType('redirect_to', 'std.str')
        redirect_to_on_signup = TypeAliasType('redirect_to_on_signup', 'OptionalProperty[std.str, ___builtins__.str]')
        flow_type = TypeAliasType('flow_type', 'FlowType')
        app_name = TypeAliasType('app_name', 'OptionalProperty[std.str, ___builtins__.str]')
        logo_url = TypeAliasType('logo_url', 'OptionalProperty[std.str, ___builtins__.str]')
        dark_logo_url = TypeAliasType('dark_logo_url', 'OptionalProperty[std.str, ___builtins__.str]')
        brand_color = TypeAliasType('brand_color', 'OptionalProperty[std.str, ___builtins__.str]')


class __UIConfig_typeof_partial__(
    cfg.__ConfigObject_typeof_partial__,
    __UIConfig_typeof_base__,
):
    class __typeof__(cfg.__ConfigObject_typeof_partial__.__typeof__):
        redirect_to = TypeAliasType('redirect_to', 'OptionalProperty[std.str, ___builtins__.str]')
        redirect_to_on_signup = TypeAliasType('redirect_to_on_signup', 'OptionalProperty[std.str, ___builtins__.str]')
        flow_type = TypeAliasType('flow_type', 'OptionalProperty[FlowType, ___builtins_1__.str]')
        app_name = TypeAliasType('app_name', 'OptionalProperty[std.str, ___builtins__.str]')
        logo_url = TypeAliasType('logo_url', 'OptionalProperty[std.str, ___builtins__.str]')
        dark_logo_url = TypeAliasType('dark_logo_url', 'OptionalProperty[std.str, ___builtins__.str]')
        brand_color = TypeAliasType('brand_color', 'OptionalProperty[std.str, ___builtins__.str]')


class UIConfig(
    __UIConfig_typeof__,
    cfg.ConfigObject,
    __gel_type_id__=UUID(int=118696617643017006394314869111520389176),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            redirect_to: ___builtins__.str,
            redirect_to_on_signup: ___builtins__.str | None = None,
            flow_type: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
            app_name: ___builtins__.str | None = None,
            logo_url: ___builtins__.str | None = None,
            dark_logo_url: ___builtins__.str | None = None,
            brand_color: ___builtins__.str | None = None,
        ) -> None:
            """Create a new ext::auth::UIConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            redirect_to: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            redirect_to_on_signup: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            flow_type: type[ext_auth.FlowType] | UnspecifiedType = Unspecified,
            app_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            logo_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            dark_logo_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            brand_color: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::UIConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            redirect_to: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            redirect_to_on_signup: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            flow_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.FlowType] | UnspecifiedType = Unspecified,
            app_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            logo_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            dark_logo_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            brand_color: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::UIConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            redirect_to: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            redirect_to_on_signup: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            flow_type: type[ext_auth.FlowType] | UnspecifiedType = Unspecified,
            app_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            logo_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            dark_logo_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            brand_color: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::UIConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            redirect_to: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            redirect_to_on_signup: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            app_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            logo_url: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            dark_logo_url: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            brand_color: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(cfg.ConfigObject.__variants__):
        class Base(
            __UIConfig_typeof__,
            cfg.ConfigObject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    redirect_to: ___builtins__.str,
                    redirect_to_on_signup: ___builtins__.str | None = None,
                    flow_type: ___builtins_1__.str | DefaultValue = DEFAULT_VALUE,
                    app_name: ___builtins__.str | None = None,
                    logo_url: ___builtins__.str | None = None,
                    dark_logo_url: ___builtins__.str | None = None,
                    brand_color: ___builtins__.str | None = None,
                ) -> None:
                    """Create a new ext::auth::UIConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    redirect_to: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    redirect_to_on_signup: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    flow_type: type[ext_auth.FlowType] | UnspecifiedType = Unspecified,
                    app_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    logo_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    dark_logo_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    brand_color: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::UIConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    redirect_to: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    redirect_to_on_signup: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    flow_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.FlowType] | UnspecifiedType = Unspecified,
                    app_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    logo_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    dark_logo_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    brand_color: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::UIConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    redirect_to: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    redirect_to_on_signup: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    flow_type: type[ext_auth.FlowType] | UnspecifiedType = Unspecified,
                    app_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    logo_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    dark_logo_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    brand_color: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::UIConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    redirect_to: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    redirect_to_on_signup: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    app_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    logo_url: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    dark_logo_url: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    brand_color: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            cfg.ConfigObject.__variants__.Required,
            __gel_variant__="Required",
        ):
            redirect_to: ___std_1__.str
            flow_type: ___ext_auth__.FlowType

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __UIConfig_typeof_partial__,
            Base,
            cfg.ConfigObject.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            cfg.ConfigObject.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            redirect_to: OptionalProperty[___std_1__.str, ___builtins__.str]
            redirect_to_on_signup: OptionalProperty[___std_1__.str, ___builtins__.str]
            flow_type: OptionalProperty[___ext_auth__.FlowType, ___builtins_1__.str]
            app_name: OptionalProperty[___std_1__.str, ___builtins__.str]
            logo_url: OptionalProperty[___std_1__.str, ___builtins__.str]
            dark_logo_url: OptionalProperty[___std_1__.str, ___builtins__.str]
            brand_color: OptionalProperty[___std_1__.str, ___builtins__.str]


        Any = TypeVar("Any", bound="UIConfig | Base | Required | Partial")
    class __links__(cfg.ConfigObject.__links__):
        pass
    class __links_partial__(cfg.ConfigObject.__links_partial__):
        pass

if not TYPE_CHECKING:
    UIConfig.__variants__.Base = UIConfig



#
# type ext::auth::WebhookConfig
#
class __WebhookConfig_typeof_base__(cfg.__ConfigObject_typeof_base__):
    class __gel_reflection__(
        cfg.__ConfigObject_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=307763587024998583260809907117765149570)
        name = SchemaPath('ext', 'auth', 'WebhookConfig')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'url': GelPointerReflection(
                    name='url',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'events': GelPointerReflection(
                    name='events',
                    type=SchemaPath('ext', 'auth', 'WebhookEvent'),
                    typexpr='ext::auth::WebhookEvent',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtLeastOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'signing_secret_key': GelPointerReflection(
                    name='signing_secret_key',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | cfg.__ConfigObject_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=307763587024998583260809907117765149570),
                name='ext::auth::WebhookConfig',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __WebhookConfig_typeof__(
    cfg.__ConfigObject_typeof__,
    __WebhookConfig_typeof_base__,
):
    class __typeof__(cfg.__ConfigObject_typeof__.__typeof__):
        url = TypeAliasType('url', 'std.str')
        events = TypeAliasType('events', 'MultiProperty[WebhookEvent, ___builtins_1__.str]')
        signing_secret_key = TypeAliasType('signing_secret_key', 'OptionalProperty[std.str, ___builtins__.str]')


class __WebhookConfig_typeof_partial__(
    cfg.__ConfigObject_typeof_partial__,
    __WebhookConfig_typeof_base__,
):
    class __typeof__(cfg.__ConfigObject_typeof_partial__.__typeof__):
        url = TypeAliasType('url', 'OptionalProperty[std.str, ___builtins__.str]')
        events = TypeAliasType('events', 'MultiProperty[WebhookEvent, ___builtins_1__.str]')
        signing_secret_key = TypeAliasType('signing_secret_key', 'OptionalProperty[std.str, ___builtins__.str]')


class WebhookConfig(
    __WebhookConfig_typeof__,
    cfg.ConfigObject,
    __gel_type_id__=UUID(int=307763587024998583260809907117765149570),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            url: ___builtins__.str,
            events: Iterable[___builtins_1__.str] = [],
            signing_secret_key: ___builtins__.str | None = None,
        ) -> None:
            """Create a new ext::auth::WebhookConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            events: type[ext_auth.WebhookEvent] | UnspecifiedType = Unspecified,
            signing_secret_key: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::WebhookConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            events: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.WebhookEvent] | UnspecifiedType = Unspecified,
            signing_secret_key: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::WebhookConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            events: type[ext_auth.WebhookEvent] | UnspecifiedType = Unspecified,
            signing_secret_key: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::WebhookConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            url: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            signing_secret_key: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(cfg.ConfigObject.__variants__):
        class Base(
            __WebhookConfig_typeof__,
            cfg.ConfigObject.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    url: ___builtins__.str,
                    events: Iterable[___builtins_1__.str] = [],
                    signing_secret_key: ___builtins__.str | None = None,
                ) -> None:
                    """Create a new ext::auth::WebhookConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    events: type[ext_auth.WebhookEvent] | UnspecifiedType = Unspecified,
                    signing_secret_key: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::WebhookConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    events: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.WebhookEvent] | UnspecifiedType = Unspecified,
                    signing_secret_key: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::WebhookConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    events: type[ext_auth.WebhookEvent] | UnspecifiedType = Unspecified,
                    signing_secret_key: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::WebhookConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    url: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    signing_secret_key: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            cfg.ConfigObject.__variants__.Required,
            __gel_variant__="Required",
        ):
            url: ___std_1__.str
            events: MultiProperty[___ext_auth__.WebhookEvent, ___builtins_1__.str]

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __WebhookConfig_typeof_partial__,
            Base,
            cfg.ConfigObject.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            cfg.ConfigObject.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            url: OptionalProperty[___std_1__.str, ___builtins__.str]
            events: MultiProperty[___ext_auth__.WebhookEvent, ___builtins_1__.str]
            signing_secret_key: OptionalProperty[___std_1__.str, ___builtins__.str]


        Any = TypeVar("Any", bound="WebhookConfig | Base | Required | Partial")
    class __links__(cfg.ConfigObject.__links__):
        pass
    class __links_partial__(cfg.ConfigObject.__links_partial__):
        pass

if not TYPE_CHECKING:
    WebhookConfig.__variants__.Base = WebhookConfig



#
# type ext::auth::Factor
#
class __Factor_typeof_base__(__Auditable_typeof_base__):
    class __gel_reflection__(__Auditable_typeof_base__.__gel_reflection__):
        id = UUID(int=120025483991736650665078440179762873093)
        name = SchemaPath('ext', 'auth', 'Factor')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'identity': GelPointerReflection(
                    name='identity',
                    type=SchemaPath('ext', 'auth', 'LocalIdentity'),
                    typexpr='ext::auth::LocalIdentity',
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
                | __Auditable_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=120025483991736650665078440179762873093),
                name='ext::auth::Factor',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __Factor_typeof__(__Auditable_typeof__, __Factor_typeof_base__):
    class __typeof__(__Auditable_typeof__.__typeof__):
        identity = TypeAliasType('identity', 'LocalIdentity')


class __Factor_typeof_partial__(
    __Auditable_typeof_partial__,
    __Factor_typeof_base__,
):
    class __typeof__(__Auditable_typeof_partial__.__typeof__):
        identity = TypeAliasType('identity', 'LocalIdentity | LocalIdentity.__variants__.Partial')


class Factor(
    __Factor_typeof__,
    Auditable,
    __gel_type_id__=UUID(int=120025483991736650665078440179762873093),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            created_at: datetime | DefaultValue = DEFAULT_VALUE,
            modified_at: datetime,
            identity: LocalIdentity | None = None,
        ) -> None:
            """Create a new ext::auth::Factor instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::Factor instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::Factor instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::Factor instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(Auditable.__variants__):
        class Base(
            __Factor_typeof__,
            Auditable.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime | DefaultValue = DEFAULT_VALUE,
                    modified_at: datetime,
                    identity: LocalIdentity | None = None,
                ) -> None:
                    """Create a new ext::auth::Factor instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::Factor instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::Factor instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::Factor instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            Auditable.__variants__.Required,
            __gel_variant__="Required",
        ):
            identity: ___ext_auth__.LocalIdentity

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __Factor_typeof_partial__,
            Base,
            Auditable.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            Auditable.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            identity: ___ext_auth__.LocalIdentity | ___ext_auth__.LocalIdentity.__variants__.Partial


        Any = TypeVar("Any", bound="Factor | Base | Required | Partial")
    class __links__(Auditable.__links__):
        pass
    class __links_partial__(Auditable.__links_partial__):
        pass

if not TYPE_CHECKING:
    Factor.__variants__.Base = Factor



#
# type ext::auth::Identity
#
class __Identity_typeof_base__(__Auditable_typeof_base__):
    class __gel_reflection__(__Auditable_typeof_base__.__gel_reflection__):
        id = UUID(int=138248657905235101912370520257758216720)
        name = SchemaPath('ext', 'auth', 'Identity')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'issuer': GelPointerReflection(
                    name='issuer',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'subject': GelPointerReflection(
                    name='subject',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __Auditable_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=138248657905235101912370520257758216720),
                name='ext::auth::Identity',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __Identity_typeof__(__Auditable_typeof__, __Identity_typeof_base__):
    class __typeof__(__Auditable_typeof__.__typeof__):
        issuer = TypeAliasType('issuer', 'std.str')
        subject = TypeAliasType('subject', 'std.str')


class __Identity_typeof_partial__(
    __Auditable_typeof_partial__,
    __Identity_typeof_base__,
):
    class __typeof__(__Auditable_typeof_partial__.__typeof__):
        issuer = TypeAliasType('issuer', 'OptionalProperty[std.str, ___builtins__.str]')
        subject = TypeAliasType('subject', 'OptionalProperty[std.str, ___builtins__.str]')


class Identity(
    __Identity_typeof__,
    Auditable,
    __gel_type_id__=UUID(int=138248657905235101912370520257758216720),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            created_at: datetime | DefaultValue = DEFAULT_VALUE,
            modified_at: datetime,
            issuer: ___builtins__.str,
            subject: ___builtins__.str,
        ) -> None:
            """Create a new ext::auth::Identity instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            issuer: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            subject: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::Identity instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            issuer: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            subject: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::Identity instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            issuer: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            subject: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::Identity instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            issuer: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            subject: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(Auditable.__variants__):
        class Base(
            __Identity_typeof__,
            Auditable.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime | DefaultValue = DEFAULT_VALUE,
                    modified_at: datetime,
                    issuer: ___builtins__.str,
                    subject: ___builtins__.str,
                ) -> None:
                    """Create a new ext::auth::Identity instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    issuer: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    subject: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::Identity instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    issuer: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    subject: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::Identity instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    issuer: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    subject: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::Identity instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    issuer: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    subject: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            Auditable.__variants__.Required,
            __gel_variant__="Required",
        ):
            issuer: ___std_1__.str
            subject: ___std_1__.str

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __Identity_typeof_partial__,
            Base,
            Auditable.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            Auditable.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            issuer: OptionalProperty[___std_1__.str, ___builtins__.str]
            subject: OptionalProperty[___std_1__.str, ___builtins__.str]


        Any = TypeVar("Any", bound="Identity | Base | Required | Partial")
    class __links__(Auditable.__links__):
        pass
    class __links_partial__(Auditable.__links_partial__):
        pass

if not TYPE_CHECKING:
    Identity.__variants__.Base = Identity



#
# type ext::auth::PKCEChallenge
#
class __PKCEChallenge_typeof_base__(__Auditable_typeof_base__):
    class __gel_reflection__(__Auditable_typeof_base__.__gel_reflection__):
        id = UUID(int=113798113130405258243975612991794868670)
        name = SchemaPath('ext', 'auth', 'PKCEChallenge')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'challenge': GelPointerReflection(
                    name='challenge',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'auth_token': GelPointerReflection(
                    name='auth_token',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'refresh_token': GelPointerReflection(
                    name='refresh_token',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'id_token': GelPointerReflection(
                    name='id_token',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'identity': GelPointerReflection(
                    name='identity',
                    type=SchemaPath('ext', 'auth', 'Identity'),
                    typexpr='ext::auth::Identity',
                    kind=PointerKind('Link'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __Auditable_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=113798113130405258243975612991794868670),
                name='ext::auth::PKCEChallenge',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __PKCEChallenge_typeof__(
    __Auditable_typeof__,
    __PKCEChallenge_typeof_base__,
):
    class __typeof__(__Auditable_typeof__.__typeof__):
        challenge = TypeAliasType('challenge', 'std.str')
        auth_token = TypeAliasType('auth_token', 'OptionalProperty[std.str, ___builtins__.str]')
        refresh_token = TypeAliasType('refresh_token', 'OptionalProperty[std.str, ___builtins__.str]')
        id_token = TypeAliasType('id_token', 'OptionalProperty[std.str, ___builtins__.str]')
        identity = TypeAliasType('identity', 'OptionalLink[Identity]')


class __PKCEChallenge_typeof_partial__(
    __Auditable_typeof_partial__,
    __PKCEChallenge_typeof_base__,
):
    class __typeof__(__Auditable_typeof_partial__.__typeof__):
        challenge = TypeAliasType('challenge', 'OptionalProperty[std.str, ___builtins__.str]')
        auth_token = TypeAliasType('auth_token', 'OptionalProperty[std.str, ___builtins__.str]')
        refresh_token = TypeAliasType('refresh_token', 'OptionalProperty[std.str, ___builtins__.str]')
        id_token = TypeAliasType('id_token', 'OptionalProperty[std.str, ___builtins__.str]')
        identity = TypeAliasType('identity', 'OptionalLink[Identity | Identity.__variants__.Partial]')


class PKCEChallenge(
    __PKCEChallenge_typeof__,
    Auditable,
    __gel_type_id__=UUID(int=113798113130405258243975612991794868670),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            created_at: datetime | DefaultValue = DEFAULT_VALUE,
            modified_at: datetime,
            challenge: ___builtins__.str,
            auth_token: ___builtins__.str | None = None,
            refresh_token: ___builtins__.str | None = None,
            id_token: ___builtins__.str | None = None,
            identity: Identity | None = None,
        ) -> None:
            """Create a new ext::auth::PKCEChallenge instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            challenge: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            auth_token: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            refresh_token: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            id_token: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.Identity] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::PKCEChallenge instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            challenge: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            auth_token: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            refresh_token: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            id_token: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.Identity] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::PKCEChallenge instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            challenge: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            auth_token: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            refresh_token: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            id_token: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.Identity] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::PKCEChallenge instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            challenge: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            auth_token: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            refresh_token: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            id_token: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(Auditable.__variants__):
        class Base(
            __PKCEChallenge_typeof__,
            Auditable.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime | DefaultValue = DEFAULT_VALUE,
                    modified_at: datetime,
                    challenge: ___builtins__.str,
                    auth_token: ___builtins__.str | None = None,
                    refresh_token: ___builtins__.str | None = None,
                    id_token: ___builtins__.str | None = None,
                    identity: Identity | None = None,
                ) -> None:
                    """Create a new ext::auth::PKCEChallenge instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    challenge: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    auth_token: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    refresh_token: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    id_token: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.Identity] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::PKCEChallenge instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    challenge: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    auth_token: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    refresh_token: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    id_token: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.Identity] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::PKCEChallenge instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    challenge: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    auth_token: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    refresh_token: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    id_token: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.Identity] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::PKCEChallenge instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    challenge: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    auth_token: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    refresh_token: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    id_token: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            Auditable.__variants__.Required,
            __gel_variant__="Required",
        ):
            challenge: ___std_1__.str

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __PKCEChallenge_typeof_partial__,
            Base,
            Auditable.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            Auditable.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            challenge: OptionalProperty[___std_1__.str, ___builtins__.str]
            auth_token: OptionalProperty[___std_1__.str, ___builtins__.str]
            refresh_token: OptionalProperty[___std_1__.str, ___builtins__.str]
            id_token: OptionalProperty[___std_1__.str, ___builtins__.str]
            identity: OptionalLink[___ext_auth__.Identity | ___ext_auth__.Identity.__variants__.Partial]


        Any = TypeVar("Any", bound="PKCEChallenge | Base | Required | Partial")
    class __links__(Auditable.__links__):
        pass
    class __links_partial__(Auditable.__links_partial__):
        pass

if not TYPE_CHECKING:
    PKCEChallenge.__variants__.Base = PKCEChallenge



#
# type ext::auth::WebAuthnAuthenticationChallenge
#
class __WebAuthnAuthenticationChallenge_typeof_base__(
    __Auditable_typeof_base__,
):
    class __gel_reflection__(__Auditable_typeof_base__.__gel_reflection__):
        id = UUID(int=339891318179715780124275799861926483086)
        name = SchemaPath('ext', 'auth', 'WebAuthnAuthenticationChallenge')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'challenge': GelPointerReflection(
                    name='challenge',
                    type=SchemaPath('std', 'bytes'),
                    typexpr='std::bytes',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'factors': GelPointerReflection(
                    name='factors',
                    type=SchemaPath('ext', 'auth', 'WebAuthnFactor'),
                    typexpr='ext::auth::WebAuthnFactor',
                    kind=PointerKind('Link'),
                    cardinality=Cardinality('AtLeastOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __Auditable_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=339891318179715780124275799861926483086),
                name='ext::auth::WebAuthnAuthenticationChallenge',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __WebAuthnAuthenticationChallenge_typeof__(
    __Auditable_typeof__,
    __WebAuthnAuthenticationChallenge_typeof_base__,
):
    class __typeof__(__Auditable_typeof__.__typeof__):
        challenge = TypeAliasType('challenge', 'std.bytes')
        factors = TypeAliasType('factors', 'RequiredMultiLink[WebAuthnFactor]')


class __WebAuthnAuthenticationChallenge_typeof_partial__(
    __Auditable_typeof_partial__,
    __WebAuthnAuthenticationChallenge_typeof_base__,
):
    class __typeof__(__Auditable_typeof_partial__.__typeof__):
        challenge = TypeAliasType('challenge', 'OptionalProperty[std.bytes, bytes]')
        factors = TypeAliasType('factors', 'RequiredMultiLink[WebAuthnFactor | WebAuthnFactor.__variants__.Partial]')


class WebAuthnAuthenticationChallenge(
    __WebAuthnAuthenticationChallenge_typeof__,
    Auditable,
    __gel_type_id__=UUID(int=339891318179715780124275799861926483086),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            created_at: datetime | DefaultValue = DEFAULT_VALUE,
            modified_at: datetime,
            challenge: bytes,
            factors: Iterable[WebAuthnFactor] = [],
        ) -> None:
            """Create a new ext::auth::WebAuthnAuthenticationChallenge instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            challenge: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
            factors: type[ext_auth.WebAuthnFactor] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::WebAuthnAuthenticationChallenge instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            challenge: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bytes] | UnspecifiedType = Unspecified,
            factors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.WebAuthnFactor] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::WebAuthnAuthenticationChallenge instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            challenge: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
            factors: type[ext_auth.WebAuthnFactor] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::WebAuthnAuthenticationChallenge instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            challenge: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(Auditable.__variants__):
        class Base(
            __WebAuthnAuthenticationChallenge_typeof__,
            Auditable.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime | DefaultValue = DEFAULT_VALUE,
                    modified_at: datetime,
                    challenge: bytes,
                    factors: Iterable[WebAuthnFactor] = [],
                ) -> None:
                    """Create a new ext::auth::WebAuthnAuthenticationChallenge instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    challenge: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
                    factors: type[ext_auth.WebAuthnFactor] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::WebAuthnAuthenticationChallenge instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    challenge: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bytes] | UnspecifiedType = Unspecified,
                    factors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.WebAuthnFactor] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::WebAuthnAuthenticationChallenge instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    challenge: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
                    factors: type[ext_auth.WebAuthnFactor] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::WebAuthnAuthenticationChallenge instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    challenge: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            Auditable.__variants__.Required,
            __gel_variant__="Required",
        ):
            challenge: ___std_1__.bytes
            factors: RequiredMultiLink[___ext_auth__.WebAuthnFactor]

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __WebAuthnAuthenticationChallenge_typeof_partial__,
            Base,
            Auditable.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            Auditable.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            challenge: OptionalProperty[___std_1__.bytes, bytes]
            factors: RequiredMultiLink[___ext_auth__.WebAuthnFactor | ___ext_auth__.WebAuthnFactor.__variants__.Partial]


        Any = TypeVar("Any", bound="WebAuthnAuthenticationChallenge | Base | Required | Partial")
    class __links__(Auditable.__links__):
        pass
    class __links_partial__(Auditable.__links_partial__):
        pass

if not TYPE_CHECKING:
    WebAuthnAuthenticationChallenge.__variants__.Base = WebAuthnAuthenticationChallenge



#
# type ext::auth::WebAuthnRegistrationChallenge
#
class __WebAuthnRegistrationChallenge_typeof_base__(__Auditable_typeof_base__):
    class __gel_reflection__(__Auditable_typeof_base__.__gel_reflection__):
        id = UUID(int=306233804239267636046194582894504152618)
        name = SchemaPath('ext', 'auth', 'WebAuthnRegistrationChallenge')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'challenge': GelPointerReflection(
                    name='challenge',
                    type=SchemaPath('std', 'bytes'),
                    typexpr='std::bytes',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'email': GelPointerReflection(
                    name='email',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'user_handle': GelPointerReflection(
                    name='user_handle',
                    type=SchemaPath('std', 'bytes'),
                    typexpr='std::bytes',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __Auditable_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=306233804239267636046194582894504152618),
                name='ext::auth::WebAuthnRegistrationChallenge',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __WebAuthnRegistrationChallenge_typeof__(
    __Auditable_typeof__,
    __WebAuthnRegistrationChallenge_typeof_base__,
):
    class __typeof__(__Auditable_typeof__.__typeof__):
        challenge = TypeAliasType('challenge', 'std.bytes')
        email = TypeAliasType('email', 'std.str')
        user_handle = TypeAliasType('user_handle', 'std.bytes')


class __WebAuthnRegistrationChallenge_typeof_partial__(
    __Auditable_typeof_partial__,
    __WebAuthnRegistrationChallenge_typeof_base__,
):
    class __typeof__(__Auditable_typeof_partial__.__typeof__):
        challenge = TypeAliasType('challenge', 'OptionalProperty[std.bytes, bytes]')
        email = TypeAliasType('email', 'OptionalProperty[std.str, ___builtins__.str]')
        user_handle = TypeAliasType('user_handle', 'OptionalProperty[std.bytes, bytes]')


class WebAuthnRegistrationChallenge(
    __WebAuthnRegistrationChallenge_typeof__,
    Auditable,
    __gel_type_id__=UUID(int=306233804239267636046194582894504152618),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            created_at: datetime | DefaultValue = DEFAULT_VALUE,
            modified_at: datetime,
            challenge: bytes,
            email: ___builtins__.str,
            user_handle: bytes,
        ) -> None:
            """Create a new ext::auth::WebAuthnRegistrationChallenge instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            challenge: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
            email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            user_handle: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::WebAuthnRegistrationChallenge instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            challenge: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bytes] | UnspecifiedType = Unspecified,
            email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            user_handle: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bytes] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::WebAuthnRegistrationChallenge instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            challenge: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
            email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            user_handle: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::WebAuthnRegistrationChallenge instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            challenge: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            email: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            user_handle: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(Auditable.__variants__):
        class Base(
            __WebAuthnRegistrationChallenge_typeof__,
            Auditable.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime | DefaultValue = DEFAULT_VALUE,
                    modified_at: datetime,
                    challenge: bytes,
                    email: ___builtins__.str,
                    user_handle: bytes,
                ) -> None:
                    """Create a new ext::auth::WebAuthnRegistrationChallenge instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    challenge: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
                    email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    user_handle: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::WebAuthnRegistrationChallenge instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    challenge: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bytes] | UnspecifiedType = Unspecified,
                    email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    user_handle: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bytes] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::WebAuthnRegistrationChallenge instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    challenge: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
                    email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    user_handle: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::WebAuthnRegistrationChallenge instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    challenge: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    email: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    user_handle: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            Auditable.__variants__.Required,
            __gel_variant__="Required",
        ):
            challenge: ___std_1__.bytes
            email: ___std_1__.str
            user_handle: ___std_1__.bytes

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __WebAuthnRegistrationChallenge_typeof_partial__,
            Base,
            Auditable.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            Auditable.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            challenge: OptionalProperty[___std_1__.bytes, bytes]
            email: OptionalProperty[___std_1__.str, ___builtins__.str]
            user_handle: OptionalProperty[___std_1__.bytes, bytes]


        Any = TypeVar("Any", bound="WebAuthnRegistrationChallenge | Base | Required | Partial")
    class __links__(Auditable.__links__):
        pass
    class __links_partial__(Auditable.__links_partial__):
        pass

if not TYPE_CHECKING:
    WebAuthnRegistrationChallenge.__variants__.Base = WebAuthnRegistrationChallenge



#
# type ext::auth::EmailPasswordProviderConfig
#
class __EmailPasswordProviderConfig_typeof_base__(
    __ProviderConfig_typeof_base__,
):
    class __gel_reflection__(
        __ProviderConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=326379458322877692783219376957490095543)
        name = SchemaPath('ext', 'auth', 'EmailPasswordProviderConfig')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'name': GelPointerReflection(
                    name='name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'require_verification': GelPointerReflection(
                    name='require_verification',
                    type=SchemaPath('std', 'bool'),
                    typexpr='std::bool',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __ProviderConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=326379458322877692783219376957490095543),
                name='ext::auth::EmailPasswordProviderConfig',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __EmailPasswordProviderConfig_typeof__(
    __ProviderConfig_typeof__,
    __EmailPasswordProviderConfig_typeof_base__,
):
    class __typeof__(__ProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        require_verification = TypeAliasType('require_verification', 'std.bool')


class __EmailPasswordProviderConfig_typeof_partial__(
    __ProviderConfig_typeof_partial__,
    __EmailPasswordProviderConfig_typeof_base__,
):
    class __typeof__(__ProviderConfig_typeof_partial__.__typeof__):
        name = TypeAliasType('name', 'OptionalProperty[std.str, ___builtins__.str]')
        require_verification = TypeAliasType('require_verification', 'OptionalProperty[std.bool, bool]')


class EmailPasswordProviderConfig(
    __EmailPasswordProviderConfig_typeof__,
    ProviderConfig,
    __gel_type_id__=UUID(int=326379458322877692783219376957490095543),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
            require_verification: bool | DefaultValue = DEFAULT_VALUE,
        ) -> None:
            """Create a new ext::auth::EmailPasswordProviderConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            require_verification: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::EmailPasswordProviderConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            require_verification: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::EmailPasswordProviderConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            require_verification: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::EmailPasswordProviderConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            require_verification: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ProviderConfig.__variants__):
        class Base(
            __EmailPasswordProviderConfig_typeof__,
            ProviderConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
                    require_verification: bool | DefaultValue = DEFAULT_VALUE,
                ) -> None:
                    """Create a new ext::auth::EmailPasswordProviderConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    require_verification: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::EmailPasswordProviderConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    require_verification: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::EmailPasswordProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    require_verification: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::EmailPasswordProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    require_verification: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            ProviderConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: ___std_1__.str
            require_verification: ___std_1__.bool

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __EmailPasswordProviderConfig_typeof_partial__,
            Base,
            ProviderConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            ProviderConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            name: OptionalProperty[___std_1__.str, ___builtins__.str]
            require_verification: OptionalProperty[___std_1__.bool, bool]


        Any = TypeVar("Any", bound="EmailPasswordProviderConfig | Base | Required | Partial")
    class __links__(ProviderConfig.__links__):
        pass
    class __links_partial__(ProviderConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    EmailPasswordProviderConfig.__variants__.Base = EmailPasswordProviderConfig



#
# type ext::auth::MagicLinkProviderConfig
#
class __MagicLinkProviderConfig_typeof_base__(__ProviderConfig_typeof_base__):
    class __gel_reflection__(
        __ProviderConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=197258520102777659735443006342865520155)
        name = SchemaPath('ext', 'auth', 'MagicLinkProviderConfig')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'name': GelPointerReflection(
                    name='name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'token_time_to_live': GelPointerReflection(
                    name='token_time_to_live',
                    type=SchemaPath('std', 'duration'),
                    typexpr='std::duration',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __ProviderConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=197258520102777659735443006342865520155),
                name='ext::auth::MagicLinkProviderConfig',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __MagicLinkProviderConfig_typeof__(
    __ProviderConfig_typeof__,
    __MagicLinkProviderConfig_typeof_base__,
):
    class __typeof__(__ProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        token_time_to_live = TypeAliasType('token_time_to_live', 'std.duration')


class __MagicLinkProviderConfig_typeof_partial__(
    __ProviderConfig_typeof_partial__,
    __MagicLinkProviderConfig_typeof_base__,
):
    class __typeof__(__ProviderConfig_typeof_partial__.__typeof__):
        name = TypeAliasType('name', 'OptionalProperty[std.str, ___builtins__.str]')
        token_time_to_live = TypeAliasType('token_time_to_live', 'OptionalProperty[std.duration, timedelta]')


class MagicLinkProviderConfig(
    __MagicLinkProviderConfig_typeof__,
    ProviderConfig,
    __gel_type_id__=UUID(int=197258520102777659735443006342865520155),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
            token_time_to_live: timedelta | DefaultValue = DEFAULT_VALUE,
        ) -> None:
            """Create a new ext::auth::MagicLinkProviderConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            token_time_to_live: ___datetime_1__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::MagicLinkProviderConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            token_time_to_live: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::MagicLinkProviderConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            token_time_to_live: ___datetime_1__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::MagicLinkProviderConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            token_time_to_live: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ProviderConfig.__variants__):
        class Base(
            __MagicLinkProviderConfig_typeof__,
            ProviderConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
                    token_time_to_live: timedelta | DefaultValue = DEFAULT_VALUE,
                ) -> None:
                    """Create a new ext::auth::MagicLinkProviderConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    token_time_to_live: ___datetime_1__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::MagicLinkProviderConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    token_time_to_live: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.duration] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::MagicLinkProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    token_time_to_live: ___datetime_1__.timedelta | type[___std__.duration] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::MagicLinkProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    token_time_to_live: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            ProviderConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: ___std_1__.str
            token_time_to_live: ___std_1__.duration

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __MagicLinkProviderConfig_typeof_partial__,
            Base,
            ProviderConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            ProviderConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            name: OptionalProperty[___std_1__.str, ___builtins__.str]
            token_time_to_live: OptionalProperty[___std_1__.duration, timedelta]


        Any = TypeVar("Any", bound="MagicLinkProviderConfig | Base | Required | Partial")
    class __links__(ProviderConfig.__links__):
        pass
    class __links_partial__(ProviderConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    MagicLinkProviderConfig.__variants__.Base = MagicLinkProviderConfig



#
# type ext::auth::OAuthProviderConfig
#
class __OAuthProviderConfig_typeof_base__(__ProviderConfig_typeof_base__):
    class __gel_reflection__(
        __ProviderConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=176191875819755481847342667895462103654)
        name = SchemaPath('ext', 'auth', 'OAuthProviderConfig')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'name': GelPointerReflection(
                    name='name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=False,
                    properties={},
                ),
                'secret': GelPointerReflection(
                    name='secret',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=False,
                    properties={},
                ),
                'client_id': GelPointerReflection(
                    name='client_id',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=False,
                    properties={},
                ),
                'display_name': GelPointerReflection(
                    name='display_name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=False,
                    properties={},
                ),
                'additional_scope': GelPointerReflection(
                    name='additional_scope',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=True,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __ProviderConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=176191875819755481847342667895462103654),
                name='ext::auth::OAuthProviderConfig',
                builtin=False,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

class __OAuthProviderConfig_typeof__(
    __ProviderConfig_typeof__,
    __OAuthProviderConfig_typeof_base__,
):
    class __typeof__(__ProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        secret = TypeAliasType('secret', 'std.str')
        client_id = TypeAliasType('client_id', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')
        additional_scope = TypeAliasType('additional_scope', 'OptionalProperty[std.str, ___builtins__.str]')


class __OAuthProviderConfig_typeof_partial__(
    __ProviderConfig_typeof_partial__,
    __OAuthProviderConfig_typeof_base__,
):
    class __typeof__(__ProviderConfig_typeof_partial__.__typeof__):
        name = TypeAliasType('name', 'OptionalProperty[std.str, ___builtins__.str]')
        secret = TypeAliasType('secret', 'OptionalProperty[std.str, ___builtins__.str]')
        client_id = TypeAliasType('client_id', 'OptionalProperty[std.str, ___builtins__.str]')
        display_name = TypeAliasType('display_name', 'OptionalProperty[std.str, ___builtins__.str]')
        additional_scope = TypeAliasType('additional_scope', 'OptionalProperty[std.str, ___builtins__.str]')


class OAuthProviderConfig(
    __OAuthProviderConfig_typeof__,
    ProviderConfig,
    __gel_type_id__=UUID(int=176191875819755481847342667895462103654),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: ___builtins__.str,
            secret: ___builtins__.str,
            client_id: ___builtins__.str,
            display_name: ___builtins__.str,
            additional_scope: ___builtins__.str | None = None,
        ) -> None:
            """Create a new ext::auth::OAuthProviderConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::auth::OAuthProviderConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::OAuthProviderConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            additional_scope: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::OAuthProviderConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            client_id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            display_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            additional_scope: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ProviderConfig.__variants__):
        class Base(
            __OAuthProviderConfig_typeof__,
            ProviderConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: ___builtins__.str,
                    secret: ___builtins__.str,
                    client_id: ___builtins__.str,
                    display_name: ___builtins__.str,
                    additional_scope: ___builtins__.str | None = None,
                ) -> None:
                    """Create a new ext::auth::OAuthProviderConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::auth::OAuthProviderConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::OAuthProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::OAuthProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    client_id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    display_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    additional_scope: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            ProviderConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: ___std_1__.str
            secret: ___std_1__.str
            client_id: ___std_1__.str
            display_name: ___std_1__.str

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __OAuthProviderConfig_typeof_partial__,
            Base,
            ProviderConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            ProviderConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            name: OptionalProperty[___std_1__.str, ___builtins__.str]
            secret: OptionalProperty[___std_1__.str, ___builtins__.str]
            client_id: OptionalProperty[___std_1__.str, ___builtins__.str]
            display_name: OptionalProperty[___std_1__.str, ___builtins__.str]
            additional_scope: OptionalProperty[___std_1__.str, ___builtins__.str]


        Any = TypeVar("Any", bound="OAuthProviderConfig | Base | Required | Partial")
    class __links__(ProviderConfig.__links__):
        pass
    class __links_partial__(ProviderConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    OAuthProviderConfig.__variants__.Base = OAuthProviderConfig



#
# type ext::auth::WebAuthnProviderConfig
#
class __WebAuthnProviderConfig_typeof_base__(__ProviderConfig_typeof_base__):
    class __gel_reflection__(
        __ProviderConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=18693980672146206883873808188444327649)
        name = SchemaPath('ext', 'auth', 'WebAuthnProviderConfig')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'name': GelPointerReflection(
                    name='name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'relying_party_origin': GelPointerReflection(
                    name='relying_party_origin',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'require_verification': GelPointerReflection(
                    name='require_verification',
                    type=SchemaPath('std', 'bool'),
                    typexpr='std::bool',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=True,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __ProviderConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=18693980672146206883873808188444327649),
                name='ext::auth::WebAuthnProviderConfig',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __WebAuthnProviderConfig_typeof__(
    __ProviderConfig_typeof__,
    __WebAuthnProviderConfig_typeof_base__,
):
    class __typeof__(__ProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        relying_party_origin = TypeAliasType('relying_party_origin', 'std.str')
        require_verification = TypeAliasType('require_verification', 'std.bool')


class __WebAuthnProviderConfig_typeof_partial__(
    __ProviderConfig_typeof_partial__,
    __WebAuthnProviderConfig_typeof_base__,
):
    class __typeof__(__ProviderConfig_typeof_partial__.__typeof__):
        name = TypeAliasType('name', 'OptionalProperty[std.str, ___builtins__.str]')
        relying_party_origin = TypeAliasType('relying_party_origin', 'OptionalProperty[std.str, ___builtins__.str]')
        require_verification = TypeAliasType('require_verification', 'OptionalProperty[std.bool, bool]')


class WebAuthnProviderConfig(
    __WebAuthnProviderConfig_typeof__,
    ProviderConfig,
    __gel_type_id__=UUID(int=18693980672146206883873808188444327649),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
            relying_party_origin: ___builtins__.str,
            require_verification: bool | DefaultValue = DEFAULT_VALUE,
        ) -> None:
            """Create a new ext::auth::WebAuthnProviderConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            relying_party_origin: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            require_verification: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::WebAuthnProviderConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            relying_party_origin: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            require_verification: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::WebAuthnProviderConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            relying_party_origin: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            require_verification: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::WebAuthnProviderConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            relying_party_origin: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            require_verification: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ProviderConfig.__variants__):
        class Base(
            __WebAuthnProviderConfig_typeof__,
            ProviderConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
                    relying_party_origin: ___builtins__.str,
                    require_verification: bool | DefaultValue = DEFAULT_VALUE,
                ) -> None:
                    """Create a new ext::auth::WebAuthnProviderConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    relying_party_origin: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    require_verification: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::WebAuthnProviderConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    relying_party_origin: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    require_verification: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bool] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::WebAuthnProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    relying_party_origin: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    require_verification: ___builtins_3__.bool | type[___std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::WebAuthnProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    relying_party_origin: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    require_verification: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            ProviderConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: ___std_1__.str
            relying_party_origin: ___std_1__.str
            require_verification: ___std_1__.bool

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __WebAuthnProviderConfig_typeof_partial__,
            Base,
            ProviderConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            ProviderConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            name: OptionalProperty[___std_1__.str, ___builtins__.str]
            relying_party_origin: OptionalProperty[___std_1__.str, ___builtins__.str]
            require_verification: OptionalProperty[___std_1__.bool, bool]


        Any = TypeVar("Any", bound="WebAuthnProviderConfig | Base | Required | Partial")
    class __links__(ProviderConfig.__links__):
        pass
    class __links_partial__(ProviderConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    WebAuthnProviderConfig.__variants__.Base = WebAuthnProviderConfig



#
# type ext::auth::EmailFactor
#
class __EmailFactor_typeof_base__(__Factor_typeof_base__):
    class __gel_reflection__(__Factor_typeof_base__.__gel_reflection__):
        id = UUID(int=267038974621553903381178302575855343752)
        name = SchemaPath('ext', 'auth', 'EmailFactor')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'email': GelPointerReflection(
                    name='email',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'verified_at': GelPointerReflection(
                    name='verified_at',
                    type=SchemaPath('std', 'datetime'),
                    typexpr='std::datetime',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __Factor_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=267038974621553903381178302575855343752),
                name='ext::auth::EmailFactor',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __EmailFactor_typeof__(__Factor_typeof__, __EmailFactor_typeof_base__):
    class __typeof__(__Factor_typeof__.__typeof__):
        email = TypeAliasType('email', 'std.str')
        verified_at = TypeAliasType('verified_at', 'OptionalProperty[std.datetime, datetime]')


class __EmailFactor_typeof_partial__(
    __Factor_typeof_partial__,
    __EmailFactor_typeof_base__,
):
    class __typeof__(__Factor_typeof_partial__.__typeof__):
        email = TypeAliasType('email', 'OptionalProperty[std.str, ___builtins__.str]')
        verified_at = TypeAliasType('verified_at', 'OptionalProperty[std.datetime, datetime]')


class EmailFactor(
    __EmailFactor_typeof__,
    Factor,
    __gel_type_id__=UUID(int=267038974621553903381178302575855343752),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            created_at: datetime | DefaultValue = DEFAULT_VALUE,
            modified_at: datetime,
            identity: LocalIdentity | None = None,
            email: ___builtins__.str,
            verified_at: datetime | None = None,
        ) -> None:
            """Create a new ext::auth::EmailFactor instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            verified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::EmailFactor instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            verified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::EmailFactor instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            verified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::EmailFactor instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            email: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            verified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(Factor.__variants__):
        class Base(
            __EmailFactor_typeof__,
            Factor.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime | DefaultValue = DEFAULT_VALUE,
                    modified_at: datetime,
                    identity: LocalIdentity | None = None,
                    email: ___builtins__.str,
                    verified_at: datetime | None = None,
                ) -> None:
                    """Create a new ext::auth::EmailFactor instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    verified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::EmailFactor instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    verified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::EmailFactor instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    verified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::EmailFactor instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    email: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    verified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            Factor.__variants__.Required,
            __gel_variant__="Required",
        ):
            email: ___std_1__.str

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __EmailFactor_typeof_partial__,
            Base,
            Factor.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            Factor.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            email: OptionalProperty[___std_1__.str, ___builtins__.str]
            verified_at: OptionalProperty[___std_1__.datetime, datetime]


        Any = TypeVar("Any", bound="EmailFactor | Base | Required | Partial")
    class __links__(Factor.__links__):
        pass
    class __links_partial__(Factor.__links_partial__):
        pass

if not TYPE_CHECKING:
    EmailFactor.__variants__.Base = EmailFactor



#
# type ext::auth::LocalIdentity
#
class __LocalIdentity_typeof_base__(__Identity_typeof_base__):
    class __gel_reflection__(__Identity_typeof_base__.__gel_reflection__):
        id = UUID(int=160831847510468337518667602858609567942)
        name = SchemaPath('ext', 'auth', 'LocalIdentity')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'subject': GelPointerReflection(
                    name='subject',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __Identity_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=160831847510468337518667602858609567942),
                name='ext::auth::LocalIdentity',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __LocalIdentity_typeof__(
    __Identity_typeof__,
    __LocalIdentity_typeof_base__,
):
    class __typeof__(__Identity_typeof__.__typeof__):
        subject = TypeAliasType('subject', 'std.str')


class __LocalIdentity_typeof_partial__(
    __Identity_typeof_partial__,
    __LocalIdentity_typeof_base__,
):
    class __typeof__(__Identity_typeof_partial__.__typeof__):
        subject = TypeAliasType('subject', 'OptionalProperty[std.str, ___builtins__.str]')


class LocalIdentity(
    __LocalIdentity_typeof__,
    Identity,
    __gel_type_id__=UUID(int=160831847510468337518667602858609567942),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            created_at: datetime | DefaultValue = DEFAULT_VALUE,
            modified_at: datetime,
            issuer: ___builtins__.str,
            subject: ___builtins__.str,
        ) -> None:
            """Create a new ext::auth::LocalIdentity instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            issuer: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            subject: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::LocalIdentity instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            issuer: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            subject: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::LocalIdentity instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            issuer: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            subject: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::LocalIdentity instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            issuer: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            subject: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(Identity.__variants__):
        class Base(
            __LocalIdentity_typeof__,
            Identity.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime | DefaultValue = DEFAULT_VALUE,
                    modified_at: datetime,
                    issuer: ___builtins__.str,
                    subject: ___builtins__.str,
                ) -> None:
                    """Create a new ext::auth::LocalIdentity instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    issuer: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    subject: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::LocalIdentity instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    issuer: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    subject: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::LocalIdentity instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    issuer: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    subject: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::LocalIdentity instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    issuer: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    subject: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            Identity.__variants__.Required,
            __gel_variant__="Required",
        ):
            subject: ___std_1__.str

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __LocalIdentity_typeof_partial__,
            Base,
            Identity.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            Identity.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            subject: OptionalProperty[___std_1__.str, ___builtins__.str]


        Any = TypeVar("Any", bound="LocalIdentity | Base | Required | Partial")
    class __links__(Identity.__links__):
        pass
    class __links_partial__(Identity.__links_partial__):
        pass

if not TYPE_CHECKING:
    LocalIdentity.__variants__.Base = LocalIdentity



#
# type ext::auth::AppleOAuthProvider
#
class __AppleOAuthProvider_typeof_base__(__OAuthProviderConfig_typeof_base__):
    class __gel_reflection__(
        __OAuthProviderConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=43000943290657793977966224514992214452)
        name = SchemaPath('ext', 'auth', 'AppleOAuthProvider')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'name': GelPointerReflection(
                    name='name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'display_name': GelPointerReflection(
                    name='display_name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __OAuthProviderConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=43000943290657793977966224514992214452),
                name='ext::auth::AppleOAuthProvider',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __AppleOAuthProvider_typeof__(
    __OAuthProviderConfig_typeof__,
    __AppleOAuthProvider_typeof_base__,
):
    class __typeof__(__OAuthProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')


class __AppleOAuthProvider_typeof_partial__(
    __OAuthProviderConfig_typeof_partial__,
    __AppleOAuthProvider_typeof_base__,
):
    class __typeof__(__OAuthProviderConfig_typeof_partial__.__typeof__):
        name = TypeAliasType('name', 'OptionalProperty[std.str, ___builtins__.str]')
        display_name = TypeAliasType('display_name', 'OptionalProperty[std.str, ___builtins__.str]')


class AppleOAuthProvider(
    __AppleOAuthProvider_typeof__,
    OAuthProviderConfig,
    __gel_type_id__=UUID(int=43000943290657793977966224514992214452),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
            secret: ___builtins__.str,
            client_id: ___builtins__.str,
            display_name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
            additional_scope: ___builtins__.str | None = None,
        ) -> None:
            """Create a new ext::auth::AppleOAuthProvider instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::auth::AppleOAuthProvider instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::AppleOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            additional_scope: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::AppleOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            client_id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            display_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            additional_scope: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(OAuthProviderConfig.__variants__):
        class Base(
            __AppleOAuthProvider_typeof__,
            OAuthProviderConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
                    secret: ___builtins__.str,
                    client_id: ___builtins__.str,
                    display_name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
                    additional_scope: ___builtins__.str | None = None,
                ) -> None:
                    """Create a new ext::auth::AppleOAuthProvider instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::auth::AppleOAuthProvider instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::AppleOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::AppleOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    client_id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    display_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    additional_scope: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            OAuthProviderConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: ___std_1__.str
            display_name: ___std_1__.str

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __AppleOAuthProvider_typeof_partial__,
            Base,
            OAuthProviderConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            OAuthProviderConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            name: OptionalProperty[___std_1__.str, ___builtins__.str]
            display_name: OptionalProperty[___std_1__.str, ___builtins__.str]


        Any = TypeVar("Any", bound="AppleOAuthProvider | Base | Required | Partial")
    class __links__(OAuthProviderConfig.__links__):
        pass
    class __links_partial__(OAuthProviderConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    AppleOAuthProvider.__variants__.Base = AppleOAuthProvider



#
# type ext::auth::AzureOAuthProvider
#
class __AzureOAuthProvider_typeof_base__(__OAuthProviderConfig_typeof_base__):
    class __gel_reflection__(
        __OAuthProviderConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=189177822115181231528998530125922317735)
        name = SchemaPath('ext', 'auth', 'AzureOAuthProvider')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'name': GelPointerReflection(
                    name='name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'display_name': GelPointerReflection(
                    name='display_name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __OAuthProviderConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=189177822115181231528998530125922317735),
                name='ext::auth::AzureOAuthProvider',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __AzureOAuthProvider_typeof__(
    __OAuthProviderConfig_typeof__,
    __AzureOAuthProvider_typeof_base__,
):
    class __typeof__(__OAuthProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')


class __AzureOAuthProvider_typeof_partial__(
    __OAuthProviderConfig_typeof_partial__,
    __AzureOAuthProvider_typeof_base__,
):
    class __typeof__(__OAuthProviderConfig_typeof_partial__.__typeof__):
        name = TypeAliasType('name', 'OptionalProperty[std.str, ___builtins__.str]')
        display_name = TypeAliasType('display_name', 'OptionalProperty[std.str, ___builtins__.str]')


class AzureOAuthProvider(
    __AzureOAuthProvider_typeof__,
    OAuthProviderConfig,
    __gel_type_id__=UUID(int=189177822115181231528998530125922317735),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
            secret: ___builtins__.str,
            client_id: ___builtins__.str,
            display_name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
            additional_scope: ___builtins__.str | None = None,
        ) -> None:
            """Create a new ext::auth::AzureOAuthProvider instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::auth::AzureOAuthProvider instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::AzureOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            additional_scope: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::AzureOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            client_id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            display_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            additional_scope: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(OAuthProviderConfig.__variants__):
        class Base(
            __AzureOAuthProvider_typeof__,
            OAuthProviderConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
                    secret: ___builtins__.str,
                    client_id: ___builtins__.str,
                    display_name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
                    additional_scope: ___builtins__.str | None = None,
                ) -> None:
                    """Create a new ext::auth::AzureOAuthProvider instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::auth::AzureOAuthProvider instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::AzureOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::AzureOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    client_id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    display_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    additional_scope: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            OAuthProviderConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: ___std_1__.str
            display_name: ___std_1__.str

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __AzureOAuthProvider_typeof_partial__,
            Base,
            OAuthProviderConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            OAuthProviderConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            name: OptionalProperty[___std_1__.str, ___builtins__.str]
            display_name: OptionalProperty[___std_1__.str, ___builtins__.str]


        Any = TypeVar("Any", bound="AzureOAuthProvider | Base | Required | Partial")
    class __links__(OAuthProviderConfig.__links__):
        pass
    class __links_partial__(OAuthProviderConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    AzureOAuthProvider.__variants__.Base = AzureOAuthProvider



#
# type ext::auth::DiscordOAuthProvider
#
class __DiscordOAuthProvider_typeof_base__(
    __OAuthProviderConfig_typeof_base__,
):
    class __gel_reflection__(
        __OAuthProviderConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=24018239224398776296098705400907496501)
        name = SchemaPath('ext', 'auth', 'DiscordOAuthProvider')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'name': GelPointerReflection(
                    name='name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'display_name': GelPointerReflection(
                    name='display_name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __OAuthProviderConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=24018239224398776296098705400907496501),
                name='ext::auth::DiscordOAuthProvider',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __DiscordOAuthProvider_typeof__(
    __OAuthProviderConfig_typeof__,
    __DiscordOAuthProvider_typeof_base__,
):
    class __typeof__(__OAuthProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')


class __DiscordOAuthProvider_typeof_partial__(
    __OAuthProviderConfig_typeof_partial__,
    __DiscordOAuthProvider_typeof_base__,
):
    class __typeof__(__OAuthProviderConfig_typeof_partial__.__typeof__):
        name = TypeAliasType('name', 'OptionalProperty[std.str, ___builtins__.str]')
        display_name = TypeAliasType('display_name', 'OptionalProperty[std.str, ___builtins__.str]')


class DiscordOAuthProvider(
    __DiscordOAuthProvider_typeof__,
    OAuthProviderConfig,
    __gel_type_id__=UUID(int=24018239224398776296098705400907496501),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
            secret: ___builtins__.str,
            client_id: ___builtins__.str,
            display_name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
            additional_scope: ___builtins__.str | None = None,
        ) -> None:
            """Create a new ext::auth::DiscordOAuthProvider instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::auth::DiscordOAuthProvider instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::DiscordOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            additional_scope: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::DiscordOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            client_id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            display_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            additional_scope: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(OAuthProviderConfig.__variants__):
        class Base(
            __DiscordOAuthProvider_typeof__,
            OAuthProviderConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
                    secret: ___builtins__.str,
                    client_id: ___builtins__.str,
                    display_name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
                    additional_scope: ___builtins__.str | None = None,
                ) -> None:
                    """Create a new ext::auth::DiscordOAuthProvider instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::auth::DiscordOAuthProvider instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::DiscordOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::DiscordOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    client_id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    display_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    additional_scope: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            OAuthProviderConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: ___std_1__.str
            display_name: ___std_1__.str

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __DiscordOAuthProvider_typeof_partial__,
            Base,
            OAuthProviderConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            OAuthProviderConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            name: OptionalProperty[___std_1__.str, ___builtins__.str]
            display_name: OptionalProperty[___std_1__.str, ___builtins__.str]


        Any = TypeVar("Any", bound="DiscordOAuthProvider | Base | Required | Partial")
    class __links__(OAuthProviderConfig.__links__):
        pass
    class __links_partial__(OAuthProviderConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    DiscordOAuthProvider.__variants__.Base = DiscordOAuthProvider



#
# type ext::auth::GitHubOAuthProvider
#
class __GitHubOAuthProvider_typeof_base__(__OAuthProviderConfig_typeof_base__):
    class __gel_reflection__(
        __OAuthProviderConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=135303881089532318040492385271633596804)
        name = SchemaPath('ext', 'auth', 'GitHubOAuthProvider')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'name': GelPointerReflection(
                    name='name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'display_name': GelPointerReflection(
                    name='display_name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __OAuthProviderConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=135303881089532318040492385271633596804),
                name='ext::auth::GitHubOAuthProvider',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __GitHubOAuthProvider_typeof__(
    __OAuthProviderConfig_typeof__,
    __GitHubOAuthProvider_typeof_base__,
):
    class __typeof__(__OAuthProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')


class __GitHubOAuthProvider_typeof_partial__(
    __OAuthProviderConfig_typeof_partial__,
    __GitHubOAuthProvider_typeof_base__,
):
    class __typeof__(__OAuthProviderConfig_typeof_partial__.__typeof__):
        name = TypeAliasType('name', 'OptionalProperty[std.str, ___builtins__.str]')
        display_name = TypeAliasType('display_name', 'OptionalProperty[std.str, ___builtins__.str]')


class GitHubOAuthProvider(
    __GitHubOAuthProvider_typeof__,
    OAuthProviderConfig,
    __gel_type_id__=UUID(int=135303881089532318040492385271633596804),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
            secret: ___builtins__.str,
            client_id: ___builtins__.str,
            display_name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
            additional_scope: ___builtins__.str | None = None,
        ) -> None:
            """Create a new ext::auth::GitHubOAuthProvider instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::auth::GitHubOAuthProvider instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::GitHubOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            additional_scope: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::GitHubOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            client_id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            display_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            additional_scope: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(OAuthProviderConfig.__variants__):
        class Base(
            __GitHubOAuthProvider_typeof__,
            OAuthProviderConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
                    secret: ___builtins__.str,
                    client_id: ___builtins__.str,
                    display_name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
                    additional_scope: ___builtins__.str | None = None,
                ) -> None:
                    """Create a new ext::auth::GitHubOAuthProvider instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::auth::GitHubOAuthProvider instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::GitHubOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::GitHubOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    client_id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    display_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    additional_scope: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            OAuthProviderConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: ___std_1__.str
            display_name: ___std_1__.str

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __GitHubOAuthProvider_typeof_partial__,
            Base,
            OAuthProviderConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            OAuthProviderConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            name: OptionalProperty[___std_1__.str, ___builtins__.str]
            display_name: OptionalProperty[___std_1__.str, ___builtins__.str]


        Any = TypeVar("Any", bound="GitHubOAuthProvider | Base | Required | Partial")
    class __links__(OAuthProviderConfig.__links__):
        pass
    class __links_partial__(OAuthProviderConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    GitHubOAuthProvider.__variants__.Base = GitHubOAuthProvider



#
# type ext::auth::GoogleOAuthProvider
#
class __GoogleOAuthProvider_typeof_base__(__OAuthProviderConfig_typeof_base__):
    class __gel_reflection__(
        __OAuthProviderConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=314152047091060873466459255621715246895)
        name = SchemaPath('ext', 'auth', 'GoogleOAuthProvider')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'name': GelPointerReflection(
                    name='name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'display_name': GelPointerReflection(
                    name='display_name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __OAuthProviderConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=314152047091060873466459255621715246895),
                name='ext::auth::GoogleOAuthProvider',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __GoogleOAuthProvider_typeof__(
    __OAuthProviderConfig_typeof__,
    __GoogleOAuthProvider_typeof_base__,
):
    class __typeof__(__OAuthProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')


class __GoogleOAuthProvider_typeof_partial__(
    __OAuthProviderConfig_typeof_partial__,
    __GoogleOAuthProvider_typeof_base__,
):
    class __typeof__(__OAuthProviderConfig_typeof_partial__.__typeof__):
        name = TypeAliasType('name', 'OptionalProperty[std.str, ___builtins__.str]')
        display_name = TypeAliasType('display_name', 'OptionalProperty[std.str, ___builtins__.str]')


class GoogleOAuthProvider(
    __GoogleOAuthProvider_typeof__,
    OAuthProviderConfig,
    __gel_type_id__=UUID(int=314152047091060873466459255621715246895),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
            secret: ___builtins__.str,
            client_id: ___builtins__.str,
            display_name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
            additional_scope: ___builtins__.str | None = None,
        ) -> None:
            """Create a new ext::auth::GoogleOAuthProvider instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::auth::GoogleOAuthProvider instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::GoogleOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            additional_scope: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::GoogleOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            client_id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            display_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            additional_scope: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(OAuthProviderConfig.__variants__):
        class Base(
            __GoogleOAuthProvider_typeof__,
            OAuthProviderConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
                    secret: ___builtins__.str,
                    client_id: ___builtins__.str,
                    display_name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
                    additional_scope: ___builtins__.str | None = None,
                ) -> None:
                    """Create a new ext::auth::GoogleOAuthProvider instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::auth::GoogleOAuthProvider instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::GoogleOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::GoogleOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    client_id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    display_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    additional_scope: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            OAuthProviderConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: ___std_1__.str
            display_name: ___std_1__.str

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __GoogleOAuthProvider_typeof_partial__,
            Base,
            OAuthProviderConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            OAuthProviderConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            name: OptionalProperty[___std_1__.str, ___builtins__.str]
            display_name: OptionalProperty[___std_1__.str, ___builtins__.str]


        Any = TypeVar("Any", bound="GoogleOAuthProvider | Base | Required | Partial")
    class __links__(OAuthProviderConfig.__links__):
        pass
    class __links_partial__(OAuthProviderConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    GoogleOAuthProvider.__variants__.Base = GoogleOAuthProvider



#
# type ext::auth::OpenIDConnectProvider
#
class __OpenIDConnectProvider_typeof_base__(
    __OAuthProviderConfig_typeof_base__,
):
    class __gel_reflection__(
        __OAuthProviderConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=266535682383167007985348307161960435089)
        name = SchemaPath('ext', 'auth', 'OpenIDConnectProvider')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'name': GelPointerReflection(
                    name='name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=False,
                    properties={},
                ),
                'display_name': GelPointerReflection(
                    name='display_name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=False,
                    properties={},
                ),
                'issuer_url': GelPointerReflection(
                    name='issuer_url',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'logo_url': GelPointerReflection(
                    name='logo_url',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('AtMostOne'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __OAuthProviderConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=266535682383167007985348307161960435089),
                name='ext::auth::OpenIDConnectProvider',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __OpenIDConnectProvider_typeof__(
    __OAuthProviderConfig_typeof__,
    __OpenIDConnectProvider_typeof_base__,
):
    class __typeof__(__OAuthProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')
        issuer_url = TypeAliasType('issuer_url', 'std.str')
        logo_url = TypeAliasType('logo_url', 'OptionalProperty[std.str, ___builtins__.str]')


class __OpenIDConnectProvider_typeof_partial__(
    __OAuthProviderConfig_typeof_partial__,
    __OpenIDConnectProvider_typeof_base__,
):
    class __typeof__(__OAuthProviderConfig_typeof_partial__.__typeof__):
        name = TypeAliasType('name', 'OptionalProperty[std.str, ___builtins__.str]')
        display_name = TypeAliasType('display_name', 'OptionalProperty[std.str, ___builtins__.str]')
        issuer_url = TypeAliasType('issuer_url', 'OptionalProperty[std.str, ___builtins__.str]')
        logo_url = TypeAliasType('logo_url', 'OptionalProperty[std.str, ___builtins__.str]')


class OpenIDConnectProvider(
    __OpenIDConnectProvider_typeof__,
    OAuthProviderConfig,
    __gel_type_id__=UUID(int=266535682383167007985348307161960435089),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: ___builtins__.str,
            secret: ___builtins__.str,
            client_id: ___builtins__.str,
            display_name: ___builtins__.str,
            additional_scope: ___builtins__.str | None = None,
            issuer_url: ___builtins__.str,
            logo_url: ___builtins__.str | None = None,
        ) -> None:
            """Create a new ext::auth::OpenIDConnectProvider instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            issuer_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            logo_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::OpenIDConnectProvider instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            issuer_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            logo_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::OpenIDConnectProvider instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            additional_scope: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            issuer_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            logo_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::OpenIDConnectProvider instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            client_id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            display_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            additional_scope: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            issuer_url: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            logo_url: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(OAuthProviderConfig.__variants__):
        class Base(
            __OpenIDConnectProvider_typeof__,
            OAuthProviderConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: ___builtins__.str,
                    secret: ___builtins__.str,
                    client_id: ___builtins__.str,
                    display_name: ___builtins__.str,
                    additional_scope: ___builtins__.str | None = None,
                    issuer_url: ___builtins__.str,
                    logo_url: ___builtins__.str | None = None,
                ) -> None:
                    """Create a new ext::auth::OpenIDConnectProvider instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    issuer_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    logo_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::OpenIDConnectProvider instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    issuer_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    logo_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::OpenIDConnectProvider instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    issuer_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    logo_url: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::OpenIDConnectProvider instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    client_id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    display_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    additional_scope: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    issuer_url: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    logo_url: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            OAuthProviderConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: ___std_1__.str
            display_name: ___std_1__.str
            issuer_url: ___std_1__.str

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __OpenIDConnectProvider_typeof_partial__,
            Base,
            OAuthProviderConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            OAuthProviderConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            name: OptionalProperty[___std_1__.str, ___builtins__.str]
            display_name: OptionalProperty[___std_1__.str, ___builtins__.str]
            issuer_url: OptionalProperty[___std_1__.str, ___builtins__.str]
            logo_url: OptionalProperty[___std_1__.str, ___builtins__.str]


        Any = TypeVar("Any", bound="OpenIDConnectProvider | Base | Required | Partial")
    class __links__(OAuthProviderConfig.__links__):
        pass
    class __links_partial__(OAuthProviderConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    OpenIDConnectProvider.__variants__.Base = OpenIDConnectProvider



#
# type ext::auth::SlackOAuthProvider
#
class __SlackOAuthProvider_typeof_base__(__OAuthProviderConfig_typeof_base__):
    class __gel_reflection__(
        __OAuthProviderConfig_typeof_base__.__gel_reflection__,
    ):
        id = UUID(int=203801692607706301177517492230120464917)
        name = SchemaPath('ext', 'auth', 'SlackOAuthProvider')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'name': GelPointerReflection(
                    name='name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
                'display_name': GelPointerReflection(
                    name='display_name',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=True,
                    has_default=True,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __OAuthProviderConfig_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=203801692607706301177517492230120464917),
                name='ext::auth::SlackOAuthProvider',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __SlackOAuthProvider_typeof__(
    __OAuthProviderConfig_typeof__,
    __SlackOAuthProvider_typeof_base__,
):
    class __typeof__(__OAuthProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')


class __SlackOAuthProvider_typeof_partial__(
    __OAuthProviderConfig_typeof_partial__,
    __SlackOAuthProvider_typeof_base__,
):
    class __typeof__(__OAuthProviderConfig_typeof_partial__.__typeof__):
        name = TypeAliasType('name', 'OptionalProperty[std.str, ___builtins__.str]')
        display_name = TypeAliasType('display_name', 'OptionalProperty[std.str, ___builtins__.str]')


class SlackOAuthProvider(
    __SlackOAuthProvider_typeof__,
    OAuthProviderConfig,
    __gel_type_id__=UUID(int=203801692607706301177517492230120464917),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
            secret: ___builtins__.str,
            client_id: ___builtins__.str,
            display_name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
            additional_scope: ___builtins__.str | None = None,
        ) -> None:
            """Create a new ext::auth::SlackOAuthProvider instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
            """Update ext::auth::SlackOAuthProvider instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::SlackOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            secret: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            client_id: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            display_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            additional_scope: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::SlackOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            client_id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            display_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            additional_scope: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(OAuthProviderConfig.__variants__):
        class Base(
            __SlackOAuthProvider_typeof__,
            OAuthProviderConfig.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
                    secret: ___builtins__.str,
                    client_id: ___builtins__.str,
                    display_name: ___builtins__.str | DefaultValue = DEFAULT_VALUE,
                    additional_scope: ___builtins__.str | None = None,
                ) -> None:
                    """Create a new ext::auth::SlackOAuthProvider instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [misc, override, unused-ignore]
                    """Update ext::auth::SlackOAuthProvider instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::SlackOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    secret: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    client_id: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    display_name: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::SlackOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    client_id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    display_name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    additional_scope: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            OAuthProviderConfig.__variants__.Required,
            __gel_variant__="Required",
        ):
            name: ___std_1__.str
            display_name: ___std_1__.str

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __SlackOAuthProvider_typeof_partial__,
            Base,
            OAuthProviderConfig.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            OAuthProviderConfig.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            name: OptionalProperty[___std_1__.str, ___builtins__.str]
            display_name: OptionalProperty[___std_1__.str, ___builtins__.str]


        Any = TypeVar("Any", bound="SlackOAuthProvider | Base | Required | Partial")
    class __links__(OAuthProviderConfig.__links__):
        pass
    class __links_partial__(OAuthProviderConfig.__links_partial__):
        pass

if not TYPE_CHECKING:
    SlackOAuthProvider.__variants__.Base = SlackOAuthProvider



#
# type ext::auth::EmailPasswordFactor
#
class __EmailPasswordFactor_typeof_base__(__EmailFactor_typeof_base__):
    class __gel_reflection__(__EmailFactor_typeof_base__.__gel_reflection__):
        id = UUID(int=31172435047994255941611898216302058127)
        name = SchemaPath('ext', 'auth', 'EmailPasswordFactor')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'email': GelPointerReflection(
                    name='email',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'password_hash': GelPointerReflection(
                    name='password_hash',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __EmailFactor_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=31172435047994255941611898216302058127),
                name='ext::auth::EmailPasswordFactor',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __EmailPasswordFactor_typeof__(
    __EmailFactor_typeof__,
    __EmailPasswordFactor_typeof_base__,
):
    class __typeof__(__EmailFactor_typeof__.__typeof__):
        email = TypeAliasType('email', 'std.str')
        password_hash = TypeAliasType('password_hash', 'std.str')


class __EmailPasswordFactor_typeof_partial__(
    __EmailFactor_typeof_partial__,
    __EmailPasswordFactor_typeof_base__,
):
    class __typeof__(__EmailFactor_typeof_partial__.__typeof__):
        email = TypeAliasType('email', 'OptionalProperty[std.str, ___builtins__.str]')
        password_hash = TypeAliasType('password_hash', 'OptionalProperty[std.str, ___builtins__.str]')


class EmailPasswordFactor(
    __EmailPasswordFactor_typeof__,
    EmailFactor,
    __gel_type_id__=UUID(int=31172435047994255941611898216302058127),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            created_at: datetime | DefaultValue = DEFAULT_VALUE,
            modified_at: datetime,
            identity: LocalIdentity | None = None,
            email: ___builtins__.str,
            verified_at: datetime | None = None,
            password_hash: ___builtins__.str,
        ) -> None:
            """Create a new ext::auth::EmailPasswordFactor instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            verified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            password_hash: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::EmailPasswordFactor instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            verified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            password_hash: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::EmailPasswordFactor instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            verified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            password_hash: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::EmailPasswordFactor instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            email: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            verified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            password_hash: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(EmailFactor.__variants__):
        class Base(
            __EmailPasswordFactor_typeof__,
            EmailFactor.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime | DefaultValue = DEFAULT_VALUE,
                    modified_at: datetime,
                    identity: LocalIdentity | None = None,
                    email: ___builtins__.str,
                    verified_at: datetime | None = None,
                    password_hash: ___builtins__.str,
                ) -> None:
                    """Create a new ext::auth::EmailPasswordFactor instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    verified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    password_hash: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::EmailPasswordFactor instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    verified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    password_hash: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::EmailPasswordFactor instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    verified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    password_hash: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::EmailPasswordFactor instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    email: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    verified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    password_hash: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            EmailFactor.__variants__.Required,
            __gel_variant__="Required",
        ):
            email: ___std_1__.str
            password_hash: ___std_1__.str

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __EmailPasswordFactor_typeof_partial__,
            Base,
            EmailFactor.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            EmailFactor.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            email: OptionalProperty[___std_1__.str, ___builtins__.str]
            password_hash: OptionalProperty[___std_1__.str, ___builtins__.str]


        Any = TypeVar("Any", bound="EmailPasswordFactor | Base | Required | Partial")
    class __links__(EmailFactor.__links__):
        pass
    class __links_partial__(EmailFactor.__links_partial__):
        pass

if not TYPE_CHECKING:
    EmailPasswordFactor.__variants__.Base = EmailPasswordFactor



#
# type ext::auth::MagicLinkFactor
#
class __MagicLinkFactor_typeof_base__(__EmailFactor_typeof_base__):
    class __gel_reflection__(__EmailFactor_typeof_base__.__gel_reflection__):
        id = UUID(int=61743578138936630624449892961906140358)
        name = SchemaPath('ext', 'auth', 'MagicLinkFactor')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'email': GelPointerReflection(
                    name='email',
                    type=SchemaPath('std', 'str'),
                    typexpr='std::str',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __EmailFactor_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=61743578138936630624449892961906140358),
                name='ext::auth::MagicLinkFactor',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __MagicLinkFactor_typeof__(
    __EmailFactor_typeof__,
    __MagicLinkFactor_typeof_base__,
):
    class __typeof__(__EmailFactor_typeof__.__typeof__):
        email = TypeAliasType('email', 'std.str')


class __MagicLinkFactor_typeof_partial__(
    __EmailFactor_typeof_partial__,
    __MagicLinkFactor_typeof_base__,
):
    class __typeof__(__EmailFactor_typeof_partial__.__typeof__):
        email = TypeAliasType('email', 'OptionalProperty[std.str, ___builtins__.str]')


class MagicLinkFactor(
    __MagicLinkFactor_typeof__,
    EmailFactor,
    __gel_type_id__=UUID(int=61743578138936630624449892961906140358),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            created_at: datetime | DefaultValue = DEFAULT_VALUE,
            modified_at: datetime,
            identity: LocalIdentity | None = None,
            email: ___builtins__.str,
            verified_at: datetime | None = None,
        ) -> None:
            """Create a new ext::auth::MagicLinkFactor instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            verified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::MagicLinkFactor instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            verified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::MagicLinkFactor instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            verified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::MagicLinkFactor instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            email: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            verified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(EmailFactor.__variants__):
        class Base(
            __MagicLinkFactor_typeof__,
            EmailFactor.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime | DefaultValue = DEFAULT_VALUE,
                    modified_at: datetime,
                    identity: LocalIdentity | None = None,
                    email: ___builtins__.str,
                    verified_at: datetime | None = None,
                ) -> None:
                    """Create a new ext::auth::MagicLinkFactor instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    verified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::MagicLinkFactor instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    verified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::MagicLinkFactor instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    verified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::MagicLinkFactor instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    email: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    verified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            EmailFactor.__variants__.Required,
            __gel_variant__="Required",
        ):
            email: ___std_1__.str

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __MagicLinkFactor_typeof_partial__,
            Base,
            EmailFactor.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            EmailFactor.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            email: OptionalProperty[___std_1__.str, ___builtins__.str]


        Any = TypeVar("Any", bound="MagicLinkFactor | Base | Required | Partial")
    class __links__(EmailFactor.__links__):
        pass
    class __links_partial__(EmailFactor.__links_partial__):
        pass

if not TYPE_CHECKING:
    MagicLinkFactor.__variants__.Base = MagicLinkFactor



#
# type ext::auth::WebAuthnFactor
#
class __WebAuthnFactor_typeof_base__(__EmailFactor_typeof_base__):
    class __gel_reflection__(__EmailFactor_typeof_base__.__gel_reflection__):
        id = UUID(int=114805788310269968559926717489578765583)
        name = SchemaPath('ext', 'auth', 'WebAuthnFactor')
        @LazyClassProperty["dict[str, GelPointerReflection]"]
        @classmethod
        def pointers(cls) -> dict[str, GelPointerReflection]:
            my_ptrs: dict[str, GelPointerReflection] = {
                'user_handle': GelPointerReflection(
                    name='user_handle',
                    type=SchemaPath('std', 'bytes'),
                    typexpr='std::bytes',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'credential_id': GelPointerReflection(
                    name='credential_id',
                    type=SchemaPath('std', 'bytes'),
                    typexpr='std::bytes',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
                'public_key': GelPointerReflection(
                    name='public_key',
                    type=SchemaPath('std', 'bytes'),
                    typexpr='std::bytes',
                    kind=PointerKind('Property'),
                    cardinality=Cardinality('One'),
                    computed=False,
                    readonly=False,
                    has_default=False,
                    properties={},
                ),
            }
            return (
                my_ptrs
                | __EmailFactor_typeof_base__.__gel_reflection__.pointers
            )

        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=114805788310269968559926717489578765583),
                name='ext::auth::WebAuthnFactor',
                builtin=False,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

class __WebAuthnFactor_typeof__(
    __EmailFactor_typeof__,
    __WebAuthnFactor_typeof_base__,
):
    class __typeof__(__EmailFactor_typeof__.__typeof__):
        user_handle = TypeAliasType('user_handle', 'std.bytes')
        credential_id = TypeAliasType('credential_id', 'std.bytes')
        public_key = TypeAliasType('public_key', 'std.bytes')


class __WebAuthnFactor_typeof_partial__(
    __EmailFactor_typeof_partial__,
    __WebAuthnFactor_typeof_base__,
):
    class __typeof__(__EmailFactor_typeof_partial__.__typeof__):
        user_handle = TypeAliasType('user_handle', 'OptionalProperty[std.bytes, bytes]')
        credential_id = TypeAliasType('credential_id', 'OptionalProperty[std.bytes, bytes]')
        public_key = TypeAliasType('public_key', 'OptionalProperty[std.bytes, bytes]')


class WebAuthnFactor(
    __WebAuthnFactor_typeof__,
    EmailFactor,
    __gel_type_id__=UUID(int=114805788310269968559926717489578765583),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            created_at: datetime | DefaultValue = DEFAULT_VALUE,
            modified_at: datetime,
            identity: LocalIdentity | None = None,
            email: ___builtins__.str,
            verified_at: datetime | None = None,
            user_handle: bytes,
            credential_id: bytes,
            public_key: bytes,
        ) -> None:
            """Create a new ext::auth::WebAuthnFactor instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

    if TYPE_CHECKING:
        @classmethod
        def update(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            verified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            user_handle: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
            credential_id: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
            public_key: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::WebAuthnFactor instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias | Literal["*"],
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
            verified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
            user_handle: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bytes] | UnspecifiedType = Unspecified,
            credential_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bytes] | UnspecifiedType = Unspecified,
            public_key: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bytes] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::WebAuthnFactor instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[___std__.bool]],
            id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
            created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
            verified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
            user_handle: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
            credential_id: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
            public_key: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::WebAuthnFactor instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [misc, override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            email: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            verified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            user_handle: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            credential_id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            public_key: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(EmailFactor.__variants__):
        class Base(
            __WebAuthnFactor_typeof__,
            EmailFactor.__variants__.Base,
            __gel_variant__="Base",
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime | DefaultValue = DEFAULT_VALUE,
                    modified_at: datetime,
                    identity: LocalIdentity | None = None,
                    email: ___builtins__.str,
                    verified_at: datetime | None = None,
                    user_handle: bytes,
                    credential_id: bytes,
                    public_key: bytes,
                ) -> None:
                    """Create a new ext::auth::WebAuthnFactor instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

            if TYPE_CHECKING:
                @classmethod
                def update(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    verified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    user_handle: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
                    credential_id: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
                    public_key: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::WebAuthnFactor instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias | Literal["*"],
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.str] | UnspecifiedType = Unspecified,
                    verified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    user_handle: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bytes] | UnspecifiedType = Unspecified,
                    credential_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bytes] | UnspecifiedType = Unspecified,
                    public_key: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[___std__.bytes] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::WebAuthnFactor instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[___std__.bool]],
                    id: UUID | type[___std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: ___builtins_1__.str | type[___std__.str] | UnspecifiedType = Unspecified,
                    verified_at: ___datetime__.datetime | type[___std__.datetime] | UnspecifiedType = Unspecified,
                    user_handle: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
                    credential_id: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
                    public_key: ___builtins_2__.bytes | type[___std__.bytes] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::WebAuthnFactor instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [misc, override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    email: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    verified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    user_handle: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    credential_id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    public_key: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

        class Required(
            Base,
            EmailFactor.__variants__.Required,
            __gel_variant__="Required",
        ):
            user_handle: ___std_1__.bytes
            credential_id: ___std_1__.bytes
            public_key: ___std_1__.bytes

        class PartialBase(  # type: ignore [misc, unused-ignore]
            __WebAuthnFactor_typeof_partial__,
            Base,
            EmailFactor.__variants__.PartialBase,
            __gel_variant__="PartialBase",
        ):
            pass

        class Partial(  # type: ignore [misc, unused-ignore]
            PartialBase,
            EmailFactor.__variants__.Partial,
            __gel_variant__="Partial",
        ):
            user_handle: OptionalProperty[___std_1__.bytes, bytes]
            credential_id: OptionalProperty[___std_1__.bytes, bytes]
            public_key: OptionalProperty[___std_1__.bytes, bytes]


        Any = TypeVar("Any", bound="WebAuthnFactor | Base | Required | Partial")
    class __links__(EmailFactor.__links__):
        pass
    class __links_partial__(EmailFactor.__links_partial__):
        pass

if not TYPE_CHECKING:
    WebAuthnFactor.__variants__.Base = WebAuthnFactor



from ...ext import auth as ___ext_auth__  # noqa: E402 F403

import builtins as ___builtins__  # noqa: E402 F403
from builtins import bool, bytes  # noqa: E402 F403
from datetime import datetime, timedelta  # noqa: E402 F403
