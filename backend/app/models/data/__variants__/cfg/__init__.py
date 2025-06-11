#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from .. import std

import gel as gel
from gel import ConfigMemory
from gel.models.pydantic import (
    AnnotatedExpr,
    AnyEnum,
    ComputedMultiLink,
    Direction,
    EmptyDirection,
    ExprCompatible,
    InfixOp,
    LazyClassProperty,
    MultiLink,
    OptionalLink,
    OptionalProperty,
    PathAlias,
    PrefixOp,
    PyConstType,
    PyTypeScalar,
    SchemaPath,
    Unspecified,
    UnspecifiedType
)

import builtins as __builtins_2__
import builtins as __builtins_1__
import builtins as __builtins__
import datetime as datetime
from builtins import str, tuple, type
from collections.abc import Callable, Iterable
from typing import Any, TYPE_CHECKING, TypeVar
from typing_extensions import Self, TypeAliasType
from uuid import UUID

if TYPE_CHECKING:

    from .. import std as __std__, sys as __sys__
    from ... import cfg, schema

    import builtins as builtins
    from typing import ClassVar


class AllowBareDDL(AnyEnum):
    AlwaysAllow = 'AlwaysAllow'
    NeverAllow = 'NeverAllow'


class ConnectionTransport(AnyEnum):
    TCP = 'TCP'
    TCP_PG = 'TCP_PG'
    HTTP = 'HTTP'
    SIMPLE_HTTP = 'SIMPLE_HTTP'
    HTTP_METRICS = 'HTTP_METRICS'
    HTTP_HEALTH = 'HTTP_HEALTH'


class QueryCacheMode(AnyEnum):
    InMemory = 'InMemory'
    RegInline = 'RegInline'
    PgFunc = 'PgFunc'
    Default = 'Default'


class QueryStatsOption(AnyEnum):
    None_ = 'None'
    All = 'All'


class SMTPSecurity(AnyEnum):
    PlainText = 'PlainText'
    TLS = 'TLS'
    STARTTLS = 'STARTTLS'
    STARTTLSOrPlainText = 'STARTTLSOrPlainText'


class StoreMigrationSDL(AnyEnum):
    AlwaysStore = 'AlwaysStore'
    NeverStore = 'NeverStore'



class __memory_meta__(std.__anyscalar_meta__):
    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: gel.ConfigMemory | memory | type[memory],
    ) -> builtins.type[__std__.bool]:
        match other:
            case gel.ConfigMemory():
                other = memory(other)
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: gel.ConfigMemory | memory | type[memory],
    ) -> builtins.type[__std__.bool]:
        match other:
            case gel.ConfigMemory():
                other = memory(other)
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: gel.ConfigMemory | memory | type[memory],
    ) -> builtins.type[__std__.bool]:
        match other:
            case gel.ConfigMemory():
                other = memory(other)
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: gel.ConfigMemory | memory | type[memory],
    ) -> builtins.type[__std__.bool]:
        match other:
            case gel.ConfigMemory():
                other = memory(other)
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: gel.ConfigMemory | memory | type[memory],
    ) -> builtins.type[__std__.bool]:
        match other:
            case gel.ConfigMemory():
                other = memory(other)
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: gel.ConfigMemory | memory | type[memory],
    ) -> builtins.type[__std__.bool]:
        match other:
            case gel.ConfigMemory():
                other = memory(other)
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class memory(
        PyTypeScalar[ConfigMemory],
        std.anyscalar,
        metaclass=__memory_meta__,
    ):
        class __gel_reflection__(__std__.anyscalar.__gel_reflection__):
            id = UUID(int=304)
            name = SchemaPath('cfg', 'memory')

if not TYPE_CHECKING:
    class memory(ConfigMemory, PyTypeScalar[ConfigMemory], std.anyscalar):
        __gel_type_class__: ClassVar[type] = __memory_meta__

        class __gel_reflection__(std.anyscalar.__gel_reflection__):
            id = UUID(int=304)
            name = SchemaPath('cfg', 'memory')




#
# type cfg::ConfigObject
#
class __ConfigObject_typeof__(std.__BaseObject_typeof__):
    class __gel_reflection__(std.__BaseObject_typeof__.__gel_reflection__):
        id = UUID(int=281837877222500969229845324319074851211)
        name = SchemaPath('cfg', 'ConfigObject')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=281837877222500969229845324319074851211),
                name='cfg::ConfigObject',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__(std.__BaseObject_typeof__.__typeof__):
        pass


class ConfigObject(
    __ConfigObject_typeof__,
    std.BaseObject,
    __gel_type_id__=UUID(int=281837877222500969229845324319074851211),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new cfg::ConfigObject instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
            """Update cfg::ConfigObject instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::ConfigObject instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::ConfigObject instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
            id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(std.BaseObject.__variants__):
        class Base(__ConfigObject_typeof__, std.BaseObject.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new cfg::ConfigObject instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
                    """Update cfg::ConfigObject instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::ConfigObject instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::ConfigObject instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
                    id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="ConfigObject | Base")
    class __links__(std.BaseObject.__links__):
        pass

if not TYPE_CHECKING:
    ConfigObject.__variants__.Base = ConfigObject



#
# type cfg::AbstractConfig
#
class __AbstractConfig_typeof__(__ConfigObject_typeof__):
    class __gel_reflection__(__ConfigObject_typeof__.__gel_reflection__):
        id = UUID(int=185296995099711029544002424773202172471)
        name = SchemaPath('cfg', 'AbstractConfig')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=185296995099711029544002424773202172471),
                name='cfg::AbstractConfig',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__(__ConfigObject_typeof__.__typeof__):
        default_transaction_access_mode = TypeAliasType('default_transaction_access_mode', 'sys.TransactionAccessMode')
        session_idle_timeout = TypeAliasType('session_idle_timeout', 'std.duration')
        default_transaction_isolation = TypeAliasType('default_transaction_isolation', 'sys.TransactionIsolation')
        default_transaction_deferrable = TypeAliasType('default_transaction_deferrable', 'sys.TransactionDeferrability')
        session_idle_transaction_timeout = TypeAliasType('session_idle_transaction_timeout', 'std.duration')
        query_execution_timeout = TypeAliasType('query_execution_timeout', 'std.duration')
        listen_port = TypeAliasType('listen_port', 'std.int32')
        listen_addresses = TypeAliasType('listen_addresses', 'list[str]')
        current_email_provider_name = TypeAliasType('current_email_provider_name', 'OptionalProperty[std.str, str]')
        allow_dml_in_functions = TypeAliasType('allow_dml_in_functions', 'OptionalProperty[std.bool, bool]')
        allow_bare_ddl = TypeAliasType('allow_bare_ddl', 'OptionalProperty[AllowBareDDL, str]')
        store_migration_sdl = TypeAliasType('store_migration_sdl', 'OptionalProperty[StoreMigrationSDL, str]')
        apply_access_policies = TypeAliasType('apply_access_policies', 'OptionalProperty[std.bool, bool]')
        apply_access_policies_pg = TypeAliasType('apply_access_policies_pg', 'OptionalProperty[std.bool, bool]')
        allow_user_specified_id = TypeAliasType('allow_user_specified_id', 'OptionalProperty[std.bool, bool]')
        simple_scoping = TypeAliasType('simple_scoping', 'OptionalProperty[std.bool, bool]')
        warn_old_scoping = TypeAliasType('warn_old_scoping', 'OptionalProperty[std.bool, bool]')
        cors_allow_origins = TypeAliasType('cors_allow_origins', 'list[str]')
        auto_rebuild_query_cache = TypeAliasType('auto_rebuild_query_cache', 'OptionalProperty[std.bool, bool]')
        auto_rebuild_query_cache_timeout = TypeAliasType('auto_rebuild_query_cache_timeout', 'OptionalProperty[std.duration, timedelta]')
        query_cache_mode = TypeAliasType('query_cache_mode', 'OptionalProperty[QueryCacheMode, str]')
        http_max_connections = TypeAliasType('http_max_connections', 'OptionalProperty[std.int64, int]')
        shared_buffers = TypeAliasType('shared_buffers', 'OptionalProperty[memory, ConfigMemory]')
        query_work_mem = TypeAliasType('query_work_mem', 'OptionalProperty[memory, ConfigMemory]')
        maintenance_work_mem = TypeAliasType('maintenance_work_mem', 'OptionalProperty[memory, ConfigMemory]')
        effective_cache_size = TypeAliasType('effective_cache_size', 'OptionalProperty[memory, ConfigMemory]')
        effective_io_concurrency = TypeAliasType('effective_io_concurrency', 'OptionalProperty[std.int64, int]')
        default_statistics_target = TypeAliasType('default_statistics_target', 'OptionalProperty[std.int64, int]')
        force_database_error = TypeAliasType('force_database_error', 'OptionalProperty[std.str, str]')
        _pg_prepared_statement_cache_size = TypeAliasType('_pg_prepared_statement_cache_size', 'std.int16')
        track_query_stats = TypeAliasType('track_query_stats', 'OptionalProperty[QueryStatsOption, str]')
        extensions = TypeAliasType('extensions', 'ComputedMultiLink[ExtensionConfig]')
        auth = TypeAliasType('auth', 'MultiLink[Auth]')
        email_providers = TypeAliasType('email_providers', 'MultiLink[EmailProviderConfig]')


class AbstractConfig(
    __AbstractConfig_typeof__,
    ConfigObject,
    __gel_type_id__=UUID(int=185296995099711029544002424773202172471),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            default_transaction_access_mode: str,
            session_idle_timeout: timedelta,
            default_transaction_isolation: str,
            default_transaction_deferrable: str,
            session_idle_transaction_timeout: timedelta,
            query_execution_timeout: timedelta,
            listen_port: int,
            listen_addresses: Iterable[str] = [],
            current_email_provider_name: str | None = None,
            allow_dml_in_functions: bool | None = None,
            allow_bare_ddl: str | None = None,
            store_migration_sdl: str | None = None,
            apply_access_policies: bool | None = None,
            apply_access_policies_pg: bool | None = None,
            allow_user_specified_id: bool | None = None,
            simple_scoping: bool | None = None,
            warn_old_scoping: bool | None = None,
            cors_allow_origins: Iterable[str] = [],
            auto_rebuild_query_cache: bool | None = None,
            auto_rebuild_query_cache_timeout: timedelta | None = None,
            query_cache_mode: str | None = None,
            http_max_connections: int | None = None,
            shared_buffers: ConfigMemory | None = None,
            query_work_mem: ConfigMemory | None = None,
            maintenance_work_mem: ConfigMemory | None = None,
            effective_cache_size: ConfigMemory | None = None,
            effective_io_concurrency: int | None = None,
            default_statistics_target: int | None = None,
            force_database_error: str | None = None,
            _pg_prepared_statement_cache_size: int,
            track_query_stats: str | None = None,
            auth: Iterable[Auth] = [],
            email_providers: Iterable[EmailProviderConfig] = [],
        ) -> None:
            """Create a new cfg::AbstractConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            default_transaction_access_mode: type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            listen_port: __builtins_1__.int | type[__std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: str | type[__std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: str | type[__std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: str | type[__std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: str | type[__std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: __builtins_1__.int | type[__std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
            auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update cfg::AbstractConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            default_transaction_access_mode: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            listen_port: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryStatsOption] | UnspecifiedType = Unspecified,
            extensions: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
            auth: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::AbstractConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            default_transaction_access_mode: type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            listen_port: __builtins_1__.int | type[__std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: str | type[__std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: str | type[__std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: str | type[__std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: str | type[__std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: __builtins_1__.int | type[__std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
            extensions: type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
            auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::AbstractConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
            id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            session_idle_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            query_execution_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            listen_port: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            listen_addresses: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            apply_access_policies: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            allow_user_specified_id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            simple_scoping: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            warn_old_scoping: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            cors_allow_origins: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            http_max_connections: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            shared_buffers: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            query_work_mem: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            maintenance_work_mem: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            effective_cache_size: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            effective_io_concurrency: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            default_statistics_target: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            force_database_error: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ConfigObject.__variants__):
        class Base(__AbstractConfig_typeof__, ConfigObject.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    default_transaction_access_mode: str,
                    session_idle_timeout: timedelta,
                    default_transaction_isolation: str,
                    default_transaction_deferrable: str,
                    session_idle_transaction_timeout: timedelta,
                    query_execution_timeout: timedelta,
                    listen_port: int,
                    listen_addresses: Iterable[str] = [],
                    current_email_provider_name: str | None = None,
                    allow_dml_in_functions: bool | None = None,
                    allow_bare_ddl: str | None = None,
                    store_migration_sdl: str | None = None,
                    apply_access_policies: bool | None = None,
                    apply_access_policies_pg: bool | None = None,
                    allow_user_specified_id: bool | None = None,
                    simple_scoping: bool | None = None,
                    warn_old_scoping: bool | None = None,
                    cors_allow_origins: Iterable[str] = [],
                    auto_rebuild_query_cache: bool | None = None,
                    auto_rebuild_query_cache_timeout: timedelta | None = None,
                    query_cache_mode: str | None = None,
                    http_max_connections: int | None = None,
                    shared_buffers: ConfigMemory | None = None,
                    query_work_mem: ConfigMemory | None = None,
                    maintenance_work_mem: ConfigMemory | None = None,
                    effective_cache_size: ConfigMemory | None = None,
                    effective_io_concurrency: int | None = None,
                    default_statistics_target: int | None = None,
                    force_database_error: str | None = None,
                    _pg_prepared_statement_cache_size: int,
                    track_query_stats: str | None = None,
                    auth: Iterable[Auth] = [],
                    email_providers: Iterable[EmailProviderConfig] = [],
                ) -> None:
                    """Create a new cfg::AbstractConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    default_transaction_access_mode: type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: __builtins_1__.int | type[__std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: __builtins_1__.int | type[__std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update cfg::AbstractConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    default_transaction_access_mode: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    extensions: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
                    auth: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::AbstractConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    default_transaction_access_mode: type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: __builtins_1__.int | type[__std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: __builtins_1__.int | type[__std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    extensions: type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
                    auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::AbstractConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
                    id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    session_idle_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    query_execution_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    listen_port: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    listen_addresses: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    apply_access_policies: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    simple_scoping: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    warn_old_scoping: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    cors_allow_origins: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    http_max_connections: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    shared_buffers: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    query_work_mem: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    effective_cache_size: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    default_statistics_target: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    force_database_error: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="AbstractConfig | Base")
    class __links__(ConfigObject.__links__):
        pass

if not TYPE_CHECKING:
    AbstractConfig.__variants__.Base = AbstractConfig



#
# type cfg::Auth
#
class __Auth_typeof__(__ConfigObject_typeof__):
    class __gel_reflection__(__ConfigObject_typeof__.__gel_reflection__):
        id = UUID(int=216303077383272593199434166037523439239)
        name = SchemaPath('cfg', 'Auth')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=216303077383272593199434166037523439239),
                name='cfg::Auth',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__ConfigObject_typeof__.__typeof__):
        priority = TypeAliasType('priority', 'std.int64')
        user = TypeAliasType('user', 'list[str]')
        comment = TypeAliasType('comment', 'OptionalProperty[std.str, str]')
        method = TypeAliasType('method', 'OptionalLink[AuthMethod]')


class Auth(
    __Auth_typeof__,
    ConfigObject,
    __gel_type_id__=UUID(int=216303077383272593199434166037523439239),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            priority: int,
            user: Iterable[str] = [],
            comment: str | None = None,
            method: AuthMethod | None = None,
        ) -> None:
            """Create a new cfg::Auth instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
            """Update cfg::Auth instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            priority: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
            user: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            comment: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            method: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.AuthMethod] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::Auth instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            priority: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            user: str | type[__std__.str] | UnspecifiedType = Unspecified,
            comment: str | type[__std__.str] | UnspecifiedType = Unspecified,
            method: type[cfg.AuthMethod] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::Auth instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
            id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            priority: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            user: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            comment: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ConfigObject.__variants__):
        class Base(__Auth_typeof__, ConfigObject.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    priority: int,
                    user: Iterable[str] = [],
                    comment: str | None = None,
                    method: AuthMethod | None = None,
                ) -> None:
                    """Create a new cfg::Auth instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
                    """Update cfg::Auth instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    priority: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
                    user: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    comment: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    method: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.AuthMethod] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::Auth instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    priority: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    user: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    comment: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    method: type[cfg.AuthMethod] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::Auth instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
                    id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    priority: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    user: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    comment: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Auth | Base")
    class __links__(ConfigObject.__links__):
        pass

if not TYPE_CHECKING:
    Auth.__variants__.Base = Auth



#
# type cfg::AuthMethod
#
class __AuthMethod_typeof__(__ConfigObject_typeof__):
    class __gel_reflection__(__ConfigObject_typeof__.__gel_reflection__):
        id = UUID(int=24672750186835429802611635273495390145)
        name = SchemaPath('cfg', 'AuthMethod')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=24672750186835429802611635273495390145),
                name='cfg::AuthMethod',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__(__ConfigObject_typeof__.__typeof__):
        transports = TypeAliasType('transports', 'list[str]')


class AuthMethod(
    __AuthMethod_typeof__,
    ConfigObject,
    __gel_type_id__=UUID(int=24672750186835429802611635273495390145),
):
    if TYPE_CHECKING:
        def __init__(self, /, *, transports: Iterable[str] = []) -> None:
            """Create a new cfg::AuthMethod instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
            """Update cfg::AuthMethod instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            transports: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::AuthMethod instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::AuthMethod instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
            id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ConfigObject.__variants__):
        class Base(__AuthMethod_typeof__, ConfigObject.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    transports: Iterable[str] = [],
                ) -> None:
                    """Create a new cfg::AuthMethod instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
                    """Update cfg::AuthMethod instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    transports: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::AuthMethod instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::AuthMethod instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
                    id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="AuthMethod | Base")
    class __links__(ConfigObject.__links__):
        pass

if not TYPE_CHECKING:
    AuthMethod.__variants__.Base = AuthMethod



#
# type cfg::EmailProviderConfig
#
class __EmailProviderConfig_typeof__(__ConfigObject_typeof__):
    class __gel_reflection__(__ConfigObject_typeof__.__gel_reflection__):
        id = UUID(int=16835018147630535051531832564638176924)
        name = SchemaPath('cfg', 'EmailProviderConfig')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=16835018147630535051531832564638176924),
                name='cfg::EmailProviderConfig',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__(__ConfigObject_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')


class EmailProviderConfig(
    __EmailProviderConfig_typeof__,
    ConfigObject,
    __gel_type_id__=UUID(int=16835018147630535051531832564638176924),
):
    if TYPE_CHECKING:
        def __init__(self, /, *, name: str) -> None:
            """Create a new cfg::EmailProviderConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            name: str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update cfg::EmailProviderConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::EmailProviderConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::EmailProviderConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
            id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            name: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ConfigObject.__variants__):
        class Base(
            __EmailProviderConfig_typeof__,
            ConfigObject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(self, /, *, name: str) -> None:
                    """Create a new cfg::EmailProviderConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    name: str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update cfg::EmailProviderConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::EmailProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::EmailProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
                    id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    name: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="EmailProviderConfig | Base")
    class __links__(ConfigObject.__links__):
        pass

if not TYPE_CHECKING:
    EmailProviderConfig.__variants__.Base = EmailProviderConfig



#
# type cfg::ExtensionConfig
#
class __ExtensionConfig_typeof__(__ConfigObject_typeof__):
    class __gel_reflection__(__ConfigObject_typeof__.__gel_reflection__):
        id = UUID(int=183410656785745777641344889607547842952)
        name = SchemaPath('cfg', 'ExtensionConfig')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=183410656785745777641344889607547842952),
                name='cfg::ExtensionConfig',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__(__ConfigObject_typeof__.__typeof__):
        cfg = TypeAliasType('cfg', 'OptionalLink[AbstractConfig]')


class ExtensionConfig(
    __ExtensionConfig_typeof__,
    ConfigObject,
    __gel_type_id__=UUID(int=183410656785745777641344889607547842952),
):
    if TYPE_CHECKING:
        def __init__(self, /, *, cfg: AbstractConfig | None = None) -> None:
            """Create a new cfg::ExtensionConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            cfg: type[cfg.AbstractConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update cfg::ExtensionConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            cfg: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.AbstractConfig] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::ExtensionConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            cfg: type[cfg.AbstractConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::ExtensionConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
            id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ConfigObject.__variants__):
        class Base(__ExtensionConfig_typeof__, ConfigObject.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    cfg: AbstractConfig | None = None,
                ) -> None:
                    """Create a new cfg::ExtensionConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    cfg: type[cfg.AbstractConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update cfg::ExtensionConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    cfg: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.AbstractConfig] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::ExtensionConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    cfg: type[cfg.AbstractConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::ExtensionConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
                    id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="ExtensionConfig | Base")
    class __links__(ConfigObject.__links__):
        pass

if not TYPE_CHECKING:
    ExtensionConfig.__variants__.Base = ExtensionConfig



#
# type cfg::Config
#
class __Config_typeof__(__AbstractConfig_typeof__):
    class __gel_reflection__(__AbstractConfig_typeof__.__gel_reflection__):
        id = UUID(int=72033782817016315085961485882846453927)
        name = SchemaPath('cfg', 'Config')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=72033782817016315085961485882846453927),
                name='cfg::Config',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__AbstractConfig_typeof__.__typeof__):
        pass


class Config(
    __Config_typeof__,
    AbstractConfig,
    __gel_type_id__=UUID(int=72033782817016315085961485882846453927),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            default_transaction_access_mode: str,
            session_idle_timeout: timedelta,
            default_transaction_isolation: str,
            default_transaction_deferrable: str,
            session_idle_transaction_timeout: timedelta,
            query_execution_timeout: timedelta,
            listen_port: int,
            listen_addresses: Iterable[str] = [],
            current_email_provider_name: str | None = None,
            allow_dml_in_functions: bool | None = None,
            allow_bare_ddl: str | None = None,
            store_migration_sdl: str | None = None,
            apply_access_policies: bool | None = None,
            apply_access_policies_pg: bool | None = None,
            allow_user_specified_id: bool | None = None,
            simple_scoping: bool | None = None,
            warn_old_scoping: bool | None = None,
            cors_allow_origins: Iterable[str] = [],
            auto_rebuild_query_cache: bool | None = None,
            auto_rebuild_query_cache_timeout: timedelta | None = None,
            query_cache_mode: str | None = None,
            http_max_connections: int | None = None,
            shared_buffers: ConfigMemory | None = None,
            query_work_mem: ConfigMemory | None = None,
            maintenance_work_mem: ConfigMemory | None = None,
            effective_cache_size: ConfigMemory | None = None,
            effective_io_concurrency: int | None = None,
            default_statistics_target: int | None = None,
            force_database_error: str | None = None,
            _pg_prepared_statement_cache_size: int,
            track_query_stats: str | None = None,
            auth: Iterable[Auth] = [],
            email_providers: Iterable[EmailProviderConfig] = [],
        ) -> None:
            """Create a new cfg::Config instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            default_transaction_access_mode: type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            listen_port: __builtins_1__.int | type[__std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: str | type[__std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: str | type[__std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: str | type[__std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: str | type[__std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: __builtins_1__.int | type[__std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
            auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update cfg::Config instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            default_transaction_access_mode: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            listen_port: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryStatsOption] | UnspecifiedType = Unspecified,
            extensions: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
            auth: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::Config instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            default_transaction_access_mode: type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            listen_port: __builtins_1__.int | type[__std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: str | type[__std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: str | type[__std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: str | type[__std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: str | type[__std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: __builtins_1__.int | type[__std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
            extensions: type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
            auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::Config instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
            id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            session_idle_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            query_execution_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            listen_port: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            listen_addresses: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            apply_access_policies: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            allow_user_specified_id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            simple_scoping: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            warn_old_scoping: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            cors_allow_origins: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            http_max_connections: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            shared_buffers: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            query_work_mem: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            maintenance_work_mem: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            effective_cache_size: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            effective_io_concurrency: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            default_statistics_target: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            force_database_error: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(AbstractConfig.__variants__):
        class Base(__Config_typeof__, AbstractConfig.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    default_transaction_access_mode: str,
                    session_idle_timeout: timedelta,
                    default_transaction_isolation: str,
                    default_transaction_deferrable: str,
                    session_idle_transaction_timeout: timedelta,
                    query_execution_timeout: timedelta,
                    listen_port: int,
                    listen_addresses: Iterable[str] = [],
                    current_email_provider_name: str | None = None,
                    allow_dml_in_functions: bool | None = None,
                    allow_bare_ddl: str | None = None,
                    store_migration_sdl: str | None = None,
                    apply_access_policies: bool | None = None,
                    apply_access_policies_pg: bool | None = None,
                    allow_user_specified_id: bool | None = None,
                    simple_scoping: bool | None = None,
                    warn_old_scoping: bool | None = None,
                    cors_allow_origins: Iterable[str] = [],
                    auto_rebuild_query_cache: bool | None = None,
                    auto_rebuild_query_cache_timeout: timedelta | None = None,
                    query_cache_mode: str | None = None,
                    http_max_connections: int | None = None,
                    shared_buffers: ConfigMemory | None = None,
                    query_work_mem: ConfigMemory | None = None,
                    maintenance_work_mem: ConfigMemory | None = None,
                    effective_cache_size: ConfigMemory | None = None,
                    effective_io_concurrency: int | None = None,
                    default_statistics_target: int | None = None,
                    force_database_error: str | None = None,
                    _pg_prepared_statement_cache_size: int,
                    track_query_stats: str | None = None,
                    auth: Iterable[Auth] = [],
                    email_providers: Iterable[EmailProviderConfig] = [],
                ) -> None:
                    """Create a new cfg::Config instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    default_transaction_access_mode: type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: __builtins_1__.int | type[__std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: __builtins_1__.int | type[__std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update cfg::Config instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    default_transaction_access_mode: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    extensions: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
                    auth: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::Config instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    default_transaction_access_mode: type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: __builtins_1__.int | type[__std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: __builtins_1__.int | type[__std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    extensions: type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
                    auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::Config instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
                    id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    session_idle_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    query_execution_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    listen_port: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    listen_addresses: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    apply_access_policies: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    simple_scoping: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    warn_old_scoping: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    cors_allow_origins: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    http_max_connections: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    shared_buffers: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    query_work_mem: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    effective_cache_size: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    default_statistics_target: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    force_database_error: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Config | Base")
    class __links__(AbstractConfig.__links__):
        pass

if not TYPE_CHECKING:
    Config.__variants__.Base = Config



#
# type cfg::DatabaseConfig
#
class __DatabaseConfig_typeof__(__AbstractConfig_typeof__):
    class __gel_reflection__(__AbstractConfig_typeof__.__gel_reflection__):
        id = UUID(int=255578330159211281383176570602312393311)
        name = SchemaPath('cfg', 'DatabaseConfig')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=255578330159211281383176570602312393311),
                name='cfg::DatabaseConfig',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__AbstractConfig_typeof__.__typeof__):
        pass


class DatabaseConfig(
    __DatabaseConfig_typeof__,
    AbstractConfig,
    __gel_type_id__=UUID(int=255578330159211281383176570602312393311),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            default_transaction_access_mode: str,
            session_idle_timeout: timedelta,
            default_transaction_isolation: str,
            default_transaction_deferrable: str,
            session_idle_transaction_timeout: timedelta,
            query_execution_timeout: timedelta,
            listen_port: int,
            listen_addresses: Iterable[str] = [],
            current_email_provider_name: str | None = None,
            allow_dml_in_functions: bool | None = None,
            allow_bare_ddl: str | None = None,
            store_migration_sdl: str | None = None,
            apply_access_policies: bool | None = None,
            apply_access_policies_pg: bool | None = None,
            allow_user_specified_id: bool | None = None,
            simple_scoping: bool | None = None,
            warn_old_scoping: bool | None = None,
            cors_allow_origins: Iterable[str] = [],
            auto_rebuild_query_cache: bool | None = None,
            auto_rebuild_query_cache_timeout: timedelta | None = None,
            query_cache_mode: str | None = None,
            http_max_connections: int | None = None,
            shared_buffers: ConfigMemory | None = None,
            query_work_mem: ConfigMemory | None = None,
            maintenance_work_mem: ConfigMemory | None = None,
            effective_cache_size: ConfigMemory | None = None,
            effective_io_concurrency: int | None = None,
            default_statistics_target: int | None = None,
            force_database_error: str | None = None,
            _pg_prepared_statement_cache_size: int,
            track_query_stats: str | None = None,
            auth: Iterable[Auth] = [],
            email_providers: Iterable[EmailProviderConfig] = [],
        ) -> None:
            """Create a new cfg::DatabaseConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            default_transaction_access_mode: type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            listen_port: __builtins_1__.int | type[__std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: str | type[__std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: str | type[__std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: str | type[__std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: str | type[__std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: __builtins_1__.int | type[__std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
            auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update cfg::DatabaseConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            default_transaction_access_mode: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            listen_port: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryStatsOption] | UnspecifiedType = Unspecified,
            extensions: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
            auth: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::DatabaseConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            default_transaction_access_mode: type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            listen_port: __builtins_1__.int | type[__std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: str | type[__std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: str | type[__std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: str | type[__std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: str | type[__std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: __builtins_1__.int | type[__std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
            extensions: type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
            auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::DatabaseConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
            id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            session_idle_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            query_execution_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            listen_port: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            listen_addresses: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            apply_access_policies: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            allow_user_specified_id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            simple_scoping: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            warn_old_scoping: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            cors_allow_origins: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            http_max_connections: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            shared_buffers: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            query_work_mem: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            maintenance_work_mem: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            effective_cache_size: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            effective_io_concurrency: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            default_statistics_target: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            force_database_error: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(AbstractConfig.__variants__):
        class Base(
            __DatabaseConfig_typeof__,
            AbstractConfig.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    default_transaction_access_mode: str,
                    session_idle_timeout: timedelta,
                    default_transaction_isolation: str,
                    default_transaction_deferrable: str,
                    session_idle_transaction_timeout: timedelta,
                    query_execution_timeout: timedelta,
                    listen_port: int,
                    listen_addresses: Iterable[str] = [],
                    current_email_provider_name: str | None = None,
                    allow_dml_in_functions: bool | None = None,
                    allow_bare_ddl: str | None = None,
                    store_migration_sdl: str | None = None,
                    apply_access_policies: bool | None = None,
                    apply_access_policies_pg: bool | None = None,
                    allow_user_specified_id: bool | None = None,
                    simple_scoping: bool | None = None,
                    warn_old_scoping: bool | None = None,
                    cors_allow_origins: Iterable[str] = [],
                    auto_rebuild_query_cache: bool | None = None,
                    auto_rebuild_query_cache_timeout: timedelta | None = None,
                    query_cache_mode: str | None = None,
                    http_max_connections: int | None = None,
                    shared_buffers: ConfigMemory | None = None,
                    query_work_mem: ConfigMemory | None = None,
                    maintenance_work_mem: ConfigMemory | None = None,
                    effective_cache_size: ConfigMemory | None = None,
                    effective_io_concurrency: int | None = None,
                    default_statistics_target: int | None = None,
                    force_database_error: str | None = None,
                    _pg_prepared_statement_cache_size: int,
                    track_query_stats: str | None = None,
                    auth: Iterable[Auth] = [],
                    email_providers: Iterable[EmailProviderConfig] = [],
                ) -> None:
                    """Create a new cfg::DatabaseConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    default_transaction_access_mode: type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: __builtins_1__.int | type[__std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: __builtins_1__.int | type[__std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update cfg::DatabaseConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    default_transaction_access_mode: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    extensions: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
                    auth: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::DatabaseConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    default_transaction_access_mode: type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: __builtins_1__.int | type[__std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: __builtins_1__.int | type[__std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    extensions: type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
                    auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::DatabaseConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
                    id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    session_idle_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    query_execution_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    listen_port: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    listen_addresses: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    apply_access_policies: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    simple_scoping: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    warn_old_scoping: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    cors_allow_origins: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    http_max_connections: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    shared_buffers: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    query_work_mem: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    effective_cache_size: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    default_statistics_target: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    force_database_error: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="DatabaseConfig | Base")
    class __links__(AbstractConfig.__links__):
        pass

if not TYPE_CHECKING:
    DatabaseConfig.__variants__.Base = DatabaseConfig



#
# type cfg::InstanceConfig
#
class __InstanceConfig_typeof__(__AbstractConfig_typeof__):
    class __gel_reflection__(__AbstractConfig_typeof__.__gel_reflection__):
        id = UUID(int=289657214145582360006880454642360258952)
        name = SchemaPath('cfg', 'InstanceConfig')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=289657214145582360006880454642360258952),
                name='cfg::InstanceConfig',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__AbstractConfig_typeof__.__typeof__):
        pass


class InstanceConfig(
    __InstanceConfig_typeof__,
    AbstractConfig,
    __gel_type_id__=UUID(int=289657214145582360006880454642360258952),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            default_transaction_access_mode: str,
            session_idle_timeout: timedelta,
            default_transaction_isolation: str,
            default_transaction_deferrable: str,
            session_idle_transaction_timeout: timedelta,
            query_execution_timeout: timedelta,
            listen_port: int,
            listen_addresses: Iterable[str] = [],
            current_email_provider_name: str | None = None,
            allow_dml_in_functions: bool | None = None,
            allow_bare_ddl: str | None = None,
            store_migration_sdl: str | None = None,
            apply_access_policies: bool | None = None,
            apply_access_policies_pg: bool | None = None,
            allow_user_specified_id: bool | None = None,
            simple_scoping: bool | None = None,
            warn_old_scoping: bool | None = None,
            cors_allow_origins: Iterable[str] = [],
            auto_rebuild_query_cache: bool | None = None,
            auto_rebuild_query_cache_timeout: timedelta | None = None,
            query_cache_mode: str | None = None,
            http_max_connections: int | None = None,
            shared_buffers: ConfigMemory | None = None,
            query_work_mem: ConfigMemory | None = None,
            maintenance_work_mem: ConfigMemory | None = None,
            effective_cache_size: ConfigMemory | None = None,
            effective_io_concurrency: int | None = None,
            default_statistics_target: int | None = None,
            force_database_error: str | None = None,
            _pg_prepared_statement_cache_size: int,
            track_query_stats: str | None = None,
            auth: Iterable[Auth] = [],
            email_providers: Iterable[EmailProviderConfig] = [],
        ) -> None:
            """Create a new cfg::InstanceConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            default_transaction_access_mode: type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            listen_port: __builtins_1__.int | type[__std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: str | type[__std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: str | type[__std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: str | type[__std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: str | type[__std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: __builtins_1__.int | type[__std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
            auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update cfg::InstanceConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            default_transaction_access_mode: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            listen_port: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryStatsOption] | UnspecifiedType = Unspecified,
            extensions: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
            auth: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::InstanceConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            default_transaction_access_mode: type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
            session_idle_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            default_transaction_isolation: type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
            default_transaction_deferrable: type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_execution_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            listen_port: __builtins_1__.int | type[__std__.int32] | UnspecifiedType = Unspecified,
            listen_addresses: str | type[__std__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: str | type[__std__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
            store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
            apply_access_policies: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_user_specified_id: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            simple_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            warn_old_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            cors_allow_origins: str | type[__std__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
            http_max_connections: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
            effective_io_concurrency: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            default_statistics_target: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            force_database_error: str | type[__std__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: __builtins_1__.int | type[__std__.int16] | UnspecifiedType = Unspecified,
            track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
            extensions: type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
            auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
            email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::InstanceConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
            id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            session_idle_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            session_idle_transaction_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            query_execution_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            listen_port: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            listen_addresses: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            current_email_provider_name: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            allow_dml_in_functions: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            apply_access_policies: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            apply_access_policies_pg: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            allow_user_specified_id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            simple_scoping: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            warn_old_scoping: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            cors_allow_origins: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            auto_rebuild_query_cache_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            http_max_connections: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            shared_buffers: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            query_work_mem: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            maintenance_work_mem: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            effective_cache_size: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            effective_io_concurrency: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            default_statistics_target: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            force_database_error: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            _pg_prepared_statement_cache_size: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(AbstractConfig.__variants__):
        class Base(
            __InstanceConfig_typeof__,
            AbstractConfig.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    default_transaction_access_mode: str,
                    session_idle_timeout: timedelta,
                    default_transaction_isolation: str,
                    default_transaction_deferrable: str,
                    session_idle_transaction_timeout: timedelta,
                    query_execution_timeout: timedelta,
                    listen_port: int,
                    listen_addresses: Iterable[str] = [],
                    current_email_provider_name: str | None = None,
                    allow_dml_in_functions: bool | None = None,
                    allow_bare_ddl: str | None = None,
                    store_migration_sdl: str | None = None,
                    apply_access_policies: bool | None = None,
                    apply_access_policies_pg: bool | None = None,
                    allow_user_specified_id: bool | None = None,
                    simple_scoping: bool | None = None,
                    warn_old_scoping: bool | None = None,
                    cors_allow_origins: Iterable[str] = [],
                    auto_rebuild_query_cache: bool | None = None,
                    auto_rebuild_query_cache_timeout: timedelta | None = None,
                    query_cache_mode: str | None = None,
                    http_max_connections: int | None = None,
                    shared_buffers: ConfigMemory | None = None,
                    query_work_mem: ConfigMemory | None = None,
                    maintenance_work_mem: ConfigMemory | None = None,
                    effective_cache_size: ConfigMemory | None = None,
                    effective_io_concurrency: int | None = None,
                    default_statistics_target: int | None = None,
                    force_database_error: str | None = None,
                    _pg_prepared_statement_cache_size: int,
                    track_query_stats: str | None = None,
                    auth: Iterable[Auth] = [],
                    email_providers: Iterable[EmailProviderConfig] = [],
                ) -> None:
                    """Create a new cfg::InstanceConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    default_transaction_access_mode: type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: __builtins_1__.int | type[__std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: __builtins_1__.int | type[__std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update cfg::InstanceConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    default_transaction_access_mode: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    extensions: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
                    auth: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::InstanceConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    default_transaction_access_mode: type[__sys__.TransactionAccessMode] | UnspecifiedType = Unspecified,
                    session_idle_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    default_transaction_isolation: type[__sys__.TransactionIsolation] | UnspecifiedType = Unspecified,
                    default_transaction_deferrable: type[__sys__.TransactionDeferrability] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_execution_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    listen_port: __builtins_1__.int | type[__std__.int32] | UnspecifiedType = Unspecified,
                    listen_addresses: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_bare_ddl: type[AllowBareDDL] | UnspecifiedType = Unspecified,
                    store_migration_sdl: type[StoreMigrationSDL] | UnspecifiedType = Unspecified,
                    apply_access_policies: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    simple_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    warn_old_scoping: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    cors_allow_origins: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    query_cache_mode: type[QueryCacheMode] | UnspecifiedType = Unspecified,
                    http_max_connections: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    shared_buffers: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    query_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_cache_size: ConfigMemory | type[memory] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    default_statistics_target: __builtins_1__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    force_database_error: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: __builtins_1__.int | type[__std__.int16] | UnspecifiedType = Unspecified,
                    track_query_stats: type[QueryStatsOption] | UnspecifiedType = Unspecified,
                    extensions: type[cfg.ExtensionConfig] | UnspecifiedType = Unspecified,
                    auth: type[cfg.Auth] | UnspecifiedType = Unspecified,
                    email_providers: type[cfg.EmailProviderConfig] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::InstanceConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
                    id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    session_idle_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    session_idle_transaction_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    query_execution_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    listen_port: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    listen_addresses: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    current_email_provider_name: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    allow_dml_in_functions: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    apply_access_policies: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    apply_access_policies_pg: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    allow_user_specified_id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    simple_scoping: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    warn_old_scoping: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    cors_allow_origins: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    auto_rebuild_query_cache_timeout: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    http_max_connections: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    shared_buffers: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    query_work_mem: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    maintenance_work_mem: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    effective_cache_size: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    effective_io_concurrency: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    default_statistics_target: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    force_database_error: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    _pg_prepared_statement_cache_size: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="InstanceConfig | Base")
    class __links__(AbstractConfig.__links__):
        pass

if not TYPE_CHECKING:
    InstanceConfig.__variants__.Base = InstanceConfig



#
# type cfg::JWT
#
class __JWT_typeof__(__AuthMethod_typeof__):
    class __gel_reflection__(__AuthMethod_typeof__.__gel_reflection__):
        id = UUID(int=104309744397328972677767160567727635579)
        name = SchemaPath('cfg', 'JWT')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=104309744397328972677767160567727635579),
                name='cfg::JWT',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__AuthMethod_typeof__.__typeof__):
        transports = TypeAliasType('transports', 'list[str]')


class JWT(
    __JWT_typeof__,
    AuthMethod,
    __gel_type_id__=UUID(int=104309744397328972677767160567727635579),
):
    if TYPE_CHECKING:
        def __init__(self, /, *, transports: Iterable[str] = []) -> None:
            """Create a new cfg::JWT instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
            """Update cfg::JWT instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            transports: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::JWT instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::JWT instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
            id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(AuthMethod.__variants__):
        class Base(__JWT_typeof__, AuthMethod.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    transports: Iterable[str] = [],
                ) -> None:
                    """Create a new cfg::JWT instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
                    """Update cfg::JWT instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    transports: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::JWT instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::JWT instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
                    id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="JWT | Base")
    class __links__(AuthMethod.__links__):
        pass

if not TYPE_CHECKING:
    JWT.__variants__.Base = JWT



#
# type cfg::Password
#
class __Password_typeof__(__AuthMethod_typeof__):
    class __gel_reflection__(__AuthMethod_typeof__.__gel_reflection__):
        id = UUID(int=209980488735293693782775477209127049182)
        name = SchemaPath('cfg', 'Password')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=209980488735293693782775477209127049182),
                name='cfg::Password',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__AuthMethod_typeof__.__typeof__):
        transports = TypeAliasType('transports', 'list[str]')


class Password(
    __Password_typeof__,
    AuthMethod,
    __gel_type_id__=UUID(int=209980488735293693782775477209127049182),
):
    if TYPE_CHECKING:
        def __init__(self, /, *, transports: Iterable[str] = []) -> None:
            """Create a new cfg::Password instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
            """Update cfg::Password instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            transports: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::Password instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::Password instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
            id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(AuthMethod.__variants__):
        class Base(__Password_typeof__, AuthMethod.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    transports: Iterable[str] = [],
                ) -> None:
                    """Create a new cfg::Password instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
                    """Update cfg::Password instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    transports: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::Password instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::Password instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
                    id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Password | Base")
    class __links__(AuthMethod.__links__):
        pass

if not TYPE_CHECKING:
    Password.__variants__.Base = Password



#
# type cfg::SCRAM
#
class __SCRAM_typeof__(__AuthMethod_typeof__):
    class __gel_reflection__(__AuthMethod_typeof__.__gel_reflection__):
        id = UUID(int=268855757711039848843614875827541315364)
        name = SchemaPath('cfg', 'SCRAM')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=268855757711039848843614875827541315364),
                name='cfg::SCRAM',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__AuthMethod_typeof__.__typeof__):
        transports = TypeAliasType('transports', 'list[str]')


class SCRAM(
    __SCRAM_typeof__,
    AuthMethod,
    __gel_type_id__=UUID(int=268855757711039848843614875827541315364),
):
    if TYPE_CHECKING:
        def __init__(self, /, *, transports: Iterable[str] = []) -> None:
            """Create a new cfg::SCRAM instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
            """Update cfg::SCRAM instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            transports: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::SCRAM instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::SCRAM instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
            id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(AuthMethod.__variants__):
        class Base(__SCRAM_typeof__, AuthMethod.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    transports: Iterable[str] = [],
                ) -> None:
                    """Create a new cfg::SCRAM instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
                    """Update cfg::SCRAM instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    transports: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::SCRAM instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::SCRAM instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
                    id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="SCRAM | Base")
    class __links__(AuthMethod.__links__):
        pass

if not TYPE_CHECKING:
    SCRAM.__variants__.Base = SCRAM



#
# type cfg::Trust
#
class __Trust_typeof__(__AuthMethod_typeof__):
    class __gel_reflection__(__AuthMethod_typeof__.__gel_reflection__):
        id = UUID(int=169812016296800753534565771606745733954)
        name = SchemaPath('cfg', 'Trust')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=169812016296800753534565771606745733954),
                name='cfg::Trust',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__AuthMethod_typeof__.__typeof__):
        pass


class Trust(
    __Trust_typeof__,
    AuthMethod,
    __gel_type_id__=UUID(int=169812016296800753534565771606745733954),
):
    if TYPE_CHECKING:
        def __init__(self, /, *, transports: Iterable[str] = []) -> None:
            """Create a new cfg::Trust instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
            """Update cfg::Trust instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            transports: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::Trust instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::Trust instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
            id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(AuthMethod.__variants__):
        class Base(__Trust_typeof__, AuthMethod.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    transports: Iterable[str] = [],
                ) -> None:
                    """Create a new cfg::Trust instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
                    """Update cfg::Trust instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    transports: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::Trust instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::Trust instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
                    id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Trust | Base")
    class __links__(AuthMethod.__links__):
        pass

if not TYPE_CHECKING:
    Trust.__variants__.Base = Trust



#
# type cfg::mTLS
#
class __mTLS_typeof__(__AuthMethod_typeof__):
    class __gel_reflection__(__AuthMethod_typeof__.__gel_reflection__):
        id = UUID(int=310279763571120869801632341122484800782)
        name = SchemaPath('cfg', 'mTLS')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=310279763571120869801632341122484800782),
                name='cfg::mTLS',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__AuthMethod_typeof__.__typeof__):
        transports = TypeAliasType('transports', 'list[str]')


class mTLS(
    __mTLS_typeof__,
    AuthMethod,
    __gel_type_id__=UUID(int=310279763571120869801632341122484800782),
):
    if TYPE_CHECKING:
        def __init__(self, /, *, transports: Iterable[str] = []) -> None:
            """Create a new cfg::mTLS instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
            """Update cfg::mTLS instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            transports: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::mTLS instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::mTLS instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
            id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(AuthMethod.__variants__):
        class Base(__mTLS_typeof__, AuthMethod.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    transports: Iterable[str] = [],
                ) -> None:
                    """Create a new cfg::mTLS instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
                    """Update cfg::mTLS instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    transports: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ConnectionTransport] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::mTLS instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    transports: type[ConnectionTransport] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::mTLS instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
                    id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="mTLS | Base")
    class __links__(AuthMethod.__links__):
        pass

if not TYPE_CHECKING:
    mTLS.__variants__.Base = mTLS



#
# type cfg::SMTPProviderConfig
#
class __SMTPProviderConfig_typeof__(__EmailProviderConfig_typeof__):
    class __gel_reflection__(
        __EmailProviderConfig_typeof__.__gel_reflection__,
    ):
        id = UUID(int=108468146439474883053972930104863702727)
        name = SchemaPath('cfg', 'SMTPProviderConfig')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=108468146439474883053972930104863702727),
                name='cfg::SMTPProviderConfig',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__EmailProviderConfig_typeof__.__typeof__):
        sender = TypeAliasType('sender', 'OptionalProperty[std.str, str]')
        host = TypeAliasType('host', 'OptionalProperty[std.str, str]')
        port = TypeAliasType('port', 'OptionalProperty[std.int32, int]')
        username = TypeAliasType('username', 'OptionalProperty[std.str, str]')
        password = TypeAliasType('password', 'OptionalProperty[std.str, str]')
        security = TypeAliasType('security', 'SMTPSecurity')
        validate_certs = TypeAliasType('validate_certs', 'std.bool')
        timeout_per_email = TypeAliasType('timeout_per_email', 'std.duration')
        timeout_per_attempt = TypeAliasType('timeout_per_attempt', 'std.duration')


class SMTPProviderConfig(
    __SMTPProviderConfig_typeof__,
    EmailProviderConfig,
    __gel_type_id__=UUID(int=108468146439474883053972930104863702727),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: str,
            sender: str | None = None,
            host: str | None = None,
            port: int | None = None,
            username: str | None = None,
            password: str | None = None,
            security: str,
            validate_certs: bool,
            timeout_per_email: timedelta,
            timeout_per_attempt: timedelta,
        ) -> None:
            """Create a new cfg::SMTPProviderConfig instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            name: str | type[__std__.str] | UnspecifiedType = Unspecified,
            sender: str | type[__std__.str] | UnspecifiedType = Unspecified,
            host: str | type[__std__.str] | UnspecifiedType = Unspecified,
            port: __builtins_1__.int | type[__std__.int32] | UnspecifiedType = Unspecified,
            username: str | type[__std__.str] | UnspecifiedType = Unspecified,
            password: str | type[__std__.str] | UnspecifiedType = Unspecified,
            security: type[SMTPSecurity] | UnspecifiedType = Unspecified,
            validate_certs: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            timeout_per_email: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            timeout_per_attempt: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update cfg::SMTPProviderConfig instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            sender: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            host: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            port: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int32] | UnspecifiedType = Unspecified,
            username: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            password: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            security: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[SMTPSecurity] | UnspecifiedType = Unspecified,
            validate_certs: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            timeout_per_email: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            timeout_per_attempt: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch cfg::SMTPProviderConfig instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: str | type[__std__.str] | UnspecifiedType = Unspecified,
            sender: str | type[__std__.str] | UnspecifiedType = Unspecified,
            host: str | type[__std__.str] | UnspecifiedType = Unspecified,
            port: __builtins_1__.int | type[__std__.int32] | UnspecifiedType = Unspecified,
            username: str | type[__std__.str] | UnspecifiedType = Unspecified,
            password: str | type[__std__.str] | UnspecifiedType = Unspecified,
            security: type[SMTPSecurity] | UnspecifiedType = Unspecified,
            validate_certs: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            timeout_per_email: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            timeout_per_attempt: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch cfg::SMTPProviderConfig instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
            id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            name: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            sender: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            host: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            port: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            username: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            password: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            validate_certs: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            timeout_per_email: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
            timeout_per_attempt: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(EmailProviderConfig.__variants__):
        class Base(
            __SMTPProviderConfig_typeof__,
            EmailProviderConfig.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: str,
                    sender: str | None = None,
                    host: str | None = None,
                    port: int | None = None,
                    username: str | None = None,
                    password: str | None = None,
                    security: str,
                    validate_certs: bool,
                    timeout_per_email: timedelta,
                    timeout_per_attempt: timedelta,
                ) -> None:
                    """Create a new cfg::SMTPProviderConfig instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    name: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    sender: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    host: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    port: __builtins_1__.int | type[__std__.int32] | UnspecifiedType = Unspecified,
                    username: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    password: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    security: type[SMTPSecurity] | UnspecifiedType = Unspecified,
                    validate_certs: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    timeout_per_email: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    timeout_per_attempt: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update cfg::SMTPProviderConfig instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    sender: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    host: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    port: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int32] | UnspecifiedType = Unspecified,
                    username: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    password: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    security: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[SMTPSecurity] | UnspecifiedType = Unspecified,
                    validate_certs: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    timeout_per_email: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    timeout_per_attempt: __builtins__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch cfg::SMTPProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    sender: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    host: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    port: __builtins_1__.int | type[__std__.int32] | UnspecifiedType = Unspecified,
                    username: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    password: str | type[__std__.str] | UnspecifiedType = Unspecified,
                    security: type[SMTPSecurity] | UnspecifiedType = Unspecified,
                    validate_certs: __builtins_2__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    timeout_per_email: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    timeout_per_attempt: datetime.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch cfg::SMTPProviderConfig instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins__.str, EmptyDirection | __builtins__.str],
                    id: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    name: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    sender: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    host: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    port: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    username: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    password: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    validate_certs: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    timeout_per_email: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                    timeout_per_attempt: Direction | __builtins__.str | __builtins__.str | __builtins__.bool | tuple[Direction | __builtins__.str, EmptyDirection | __builtins__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="SMTPProviderConfig | Base")
    class __links__(EmailProviderConfig.__links__):
        pass

if not TYPE_CHECKING:
    SMTPProviderConfig.__variants__.Base = SMTPProviderConfig



from .. import sys  # noqa: E402 F403

from builtins import bool, int  # noqa: E402 F403
from datetime import timedelta  # noqa: E402 F403
