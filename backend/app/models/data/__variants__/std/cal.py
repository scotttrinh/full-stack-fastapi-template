#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from .. import std

import gel as gel
from gel import DateDuration, RelativeDuration
from gel.models.pydantic import (
    AnnotatedExpr,
    DateTimeLike,
    InfixOp,
    PrefixOp,
    PyTypeScalar,
    SchemaPath,
    dispatch_overload
)

import datetime as datetime
import datetime as __datetime__
from builtins import type
from datetime import date, time
from typing import Any, TYPE_CHECKING, overload
from uuid import UUID

if TYPE_CHECKING:

    from .. import std as __std__

    import builtins as builtins
    from typing import ClassVar



class __date_duration_meta__(std.__anyscalar_meta__):
    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | type[local_date],
    ) -> builtins.type[local_date]:
        match other:
            case datetime.date():
                other = local_date(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'local_date'),
        )
        return AnnotatedExpr(local_date, op)  # type: ignore [return-value]

    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: date_duration | gel.DateDuration | type[date_duration],
    ) -> builtins.type[date_duration]:
        match other:
            case gel.DateDuration():
                other = date_duration(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'date_duration'),
        )
        return AnnotatedExpr(date_duration, op)  # type: ignore [return-value]

    def __add__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__add__, *args, **kwargs)  # type: ignore [no-any-return]

    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: date_duration | gel.DateDuration | type[date_duration],
    ) -> builtins.type[date_duration]:
        match other:
            case gel.DateDuration():
                other = date_duration(other)
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'date_duration'),
        )
        return AnnotatedExpr(date_duration, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class date_duration(
        PyTypeScalar[DateDuration],
        std.anyscalar,
        metaclass=__date_duration_meta__,
    ):
        class __gel_reflection__(__std__.anyscalar.__gel_reflection__):
            id = UUID(int=274)
            name = SchemaPath('std', 'cal', 'date_duration')

if not TYPE_CHECKING:
    class date_duration(
        DateDuration,
        PyTypeScalar[DateDuration],
        std.anyscalar,
    ):
        __gel_type_class__: ClassVar[type] = __date_duration_meta__

        class __gel_reflection__(std.anyscalar.__gel_reflection__):
            id = UUID(int=274)
            name = SchemaPath('std', 'cal', 'date_duration')



class __local_date_meta__(std.__anydiscrete_meta__):
    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | type[local_date],
    ) -> builtins.type[__std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | type[local_date],
    ) -> builtins.type[__std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | type[local_date],
    ) -> builtins.type[__std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | type[local_date],
    ) -> builtins.type[__std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | type[local_date],
    ) -> builtins.type[__std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | type[local_date],
    ) -> builtins.type[__std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: __std__.duration | datetime.timedelta | gel.RelativeDuration | relative_duration | type[__std__.duration] | type[relative_duration],
    ) -> builtins.type[local_datetime]:
        match other:
            case gel.RelativeDuration():
                other = relative_duration(other)
            case datetime.timedelta():
                other = std.duration(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
        return AnnotatedExpr(local_datetime, op)  # type: ignore [return-value]

    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: date_duration | gel.DateDuration | type[date_duration],
    ) -> builtins.type[local_date]:
        match other:
            case gel.DateDuration():
                other = date_duration(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'local_date'),
        )
        return AnnotatedExpr(local_date, op)  # type: ignore [return-value]

    def __add__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__add__, *args, **kwargs)  # type: ignore [no-any-return]

    @overload
    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: __std__.duration | datetime.timedelta | gel.RelativeDuration | relative_duration | type[__std__.duration] | type[relative_duration],
    ) -> builtins.type[local_datetime]:
        match other:
            case gel.RelativeDuration():
                other = relative_duration(other)
            case datetime.timedelta():
                other = std.duration(other)
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
        return AnnotatedExpr(local_datetime, op)  # type: ignore [return-value]

    @overload
    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: date_duration | gel.DateDuration | type[date_duration],
    ) -> builtins.type[local_date]:
        match other:
            case gel.DateDuration():
                other = date_duration(other)
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'local_date'),
        )
        return AnnotatedExpr(local_date, op)  # type: ignore [return-value]

    @overload
    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | type[local_date],
    ) -> builtins.type[date_duration]:
        match other:
            case datetime.date():
                other = local_date(other)
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'date_duration'),
        )
        return AnnotatedExpr(date_duration, op)  # type: ignore [return-value]

    def __sub__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__sub__, *args, **kwargs)  # type: ignore [no-any-return]

if TYPE_CHECKING:
    class local_date(
        PyTypeScalar[date],
        std.anydiscrete,
        metaclass=__local_date_meta__,
    ):
        class __gel_reflection__(__std__.anydiscrete.__gel_reflection__):
            id = UUID(int=268)
            name = SchemaPath('std', 'cal', 'local_date')

if not TYPE_CHECKING:
    class local_date(date, PyTypeScalar[date], std.anydiscrete):
        __gel_type_class__: ClassVar[type] = __local_date_meta__

        class __gel_reflection__(std.anydiscrete.__gel_reflection__):
            id = UUID(int=268)
            name = SchemaPath('std', 'cal', 'local_date')



class __local_datetime_meta__(std.__anycontiguous_meta__):
    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | local_datetime | type[local_date] | type[local_datetime],
    ) -> builtins.type[__std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | local_datetime | type[local_date] | type[local_datetime],
    ) -> builtins.type[__std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | local_datetime | type[local_date] | type[local_datetime],
    ) -> builtins.type[__std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | local_datetime | type[local_date] | type[local_datetime],
    ) -> builtins.type[__std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | local_datetime | type[local_date] | type[local_datetime],
    ) -> builtins.type[__std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | local_datetime | type[local_date] | type[local_datetime],
    ) -> builtins.type[__std__.bool]:
        match other:
            case datetime.date():
                other = local_date(other)
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: __std__.duration | date_duration | datetime.timedelta | gel.DateDuration | gel.RelativeDuration | relative_duration | type[__std__.duration] | type[date_duration] | type[relative_duration],
    ) -> builtins.type[local_datetime]:
        match other:
            case gel.RelativeDuration():
                other = relative_duration(other)
            case gel.DateDuration():
                other = date_duration(other)
            case datetime.timedelta():
                other = std.duration(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
        return AnnotatedExpr(local_datetime, op)  # type: ignore [return-value]

    @overload
    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: __std__.duration | date_duration | datetime.timedelta | gel.DateDuration | gel.RelativeDuration | relative_duration | type[__std__.duration] | type[date_duration] | type[relative_duration],
    ) -> builtins.type[local_datetime]:
        match other:
            case gel.RelativeDuration():
                other = relative_duration(other)
            case gel.DateDuration():
                other = date_duration(other)
            case datetime.timedelta():
                other = std.duration(other)
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
        return AnnotatedExpr(local_datetime, op)  # type: ignore [return-value]

    @overload
    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | local_datetime | type[local_date] | type[local_datetime],
    ) -> builtins.type[relative_duration]:
        match other:
            case datetime.date():
                other = local_date(other)
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        )
        return AnnotatedExpr(relative_duration, op)  # type: ignore [return-value]

    def __sub__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__sub__, *args, **kwargs)  # type: ignore [no-any-return]

if TYPE_CHECKING:
    class local_datetime(
        PyTypeScalar[__datetime__.datetime],
        std.anycontiguous,
        metaclass=__local_datetime_meta__,
    ):
        class __gel_reflection__(__std__.anycontiguous.__gel_reflection__):
            id = UUID(int=267)
            name = SchemaPath('std', 'cal', 'local_datetime')

if not TYPE_CHECKING:
    class local_datetime(
        __datetime__.datetime,
        PyTypeScalar[__datetime__.datetime],
        std.anycontiguous,
    ):
        __gel_type_class__: ClassVar[type] = __local_datetime_meta__

        class __gel_reflection__(std.anycontiguous.__gel_reflection__):
            id = UUID(int=267)
            name = SchemaPath('std', 'cal', 'local_datetime')



class __local_time_meta__(std.__anyscalar_meta__):
    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.time | local_time | type[local_time],
    ) -> builtins.type[__std__.bool]:
        match other:
            case datetime.time():
                other = local_time(other)
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.time | local_time | type[local_time],
    ) -> builtins.type[__std__.bool]:
        match other:
            case datetime.time():
                other = local_time(other)
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.time | local_time | type[local_time],
    ) -> builtins.type[__std__.bool]:
        match other:
            case datetime.time():
                other = local_time(other)
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.time | local_time | type[local_time],
    ) -> builtins.type[__std__.bool]:
        match other:
            case datetime.time():
                other = local_time(other)
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.time | local_time | type[local_time],
    ) -> builtins.type[__std__.bool]:
        match other:
            case datetime.time():
                other = local_time(other)
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.time | local_time | type[local_time],
    ) -> builtins.type[__std__.bool]:
        match other:
            case datetime.time():
                other = local_time(other)
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: __std__.duration | date_duration | datetime.timedelta | gel.DateDuration | gel.RelativeDuration | relative_duration | type[__std__.duration] | type[date_duration] | type[relative_duration],
    ) -> builtins.type[local_time]:
        match other:
            case gel.RelativeDuration():
                other = relative_duration(other)
            case gel.DateDuration():
                other = date_duration(other)
            case datetime.timedelta():
                other = std.duration(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'local_time'),
        )
        return AnnotatedExpr(local_time, op)  # type: ignore [return-value]

    @overload
    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: __std__.duration | date_duration | datetime.timedelta | gel.DateDuration | gel.RelativeDuration | relative_duration | type[__std__.duration] | type[date_duration] | type[relative_duration],
    ) -> builtins.type[local_time]:
        match other:
            case gel.RelativeDuration():
                other = relative_duration(other)
            case gel.DateDuration():
                other = date_duration(other)
            case datetime.timedelta():
                other = std.duration(other)
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'local_time'),
        )
        return AnnotatedExpr(local_time, op)  # type: ignore [return-value]

    @overload
    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.time | local_time | type[local_time],
    ) -> builtins.type[relative_duration]:
        match other:
            case datetime.time():
                other = local_time(other)
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        )
        return AnnotatedExpr(relative_duration, op)  # type: ignore [return-value]

    def __sub__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__sub__, *args, **kwargs)  # type: ignore [no-any-return]

if TYPE_CHECKING:
    class local_time(
        PyTypeScalar[time],
        std.anyscalar,
        metaclass=__local_time_meta__,
    ):
        class __gel_reflection__(__std__.anyscalar.__gel_reflection__):
            id = UUID(int=269)
            name = SchemaPath('std', 'cal', 'local_time')

if not TYPE_CHECKING:
    class local_time(time, PyTypeScalar[time], std.anyscalar):
        __gel_type_class__: ClassVar[type] = __local_time_meta__

        class __gel_reflection__(std.anyscalar.__gel_reflection__):
            id = UUID(int=269)
            name = SchemaPath('std', 'cal', 'local_time')



class __relative_duration_meta__(std.__anyscalar_meta__):
    def __neg__(cls) -> builtins.type[relative_duration]:
        return AnnotatedExpr(  # type: ignore [return-value]
            relative_duration,
            PrefixOp(
            expr=cls,
            op="-",
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        ),
        )

    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: DateTimeLike | __std__.datetime | type[__std__.datetime],
    ) -> builtins.type[__std__.datetime]:
        match other:
            case DateTimeLike():
                other = std.datetime(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'datetime'),
        )
        return AnnotatedExpr(std.datetime, op)  # type: ignore [return-value]

    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.date | local_date | local_datetime | type[local_date] | type[local_datetime],
    ) -> builtins.type[local_datetime]:
        match other:
            case datetime.date():
                other = local_date(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'local_datetime'),
        )
        return AnnotatedExpr(local_datetime, op)  # type: ignore [return-value]

    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: datetime.time | local_time | type[local_time],
    ) -> builtins.type[local_time]:
        match other:
            case datetime.time():
                other = local_time(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'local_time'),
        )
        return AnnotatedExpr(local_time, op)  # type: ignore [return-value]

    @overload
    def __add__(  # type: ignore [override, unused-ignore]
        cls,
        other: __std__.duration | date_duration | datetime.timedelta | gel.DateDuration | gel.RelativeDuration | relative_duration | type[__std__.duration] | type[date_duration] | type[relative_duration],
    ) -> builtins.type[relative_duration]:
        match other:
            case gel.RelativeDuration():
                other = relative_duration(other)
            case gel.DateDuration():
                other = date_duration(other)
            case datetime.timedelta():
                other = std.duration(other)
        op = InfixOp(
            lexpr=cls,
            op="+",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        )
        return AnnotatedExpr(relative_duration, op)  # type: ignore [return-value]

    def __add__(cls, *args: Any, **kwargs: Any) -> type:
        return dispatch_overload(cls.__add__, *args, **kwargs)  # type: ignore [no-any-return]

    def __eq__(  # type: ignore [override, unused-ignore]
        cls,
        other: date_duration | gel.DateDuration | gel.RelativeDuration | relative_duration | type[date_duration] | type[relative_duration],
    ) -> builtins.type[__std__.bool]:
        match other:
            case gel.RelativeDuration():
                other = relative_duration(other)
            case gel.DateDuration():
                other = date_duration(other)
        op = InfixOp(
            lexpr=cls,
            op="=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __ne__(  # type: ignore [override, unused-ignore]
        cls,
        other: date_duration | gel.DateDuration | gel.RelativeDuration | relative_duration | type[date_duration] | type[relative_duration],
    ) -> builtins.type[__std__.bool]:
        match other:
            case gel.RelativeDuration():
                other = relative_duration(other)
            case gel.DateDuration():
                other = date_duration(other)
        op = InfixOp(
            lexpr=cls,
            op="!=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __gt__(  # type: ignore [override, unused-ignore]
        cls,
        other: date_duration | gel.DateDuration | gel.RelativeDuration | relative_duration | type[date_duration] | type[relative_duration],
    ) -> builtins.type[__std__.bool]:
        match other:
            case gel.RelativeDuration():
                other = relative_duration(other)
            case gel.DateDuration():
                other = date_duration(other)
        op = InfixOp(
            lexpr=cls,
            op=">",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __ge__(  # type: ignore [override, unused-ignore]
        cls,
        other: date_duration | gel.DateDuration | gel.RelativeDuration | relative_duration | type[date_duration] | type[relative_duration],
    ) -> builtins.type[__std__.bool]:
        match other:
            case gel.RelativeDuration():
                other = relative_duration(other)
            case gel.DateDuration():
                other = date_duration(other)
        op = InfixOp(
            lexpr=cls,
            op=">=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __lt__(  # type: ignore [override, unused-ignore]
        cls,
        other: date_duration | gel.DateDuration | gel.RelativeDuration | relative_duration | type[date_duration] | type[relative_duration],
    ) -> builtins.type[__std__.bool]:
        match other:
            case gel.RelativeDuration():
                other = relative_duration(other)
            case gel.DateDuration():
                other = date_duration(other)
        op = InfixOp(
            lexpr=cls,
            op="<",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __le__(  # type: ignore [override, unused-ignore]
        cls,
        other: date_duration | gel.DateDuration | gel.RelativeDuration | relative_duration | type[date_duration] | type[relative_duration],
    ) -> builtins.type[__std__.bool]:
        match other:
            case gel.RelativeDuration():
                other = relative_duration(other)
            case gel.DateDuration():
                other = date_duration(other)
        op = InfixOp(
            lexpr=cls,
            op="<=",
            rexpr=other,
            type_=SchemaPath('std', 'bool'),
        )
        return AnnotatedExpr(std.bool, op)  # type: ignore [return-value]

    def __sub__(  # type: ignore [override, unused-ignore]
        cls,
        other: __std__.duration | date_duration | datetime.timedelta | gel.DateDuration | gel.RelativeDuration | relative_duration | type[__std__.duration] | type[date_duration] | type[relative_duration],
    ) -> builtins.type[relative_duration]:
        match other:
            case gel.RelativeDuration():
                other = relative_duration(other)
            case gel.DateDuration():
                other = date_duration(other)
            case datetime.timedelta():
                other = std.duration(other)
        op = InfixOp(
            lexpr=cls,
            op="-",
            rexpr=other,
            type_=SchemaPath('std', 'cal', 'relative_duration'),
        )
        return AnnotatedExpr(relative_duration, op)  # type: ignore [return-value]

if TYPE_CHECKING:
    class relative_duration(
        PyTypeScalar[RelativeDuration],
        std.anyscalar,
        metaclass=__relative_duration_meta__,
    ):
        class __gel_reflection__(__std__.anyscalar.__gel_reflection__):
            id = UUID(int=273)
            name = SchemaPath('std', 'cal', 'relative_duration')

if not TYPE_CHECKING:
    class relative_duration(
        RelativeDuration,
        PyTypeScalar[RelativeDuration],
        std.anyscalar,
    ):
        __gel_type_class__: ClassVar[type] = __relative_duration_meta__

        class __gel_reflection__(std.anyscalar.__gel_reflection__):
            id = UUID(int=273)
            name = SchemaPath('std', 'cal', 'relative_duration')


