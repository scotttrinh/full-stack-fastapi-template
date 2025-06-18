#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from . import std

from gel.models.pydantic import AnyNamedTuple, GelTypeMetadata, SchemaPath

from typing import NamedTuple
from uuid import UUID


#
# tuple type tuple<header:std::str, payload:std::str, signature:std::str>
#
class _HeaderPayloadSignature_Tuple_e_sBBg(NamedTuple):
    header: std.str
    payload: std.str
    signature: std.str


class HeaderPayloadSignature_Tuple_e_sBBg(
    _HeaderPayloadSignature_Tuple_e_sBBg,
    AnyNamedTuple,
):
    class __gel_reflection__(GelTypeMetadata.__gel_reflection__):
        id = UUID(int=164798330796699462868874118661116466001)
        name = SchemaPath('tuple<header:std::str, payload:std::str, signature:std::str>')

    __slots__ = ()

