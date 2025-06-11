#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from ... import std

from gel.models.pydantic import (
    AnyEnum,
    Array,
    Direction,
    EmptyDirection,
    ExprCompatible,
    LazyClassProperty,
    OptionalComputedLink,
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
from builtins import list, tuple, type
from collections.abc import Callable
from typing import TYPE_CHECKING, TypeVar
from typing_extensions import Self, TypeAliasType
from uuid import UUID

if TYPE_CHECKING:

    from .. import net as __std_net__
    from ... import std as __std__
    from .... import schema
    from ....std import __types__ as __std___types____, __types__ as std___types__
    from ....std.net import http as std_net_http


class Method(AnyEnum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    HEAD = 'HEAD'
    OPTIONS = 'OPTIONS'
    PATCH = 'PATCH'




#
# type std::net::http::Response
#
class __Response_typeof__(std.__BaseObject_typeof__):
    class __gel_reflection__(std.__BaseObject_typeof__.__gel_reflection__):
        id = UUID(int=147718222496950996262069719176207702606)
        name = SchemaPath('std', 'net', 'http', 'Response')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ....schema import ObjectType
            return ObjectType(
                id=UUID(int=147718222496950996262069719176207702606),
                name='std::net::http::Response',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(std.__BaseObject_typeof__.__typeof__):
        created_at = TypeAliasType('created_at', 'std.datetime')
        status = TypeAliasType('status', 'OptionalProperty[std.int16, int]')
        headers = TypeAliasType('headers', 'OptionalProperty[Array[NameValue_Tuple_CO3mqQ], list[tuple[str, str]]]')
        body = TypeAliasType('body', 'OptionalProperty[std.bytes, bytes]')
        request = TypeAliasType('request', 'OptionalComputedLink[ScheduledRequest]')


class Response(
    __Response_typeof__,
    std.BaseObject,
    __gel_type_id__=UUID(int=147718222496950996262069719176207702606),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            created_at: datetime,
            status: int | None = None,
            headers: list[tuple[str, str]] | None = None,
            body: bytes | None = None,
        ) -> None:
            """Create a new std::net::http::Response instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            status: __builtins__.int | type[__std__.int16] | UnspecifiedType = Unspecified,
            headers: type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
            body: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update std::net::http::Response instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            status: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int16] | UnspecifiedType = Unspecified,
            headers: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
            body: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bytes] | UnspecifiedType = Unspecified,
            request: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[std_net_http.ScheduledRequest] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch std::net::http::Response instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            status: __builtins__.int | type[__std__.int16] | UnspecifiedType = Unspecified,
            headers: type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
            body: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
            request: type[std_net_http.ScheduledRequest] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch std::net::http::Response instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            status: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            body: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(std.BaseObject.__variants__):
        class Base(__Response_typeof__, std.BaseObject.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    created_at: datetime,
                    status: int | None = None,
                    headers: list[tuple[str, str]] | None = None,
                    body: bytes | None = None,
                ) -> None:
                    """Create a new std::net::http::Response instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    status: __builtins__.int | type[__std__.int16] | UnspecifiedType = Unspecified,
                    headers: type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
                    body: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update std::net::http::Response instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    status: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int16] | UnspecifiedType = Unspecified,
                    headers: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
                    body: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bytes] | UnspecifiedType = Unspecified,
                    request: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[std_net_http.ScheduledRequest] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch std::net::http::Response instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    status: __builtins__.int | type[__std__.int16] | UnspecifiedType = Unspecified,
                    headers: type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
                    body: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
                    request: type[std_net_http.ScheduledRequest] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch std::net::http::Response instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    status: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    body: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Response | Base")
    class __links__(std.BaseObject.__links__):
        pass

if not TYPE_CHECKING:
    Response.__variants__.Base = Response



#
# type std::net::http::ScheduledRequest
#
class __ScheduledRequest_typeof__(std.__BaseObject_typeof__):
    class __gel_reflection__(std.__BaseObject_typeof__.__gel_reflection__):
        id = UUID(int=306714282403613484767691626551873154557)
        name = SchemaPath('std', 'net', 'http', 'ScheduledRequest')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ....schema import ObjectType
            return ObjectType(
                id=UUID(int=306714282403613484767691626551873154557),
                name='std::net::http::ScheduledRequest',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(std.__BaseObject_typeof__.__typeof__):
        state = TypeAliasType('state', 'std_net.RequestState')
        created_at = TypeAliasType('created_at', 'std.datetime')
        updated_at = TypeAliasType('updated_at', 'std.datetime')
        failure = TypeAliasType('failure', 'OptionalProperty[KindMessage_Tuple_hRjfgQ, tuple[__builtins_2__.str, str]]')
        url = TypeAliasType('url', 'std.str')
        method = TypeAliasType('method', 'Method')
        headers = TypeAliasType('headers', 'OptionalProperty[Array[NameValue_Tuple_CO3mqQ], list[tuple[str, str]]]')
        body = TypeAliasType('body', 'OptionalProperty[std.bytes, bytes]')
        response = TypeAliasType('response', 'OptionalLink[Response]')


class ScheduledRequest(
    __ScheduledRequest_typeof__,
    std.BaseObject,
    __gel_type_id__=UUID(int=306714282403613484767691626551873154557),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            state: __builtins_2__.str,
            created_at: datetime,
            updated_at: datetime,
            failure: tuple[__builtins_2__.str, str] | None = None,
            url: str,
            method: __builtins_2__.str,
            headers: list[tuple[str, str]] | None = None,
            body: bytes | None = None,
            response: Response | None = None,
        ) -> None:
            """Create a new std::net::http::ScheduledRequest instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            state: type[__std_net__.RequestState] | UnspecifiedType = Unspecified,
            created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            updated_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            failure: type[__std___types____.KindMessage_Tuple_hRjfgQ] | UnspecifiedType = Unspecified,
            url: __builtins_2__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            method: type[Method] | UnspecifiedType = Unspecified,
            headers: type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
            body: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
            response: type[std_net_http.Response] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update std::net::http::ScheduledRequest instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            state: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std_net__.RequestState] | UnspecifiedType = Unspecified,
            created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            updated_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            failure: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std___types____.KindMessage_Tuple_hRjfgQ] | UnspecifiedType = Unspecified,
            url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            method: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Method] | UnspecifiedType = Unspecified,
            headers: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
            body: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bytes] | UnspecifiedType = Unspecified,
            response: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[std_net_http.Response] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch std::net::http::ScheduledRequest instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            state: type[__std_net__.RequestState] | UnspecifiedType = Unspecified,
            created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            updated_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            failure: type[__std___types____.KindMessage_Tuple_hRjfgQ] | UnspecifiedType = Unspecified,
            url: __builtins_2__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            method: type[Method] | UnspecifiedType = Unspecified,
            headers: type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
            body: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
            response: type[std_net_http.Response] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch std::net::http::ScheduledRequest instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            updated_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            url: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            body: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(std.BaseObject.__variants__):
        class Base(
            __ScheduledRequest_typeof__,
            std.BaseObject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    state: __builtins_2__.str,
                    created_at: datetime,
                    updated_at: datetime,
                    failure: tuple[__builtins_2__.str, str] | None = None,
                    url: str,
                    method: __builtins_2__.str,
                    headers: list[tuple[str, str]] | None = None,
                    body: bytes | None = None,
                    response: Response | None = None,
                ) -> None:
                    """Create a new std::net::http::ScheduledRequest instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    state: type[__std_net__.RequestState] | UnspecifiedType = Unspecified,
                    created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    updated_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    failure: type[__std___types____.KindMessage_Tuple_hRjfgQ] | UnspecifiedType = Unspecified,
                    url: __builtins_2__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    method: type[Method] | UnspecifiedType = Unspecified,
                    headers: type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
                    body: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
                    response: type[std_net_http.Response] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update std::net::http::ScheduledRequest instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    state: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std_net__.RequestState] | UnspecifiedType = Unspecified,
                    created_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    updated_at: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    failure: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std___types____.KindMessage_Tuple_hRjfgQ] | UnspecifiedType = Unspecified,
                    url: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    method: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Method] | UnspecifiedType = Unspecified,
                    headers: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
                    body: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bytes] | UnspecifiedType = Unspecified,
                    response: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[std_net_http.Response] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch std::net::http::ScheduledRequest instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    state: type[__std_net__.RequestState] | UnspecifiedType = Unspecified,
                    created_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    updated_at: __datetime__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    failure: type[__std___types____.KindMessage_Tuple_hRjfgQ] | UnspecifiedType = Unspecified,
                    url: __builtins_2__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    method: type[Method] | UnspecifiedType = Unspecified,
                    headers: type[Array[std___types__.NameValue_Tuple_CO3mqQ]] | UnspecifiedType = Unspecified,
                    body: __builtins_1__.bytes | type[__std__.bytes] | UnspecifiedType = Unspecified,
                    response: type[std_net_http.Response] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch std::net::http::ScheduledRequest instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    created_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    updated_at: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    url: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    body: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="ScheduledRequest | Base")
    class __links__(std.BaseObject.__links__):
        pass

if not TYPE_CHECKING:
    ScheduledRequest.__variants__.Base = ScheduledRequest



from .. import net as std_net  # noqa: E402 F403
from ....std.__types__ import KindMessage_Tuple_hRjfgQ, NameValue_Tuple_CO3mqQ  # noqa: E402 F403

from builtins import bytes, int, str  # noqa: E402 F403
from datetime import datetime  # noqa: E402 F403
