#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

import gel as gel
from gel.models.pydantic import (
    AnnotatedExpr,
    AnyEnum,
    BaseScalar,
    DateTimeLike,
    Direction,
    EmptyDirection,
    ExprCompatible,
    GelModel,
    GelModelMeta,
    GelTypeMeta,
    GelTypeMetadata,
    IdProperty,
    InfixOp,
    LazyClassProperty,
    LinkClassNamespace,
    PathAlias,
    PrefixOp,
    PyConstType,
    PyTypeScalar,
    SchemaPath,
    Unspecified,
    UnspecifiedType,
    dispatch_overload
)

import builtins as __builtins_2__
import builtins as __builtins_3__
import builtins as __builtins_1__
import builtins as __builtins__
import datetime as __datetime__
import datetime as __datetime_1__
import decimal as __decimal__
import uuid as __uuid__
from builtins import float, int, tuple, type
from collections.abc import Callable
from datetime import timedelta
from decimal import Decimal
from typing import Any, TYPE_CHECKING, TypeVar, overload
from typing_extensions import Self, TypeAliasType
from uuid import UUID

if TYPE_CHECKING:

    from . import cal as std_cal
    from ... import schema, std

    import builtins as builtins
    from typing import ClassVar



class __anyscalar_meta__(GelTypeMeta):
    def __eq__(cls, other: anyscalar | type[anyscalar]) -> builtins.type[bool]:  # type: ignore [override, unused-ignore]
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ne__(cls, other: anyscalar | type[anyscalar]) -> builtins.type[bool]:  # type: ignore [override, unused-ignore]
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ge__(cls, other: anyscalar | type[anyscalar]) -> builtins.type[bool]:  # type: ignore [override, unused-ignore]
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __gt__(cls, other: anyscalar | type[anyscalar]) -> builtins.type[bool]:  # type: ignore [override, unused-ignore]
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __le__(cls, other: anyscalar | type[anyscalar]) -> builtins.type[bool]:  # type: ignore [override, unused-ignore]
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __lt__(cls, other: anyscalar | type[anyscalar]) -> builtins.type[bool]:  # type: ignore [override, unused-ignore]
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class anyscalar(BaseScalar, metaclass=__anyscalar_meta__):
        class __gel_reflection__:
            id = UUID(int=221050124307656686636337380669752814245)
            name = SchemaPath('std', 'anyscalar')

if not TYPE_CHECKING:
    class anyscalar(BaseScalar):
        __gel_type_class__: ClassVar[type] = __anyscalar_meta__

        class __gel_reflection__:
            id = UUID(int=221050124307656686636337380669752814245)
            name = SchemaPath('std', 'anyscalar')



class __anyenum_meta__(__anyscalar_meta__):
    def __eq__(cls, other: anyenum | type[anyenum]) -> builtins.type[bool]:  # type: ignore [override, unused-ignore]
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ne__(cls, other: anyenum | type[anyenum]) -> builtins.type[bool]:  # type: ignore [override, unused-ignore]
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ge__(cls, other: anyenum | type[anyenum]) -> builtins.type[bool]:  # type: ignore [override, unused-ignore]
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __gt__(cls, other: anyenum | type[anyenum]) -> builtins.type[bool]:  # type: ignore [override, unused-ignore]
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __le__(cls, other: anyenum | type[anyenum]) -> builtins.type[bool]:  # type: ignore [override, unused-ignore]
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __lt__(cls, other: anyenum | type[anyenum]) -> builtins.type[bool]:  # type: ignore [override, unused-ignore]
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class anyenum(anyscalar, metaclass=__anyenum_meta__):
        class __gel_reflection__(anyscalar.__gel_reflection__):
            id = UUID(int=96418005353275310736156338735181295333)
            name = SchemaPath('std', 'anyenum')

if not TYPE_CHECKING:
    class anyenum(anyscalar):
        __gel_type_class__: ClassVar[type] = __anyenum_meta__

        class __gel_reflection__(anyscalar.__gel_reflection__):
            id = UUID(int=96418005353275310736156338735181295333)
            name = SchemaPath('std', 'anyenum')



class __anypoint_meta__(__anyscalar_meta__):
    pass
if TYPE_CHECKING:
    class anypoint(anyscalar, metaclass=__anypoint_meta__):
        class __gel_reflection__(anyscalar.__gel_reflection__):
            id = UUID(int=117112319472524089162671685900492542739)
            name = SchemaPath('std', 'anypoint')

if not TYPE_CHECKING:
    class anypoint(anyscalar):
        __gel_type_class__: ClassVar[type] = __anypoint_meta__

        class __gel_reflection__(anyscalar.__gel_reflection__):
            id = UUID(int=117112319472524089162671685900492542739)
            name = SchemaPath('std', 'anypoint')



class __anyreal_meta__(__anyscalar_meta__):
    pass
if TYPE_CHECKING:
    class anyreal(anyscalar, metaclass=__anyreal_meta__):
        class __gel_reflection__(anyscalar.__gel_reflection__):
            id = UUID(int=6103002804295905587116371414455506971)
            name = SchemaPath('std', 'anyreal')

if not TYPE_CHECKING:
    class anyreal(anyscalar):
        __gel_type_class__: ClassVar[type] = __anyreal_meta__

        class __gel_reflection__(anyscalar.__gel_reflection__):
            id = UUID(int=6103002804295905587116371414455506971)
            name = SchemaPath('std', 'anyreal')



class __bool_meta__(__anyscalar_meta__):
    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.bool | bool | type[bool],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.bool():
                other = bool(other)
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.bool | bool | type[bool],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.bool():
                other = bool(other)
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.bool | bool | type[bool],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.bool():
                other = bool(other)
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.bool | bool | type[bool],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.bool():
                other = bool(other)
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.bool | bool | type[bool],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.bool():
                other = bool(other)
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.bool | bool | type[bool],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.bool():
                other = bool(other)
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class bool(
        PyTypeScalar[__builtins__.bool],
        anyscalar,
        metaclass=__bool_meta__,
    ):
        class __gel_reflection__(anyscalar.__gel_reflection__):
            id = UUID(int=265)
            name = SchemaPath('std', 'bool')

if not TYPE_CHECKING:
    class bool(int, PyTypeScalar[__builtins__.bool], anyscalar):
        __gel_type_class__: ClassVar[type] = __bool_meta__

        class __gel_reflection__(anyscalar.__gel_reflection__):
            id = UUID(int=265)
            name = SchemaPath('std', 'bool')



class __bytes_meta__(__anyscalar_meta__):
    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.bytes | bytes | type[bytes],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.bytes():
                other = bytes(other)
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.bytes | bytes | type[bytes],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.bytes():
                other = bytes(other)
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.bytes | bytes | type[bytes],
    ) -> builtins.type[bytes]:
        match other:
            case __builtins_1__.bytes():
                other = bytes(other)
        op = InfixOp(
            lexpr=cls,
            op="++",
            rexpr=other,
            type_=SchemaPath('std', 'bytes'),
        )
        return AnnotatedExpr(bytes, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.bytes | bytes | type[bytes],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.bytes():
                other = bytes(other)
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.bytes | bytes | type[bytes],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.bytes():
                other = bytes(other)
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.bytes | bytes | type[bytes],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.bytes():
                other = bytes(other)
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.bytes | bytes | type[bytes],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.bytes():
                other = bytes(other)
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class bytes(
        PyTypeScalar[__builtins_2__.bytes],
        anyscalar,
        metaclass=__bytes_meta__,
    ):
        class __gel_reflection__(anyscalar.__gel_reflection__):
            id = UUID(int=258)
            name = SchemaPath('std', 'bytes')

if not TYPE_CHECKING:
    class bytes(
        __builtins_2__.bytes,
        PyTypeScalar[__builtins_2__.bytes],
        anyscalar,
    ):
        __gel_type_class__: ClassVar[type] = __bytes_meta__

        class __gel_reflection__(anyscalar.__gel_reflection__):
            id = UUID(int=258)
            name = SchemaPath('std', 'bytes')



class __json_meta__(__anyscalar_meta__):
    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.str | json | type[json],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.str():
                other = json(other)
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.str | json | type[json],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.str():
                other = json(other)
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.str | json | type[json],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.str():
                other = json(other)
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.str | json | type[json],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.str():
                other = json(other)
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.str | json | type[json],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.str():
                other = json(other)
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.str | json | type[json],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.str():
                other = json(other)
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.str | json | type[json],
    ) -> builtins.type[json]:
        match other:
            case __builtins_1__.str():
                other = json(other)
        op = InfixOp(
            lexpr=cls,
            op="++",
            rexpr=other,
            type_=SchemaPath('std', 'json'),
        )
        return AnnotatedExpr(json, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class json(
        PyTypeScalar[__builtins_3__.str],
        anyscalar,
        metaclass=__json_meta__,
    ):
        class __gel_reflection__(anyscalar.__gel_reflection__):
            id = UUID(int=271)
            name = SchemaPath('std', 'json')

if not TYPE_CHECKING:
    class json(
        __builtins_3__.str,
        PyTypeScalar[__builtins_3__.str],
        anyscalar,
    ):
        __gel_type_class__: ClassVar[type] = __json_meta__

        class __gel_reflection__(anyscalar.__gel_reflection__):
            id = UUID(int=271)
            name = SchemaPath('std', 'json')



class __str_meta__(__anyscalar_meta__):
    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.str | str | type[str],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.str():
                other = str(other)
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.str | str | type[str],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.str():
                other = str(other)
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.str | str | type[str],
    ) -> builtins.type[str]:
        match other:
            case __builtins_1__.str():
                other = str(other)
        op = InfixOp(
            lexpr=cls,
            op="++",
            rexpr=other,
            type_=SchemaPath('std', 'str'),
        )
        return AnnotatedExpr(str, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.str | str | type[str],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.str():
                other = str(other)
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.str | str | type[str],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.str():
                other = str(other)
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.str | str | type[str],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.str():
                other = str(other)
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.str | str | type[str],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.str():
                other = str(other)
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class str(
        PyTypeScalar[__builtins_3__.str],
        anyscalar,
        metaclass=__str_meta__,
    ):
        class __gel_reflection__(anyscalar.__gel_reflection__):
            id = UUID(int=257)
            name = SchemaPath('std', 'str')

if not TYPE_CHECKING:
    class str(__builtins_3__.str, PyTypeScalar[__builtins_3__.str], anyscalar):
        __gel_type_class__: ClassVar[type] = __str_meta__

        class __gel_reflection__(anyscalar.__gel_reflection__):
            id = UUID(int=257)
            name = SchemaPath('std', 'str')



class __uuid_meta__(__anyscalar_meta__):
    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: __uuid__.UUID | type[uuid] | uuid,
    ) -> builtins.type[bool]:
        match other:
            case __uuid__.UUID():
                other = uuid(other)
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: __uuid__.UUID | type[uuid] | uuid,
    ) -> builtins.type[bool]:
        match other:
            case __uuid__.UUID():
                other = uuid(other)
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: __uuid__.UUID | type[uuid] | uuid,
    ) -> builtins.type[bool]:
        match other:
            case __uuid__.UUID():
                other = uuid(other)
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __uuid__.UUID | type[uuid] | uuid,
    ) -> builtins.type[bool]:
        match other:
            case __uuid__.UUID():
                other = uuid(other)
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: __uuid__.UUID | type[uuid] | uuid,
    ) -> builtins.type[bool]:
        match other:
            case __uuid__.UUID():
                other = uuid(other)
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __uuid__.UUID | type[uuid] | uuid,
    ) -> builtins.type[bool]:
        match other:
            case __uuid__.UUID():
                other = uuid(other)
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class uuid(PyTypeScalar[UUID], anyscalar, metaclass=__uuid_meta__):
        class __gel_reflection__(anyscalar.__gel_reflection__):
            id = UUID(int=256)
            name = SchemaPath('std', 'uuid')

if not TYPE_CHECKING:
    class uuid(UUID, PyTypeScalar[UUID], anyscalar):
        __gel_type_class__: ClassVar[type] = __uuid_meta__

        class __gel_reflection__(anyscalar.__gel_reflection__):
            id = UUID(int=256)
            name = SchemaPath('std', 'uuid')


class Endian(AnyEnum):
    Little = 'Little'
    Big = 'Big'


class JsonEmpty(AnyEnum):
    ReturnEmpty = 'ReturnEmpty'
    ReturnTarget = 'ReturnTarget'
    Error = 'Error'
    UseNull = 'UseNull'
    DeleteKey = 'DeleteKey'



class __anycontiguous_meta__(__anypoint_meta__):
    pass
if TYPE_CHECKING:
    class anycontiguous(anypoint, metaclass=__anycontiguous_meta__):
        class __gel_reflection__(anypoint.__gel_reflection__):
            id = UUID(int=40631814268544335276538168500625238426)
            name = SchemaPath('std', 'anycontiguous')

if not TYPE_CHECKING:
    class anycontiguous(anypoint):
        __gel_type_class__: ClassVar[type] = __anycontiguous_meta__

        class __gel_reflection__(anypoint.__gel_reflection__):
            id = UUID(int=40631814268544335276538168500625238426)
            name = SchemaPath('std', 'anycontiguous')



class __anydiscrete_meta__(__anypoint_meta__):
    pass
if TYPE_CHECKING:
    class anydiscrete(anypoint, metaclass=__anydiscrete_meta__):
        class __gel_reflection__(anypoint.__gel_reflection__):
            id = UUID(int=256645214055892808765094824325499150546)
            name = SchemaPath('std', 'anydiscrete')

if not TYPE_CHECKING:
    class anydiscrete(anypoint):
        __gel_type_class__: ClassVar[type] = __anydiscrete_meta__

        class __gel_reflection__(anypoint.__gel_reflection__):
            id = UUID(int=256645214055892808765094824325499150546)
            name = SchemaPath('std', 'anydiscrete')



class __anyint_meta__(__anyreal_meta__):
    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | __decimal__.Decimal | bigint | decimal | int16 | int32 | int64 | type[bigint] | type[decimal] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
            case __decimal__.Decimal():
                other = decimal(other)
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | __decimal__.Decimal | bigint | decimal | int16 | int32 | int64 | type[bigint] | type[decimal] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
            case __decimal__.Decimal():
                other = decimal(other)
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | __decimal__.Decimal | bigint | decimal | int16 | int32 | int64 | type[bigint] | type[decimal] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
            case __decimal__.Decimal():
                other = decimal(other)
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | __decimal__.Decimal | bigint | decimal | int16 | int32 | int64 | type[bigint] | type[decimal] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
            case __decimal__.Decimal():
                other = decimal(other)
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | __decimal__.Decimal | bigint | decimal | int16 | int32 | int64 | type[bigint] | type[decimal] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
            case __decimal__.Decimal():
                other = decimal(other)
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | __decimal__.Decimal | bigint | decimal | int16 | int32 | int64 | type[bigint] | type[decimal] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
            case __decimal__.Decimal():
                other = decimal(other)
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class anyint(anyreal, metaclass=__anyint_meta__):
        class __gel_reflection__(anyreal.__gel_reflection__):
            id = UUID(int=28170110488985293494671261159664909169)
            name = SchemaPath('std', 'anyint')

if not TYPE_CHECKING:
    class anyint(anyreal):
        __gel_type_class__: ClassVar[type] = __anyint_meta__

        class __gel_reflection__(anyreal.__gel_reflection__):
            id = UUID(int=28170110488985293494671261159664909169)
            name = SchemaPath('std', 'anyint')



class __anynumeric_meta__(__anyreal_meta__):
    pass
if TYPE_CHECKING:
    class anynumeric(anyreal, metaclass=__anynumeric_meta__):
        class __gel_reflection__(anyreal.__gel_reflection__):
            id = UUID(int=71430921192635612933183721885579900210)
            name = SchemaPath('std', 'anynumeric')

if not TYPE_CHECKING:
    class anynumeric(anyreal):
        __gel_type_class__: ClassVar[type] = __anynumeric_meta__

        class __gel_reflection__(anyreal.__gel_reflection__):
            id = UUID(int=71430921192635612933183721885579900210)
            name = SchemaPath('std', 'anynumeric')



class __anyfloat_meta__(__anyreal_meta__, __anycontiguous_meta__):
    pass
if TYPE_CHECKING:
    class anyfloat(anyreal, anycontiguous, metaclass=__anyfloat_meta__):
        class __gel_reflection__(
            anyreal.__gel_reflection__,
            anycontiguous.__gel_reflection__,
        ):
            id = UUID(int=149491360612205087974139247007006500201)
            name = SchemaPath('std', 'anyfloat')

if not TYPE_CHECKING:
    class anyfloat(anyreal, anycontiguous):
        __gel_type_class__: ClassVar[type] = __anyfloat_meta__

        class __gel_reflection__(
            anyreal.__gel_reflection__,
            anycontiguous.__gel_reflection__,
        ):
            id = UUID(int=149491360612205087974139247007006500201)
            name = SchemaPath('std', 'anyfloat')



class __datetime_meta__(__anycontiguous_meta__):
    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: DateTimeLike | datetime | type[datetime],
    ) -> builtins.type[bool]:
        match other:
            case DateTimeLike():
                other = datetime(other)
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: DateTimeLike | datetime | type[datetime],
    ) -> builtins.type[bool]:
        match other:
            case DateTimeLike():
                other = datetime(other)
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: DateTimeLike | datetime | type[datetime],
    ) -> builtins.type[bool]:
        match other:
            case DateTimeLike():
                other = datetime(other)
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: DateTimeLike | datetime | type[datetime],
    ) -> builtins.type[bool]:
        match other:
            case DateTimeLike():
                other = datetime(other)
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: DateTimeLike | datetime | type[datetime],
    ) -> builtins.type[bool]:
        match other:
            case DateTimeLike():
                other = datetime(other)
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: DateTimeLike | datetime | type[datetime],
    ) -> builtins.type[bool]:
        match other:
            case DateTimeLike():
                other = datetime(other)
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: __datetime_1__.timedelta | duration | gel.DateDuration | gel.RelativeDuration | std_cal.date_duration | std_cal.relative_duration | type[duration] | type[std_cal.date_duration] | type[std_cal.relative_duration],
    ) -> builtins.type[datetime]:
        match other:
            case gel.RelativeDuration():
                other = __std_cal__.relative_duration(other)
            case gel.DateDuration():
                other = __std_cal__.date_duration(other)
            case __datetime_1__.timedelta():
                other = duration(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'datetime'),
        )
        return AnnotatedExpr(datetime, op)  # type: ignore [return-value]

    @overload
    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: __datetime_1__.timedelta | duration | gel.DateDuration | gel.RelativeDuration | std_cal.date_duration | std_cal.relative_duration | type[duration] | type[std_cal.date_duration] | type[std_cal.relative_duration],
    ) -> builtins.type[datetime]:
        match other:
            case gel.RelativeDuration():
                other = __std_cal__.relative_duration(other)
            case gel.DateDuration():
                other = __std_cal__.date_duration(other)
            case __datetime_1__.timedelta():
                other = duration(other)
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=other,
            type_=SchemaPath('std', 'datetime'),
        )
        return AnnotatedExpr(datetime, op)  # type: ignore [return-value]

    @overload
    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: DateTimeLike | datetime | type[datetime],
    ) -> builtins.type[duration]:
        match other:
            case DateTimeLike():
                other = datetime(other)
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=other,
            type_=SchemaPath('std', 'duration'),
        )
        return AnnotatedExpr(duration, op)  # type: ignore [return-value]

    def __sub__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__sub__, *args, **kwargs)  # type: ignore [no-any-return]

if TYPE_CHECKING:
    class datetime(
        PyTypeScalar[__datetime__.datetime],
        anycontiguous,
        metaclass=__datetime_meta__,
    ):
        class __gel_reflection__(anycontiguous.__gel_reflection__):
            id = UUID(int=266)
            name = SchemaPath('std', 'datetime')

if not TYPE_CHECKING:
    class datetime(
        __datetime__.datetime,
        PyTypeScalar[__datetime__.datetime],
        anycontiguous,
    ):
        __gel_type_class__: ClassVar[type] = __datetime_meta__

        class __gel_reflection__(anycontiguous.__gel_reflection__):
            id = UUID(int=266)
            name = SchemaPath('std', 'datetime')



class __duration_meta__(__anycontiguous_meta__):
    def __neg__(cls) -> builtins.type[duration]:
        return AnnotatedExpr(  # type: ignore [return-value]
            duration,
            PrefixOp(expr=cls, op="-", type_=SchemaPath('std', 'duration')),
        )

    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: DateTimeLike | datetime | type[datetime],
    ) -> builtins.type[datetime]:
        match other:
            case DateTimeLike():
                other = datetime(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'datetime'),
        )
        return AnnotatedExpr(datetime, op)  # type: ignore [return-value]

    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: __datetime_1__.timedelta | duration | type[duration],
    ) -> builtins.type[duration]:
        match other:
            case __datetime_1__.timedelta():
                other = duration(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'duration'),
        )
        return AnnotatedExpr(duration, op)  # type: ignore [return-value]

    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: __datetime_1__.date | std_cal.local_date | std_cal.local_datetime | type[std_cal.local_date] | type[std_cal.local_datetime],
    ) -> builtins.type[std_cal.local_datetime]:
        match other:
            case __datetime_1__.date():
                other = __std_cal__.local_date(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
        return AnnotatedExpr(__std_cal__.local_datetime, op)  # type: ignore [return-value]

    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: __datetime_1__.time | std_cal.local_time | type[std_cal.local_time],
    ) -> builtins.type[std_cal.local_time]:
        match other:
            case __datetime_1__.time():
                other = __std_cal__.local_time(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'local_time'),
        )
        return AnnotatedExpr(__std_cal__.local_time, op)  # type: ignore [return-value]

    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: gel.DateDuration | gel.RelativeDuration | std_cal.date_duration | std_cal.relative_duration | type[std_cal.date_duration] | type[std_cal.relative_duration],
    ) -> builtins.type[std_cal.relative_duration]:
        match other:
            case gel.RelativeDuration():
                other = __std_cal__.relative_duration(other)
            case gel.DateDuration():
                other = __std_cal__.date_duration(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        )
        return AnnotatedExpr(__std_cal__.relative_duration, op)  # type: ignore [return-value]

    def __add__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__add__, *args, **kwargs)  # type: ignore [no-any-return]

    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: __datetime_1__.timedelta | duration | type[duration],
    ) -> builtins.type[bool]:
        match other:
            case __datetime_1__.timedelta():
                other = duration(other)
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: __datetime_1__.timedelta | duration | type[duration],
    ) -> builtins.type[bool]:
        match other:
            case __datetime_1__.timedelta():
                other = duration(other)
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __datetime_1__.timedelta | duration | type[duration],
    ) -> builtins.type[bool]:
        match other:
            case __datetime_1__.timedelta():
                other = duration(other)
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: __datetime_1__.timedelta | duration | type[duration],
    ) -> builtins.type[bool]:
        match other:
            case __datetime_1__.timedelta():
                other = duration(other)
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __datetime_1__.timedelta | duration | type[duration],
    ) -> builtins.type[bool]:
        match other:
            case __datetime_1__.timedelta():
                other = duration(other)
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: __datetime_1__.timedelta | duration | type[duration],
    ) -> builtins.type[bool]:
        match other:
            case __datetime_1__.timedelta():
                other = duration(other)
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    @overload
    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: __datetime_1__.timedelta | duration | type[duration],
    ) -> builtins.type[duration]:
        match other:
            case __datetime_1__.timedelta():
                other = duration(other)
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=other,
            type_=SchemaPath('std', 'duration'),
        )
        return AnnotatedExpr(duration, op)  # type: ignore [return-value]

    @overload
    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: gel.DateDuration | gel.RelativeDuration | std_cal.date_duration | std_cal.relative_duration | type[std_cal.date_duration] | type[std_cal.relative_duration],
    ) -> builtins.type[std_cal.relative_duration]:
        match other:
            case gel.RelativeDuration():
                other = __std_cal__.relative_duration(other)
            case gel.DateDuration():
                other = __std_cal__.date_duration(other)
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        )
        return AnnotatedExpr(__std_cal__.relative_duration, op)  # type: ignore [return-value]

    def __sub__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__sub__, *args, **kwargs)  # type: ignore [no-any-return]

if TYPE_CHECKING:
    class duration(
        PyTypeScalar[timedelta],
        anycontiguous,
        metaclass=__duration_meta__,
    ):
        class __gel_reflection__(anycontiguous.__gel_reflection__):
            id = UUID(int=270)
            name = SchemaPath('std', 'duration')

if not TYPE_CHECKING:
    class duration(timedelta, PyTypeScalar[timedelta], anycontiguous):
        __gel_type_class__: ClassVar[type] = __duration_meta__

        class __gel_reflection__(anycontiguous.__gel_reflection__):
            id = UUID(int=270)
            name = SchemaPath('std', 'duration')



class __int16_meta__(__anyint_meta__):
    def __pos__(cls) -> builtins.type[int16]:
        return AnnotatedExpr(  # type: ignore [return-value]
            int16,
            PrefixOp(expr=cls, op="+", type_=SchemaPath('std', 'int16')),
        )

    def __neg__(cls) -> builtins.type[int16]:
        return AnnotatedExpr(  # type: ignore [return-value]
            int16,
            PrefixOp(expr=cls, op="-", type_=SchemaPath('std', 'int16')),
        )

    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | int64 | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | int64 | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | int64 | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | int64 | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | int64 | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | int64 | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | type[int16],
    ) -> builtins.type[int16]:
        match other:
            case __builtins_1__.int():
                other = int16(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'int16'),
        )
        return AnnotatedExpr(int16, op)  # type: ignore [return-value]

    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | type[int16],
    ) -> builtins.type[int16]:
        match other:
            case __builtins_1__.int():
                other = int16(other)
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=other,
            type_=SchemaPath('std', 'int16'),
        )
        return AnnotatedExpr(int16, op)  # type: ignore [return-value]

    def __mul__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | type[int16],
    ) -> builtins.type[int16]:
        match other:
            case __builtins_1__.int():
                other = int16(other)
        op = InfixOp(
            lexpr=cls,
            op="*",
            rexpr=other,
            type_=SchemaPath('std', 'int16'),
        )
        return AnnotatedExpr(int16, op)  # type: ignore [return-value]

    def __floordiv__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | type[int16],
    ) -> builtins.type[int16]:
        match other:
            case __builtins_1__.int():
                other = int16(other)
        op = InfixOp(
            lexpr=cls,
            op="",
            rexpr=other,
            type_=SchemaPath('std', 'int16'),
        )
        return AnnotatedExpr(int16, op)  # type: ignore [return-value]

    def __mod__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | type[int16],
    ) -> builtins.type[int16]:
        match other:
            case __builtins_1__.int():
                other = int16(other)
        op = InfixOp(
            lexpr=cls,
            op="%",
            rexpr=other,
            type_=SchemaPath('std', 'int16'),
        )
        return AnnotatedExpr(int16, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class int16(PyTypeScalar[int], anyint, metaclass=__int16_meta__):
        class __gel_reflection__(anyint.__gel_reflection__):
            id = UUID(int=259)
            name = SchemaPath('std', 'int16')

if not TYPE_CHECKING:
    class int16(int, PyTypeScalar[int], anyint):
        __gel_type_class__: ClassVar[type] = __int16_meta__

        class __gel_reflection__(anyint.__gel_reflection__):
            id = UUID(int=259)
            name = SchemaPath('std', 'int16')



class __int32_meta__(__anyint_meta__, __anydiscrete_meta__):
    def __pos__(cls) -> builtins.type[int32]:
        return AnnotatedExpr(  # type: ignore [return-value]
            int32,
            PrefixOp(expr=cls, op="+", type_=SchemaPath('std', 'int32')),
        )

    def __neg__(cls) -> builtins.type[int32]:
        return AnnotatedExpr(  # type: ignore [return-value]
            int32,
            PrefixOp(expr=cls, op="-", type_=SchemaPath('std', 'int32')),
        )

    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | int64 | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | int64 | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | int16 | int32 | int64 | type[float32] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float32(other)
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | int16 | int32 | int64 | type[float32] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float32(other)
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | int16 | int32 | int64 | type[float32] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float32(other)
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | int16 | int32 | int64 | type[float32] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float32(other)
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | type[int16] | type[int32],
    ) -> builtins.type[int32]:
        match other:
            case __builtins_1__.int():
                other = int32(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'int32'),
        )
        return AnnotatedExpr(int32, op)  # type: ignore [return-value]

    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | type[int16] | type[int32],
    ) -> builtins.type[int32]:
        match other:
            case __builtins_1__.int():
                other = int32(other)
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=other,
            type_=SchemaPath('std', 'int32'),
        )
        return AnnotatedExpr(int32, op)  # type: ignore [return-value]

    def __mul__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | type[int16] | type[int32],
    ) -> builtins.type[int32]:
        match other:
            case __builtins_1__.int():
                other = int32(other)
        op = InfixOp(
            lexpr=cls,
            op="*",
            rexpr=other,
            type_=SchemaPath('std', 'int32'),
        )
        return AnnotatedExpr(int32, op)  # type: ignore [return-value]

    def __floordiv__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | type[int16] | type[int32],
    ) -> builtins.type[int32]:
        match other:
            case __builtins_1__.int():
                other = int32(other)
        op = InfixOp(
            lexpr=cls,
            op="",
            rexpr=other,
            type_=SchemaPath('std', 'int32'),
        )
        return AnnotatedExpr(int32, op)  # type: ignore [return-value]

    def __mod__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | type[int16] | type[int32],
    ) -> builtins.type[int32]:
        match other:
            case __builtins_1__.int():
                other = int32(other)
        op = InfixOp(
            lexpr=cls,
            op="%",
            rexpr=other,
            type_=SchemaPath('std', 'int32'),
        )
        return AnnotatedExpr(int32, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class int32(
        PyTypeScalar[int],
        anyint,
        anydiscrete,
        metaclass=__int32_meta__,
    ):
        class __gel_reflection__(
            anyint.__gel_reflection__,
            anydiscrete.__gel_reflection__,
        ):
            id = UUID(int=260)
            name = SchemaPath('std', 'int32')

if not TYPE_CHECKING:
    class int32(int, PyTypeScalar[int], anyint, anydiscrete):
        __gel_type_class__: ClassVar[type] = __int32_meta__

        class __gel_reflection__(
            anyint.__gel_reflection__,
            anydiscrete.__gel_reflection__,
        ):
            id = UUID(int=260)
            name = SchemaPath('std', 'int32')



class __int64_meta__(__anyint_meta__, __anydiscrete_meta__):
    def __pos__(cls) -> builtins.type[int64]:
        return AnnotatedExpr(  # type: ignore [return-value]
            int64,
            PrefixOp(expr=cls, op="+", type_=SchemaPath('std', 'int64')),
        )

    def __neg__(cls) -> builtins.type[int64]:
        return AnnotatedExpr(  # type: ignore [return-value]
            int64,
            PrefixOp(expr=cls, op="-", type_=SchemaPath('std', 'int64')),
        )

    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | int64 | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | int64 | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | int64 | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[int64]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'int64'),
        )
        return AnnotatedExpr(int64, op)  # type: ignore [return-value]

    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | int64 | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[int64]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=other,
            type_=SchemaPath('std', 'int64'),
        )
        return AnnotatedExpr(int64, op)  # type: ignore [return-value]

    def __mul__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | int64 | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[int64]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
        op = InfixOp(
            lexpr=cls,
            op="*",
            rexpr=other,
            type_=SchemaPath('std', 'int64'),
        )
        return AnnotatedExpr(int64, op)  # type: ignore [return-value]

    def __truediv__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | int64 | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[float64]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
        op = InfixOp(
            lexpr=cls,
            op="",
            rexpr=other,
            type_=SchemaPath('std', 'float64'),
        )
        return AnnotatedExpr(float64, op)  # type: ignore [return-value]

    def __floordiv__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | int64 | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[int64]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
        op = InfixOp(
            lexpr=cls,
            op="",
            rexpr=other,
            type_=SchemaPath('std', 'int64'),
        )
        return AnnotatedExpr(int64, op)  # type: ignore [return-value]

    def __mod__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | int64 | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[int64]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
        op = InfixOp(
            lexpr=cls,
            op="%",
            rexpr=other,
            type_=SchemaPath('std', 'int64'),
        )
        return AnnotatedExpr(int64, op)  # type: ignore [return-value]

    def __pow__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | int16 | int32 | int64 | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[float64]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
        op = InfixOp(
            lexpr=cls,
            op="^",
            rexpr=other,
            type_=SchemaPath('std', 'float64'),
        )
        return AnnotatedExpr(float64, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class int64(
        PyTypeScalar[int],
        anyint,
        anydiscrete,
        metaclass=__int64_meta__,
    ):
        class __gel_reflection__(
            anyint.__gel_reflection__,
            anydiscrete.__gel_reflection__,
        ):
            id = UUID(int=261)
            name = SchemaPath('std', 'int64')

if not TYPE_CHECKING:
    class int64(int, PyTypeScalar[int], anyint, anydiscrete):
        __gel_type_class__: ClassVar[type] = __int64_meta__

        class __gel_reflection__(
            anyint.__gel_reflection__,
            anydiscrete.__gel_reflection__,
        ):
            id = UUID(int=261)
            name = SchemaPath('std', 'int64')



class __bigint_meta__(__anynumeric_meta__, __anyint_meta__):
    def __pos__(cls) -> builtins.type[bigint]:
        return AnnotatedExpr(  # type: ignore [return-value]
            bigint,
            PrefixOp(expr=cls, op="+", type_=SchemaPath('std', 'bigint')),
        )

    def __neg__(cls) -> builtins.type[bigint]:
        return AnnotatedExpr(  # type: ignore [return-value]
            bigint,
            PrefixOp(expr=cls, op="-", type_=SchemaPath('std', 'bigint')),
        )

    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | bigint | int16 | int32 | int64 | type[bigint] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | bigint | int16 | int32 | int64 | type[bigint] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | bigint | int16 | int32 | int64 | type[bigint] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | bigint | int16 | int32 | int64 | type[bigint] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | bigint | int16 | int32 | int64 | type[bigint] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | bigint | int16 | int32 | int64 | type[bigint] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | bigint | int16 | int32 | int64 | type[bigint] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bigint]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'bigint'),
        )
        return AnnotatedExpr(bigint, op)  # type: ignore [return-value]

    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | bigint | int16 | int32 | int64 | type[bigint] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bigint]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=other,
            type_=SchemaPath('std', 'bigint'),
        )
        return AnnotatedExpr(bigint, op)  # type: ignore [return-value]

    def __mul__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | bigint | int16 | int32 | int64 | type[bigint] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bigint]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
        op = InfixOp(
            lexpr=cls,
            op="*",
            rexpr=other,
            type_=SchemaPath('std', 'bigint'),
        )
        return AnnotatedExpr(bigint, op)  # type: ignore [return-value]

    def __floordiv__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | bigint | int16 | int32 | int64 | type[bigint] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bigint]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
        op = InfixOp(
            lexpr=cls,
            op="",
            rexpr=other,
            type_=SchemaPath('std', 'bigint'),
        )
        return AnnotatedExpr(bigint, op)  # type: ignore [return-value]

    def __mod__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | bigint | int16 | int32 | int64 | type[bigint] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bigint]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
        op = InfixOp(
            lexpr=cls,
            op="%",
            rexpr=other,
            type_=SchemaPath('std', 'bigint'),
        )
        return AnnotatedExpr(bigint, op)  # type: ignore [return-value]

    def __pow__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | bigint | int16 | int32 | int64 | type[bigint] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[decimal]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
        op = InfixOp(
            lexpr=cls,
            op="^",
            rexpr=other,
            type_=SchemaPath('std', 'decimal'),
        )
        return AnnotatedExpr(decimal, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class bigint(
        PyTypeScalar[int],
        anynumeric,
        anyint,
        metaclass=__bigint_meta__,
    ):
        class __gel_reflection__(
            anynumeric.__gel_reflection__,
            anyint.__gel_reflection__,
        ):
            id = UUID(int=272)
            name = SchemaPath('std', 'bigint')

if not TYPE_CHECKING:
    class bigint(int, PyTypeScalar[int], anynumeric, anyint):
        __gel_type_class__: ClassVar[type] = __bigint_meta__

        class __gel_reflection__(
            anynumeric.__gel_reflection__,
            anyint.__gel_reflection__,
        ):
            id = UUID(int=272)
            name = SchemaPath('std', 'bigint')



class __decimal_meta__(__anynumeric_meta__, __anycontiguous_meta__):
    def __pos__(cls) -> builtins.type[decimal]:
        return AnnotatedExpr(  # type: ignore [return-value]
            decimal,
            PrefixOp(expr=cls, op="+", type_=SchemaPath('std', 'decimal')),
        )

    def __neg__(cls) -> builtins.type[decimal]:
        return AnnotatedExpr(  # type: ignore [return-value]
            decimal,
            PrefixOp(expr=cls, op="-", type_=SchemaPath('std', 'decimal')),
        )

    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | __decimal__.Decimal | anyint | bigint | decimal | int16 | int32 | int64 | type[anyint] | type[bigint] | type[decimal] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
            case __decimal__.Decimal():
                other = decimal(other)
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | __decimal__.Decimal | anyint | bigint | decimal | int16 | int32 | int64 | type[anyint] | type[bigint] | type[decimal] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
            case __decimal__.Decimal():
                other = decimal(other)
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | __decimal__.Decimal | anyint | bigint | decimal | int16 | int32 | int64 | type[anyint] | type[bigint] | type[decimal] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
            case __decimal__.Decimal():
                other = decimal(other)
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | __decimal__.Decimal | anyint | bigint | decimal | int16 | int32 | int64 | type[anyint] | type[bigint] | type[decimal] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
            case __decimal__.Decimal():
                other = decimal(other)
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | __decimal__.Decimal | anyint | bigint | decimal | int16 | int32 | int64 | type[anyint] | type[bigint] | type[decimal] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
            case __decimal__.Decimal():
                other = decimal(other)
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | __decimal__.Decimal | anyint | bigint | decimal | int16 | int32 | int64 | type[anyint] | type[bigint] | type[decimal] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
            case __decimal__.Decimal():
                other = decimal(other)
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | __decimal__.Decimal | bigint | decimal | int16 | int32 | int64 | type[bigint] | type[decimal] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[decimal]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
            case __decimal__.Decimal():
                other = decimal(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'decimal'),
        )
        return AnnotatedExpr(decimal, op)  # type: ignore [return-value]

    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | __decimal__.Decimal | bigint | decimal | int16 | int32 | int64 | type[bigint] | type[decimal] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[decimal]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
            case __decimal__.Decimal():
                other = decimal(other)
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=other,
            type_=SchemaPath('std', 'decimal'),
        )
        return AnnotatedExpr(decimal, op)  # type: ignore [return-value]

    def __mul__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | __decimal__.Decimal | bigint | decimal | int16 | int32 | int64 | type[bigint] | type[decimal] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[decimal]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
            case __decimal__.Decimal():
                other = decimal(other)
        op = InfixOp(
            lexpr=cls,
            op="*",
            rexpr=other,
            type_=SchemaPath('std', 'decimal'),
        )
        return AnnotatedExpr(decimal, op)  # type: ignore [return-value]

    def __truediv__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | __decimal__.Decimal | bigint | decimal | int16 | int32 | int64 | type[bigint] | type[decimal] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[decimal]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
            case __decimal__.Decimal():
                other = decimal(other)
        op = InfixOp(
            lexpr=cls,
            op="",
            rexpr=other,
            type_=SchemaPath('std', 'decimal'),
        )
        return AnnotatedExpr(decimal, op)  # type: ignore [return-value]

    def __floordiv__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | __decimal__.Decimal | bigint | decimal | int16 | int32 | int64 | type[bigint] | type[decimal] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[decimal]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
            case __decimal__.Decimal():
                other = decimal(other)
        op = InfixOp(
            lexpr=cls,
            op="",
            rexpr=other,
            type_=SchemaPath('std', 'decimal'),
        )
        return AnnotatedExpr(decimal, op)  # type: ignore [return-value]

    def __mod__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | __decimal__.Decimal | bigint | decimal | int16 | int32 | int64 | type[bigint] | type[decimal] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[decimal]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
            case __decimal__.Decimal():
                other = decimal(other)
        op = InfixOp(
            lexpr=cls,
            op="%",
            rexpr=other,
            type_=SchemaPath('std', 'decimal'),
        )
        return AnnotatedExpr(decimal, op)  # type: ignore [return-value]

    def __pow__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.int | __decimal__.Decimal | bigint | decimal | int16 | int32 | int64 | type[bigint] | type[decimal] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[decimal]:
        match other:
            case __builtins_1__.int():
                other = bigint(other)
            case __decimal__.Decimal():
                other = decimal(other)
        op = InfixOp(
            lexpr=cls,
            op="^",
            rexpr=other,
            type_=SchemaPath('std', 'decimal'),
        )
        return AnnotatedExpr(decimal, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class decimal(
        PyTypeScalar[Decimal],
        anynumeric,
        anycontiguous,
        metaclass=__decimal_meta__,
    ):
        class __gel_reflection__(
            anynumeric.__gel_reflection__,
            anycontiguous.__gel_reflection__,
        ):
            id = UUID(int=264)
            name = SchemaPath('std', 'decimal')

if not TYPE_CHECKING:
    class decimal(Decimal, PyTypeScalar[Decimal], anynumeric, anycontiguous):
        __gel_type_class__: ClassVar[type] = __decimal_meta__

        class __gel_reflection__(
            anynumeric.__gel_reflection__,
            anycontiguous.__gel_reflection__,
        ):
            id = UUID(int=264)
            name = SchemaPath('std', 'decimal')



class __float32_meta__(__anyfloat_meta__):
    def __pos__(cls) -> builtins.type[float32]:
        return AnnotatedExpr(  # type: ignore [return-value]
            float32,
            PrefixOp(expr=cls, op="+", type_=SchemaPath('std', 'float32')),
        )

    def __neg__(cls) -> builtins.type[float32]:
        return AnnotatedExpr(  # type: ignore [return-value]
            float32,
            PrefixOp(expr=cls, op="-", type_=SchemaPath('std', 'float32')),
        )

    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int32(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int32(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int32(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int32(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | int16 | type[float32] | type[int16],
    ) -> builtins.type[float32]:
        match other:
            case __builtins_1__.int():
                other = int16(other)
            case __builtins_1__.float():
                other = float32(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'float32'),
        )
        return AnnotatedExpr(float32, op)  # type: ignore [return-value]

    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | int16 | type[float32] | type[int16],
    ) -> builtins.type[float32]:
        match other:
            case __builtins_1__.int():
                other = int16(other)
            case __builtins_1__.float():
                other = float32(other)
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=other,
            type_=SchemaPath('std', 'float32'),
        )
        return AnnotatedExpr(float32, op)  # type: ignore [return-value]

    def __mul__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | int16 | type[float32] | type[int16],
    ) -> builtins.type[float32]:
        match other:
            case __builtins_1__.int():
                other = int16(other)
            case __builtins_1__.float():
                other = float32(other)
        op = InfixOp(
            lexpr=cls,
            op="*",
            rexpr=other,
            type_=SchemaPath('std', 'float32'),
        )
        return AnnotatedExpr(float32, op)  # type: ignore [return-value]

    def __truediv__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | int16 | type[float32] | type[int16],
    ) -> builtins.type[float32]:
        match other:
            case __builtins_1__.int():
                other = int16(other)
            case __builtins_1__.float():
                other = float32(other)
        op = InfixOp(
            lexpr=cls,
            op="",
            rexpr=other,
            type_=SchemaPath('std', 'float32'),
        )
        return AnnotatedExpr(float32, op)  # type: ignore [return-value]

    def __floordiv__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | int16 | type[float32] | type[int16],
    ) -> builtins.type[float32]:
        match other:
            case __builtins_1__.int():
                other = int16(other)
            case __builtins_1__.float():
                other = float32(other)
        op = InfixOp(
            lexpr=cls,
            op="",
            rexpr=other,
            type_=SchemaPath('std', 'float32'),
        )
        return AnnotatedExpr(float32, op)  # type: ignore [return-value]

    def __mod__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | int16 | type[float32] | type[int16],
    ) -> builtins.type[float32]:
        match other:
            case __builtins_1__.int():
                other = int16(other)
            case __builtins_1__.float():
                other = float32(other)
        op = InfixOp(
            lexpr=cls,
            op="%",
            rexpr=other,
            type_=SchemaPath('std', 'float32'),
        )
        return AnnotatedExpr(float32, op)  # type: ignore [return-value]

    def __pow__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | int16 | type[float32] | type[int16],
    ) -> builtins.type[float32]:
        match other:
            case __builtins_1__.int():
                other = int16(other)
            case __builtins_1__.float():
                other = float32(other)
        op = InfixOp(
            lexpr=cls,
            op="^",
            rexpr=other,
            type_=SchemaPath('std', 'float32'),
        )
        return AnnotatedExpr(float32, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class float32(PyTypeScalar[float], anyfloat, metaclass=__float32_meta__):
        class __gel_reflection__(anyfloat.__gel_reflection__):
            id = UUID(int=262)
            name = SchemaPath('std', 'float32')

if not TYPE_CHECKING:
    class float32(float, PyTypeScalar[float], anyfloat):
        __gel_type_class__: ClassVar[type] = __float32_meta__

        class __gel_reflection__(anyfloat.__gel_reflection__):
            id = UUID(int=262)
            name = SchemaPath('std', 'float32')



class __float64_meta__(__anyfloat_meta__):
    def __pos__(cls) -> builtins.type[float64]:
        return AnnotatedExpr(  # type: ignore [return-value]
            float64,
            PrefixOp(expr=cls, op="+", type_=SchemaPath('std', 'float64')),
        )

    def __neg__(cls) -> builtins.type[float64]:
        return AnnotatedExpr(  # type: ignore [return-value]
            float64,
            PrefixOp(expr=cls, op="-", type_=SchemaPath('std', 'float64')),
        )

    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[bool]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[float64]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'float64'),
        )
        return AnnotatedExpr(float64, op)  # type: ignore [return-value]

    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[float64]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=other,
            type_=SchemaPath('std', 'float64'),
        )
        return AnnotatedExpr(float64, op)  # type: ignore [return-value]

    def __mul__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[float64]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op="*",
            rexpr=other,
            type_=SchemaPath('std', 'float64'),
        )
        return AnnotatedExpr(float64, op)  # type: ignore [return-value]

    def __truediv__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[float64]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op="",
            rexpr=other,
            type_=SchemaPath('std', 'float64'),
        )
        return AnnotatedExpr(float64, op)  # type: ignore [return-value]

    def __floordiv__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[float64]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op="",
            rexpr=other,
            type_=SchemaPath('std', 'float64'),
        )
        return AnnotatedExpr(float64, op)  # type: ignore [return-value]

    def __mod__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[float64]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op="%",
            rexpr=other,
            type_=SchemaPath('std', 'float64'),
        )
        return AnnotatedExpr(float64, op)  # type: ignore [return-value]

    def __pow__(  # type: ignore [override, unused-ignore]
        cls,
        other: __builtins_1__.float | __builtins_1__.int | float32 | float64 | int16 | int32 | int64 | type[float32] | type[float64] | type[int16] | type[int32] | type[int64],
    ) -> builtins.type[float64]:
        match other:
            case __builtins_1__.int():
                other = int64(other)
            case __builtins_1__.float():
                other = float64(other)
        op = InfixOp(
            lexpr=cls,
            op="^",
            rexpr=other,
            type_=SchemaPath('std', 'float64'),
        )
        return AnnotatedExpr(float64, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class float64(PyTypeScalar[float], anyfloat, metaclass=__float64_meta__):
        class __gel_reflection__(anyfloat.__gel_reflection__):
            id = UUID(int=263)
            name = SchemaPath('std', 'float64')

if not TYPE_CHECKING:
    class float64(float, PyTypeScalar[float], anyfloat):
        __gel_type_class__: ClassVar[type] = __float64_meta__

        class __gel_reflection__(anyfloat.__gel_reflection__):
            id = UUID(int=263)
            name = SchemaPath('std', 'float64')



class __sequence_meta__(__int64_meta__):
    pass
if TYPE_CHECKING:
    class sequence(int64, metaclass=__sequence_meta__):
        class __gel_reflection__(int64.__gel_reflection__):
            id = UUID(int=336441748978705185582592859268133356285)
            name = SchemaPath('std', 'sequence')

if not TYPE_CHECKING:
    class sequence(int64):
        __gel_type_class__: ClassVar[type] = __sequence_meta__

        class __gel_reflection__(int64.__gel_reflection__):
            id = UUID(int=336441748978705185582592859268133356285)
            name = SchemaPath('std', 'sequence')




#
# type std::BaseObject
#
class __BaseObject_typeof__(GelTypeMetadata):
    class __gel_reflection__:
        id = UUID(int=17388446936501731861753544685220838082)
        name = SchemaPath('std', 'BaseObject')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=17388446936501731861753544685220838082),
                name='std::BaseObject',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__:
        id = TypeAliasType('id', 'uuid')
        __type__ = TypeAliasType('__type__', '__schema__.ObjectType')


class __BaseObject_ops__(GelModelMeta):
    def __eq__(cls, other: type[std.BaseObject]) -> builtins.type[bool]:  # type: ignore [override, unused-ignore]
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ne__(cls, other: type[std.BaseObject]) -> builtins.type[bool]:  # type: ignore [override, unused-ignore]
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __ge__(cls, other: type[std.BaseObject]) -> builtins.type[bool]:  # type: ignore [override, unused-ignore]
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __gt__(cls, other: type[std.BaseObject]) -> builtins.type[bool]:  # type: ignore [override, unused-ignore]
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __le__(cls, other: type[std.BaseObject]) -> builtins.type[bool]:  # type: ignore [override, unused-ignore]
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

    def __lt__(cls, other: type[std.BaseObject]) -> builtins.type[bool]:  # type: ignore [override, unused-ignore]
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(bool, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    __BaseObject_meta__ = __BaseObject_ops__
if not TYPE_CHECKING:
    __BaseObject_meta__ = GelModelMeta
class BaseObject(
    __BaseObject_typeof__,
    GelModel,
    metaclass=__BaseObject_meta__,
    __gel_type_id__=UUID(int=17388446936501731861753544685220838082),
):
    if not TYPE_CHECKING:
        __gel_type_class__ = __BaseObject_ops__
    id: IdProperty[uuid, UUID] # type: ignore [assignment]

    @property
    def __type__(self) -> __schema_1__.ObjectType:
        tid = self.__class__.__gel_reflection__.id
        actualcls = GelModelMeta.get_class_by_id(tid)
        return actualcls.__gel_reflection__.object  # type: ignore [attr-defined, no-any-return]

    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new std::BaseObject instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
            """Update std::BaseObject instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: __builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch std::BaseObject instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[bool]],
            id: UUID | type[uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch std::BaseObject instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins_1__.str, EmptyDirection | __builtins_1__.str],
            id: Direction | __builtins_1__.str | __builtins_1__.str | __builtins_1__.bool | tuple[Direction | __builtins_1__.str, EmptyDirection | __builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...

        @classmethod
        def limit(cls, value: type[int64] | int) -> type[Self]:
            """Limit selection to a set number of entries."""
            ...

        @classmethod
        def offset(cls, value: type[int64] | int) -> type[Self]:
            """Start selection from a specific offset."""
            ...


    class __variants__:
        class Base(
            __BaseObject_typeof__,
            GelModel,
            metaclass=__BaseObject_meta__,
        ):
            id: IdProperty[uuid, UUID] # type: ignore [assignment]

            @property
            def __type__(self) -> __schema_1__.ObjectType:
                tid = self.__class__.__gel_reflection__.id
                actualcls = GelModelMeta.get_class_by_id(tid)
                return actualcls.__gel_reflection__.object  # type: ignore [attr-defined, no-any-return]

            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new std::BaseObject instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
                    """Update std::BaseObject instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: __builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch std::BaseObject instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[bool]],
                    id: UUID | type[uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch std::BaseObject instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins_1__.str, EmptyDirection | __builtins_1__.str],
                    id: Direction | __builtins_1__.str | __builtins_1__.str | __builtins_1__.bool | tuple[Direction | __builtins_1__.str, EmptyDirection | __builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

                @classmethod
                def limit(cls, value: type[int64] | int) -> type[Self]:
                    """Limit selection to a set number of entries."""
                    ...

                @classmethod
                def offset(cls, value: type[int64] | int) -> type[Self]:
                    """Start selection from a specific offset."""
                    ...


        Any = TypeVar("Any", bound="BaseObject | Base")
    class __links__(LinkClassNamespace):
        pass

if not TYPE_CHECKING:
    BaseObject.__variants__.Base = BaseObject



#
# type std::FreeObject
#
class __FreeObject_typeof__(GelTypeMetadata):
    class __gel_reflection__:
        id = UUID(int=79027269369460379376539429265091668712)
        name = SchemaPath('std', 'FreeObject')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=79027269369460379376539429265091668712),
                name='std::FreeObject',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__:
        pass


class __FreeObject_ops__(GelModelMeta):
    pass
if TYPE_CHECKING:
    __FreeObject_meta__ = __FreeObject_ops__
if not TYPE_CHECKING:
    __FreeObject_meta__ = GelModelMeta
class FreeObject(
    __FreeObject_typeof__,
    GelModel,
    metaclass=__FreeObject_meta__,
    __gel_type_id__=UUID(int=79027269369460379376539429265091668712),
):
    if not TYPE_CHECKING:
        __gel_type_class__ = __FreeObject_ops__
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new std::FreeObject instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
            """Update std::FreeObject instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch std::FreeObject instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[bool]],
        ) -> type[Self]:
            """Fetch std::FreeObject instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins_1__.str, EmptyDirection | __builtins_1__.str],
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__:
        class Base(
            __FreeObject_typeof__,
            GelModel,
            metaclass=__FreeObject_meta__,
        ):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new std::FreeObject instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
                    """Update std::FreeObject instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch std::FreeObject instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[bool]],
                ) -> type[Self]:
                    """Fetch std::FreeObject instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins_1__.str, EmptyDirection | __builtins_1__.str],
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="FreeObject | Base")
    class __links__(LinkClassNamespace):
        pass

if not TYPE_CHECKING:
    FreeObject.__variants__.Base = FreeObject



#
# type std::Object
#
class __Object_typeof__(__BaseObject_typeof__):
    class __gel_reflection__(__BaseObject_typeof__.__gel_reflection__):
        id = UUID(int=187300570928289568776573349376249136520)
        name = SchemaPath('std', 'Object')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=187300570928289568776573349376249136520),
                name='std::Object',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__(__BaseObject_typeof__.__typeof__):
        pass


class Object(
    __Object_typeof__,
    BaseObject,
    __gel_type_id__=UUID(int=187300570928289568776573349376249136520),
):
    if TYPE_CHECKING:
        def __init__(self) -> None:
            """Create a new std::Object instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
            """Update std::Object instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: __builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[uuid] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch std::Object instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[bool]],
            id: UUID | type[uuid] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch std::Object instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins_1__.str, EmptyDirection | __builtins_1__.str],
            id: Direction | __builtins_1__.str | __builtins_1__.str | __builtins_1__.bool | tuple[Direction | __builtins_1__.str, EmptyDirection | __builtins_1__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(BaseObject.__variants__):
        class Base(__Object_typeof__, BaseObject.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(self) -> None:
                    """Create a new std::Object instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(cls) -> type[Self]:  # type: ignore [override, unused-ignore]
                    """Update std::Object instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: __builtins_1__.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[uuid] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch std::Object instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[bool]],
                    id: UUID | type[uuid] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch std::Object instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins_1__.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | __builtins_1__.str, EmptyDirection | __builtins_1__.str],
                    id: Direction | __builtins_1__.str | __builtins_1__.str | __builtins_1__.bool | tuple[Direction | __builtins_1__.str, EmptyDirection | __builtins_1__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Object | Base")
    class __links__(BaseObject.__links__):
        pass

if not TYPE_CHECKING:
    Object.__variants__.Base = Object



from . import cal as __std_cal__  # noqa: E402 F403
from .. import schema as __schema__  # noqa: E402 F403
from ... import schema as __schema_1__  # noqa: E402 F403
