#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from .. import std as ___std__

from gel.models.pydantic import (
    AnnotatedExpr,
    FuncCall,
    SchemaPath,
    Unspecified,
    dispatch_overload
)

from builtins import dict, list, str
from typing import Any, TYPE_CHECKING, overload

if TYPE_CHECKING:

    from .. import std

    from gel.models.pydantic import GelType

    import builtins as builtins
    import typing as typing
    from builtins import type


@overload
def digest(data: type[std.str], type: type[std.str]) -> type[std.bytes]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [data, type]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.bytes,
        FuncCall(
            fname="ext::pgcrypto::digest",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bytes'),
        )
    )

@overload
def digest(data: type[std.bytes], type: type[std.str]) -> type[std.bytes]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [data, type]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.bytes,
        FuncCall(
            fname="ext::pgcrypto::digest",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bytes'),
        )
    )

def digest(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(digest, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def hmac(  # type: ignore [overload-cannot-match, unused-ignore]
    data: type[std.str],
    key: type[std.str],
    type: type[std.str],
) -> type[std.bytes]:
    args: list[Any] = [data, key, type]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.bytes,
        FuncCall(
            fname="ext::pgcrypto::hmac",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bytes'),
        )
    )

@overload
def hmac(  # type: ignore [overload-cannot-match, unused-ignore]
    data: type[std.bytes],
    key: type[std.bytes],
    type: type[std.str],
) -> type[std.bytes]:
    args: list[Any] = [data, key, type]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.bytes,
        FuncCall(
            fname="ext::pgcrypto::hmac",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'bytes'),
        )
    )

def hmac(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(hmac, *args, **kwargs)  # type: ignore [no-any-return]

@overload
def gen_salt() -> type[std.str]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = []
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.str,
        FuncCall(
            fname="ext::pgcrypto::gen_salt",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

@overload
def gen_salt(type: type[std.str]) -> type[std.str]:  # type: ignore [overload-cannot-match, unused-ignore]
    args: list[Any] = [type]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.str,
        FuncCall(
            fname="ext::pgcrypto::gen_salt",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

@overload
def gen_salt(  # type: ignore [overload-cannot-match, unused-ignore]
    type: type[std.str],
    iter_count: type[std.int64],
) -> type[std.str]:
    args: list[Any] = [type, iter_count]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.str,
        FuncCall(
            fname="ext::pgcrypto::gen_salt",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

def gen_salt(*args: typing.Any, **kwargs: typing.Any) -> type[GelType]:
    return dispatch_overload(gen_salt, *args, **kwargs)  # type: ignore [no-any-return]

def crypt(
    password: type[std.str] | builtins.str,
    salt: type[std.str] | builtins.str,
) -> type[std.str]:
    args: list[Any] = [password, salt]
    kw: dict[str, Any] = {}
    return AnnotatedExpr(  # type: ignore [return-value]
        ___std__.str,
        FuncCall(
            fname="ext::pgcrypto::crypt",
            args=[v for v in args if v is not Unspecified],
            kwargs={n: v for n, v in kw.items() if v is not Unspecified},
            type_=SchemaPath('std', 'str'),
        )
    )

