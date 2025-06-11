#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from .. import cfg, std

from gel.models.pydantic import (
    AnyEnum,
    Direction,
    EmptyDirection,
    ExprCompatible,
    LazyClassProperty,
    MultiLink,
    OptionalLink,
    OptionalProperty,
    PathAlias,
    PyConstType,
    SchemaPath,
    Unspecified,
    UnspecifiedType
)

import builtins as __builtins_2__
import builtins as __builtins_1__
import builtins as builtins
import builtins as __builtins__
import datetime as __datetime__
import datetime as __datetime_1__
from builtins import tuple, type
from collections.abc import Callable, Iterable
from typing import TYPE_CHECKING, TypeVar
from typing_extensions import Self, TypeAliasType
from uuid import UUID

if TYPE_CHECKING:

    from ... import cfg as __cfg__, schema, std as __std__
    from ...ext import auth as ext_auth


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
class __Auditable_typeof__(std.__BaseObject_typeof__):
    class __gel_reflection__(std.__BaseObject_typeof__.__gel_reflection__):
        id = UUID(int=89170665678168121361218419839485559093)
        name = SchemaPath('ext', 'auth', 'Auditable')
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

    class __typeof__(std.__BaseObject_typeof__.__typeof__):
        created_at = TypeAliasType('created_at', 'std.datetime')
        modified_at = TypeAliasType('modified_at', 'std.datetime')


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
            created_at: datetime,
            modified_at: datetime,
        ) -> None:
            """Create a new ext::auth::Auditable instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::Auditable instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::Auditable instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::Auditable instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        class Base(__Auditable_typeof__, std.BaseObject.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime,
                    modified_at: datetime,
                ) -> None:
                    """Create a new ext::auth::Auditable instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::Auditable instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::Auditable instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::Auditable instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Auditable | Base")
    class __links__(std.BaseObject.__links__):
        pass

if not TYPE_CHECKING:
    Auditable.__variants__.Base = Auditable



#
# type ext::auth::AuthConfig
#
class __AuthConfig_typeof__(cfg.__ExtensionConfig_typeof__):
    class __gel_reflection__(
        cfg.__ExtensionConfig_typeof__.__gel_reflection__,
    ):
        id = UUID(int=82556222219052082021678686650866392229)
        name = SchemaPath('ext', 'auth', 'AuthConfig')
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

    class __typeof__(cfg.__ExtensionConfig_typeof__.__typeof__):
        app_name = TypeAliasType('app_name', 'OptionalProperty[std.str, str]')
        logo_url = TypeAliasType('logo_url', 'OptionalProperty[std.str, str]')
        dark_logo_url = TypeAliasType('dark_logo_url', 'OptionalProperty[std.str, str]')
        brand_color = TypeAliasType('brand_color', 'OptionalProperty[std.str, str]')
        auth_signing_key = TypeAliasType('auth_signing_key', 'OptionalProperty[std.str, str]')
        token_time_to_live = TypeAliasType('token_time_to_live', 'OptionalProperty[std.duration, timedelta]')
        allowed_redirect_urls = TypeAliasType('allowed_redirect_urls', 'list[str]')
        providers = TypeAliasType('providers', 'MultiLink[ProviderConfig]')
        ui = TypeAliasType('ui', 'OptionalLink[UIConfig]')
        webhooks = TypeAliasType('webhooks', 'MultiLink[WebhookConfig]')


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
            app_name: str | None = None,
            logo_url: str | None = None,
            dark_logo_url: str | None = None,
            brand_color: str | None = None,
            auth_signing_key: str | None = None,
            token_time_to_live: timedelta | None = None,
            allowed_redirect_urls: Iterable[str] = [],
            providers: Iterable[ProviderConfig] = [],
            ui: UIConfig | None = None,
            webhooks: Iterable[WebhookConfig] = [],
        ) -> None:
            """Create a new ext::auth::AuthConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            cfg: type[__cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
            app_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            logo_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            dark_logo_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            brand_color: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            auth_signing_key: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            token_time_to_live: __datetime_1__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            allowed_redirect_urls: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            providers: type[ext_auth.ProviderConfig] | UnspecifiedType = Unspecified,
            ui: type[ext_auth.UIConfig] | UnspecifiedType = Unspecified,
            webhooks: type[ext_auth.WebhookConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::AuthConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            cfg: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
            app_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            logo_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            dark_logo_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            brand_color: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            auth_signing_key: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            token_time_to_live: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            allowed_redirect_urls: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            providers: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.ProviderConfig] | UnspecifiedType = Unspecified,
            ui: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.UIConfig] | UnspecifiedType = Unspecified,
            webhooks: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.WebhookConfig] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::AuthConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            cfg: type[__cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
            app_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            logo_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            dark_logo_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            brand_color: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            auth_signing_key: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            token_time_to_live: __datetime_1__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            allowed_redirect_urls: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            providers: type[ext_auth.ProviderConfig] | UnspecifiedType = Unspecified,
            ui: type[ext_auth.UIConfig] | UnspecifiedType = Unspecified,
            webhooks: type[ext_auth.WebhookConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::AuthConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    cfg: cfg.AbstractConfig | None = None,
                    app_name: str | None = None,
                    logo_url: str | None = None,
                    dark_logo_url: str | None = None,
                    brand_color: str | None = None,
                    auth_signing_key: str | None = None,
                    token_time_to_live: timedelta | None = None,
                    allowed_redirect_urls: Iterable[str] = [],
                    providers: Iterable[ProviderConfig] = [],
                    ui: UIConfig | None = None,
                    webhooks: Iterable[WebhookConfig] = [],
                ) -> None:
                    """Create a new ext::auth::AuthConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    cfg: type[__cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
                    app_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    logo_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    dark_logo_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    brand_color: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    auth_signing_key: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    token_time_to_live: __datetime_1__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    allowed_redirect_urls: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    providers: type[ext_auth.ProviderConfig] | UnspecifiedType = Unspecified,
                    ui: type[ext_auth.UIConfig] | UnspecifiedType = Unspecified,
                    webhooks: type[ext_auth.WebhookConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::AuthConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    cfg: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
                    app_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    logo_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    dark_logo_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    brand_color: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    auth_signing_key: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    token_time_to_live: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    allowed_redirect_urls: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    providers: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.ProviderConfig] | UnspecifiedType = Unspecified,
                    ui: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.UIConfig] | UnspecifiedType = Unspecified,
                    webhooks: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.WebhookConfig] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::AuthConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    cfg: type[__cfg__.AbstractConfig] | UnspecifiedType = Unspecified,
                    app_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    logo_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    dark_logo_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    brand_color: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    auth_signing_key: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    token_time_to_live: __datetime_1__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    allowed_redirect_urls: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    providers: type[ext_auth.ProviderConfig] | UnspecifiedType = Unspecified,
                    ui: type[ext_auth.UIConfig] | UnspecifiedType = Unspecified,
                    webhooks: type[ext_auth.WebhookConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::AuthConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
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


        Any = TypeVar("Any", bound="AuthConfig | Base")
    class __links__(cfg.ExtensionConfig.__links__):
        pass

if not TYPE_CHECKING:
    AuthConfig.__variants__.Base = AuthConfig



#
# type ext::auth::ProviderConfig
#
class __ProviderConfig_typeof__(cfg.__ConfigObject_typeof__):
    class __gel_reflection__(cfg.__ConfigObject_typeof__.__gel_reflection__):
        id = UUID(int=118712192702193322452317409393620995308)
        name = SchemaPath('ext', 'auth', 'ProviderConfig')
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

    class __typeof__(cfg.__ConfigObject_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')


class ProviderConfig(
    __ProviderConfig_typeof__,
    cfg.ConfigObject,
    __gel_type_id__=UUID(int=118712192702193322452317409393620995308),
):
    if TYPE_CHECKING:
        def __init__(self, /, *, name: str) -> None:
            """Create a new ext::auth::ProviderConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
            """Update ext::auth::ProviderConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::ProviderConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::ProviderConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        ):
            if TYPE_CHECKING:
                def __init__(self, /, *, name: str) -> None:
                    """Create a new ext::auth::ProviderConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
                    """Update ext::auth::ProviderConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::ProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::ProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="ProviderConfig | Base")
    class __links__(cfg.ConfigObject.__links__):
        pass

if not TYPE_CHECKING:
    ProviderConfig.__variants__.Base = ProviderConfig



#
# type ext::auth::UIConfig
#
class __UIConfig_typeof__(cfg.__ConfigObject_typeof__):
    class __gel_reflection__(cfg.__ConfigObject_typeof__.__gel_reflection__):
        id = UUID(int=118696617643017006394314869111520389176)
        name = SchemaPath('ext', 'auth', 'UIConfig')
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

    class __typeof__(cfg.__ConfigObject_typeof__.__typeof__):
        redirect_to = TypeAliasType('redirect_to', 'std.str')
        redirect_to_on_signup = TypeAliasType('redirect_to_on_signup', 'OptionalProperty[std.str, str]')
        flow_type = TypeAliasType('flow_type', 'FlowType')
        app_name = TypeAliasType('app_name', 'OptionalProperty[std.str, str]')
        logo_url = TypeAliasType('logo_url', 'OptionalProperty[std.str, str]')
        dark_logo_url = TypeAliasType('dark_logo_url', 'OptionalProperty[std.str, str]')
        brand_color = TypeAliasType('brand_color', 'OptionalProperty[std.str, str]')


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
            redirect_to: str,
            redirect_to_on_signup: str | None = None,
            flow_type: __builtins__.str,
            app_name: str | None = None,
            logo_url: str | None = None,
            dark_logo_url: str | None = None,
            brand_color: str | None = None,
        ) -> None:
            """Create a new ext::auth::UIConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            redirect_to: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            redirect_to_on_signup: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            flow_type: type[ext_auth.FlowType] | UnspecifiedType = Unspecified,
            app_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            logo_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            dark_logo_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            brand_color: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::UIConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            redirect_to: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            redirect_to_on_signup: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            flow_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.FlowType] | UnspecifiedType = Unspecified,
            app_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            logo_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            dark_logo_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            brand_color: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::UIConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            redirect_to: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            redirect_to_on_signup: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            flow_type: type[ext_auth.FlowType] | UnspecifiedType = Unspecified,
            app_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            logo_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            dark_logo_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            brand_color: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::UIConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        class Base(__UIConfig_typeof__, cfg.ConfigObject.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    redirect_to: str,
                    redirect_to_on_signup: str | None = None,
                    flow_type: __builtins__.str,
                    app_name: str | None = None,
                    logo_url: str | None = None,
                    dark_logo_url: str | None = None,
                    brand_color: str | None = None,
                ) -> None:
                    """Create a new ext::auth::UIConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    redirect_to: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    redirect_to_on_signup: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    flow_type: type[ext_auth.FlowType] | UnspecifiedType = Unspecified,
                    app_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    logo_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    dark_logo_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    brand_color: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::UIConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    redirect_to: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    redirect_to_on_signup: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    flow_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.FlowType] | UnspecifiedType = Unspecified,
                    app_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    logo_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    dark_logo_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    brand_color: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::UIConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    redirect_to: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    redirect_to_on_signup: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    flow_type: type[ext_auth.FlowType] | UnspecifiedType = Unspecified,
                    app_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    logo_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    dark_logo_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    brand_color: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::UIConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
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


        Any = TypeVar("Any", bound="UIConfig | Base")
    class __links__(cfg.ConfigObject.__links__):
        pass

if not TYPE_CHECKING:
    UIConfig.__variants__.Base = UIConfig



#
# type ext::auth::WebhookConfig
#
class __WebhookConfig_typeof__(cfg.__ConfigObject_typeof__):
    class __gel_reflection__(cfg.__ConfigObject_typeof__.__gel_reflection__):
        id = UUID(int=307763587024998583260809907117765149570)
        name = SchemaPath('ext', 'auth', 'WebhookConfig')
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

    class __typeof__(cfg.__ConfigObject_typeof__.__typeof__):
        url = TypeAliasType('url', 'std.str')
        events = TypeAliasType('events', 'list[__builtins__.str]')
        signing_secret_key = TypeAliasType('signing_secret_key', 'OptionalProperty[std.str, str]')


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
            url: str,
            events: Iterable[__builtins__.str] = [],
            signing_secret_key: str | None = None,
        ) -> None:
            """Create a new ext::auth::WebhookConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            events: type[ext_auth.WebhookEvent] | UnspecifiedType = Unspecified,
            signing_secret_key: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::WebhookConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            events: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.WebhookEvent] | UnspecifiedType = Unspecified,
            signing_secret_key: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::WebhookConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            events: type[ext_auth.WebhookEvent] | UnspecifiedType = Unspecified,
            signing_secret_key: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::WebhookConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    url: str,
                    events: Iterable[__builtins__.str] = [],
                    signing_secret_key: str | None = None,
                ) -> None:
                    """Create a new ext::auth::WebhookConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    events: type[ext_auth.WebhookEvent] | UnspecifiedType = Unspecified,
                    signing_secret_key: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::WebhookConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    events: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.WebhookEvent] | UnspecifiedType = Unspecified,
                    signing_secret_key: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::WebhookConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    events: type[ext_auth.WebhookEvent] | UnspecifiedType = Unspecified,
                    signing_secret_key: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::WebhookConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    url: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    signing_secret_key: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="WebhookConfig | Base")
    class __links__(cfg.ConfigObject.__links__):
        pass

if not TYPE_CHECKING:
    WebhookConfig.__variants__.Base = WebhookConfig



#
# type ext::auth::Factor
#
class __Factor_typeof__(__Auditable_typeof__):
    class __gel_reflection__(__Auditable_typeof__.__gel_reflection__):
        id = UUID(int=120025483991736650665078440179762873093)
        name = SchemaPath('ext', 'auth', 'Factor')
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

    class __typeof__(__Auditable_typeof__.__typeof__):
        identity = TypeAliasType('identity', 'OptionalLink[LocalIdentity]')


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
            created_at: datetime,
            modified_at: datetime,
            identity: LocalIdentity | None = None,
        ) -> None:
            """Create a new ext::auth::Factor instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::Factor instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::Factor instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::Factor instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        class Base(__Factor_typeof__, Auditable.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime,
                    modified_at: datetime,
                    identity: LocalIdentity | None = None,
                ) -> None:
                    """Create a new ext::auth::Factor instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::Factor instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::Factor instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::Factor instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    modified_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Factor | Base")
    class __links__(Auditable.__links__):
        pass

if not TYPE_CHECKING:
    Factor.__variants__.Base = Factor



#
# type ext::auth::Identity
#
class __Identity_typeof__(__Auditable_typeof__):
    class __gel_reflection__(__Auditable_typeof__.__gel_reflection__):
        id = UUID(int=138248657905235101912370520257758216720)
        name = SchemaPath('ext', 'auth', 'Identity')
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

    class __typeof__(__Auditable_typeof__.__typeof__):
        issuer = TypeAliasType('issuer', 'std.str')
        subject = TypeAliasType('subject', 'std.str')


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
            created_at: datetime,
            modified_at: datetime,
            issuer: str,
            subject: str,
        ) -> None:
            """Create a new ext::auth::Identity instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            issuer: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            subject: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::Identity instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            issuer: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            subject: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::Identity instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            issuer: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            subject: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::Identity instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        class Base(__Identity_typeof__, Auditable.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime,
                    modified_at: datetime,
                    issuer: str,
                    subject: str,
                ) -> None:
                    """Create a new ext::auth::Identity instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    issuer: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    subject: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::Identity instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    issuer: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    subject: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::Identity instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    issuer: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    subject: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::Identity instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
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


        Any = TypeVar("Any", bound="Identity | Base")
    class __links__(Auditable.__links__):
        pass

if not TYPE_CHECKING:
    Identity.__variants__.Base = Identity



#
# type ext::auth::PKCEChallenge
#
class __PKCEChallenge_typeof__(__Auditable_typeof__):
    class __gel_reflection__(__Auditable_typeof__.__gel_reflection__):
        id = UUID(int=113798113130405258243975612991794868670)
        name = SchemaPath('ext', 'auth', 'PKCEChallenge')
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

    class __typeof__(__Auditable_typeof__.__typeof__):
        challenge = TypeAliasType('challenge', 'std.str')
        auth_token = TypeAliasType('auth_token', 'OptionalProperty[std.str, str]')
        refresh_token = TypeAliasType('refresh_token', 'OptionalProperty[std.str, str]')
        id_token = TypeAliasType('id_token', 'OptionalProperty[std.str, str]')
        identity = TypeAliasType('identity', 'OptionalLink[Identity]')


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
            created_at: datetime,
            modified_at: datetime,
            challenge: str,
            auth_token: str | None = None,
            refresh_token: str | None = None,
            id_token: str | None = None,
            identity: Identity | None = None,
        ) -> None:
            """Create a new ext::auth::PKCEChallenge instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            challenge: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            auth_token: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            refresh_token: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            id_token: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.Identity] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::PKCEChallenge instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            challenge: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            auth_token: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            refresh_token: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            id_token: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.Identity] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::PKCEChallenge instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            challenge: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            auth_token: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            refresh_token: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            id_token: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.Identity] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::PKCEChallenge instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        class Base(__PKCEChallenge_typeof__, Auditable.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime,
                    modified_at: datetime,
                    challenge: str,
                    auth_token: str | None = None,
                    refresh_token: str | None = None,
                    id_token: str | None = None,
                    identity: Identity | None = None,
                ) -> None:
                    """Create a new ext::auth::PKCEChallenge instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    challenge: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    auth_token: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    refresh_token: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    id_token: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.Identity] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::PKCEChallenge instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    challenge: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    auth_token: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    refresh_token: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    id_token: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.Identity] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::PKCEChallenge instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    challenge: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    auth_token: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    refresh_token: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    id_token: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.Identity] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::PKCEChallenge instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
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


        Any = TypeVar("Any", bound="PKCEChallenge | Base")
    class __links__(Auditable.__links__):
        pass

if not TYPE_CHECKING:
    PKCEChallenge.__variants__.Base = PKCEChallenge



#
# type ext::auth::WebAuthnAuthenticationChallenge
#
class __WebAuthnAuthenticationChallenge_typeof__(__Auditable_typeof__):
    class __gel_reflection__(__Auditable_typeof__.__gel_reflection__):
        id = UUID(int=339891318179715780124275799861926483086)
        name = SchemaPath('ext', 'auth', 'WebAuthnAuthenticationChallenge')
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

    class __typeof__(__Auditable_typeof__.__typeof__):
        challenge = TypeAliasType('challenge', 'std.bytes')
        factors = TypeAliasType('factors', 'MultiLink[WebAuthnFactor]')


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
            created_at: datetime,
            modified_at: datetime,
            challenge: bytes,
            factors: Iterable[WebAuthnFactor] = [],
        ) -> None:
            """Create a new ext::auth::WebAuthnAuthenticationChallenge instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            challenge: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
            factors: type[ext_auth.WebAuthnFactor] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::WebAuthnAuthenticationChallenge instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            challenge: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bytes] | UnspecifiedType = Unspecified,
            factors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.WebAuthnFactor] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::WebAuthnAuthenticationChallenge instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            challenge: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
            factors: type[ext_auth.WebAuthnFactor] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::WebAuthnAuthenticationChallenge instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime,
                    modified_at: datetime,
                    challenge: bytes,
                    factors: Iterable[WebAuthnFactor] = [],
                ) -> None:
                    """Create a new ext::auth::WebAuthnAuthenticationChallenge instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    challenge: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
                    factors: type[ext_auth.WebAuthnFactor] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::WebAuthnAuthenticationChallenge instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    challenge: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bytes] | UnspecifiedType = Unspecified,
                    factors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.WebAuthnFactor] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::WebAuthnAuthenticationChallenge instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    challenge: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
                    factors: type[ext_auth.WebAuthnFactor] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::WebAuthnAuthenticationChallenge instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
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


        Any = TypeVar("Any", bound="WebAuthnAuthenticationChallenge | Base")
    class __links__(Auditable.__links__):
        pass

if not TYPE_CHECKING:
    WebAuthnAuthenticationChallenge.__variants__.Base = WebAuthnAuthenticationChallenge



#
# type ext::auth::WebAuthnRegistrationChallenge
#
class __WebAuthnRegistrationChallenge_typeof__(__Auditable_typeof__):
    class __gel_reflection__(__Auditable_typeof__.__gel_reflection__):
        id = UUID(int=306233804239267636046194582894504152618)
        name = SchemaPath('ext', 'auth', 'WebAuthnRegistrationChallenge')
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

    class __typeof__(__Auditable_typeof__.__typeof__):
        challenge = TypeAliasType('challenge', 'std.bytes')
        email = TypeAliasType('email', 'std.str')
        user_handle = TypeAliasType('user_handle', 'std.bytes')


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
            created_at: datetime,
            modified_at: datetime,
            challenge: bytes,
            email: str,
            user_handle: bytes,
        ) -> None:
            """Create a new ext::auth::WebAuthnRegistrationChallenge instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            challenge: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
            email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            user_handle: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::WebAuthnRegistrationChallenge instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            challenge: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bytes] | UnspecifiedType = Unspecified,
            email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            user_handle: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bytes] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::WebAuthnRegistrationChallenge instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            challenge: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
            email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            user_handle: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::WebAuthnRegistrationChallenge instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime,
                    modified_at: datetime,
                    challenge: bytes,
                    email: str,
                    user_handle: bytes,
                ) -> None:
                    """Create a new ext::auth::WebAuthnRegistrationChallenge instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    challenge: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
                    email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    user_handle: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::WebAuthnRegistrationChallenge instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    challenge: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bytes] | UnspecifiedType = Unspecified,
                    email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    user_handle: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bytes] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::WebAuthnRegistrationChallenge instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    challenge: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
                    email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    user_handle: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::WebAuthnRegistrationChallenge instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
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


        Any = TypeVar("Any", bound="WebAuthnRegistrationChallenge | Base")
    class __links__(Auditable.__links__):
        pass

if not TYPE_CHECKING:
    WebAuthnRegistrationChallenge.__variants__.Base = WebAuthnRegistrationChallenge



#
# type ext::auth::EmailPasswordProviderConfig
#
class __EmailPasswordProviderConfig_typeof__(__ProviderConfig_typeof__):
    class __gel_reflection__(__ProviderConfig_typeof__.__gel_reflection__):
        id = UUID(int=326379458322877692783219376957490095543)
        name = SchemaPath('ext', 'auth', 'EmailPasswordProviderConfig')
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

    class __typeof__(__ProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        require_verification = TypeAliasType('require_verification', 'std.bool')


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
            name: str,
            require_verification: bool,
        ) -> None:
            """Create a new ext::auth::EmailPasswordProviderConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            require_verification: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::EmailPasswordProviderConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            require_verification: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::EmailPasswordProviderConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            require_verification: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::EmailPasswordProviderConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: str,
                    require_verification: bool,
                ) -> None:
                    """Create a new ext::auth::EmailPasswordProviderConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    require_verification: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::EmailPasswordProviderConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    require_verification: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::EmailPasswordProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    require_verification: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::EmailPasswordProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    require_verification: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="EmailPasswordProviderConfig | Base")
    class __links__(ProviderConfig.__links__):
        pass

if not TYPE_CHECKING:
    EmailPasswordProviderConfig.__variants__.Base = EmailPasswordProviderConfig



#
# type ext::auth::MagicLinkProviderConfig
#
class __MagicLinkProviderConfig_typeof__(__ProviderConfig_typeof__):
    class __gel_reflection__(__ProviderConfig_typeof__.__gel_reflection__):
        id = UUID(int=197258520102777659735443006342865520155)
        name = SchemaPath('ext', 'auth', 'MagicLinkProviderConfig')
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

    class __typeof__(__ProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        token_time_to_live = TypeAliasType('token_time_to_live', 'std.duration')


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
            name: str,
            token_time_to_live: timedelta,
        ) -> None:
            """Create a new ext::auth::MagicLinkProviderConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            token_time_to_live: __datetime_1__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::MagicLinkProviderConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            token_time_to_live: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::MagicLinkProviderConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            token_time_to_live: __datetime_1__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::MagicLinkProviderConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: str,
                    token_time_to_live: timedelta,
                ) -> None:
                    """Create a new ext::auth::MagicLinkProviderConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    token_time_to_live: __datetime_1__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::MagicLinkProviderConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    token_time_to_live: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::MagicLinkProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    token_time_to_live: __datetime_1__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::MagicLinkProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    token_time_to_live: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="MagicLinkProviderConfig | Base")
    class __links__(ProviderConfig.__links__):
        pass

if not TYPE_CHECKING:
    MagicLinkProviderConfig.__variants__.Base = MagicLinkProviderConfig



#
# type ext::auth::OAuthProviderConfig
#
class __OAuthProviderConfig_typeof__(__ProviderConfig_typeof__):
    class __gel_reflection__(__ProviderConfig_typeof__.__gel_reflection__):
        id = UUID(int=176191875819755481847342667895462103654)
        name = SchemaPath('ext', 'auth', 'OAuthProviderConfig')
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

    class __typeof__(__ProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        secret = TypeAliasType('secret', 'std.str')
        client_id = TypeAliasType('client_id', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')
        additional_scope = TypeAliasType('additional_scope', 'OptionalProperty[std.str, str]')


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
            name: str,
            secret: str,
            client_id: str,
            display_name: str,
            additional_scope: str | None = None,
        ) -> None:
            """Create a new ext::auth::OAuthProviderConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
            """Update ext::auth::OAuthProviderConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::OAuthProviderConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            client_id: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            display_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            additional_scope: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::OAuthProviderConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: str,
                    secret: str,
                    client_id: str,
                    display_name: str,
                    additional_scope: str | None = None,
                ) -> None:
                    """Create a new ext::auth::OAuthProviderConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
                    """Update ext::auth::OAuthProviderConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::OAuthProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    client_id: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    display_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::OAuthProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
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


        Any = TypeVar("Any", bound="OAuthProviderConfig | Base")
    class __links__(ProviderConfig.__links__):
        pass

if not TYPE_CHECKING:
    OAuthProviderConfig.__variants__.Base = OAuthProviderConfig



#
# type ext::auth::WebAuthnProviderConfig
#
class __WebAuthnProviderConfig_typeof__(__ProviderConfig_typeof__):
    class __gel_reflection__(__ProviderConfig_typeof__.__gel_reflection__):
        id = UUID(int=18693980672146206883873808188444327649)
        name = SchemaPath('ext', 'auth', 'WebAuthnProviderConfig')
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

    class __typeof__(__ProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        relying_party_origin = TypeAliasType('relying_party_origin', 'std.str')
        require_verification = TypeAliasType('require_verification', 'std.bool')


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
            name: str,
            relying_party_origin: str,
            require_verification: bool,
        ) -> None:
            """Create a new ext::auth::WebAuthnProviderConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            relying_party_origin: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            require_verification: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::WebAuthnProviderConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            relying_party_origin: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            require_verification: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::WebAuthnProviderConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            relying_party_origin: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            require_verification: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::WebAuthnProviderConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: str,
                    relying_party_origin: str,
                    require_verification: bool,
                ) -> None:
                    """Create a new ext::auth::WebAuthnProviderConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    relying_party_origin: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    require_verification: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::WebAuthnProviderConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    relying_party_origin: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    require_verification: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::WebAuthnProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    relying_party_origin: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    require_verification: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::WebAuthnProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
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


        Any = TypeVar("Any", bound="WebAuthnProviderConfig | Base")
    class __links__(ProviderConfig.__links__):
        pass

if not TYPE_CHECKING:
    WebAuthnProviderConfig.__variants__.Base = WebAuthnProviderConfig



#
# type ext::auth::EmailFactor
#
class __EmailFactor_typeof__(__Factor_typeof__):
    class __gel_reflection__(__Factor_typeof__.__gel_reflection__):
        id = UUID(int=267038974621553903381178302575855343752)
        name = SchemaPath('ext', 'auth', 'EmailFactor')
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

    class __typeof__(__Factor_typeof__.__typeof__):
        email = TypeAliasType('email', 'std.str')
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
            created_at: datetime,
            modified_at: datetime,
            identity: LocalIdentity | None = None,
            email: str,
            verified_at: datetime | None = None,
        ) -> None:
            """Create a new ext::auth::EmailFactor instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            verified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::EmailFactor instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            verified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::EmailFactor instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            verified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::EmailFactor instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        class Base(__EmailFactor_typeof__, Factor.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime,
                    modified_at: datetime,
                    identity: LocalIdentity | None = None,
                    email: str,
                    verified_at: datetime | None = None,
                ) -> None:
                    """Create a new ext::auth::EmailFactor instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    verified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::EmailFactor instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    verified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::EmailFactor instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    verified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::EmailFactor instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
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


        Any = TypeVar("Any", bound="EmailFactor | Base")
    class __links__(Factor.__links__):
        pass

if not TYPE_CHECKING:
    EmailFactor.__variants__.Base = EmailFactor



#
# type ext::auth::LocalIdentity
#
class __LocalIdentity_typeof__(__Identity_typeof__):
    class __gel_reflection__(__Identity_typeof__.__gel_reflection__):
        id = UUID(int=160831847510468337518667602858609567942)
        name = SchemaPath('ext', 'auth', 'LocalIdentity')
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

    class __typeof__(__Identity_typeof__.__typeof__):
        subject = TypeAliasType('subject', 'std.str')


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
            created_at: datetime,
            modified_at: datetime,
            issuer: str,
            subject: str,
        ) -> None:
            """Create a new ext::auth::LocalIdentity instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            issuer: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            subject: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::LocalIdentity instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            issuer: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            subject: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::LocalIdentity instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            issuer: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            subject: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::LocalIdentity instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        class Base(__LocalIdentity_typeof__, Identity.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime,
                    modified_at: datetime,
                    issuer: str,
                    subject: str,
                ) -> None:
                    """Create a new ext::auth::LocalIdentity instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    issuer: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    subject: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::LocalIdentity instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    issuer: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    subject: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::LocalIdentity instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    issuer: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    subject: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::LocalIdentity instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
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


        Any = TypeVar("Any", bound="LocalIdentity | Base")
    class __links__(Identity.__links__):
        pass

if not TYPE_CHECKING:
    LocalIdentity.__variants__.Base = LocalIdentity



#
# type ext::auth::AppleOAuthProvider
#
class __AppleOAuthProvider_typeof__(__OAuthProviderConfig_typeof__):
    class __gel_reflection__(
        __OAuthProviderConfig_typeof__.__gel_reflection__,
    ):
        id = UUID(int=43000943290657793977966224514992214452)
        name = SchemaPath('ext', 'auth', 'AppleOAuthProvider')
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

    class __typeof__(__OAuthProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')


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
            name: str,
            secret: str,
            client_id: str,
            display_name: str,
            additional_scope: str | None = None,
        ) -> None:
            """Create a new ext::auth::AppleOAuthProvider instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
            """Update ext::auth::AppleOAuthProvider instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::AppleOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            client_id: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            display_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            additional_scope: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::AppleOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: str,
                    secret: str,
                    client_id: str,
                    display_name: str,
                    additional_scope: str | None = None,
                ) -> None:
                    """Create a new ext::auth::AppleOAuthProvider instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
                    """Update ext::auth::AppleOAuthProvider instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::AppleOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    client_id: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    display_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::AppleOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
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


        Any = TypeVar("Any", bound="AppleOAuthProvider | Base")
    class __links__(OAuthProviderConfig.__links__):
        pass

if not TYPE_CHECKING:
    AppleOAuthProvider.__variants__.Base = AppleOAuthProvider



#
# type ext::auth::AzureOAuthProvider
#
class __AzureOAuthProvider_typeof__(__OAuthProviderConfig_typeof__):
    class __gel_reflection__(
        __OAuthProviderConfig_typeof__.__gel_reflection__,
    ):
        id = UUID(int=189177822115181231528998530125922317735)
        name = SchemaPath('ext', 'auth', 'AzureOAuthProvider')
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

    class __typeof__(__OAuthProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')


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
            name: str,
            secret: str,
            client_id: str,
            display_name: str,
            additional_scope: str | None = None,
        ) -> None:
            """Create a new ext::auth::AzureOAuthProvider instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
            """Update ext::auth::AzureOAuthProvider instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::AzureOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            client_id: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            display_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            additional_scope: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::AzureOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: str,
                    secret: str,
                    client_id: str,
                    display_name: str,
                    additional_scope: str | None = None,
                ) -> None:
                    """Create a new ext::auth::AzureOAuthProvider instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
                    """Update ext::auth::AzureOAuthProvider instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::AzureOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    client_id: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    display_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::AzureOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
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


        Any = TypeVar("Any", bound="AzureOAuthProvider | Base")
    class __links__(OAuthProviderConfig.__links__):
        pass

if not TYPE_CHECKING:
    AzureOAuthProvider.__variants__.Base = AzureOAuthProvider



#
# type ext::auth::DiscordOAuthProvider
#
class __DiscordOAuthProvider_typeof__(__OAuthProviderConfig_typeof__):
    class __gel_reflection__(
        __OAuthProviderConfig_typeof__.__gel_reflection__,
    ):
        id = UUID(int=24018239224398776296098705400907496501)
        name = SchemaPath('ext', 'auth', 'DiscordOAuthProvider')
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

    class __typeof__(__OAuthProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')


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
            name: str,
            secret: str,
            client_id: str,
            display_name: str,
            additional_scope: str | None = None,
        ) -> None:
            """Create a new ext::auth::DiscordOAuthProvider instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
            """Update ext::auth::DiscordOAuthProvider instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::DiscordOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            client_id: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            display_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            additional_scope: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::DiscordOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: str,
                    secret: str,
                    client_id: str,
                    display_name: str,
                    additional_scope: str | None = None,
                ) -> None:
                    """Create a new ext::auth::DiscordOAuthProvider instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
                    """Update ext::auth::DiscordOAuthProvider instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::DiscordOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    client_id: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    display_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::DiscordOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
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


        Any = TypeVar("Any", bound="DiscordOAuthProvider | Base")
    class __links__(OAuthProviderConfig.__links__):
        pass

if not TYPE_CHECKING:
    DiscordOAuthProvider.__variants__.Base = DiscordOAuthProvider



#
# type ext::auth::GitHubOAuthProvider
#
class __GitHubOAuthProvider_typeof__(__OAuthProviderConfig_typeof__):
    class __gel_reflection__(
        __OAuthProviderConfig_typeof__.__gel_reflection__,
    ):
        id = UUID(int=135303881089532318040492385271633596804)
        name = SchemaPath('ext', 'auth', 'GitHubOAuthProvider')
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

    class __typeof__(__OAuthProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')


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
            name: str,
            secret: str,
            client_id: str,
            display_name: str,
            additional_scope: str | None = None,
        ) -> None:
            """Create a new ext::auth::GitHubOAuthProvider instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
            """Update ext::auth::GitHubOAuthProvider instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::GitHubOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            client_id: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            display_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            additional_scope: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::GitHubOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: str,
                    secret: str,
                    client_id: str,
                    display_name: str,
                    additional_scope: str | None = None,
                ) -> None:
                    """Create a new ext::auth::GitHubOAuthProvider instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
                    """Update ext::auth::GitHubOAuthProvider instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::GitHubOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    client_id: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    display_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::GitHubOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
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


        Any = TypeVar("Any", bound="GitHubOAuthProvider | Base")
    class __links__(OAuthProviderConfig.__links__):
        pass

if not TYPE_CHECKING:
    GitHubOAuthProvider.__variants__.Base = GitHubOAuthProvider



#
# type ext::auth::GoogleOAuthProvider
#
class __GoogleOAuthProvider_typeof__(__OAuthProviderConfig_typeof__):
    class __gel_reflection__(
        __OAuthProviderConfig_typeof__.__gel_reflection__,
    ):
        id = UUID(int=314152047091060873466459255621715246895)
        name = SchemaPath('ext', 'auth', 'GoogleOAuthProvider')
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

    class __typeof__(__OAuthProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')


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
            name: str,
            secret: str,
            client_id: str,
            display_name: str,
            additional_scope: str | None = None,
        ) -> None:
            """Create a new ext::auth::GoogleOAuthProvider instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
            """Update ext::auth::GoogleOAuthProvider instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::GoogleOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            client_id: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            display_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            additional_scope: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::GoogleOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: str,
                    secret: str,
                    client_id: str,
                    display_name: str,
                    additional_scope: str | None = None,
                ) -> None:
                    """Create a new ext::auth::GoogleOAuthProvider instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
                    """Update ext::auth::GoogleOAuthProvider instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::GoogleOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    client_id: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    display_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::GoogleOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
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


        Any = TypeVar("Any", bound="GoogleOAuthProvider | Base")
    class __links__(OAuthProviderConfig.__links__):
        pass

if not TYPE_CHECKING:
    GoogleOAuthProvider.__variants__.Base = GoogleOAuthProvider



#
# type ext::auth::OpenIDConnectProvider
#
class __OpenIDConnectProvider_typeof__(__OAuthProviderConfig_typeof__):
    class __gel_reflection__(
        __OAuthProviderConfig_typeof__.__gel_reflection__,
    ):
        id = UUID(int=266535682383167007985348307161960435089)
        name = SchemaPath('ext', 'auth', 'OpenIDConnectProvider')
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

    class __typeof__(__OAuthProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')
        issuer_url = TypeAliasType('issuer_url', 'std.str')
        logo_url = TypeAliasType('logo_url', 'OptionalProperty[std.str, str]')


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
            name: str,
            secret: str,
            client_id: str,
            display_name: str,
            additional_scope: str | None = None,
            issuer_url: str,
            logo_url: str | None = None,
        ) -> None:
            """Create a new ext::auth::OpenIDConnectProvider instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            issuer_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            logo_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::OpenIDConnectProvider instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            issuer_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            logo_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::OpenIDConnectProvider instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            client_id: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            display_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            additional_scope: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            issuer_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            logo_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::OpenIDConnectProvider instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: str,
                    secret: str,
                    client_id: str,
                    display_name: str,
                    additional_scope: str | None = None,
                    issuer_url: str,
                    logo_url: str | None = None,
                ) -> None:
                    """Create a new ext::auth::OpenIDConnectProvider instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    issuer_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    logo_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::OpenIDConnectProvider instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    issuer_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    logo_url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::OpenIDConnectProvider instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    client_id: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    display_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    issuer_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    logo_url: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::OpenIDConnectProvider instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
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


        Any = TypeVar("Any", bound="OpenIDConnectProvider | Base")
    class __links__(OAuthProviderConfig.__links__):
        pass

if not TYPE_CHECKING:
    OpenIDConnectProvider.__variants__.Base = OpenIDConnectProvider



#
# type ext::auth::SlackOAuthProvider
#
class __SlackOAuthProvider_typeof__(__OAuthProviderConfig_typeof__):
    class __gel_reflection__(
        __OAuthProviderConfig_typeof__.__gel_reflection__,
    ):
        id = UUID(int=203801692607706301177517492230120464917)
        name = SchemaPath('ext', 'auth', 'SlackOAuthProvider')
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

    class __typeof__(__OAuthProviderConfig_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        display_name = TypeAliasType('display_name', 'std.str')


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
            name: str,
            secret: str,
            client_id: str,
            display_name: str,
            additional_scope: str | None = None,
        ) -> None:
            """Create a new ext::auth::SlackOAuthProvider instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
            """Update ext::auth::SlackOAuthProvider instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::SlackOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            client_id: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            display_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            additional_scope: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::SlackOAuthProvider instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: str,
                    secret: str,
                    client_id: str,
                    display_name: str,
                    additional_scope: str | None = None,
                ) -> None:
                    """Create a new ext::auth::SlackOAuthProvider instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
                    """Update ext::auth::SlackOAuthProvider instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    client_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    display_name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::SlackOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    client_id: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    display_name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    additional_scope: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::SlackOAuthProvider instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
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


        Any = TypeVar("Any", bound="SlackOAuthProvider | Base")
    class __links__(OAuthProviderConfig.__links__):
        pass

if not TYPE_CHECKING:
    SlackOAuthProvider.__variants__.Base = SlackOAuthProvider



#
# type ext::auth::EmailPasswordFactor
#
class __EmailPasswordFactor_typeof__(__EmailFactor_typeof__):
    class __gel_reflection__(__EmailFactor_typeof__.__gel_reflection__):
        id = UUID(int=31172435047994255941611898216302058127)
        name = SchemaPath('ext', 'auth', 'EmailPasswordFactor')
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

    class __typeof__(__EmailFactor_typeof__.__typeof__):
        email = TypeAliasType('email', 'std.str')
        password_hash = TypeAliasType('password_hash', 'std.str')


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
            created_at: datetime,
            modified_at: datetime,
            identity: LocalIdentity | None = None,
            email: str,
            verified_at: datetime | None = None,
            password_hash: str,
        ) -> None:
            """Create a new ext::auth::EmailPasswordFactor instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            verified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            password_hash: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::EmailPasswordFactor instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            verified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            password_hash: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::EmailPasswordFactor instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            verified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            password_hash: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::EmailPasswordFactor instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime,
                    modified_at: datetime,
                    identity: LocalIdentity | None = None,
                    email: str,
                    verified_at: datetime | None = None,
                    password_hash: str,
                ) -> None:
                    """Create a new ext::auth::EmailPasswordFactor instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    verified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    password_hash: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::EmailPasswordFactor instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    verified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    password_hash: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::EmailPasswordFactor instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    verified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    password_hash: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::EmailPasswordFactor instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
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


        Any = TypeVar("Any", bound="EmailPasswordFactor | Base")
    class __links__(EmailFactor.__links__):
        pass

if not TYPE_CHECKING:
    EmailPasswordFactor.__variants__.Base = EmailPasswordFactor



#
# type ext::auth::MagicLinkFactor
#
class __MagicLinkFactor_typeof__(__EmailFactor_typeof__):
    class __gel_reflection__(__EmailFactor_typeof__.__gel_reflection__):
        id = UUID(int=61743578138936630624449892961906140358)
        name = SchemaPath('ext', 'auth', 'MagicLinkFactor')
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

    class __typeof__(__EmailFactor_typeof__.__typeof__):
        email = TypeAliasType('email', 'std.str')


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
            created_at: datetime,
            modified_at: datetime,
            identity: LocalIdentity | None = None,
            email: str,
            verified_at: datetime | None = None,
        ) -> None:
            """Create a new ext::auth::MagicLinkFactor instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            verified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::MagicLinkFactor instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            verified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::MagicLinkFactor instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            verified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::MagicLinkFactor instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        class Base(__MagicLinkFactor_typeof__, EmailFactor.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime,
                    modified_at: datetime,
                    identity: LocalIdentity | None = None,
                    email: str,
                    verified_at: datetime | None = None,
                ) -> None:
                    """Create a new ext::auth::MagicLinkFactor instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    verified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::MagicLinkFactor instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    verified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::MagicLinkFactor instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    verified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::MagicLinkFactor instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
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


        Any = TypeVar("Any", bound="MagicLinkFactor | Base")
    class __links__(EmailFactor.__links__):
        pass

if not TYPE_CHECKING:
    MagicLinkFactor.__variants__.Base = MagicLinkFactor



#
# type ext::auth::WebAuthnFactor
#
class __WebAuthnFactor_typeof__(__EmailFactor_typeof__):
    class __gel_reflection__(__EmailFactor_typeof__.__gel_reflection__):
        id = UUID(int=114805788310269968559926717489578765583)
        name = SchemaPath('ext', 'auth', 'WebAuthnFactor')
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

    class __typeof__(__EmailFactor_typeof__.__typeof__):
        user_handle = TypeAliasType('user_handle', 'std.bytes')
        credential_id = TypeAliasType('credential_id', 'std.bytes')
        public_key = TypeAliasType('public_key', 'std.bytes')


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
            created_at: datetime,
            modified_at: datetime,
            identity: LocalIdentity | None = None,
            email: str,
            verified_at: datetime | None = None,
            user_handle: bytes,
            credential_id: bytes,
            public_key: bytes,
        ) -> None:
            """Create a new ext::auth::WebAuthnFactor instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            verified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            user_handle: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
            credential_id: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
            public_key: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update ext::auth::WebAuthnFactor instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            verified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            user_handle: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bytes] | UnspecifiedType = Unspecified,
            credential_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bytes] | UnspecifiedType = Unspecified,
            public_key: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bytes] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch ext::auth::WebAuthnFactor instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
            email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            verified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            user_handle: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
            credential_id: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
            public_key: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch ext::auth::WebAuthnFactor instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
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
        class Base(__WebAuthnFactor_typeof__, EmailFactor.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime,
                    modified_at: datetime,
                    identity: LocalIdentity | None = None,
                    email: str,
                    verified_at: datetime | None = None,
                    user_handle: bytes,
                    credential_id: bytes,
                    public_key: bytes,
                ) -> None:
                    """Create a new ext::auth::WebAuthnFactor instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    verified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    user_handle: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
                    credential_id: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
                    public_key: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update ext::auth::WebAuthnFactor instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    identity: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    verified_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    user_handle: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bytes] | UnspecifiedType = Unspecified,
                    credential_id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bytes] | UnspecifiedType = Unspecified,
                    public_key: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bytes] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch ext::auth::WebAuthnFactor instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    modified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    identity: type[ext_auth.LocalIdentity] | UnspecifiedType = Unspecified,
                    email: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    verified_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    user_handle: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
                    credential_id: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
                    public_key: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch ext::auth::WebAuthnFactor instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
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


        Any = TypeVar("Any", bound="WebAuthnFactor | Base")
    class __links__(EmailFactor.__links__):
        pass

if not TYPE_CHECKING:
    WebAuthnFactor.__variants__.Base = WebAuthnFactor



from builtins import bool, bytes, str  # noqa: E402 F403
from datetime import datetime, timedelta  # noqa: E402 F403
