#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from .. import schema

from gel.models.pydantic import (
    AnyEnum,
    Array,
    ComputedProperty,
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
from builtins import list, tuple, type
from collections.abc import Callable, Iterable
from typing import TYPE_CHECKING, TypeVar
from typing_extensions import Self, TypeAliasType
from uuid import UUID

if TYPE_CHECKING:

    from .. import std as __std__
    from ... import schema as __schema__, sys
    from ...std import __types__ as __std___types____, __types__ as std___types__


class OutputFormat(AnyEnum):
    BINARY = 'BINARY'
    JSON = 'JSON'
    JSON_ELEMENTS = 'JSON_ELEMENTS'
    NONE = 'NONE'


class QueryType(AnyEnum):
    EdgeQL = 'EdgeQL'
    SQL = 'SQL'


class TransactionAccessMode(AnyEnum):
    ReadOnly = 'ReadOnly'
    ReadWrite = 'ReadWrite'


class TransactionDeferrability(AnyEnum):
    Deferrable = 'Deferrable'
    NotDeferrable = 'NotDeferrable'


class TransactionIsolation(AnyEnum):
    RepeatableRead = 'RepeatableRead'
    Serializable = 'Serializable'


class VersionStage(AnyEnum):
    dev = 'dev'
    alpha = 'alpha'
    beta = 'beta'
    rc = 'rc'
    final = 'final'




#
# type sys::SystemObject
#
class __SystemObject_typeof__(schema.__Object_typeof__):
    class __gel_reflection__(schema.__Object_typeof__.__gel_reflection__):
        id = UUID(int=90350303980132584494185812701624669976)
        name = SchemaPath('sys', 'SystemObject')
        @LazyClassProperty["__schema__.ObjectType"]
        @classmethod
        def object(cls) -> __schema__.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=90350303980132584494185812701624669976),
                name='sys::SystemObject',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__(schema.__Object_typeof__.__typeof__):
        pass


class SystemObject(
    __SystemObject_typeof__,
    schema.Object,
    __gel_type_id__=UUID(int=90350303980132584494185812701624669976),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
        ) -> None:
            """Create a new sys::SystemObject instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update sys::SystemObject instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[__std__.str]] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch sys::SystemObject instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch sys::SystemObject instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            internal: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            builtin: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(schema.Object.__variants__):
        class Base(__SystemObject_typeof__, schema.Object.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                ) -> None:
                    """Create a new sys::SystemObject instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update sys::SystemObject instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch sys::SystemObject instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch sys::SystemObject instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    internal: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    builtin: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="SystemObject | Base")
    class __links__(schema.Object.__links__):
        pass

if not TYPE_CHECKING:
    SystemObject.__variants__.Base = SystemObject



#
# type sys::ExtensionPackage
#
class __ExtensionPackage_typeof__(
    __SystemObject_typeof__,
    schema.__AnnotationSubject_typeof__,
):
    class __gel_reflection__(
        __SystemObject_typeof__.__gel_reflection__,
        schema.__AnnotationSubject_typeof__.__gel_reflection__,
    ):
        id = UUID(int=180071320089194630696024936739719303821)
        name = SchemaPath('sys', 'ExtensionPackage')
        @LazyClassProperty["__schema__.ObjectType"]
        @classmethod
        def object(cls) -> __schema__.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=180071320089194630696024936739719303821),
                name='sys::ExtensionPackage',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __SystemObject_typeof__.__typeof__,
        schema.__AnnotationSubject_typeof__.__typeof__,
    ):
        script = TypeAliasType('script', 'std.str')
        version = TypeAliasType('version', 'MajorMinorStageStage_noLocal_Tuple_SKRhXQ')


class ExtensionPackage(
    __ExtensionPackage_typeof__,
    SystemObject,
    schema.AnnotationSubject,
    __gel_type_id__=UUID(int=180071320089194630696024936739719303821),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[schema.Annotation] = [],
            script: str,
            version: tuple[int, int, __builtins__.str, int, list[str]],
        ) -> None:
            """Create a new sys::ExtensionPackage instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[__schema__.Annotation] | UnspecifiedType = Unspecified,
            script: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update sys::ExtensionPackage instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__schema__.Annotation] | UnspecifiedType = Unspecified,
            script: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            version: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch sys::ExtensionPackage instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[__schema__.Annotation] | UnspecifiedType = Unspecified,
            script: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch sys::ExtensionPackage instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            internal: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            builtin: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            script: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        SystemObject.__variants__,
        schema.AnnotationSubject.__variants__,
    ):
        class Base(
            __ExtensionPackage_typeof__,
            SystemObject.__variants__.Base,
            schema.AnnotationSubject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[schema.Annotation] = [],
                    script: str,
                    version: tuple[int, int, __builtins__.str, int, list[str]],
                ) -> None:
                    """Create a new sys::ExtensionPackage instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[__schema__.Annotation] | UnspecifiedType = Unspecified,
                    script: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update sys::ExtensionPackage instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__schema__.Annotation] | UnspecifiedType = Unspecified,
                    script: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    version: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch sys::ExtensionPackage instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[__schema__.Annotation] | UnspecifiedType = Unspecified,
                    script: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch sys::ExtensionPackage instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    internal: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    builtin: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    script: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="ExtensionPackage | Base")
    class __links__(
        SystemObject.__links__,
        schema.AnnotationSubject.__links__,
    ):
        pass

if not TYPE_CHECKING:
    ExtensionPackage.__variants__.Base = ExtensionPackage



#
# type sys::ExtensionPackageMigration
#
class __ExtensionPackageMigration_typeof__(
    __SystemObject_typeof__,
    schema.__AnnotationSubject_typeof__,
):
    class __gel_reflection__(
        __SystemObject_typeof__.__gel_reflection__,
        schema.__AnnotationSubject_typeof__.__gel_reflection__,
    ):
        id = UUID(int=302620932575936177542260435729933168552)
        name = SchemaPath('sys', 'ExtensionPackageMigration')
        @LazyClassProperty["__schema__.ObjectType"]
        @classmethod
        def object(cls) -> __schema__.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=302620932575936177542260435729933168552),
                name='sys::ExtensionPackageMigration',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __SystemObject_typeof__.__typeof__,
        schema.__AnnotationSubject_typeof__.__typeof__,
    ):
        script = TypeAliasType('script', 'std.str')
        from_version = TypeAliasType('from_version', 'MajorMinorStageStage_noLocal_Tuple_SKRhXQ')
        to_version = TypeAliasType('to_version', 'MajorMinorStageStage_noLocal_Tuple_SKRhXQ')


class ExtensionPackageMigration(
    __ExtensionPackageMigration_typeof__,
    SystemObject,
    schema.AnnotationSubject,
    __gel_type_id__=UUID(int=302620932575936177542260435729933168552),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[schema.Annotation] = [],
            script: str,
            from_version: tuple[int, int, __builtins__.str, int, list[str]],
            to_version: tuple[int, int, __builtins__.str, int, list[str]],
        ) -> None:
            """Create a new sys::ExtensionPackageMigration instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[__schema__.Annotation] | UnspecifiedType = Unspecified,
            script: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
            to_version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update sys::ExtensionPackageMigration instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__schema__.Annotation] | UnspecifiedType = Unspecified,
            script: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            from_version: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
            to_version: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch sys::ExtensionPackageMigration instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[__schema__.Annotation] | UnspecifiedType = Unspecified,
            script: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
            to_version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch sys::ExtensionPackageMigration instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            internal: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            builtin: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            script: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        SystemObject.__variants__,
        schema.AnnotationSubject.__variants__,
    ):
        class Base(
            __ExtensionPackageMigration_typeof__,
            SystemObject.__variants__.Base,
            schema.AnnotationSubject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[schema.Annotation] = [],
                    script: str,
                    from_version: tuple[int, int, __builtins__.str, int, list[str]],
                    to_version: tuple[int, int, __builtins__.str, int, list[str]],
                ) -> None:
                    """Create a new sys::ExtensionPackageMigration instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[__schema__.Annotation] | UnspecifiedType = Unspecified,
                    script: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
                    to_version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update sys::ExtensionPackageMigration instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__schema__.Annotation] | UnspecifiedType = Unspecified,
                    script: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_version: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
                    to_version: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch sys::ExtensionPackageMigration instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[__schema__.Annotation] | UnspecifiedType = Unspecified,
                    script: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
                    to_version: type[std___types__.MajorMinorStageStage_noLocal_Tuple_SKRhXQ] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch sys::ExtensionPackageMigration instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    internal: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    builtin: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    script: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="ExtensionPackageMigration | Base")
    class __links__(
        SystemObject.__links__,
        schema.AnnotationSubject.__links__,
    ):
        pass

if not TYPE_CHECKING:
    ExtensionPackageMigration.__variants__.Base = ExtensionPackageMigration



#
# type sys::ExternalObject
#
class __ExternalObject_typeof__(__SystemObject_typeof__):
    class __gel_reflection__(__SystemObject_typeof__.__gel_reflection__):
        id = UUID(int=302417707415983282126938051159487614287)
        name = SchemaPath('sys', 'ExternalObject')
        @LazyClassProperty["__schema__.ObjectType"]
        @classmethod
        def object(cls) -> __schema__.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=302417707415983282126938051159487614287),
                name='sys::ExternalObject',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__(__SystemObject_typeof__.__typeof__):
        pass


class ExternalObject(
    __ExternalObject_typeof__,
    SystemObject,
    __gel_type_id__=UUID(int=302417707415983282126938051159487614287),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
        ) -> None:
            """Create a new sys::ExternalObject instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update sys::ExternalObject instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[__std__.str]] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch sys::ExternalObject instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch sys::ExternalObject instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            internal: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            builtin: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(SystemObject.__variants__):
        class Base(__ExternalObject_typeof__, SystemObject.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                ) -> None:
                    """Create a new sys::ExternalObject instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update sys::ExternalObject instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch sys::ExternalObject instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch sys::ExternalObject instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    internal: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    builtin: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="ExternalObject | Base")
    class __links__(SystemObject.__links__):
        pass

if not TYPE_CHECKING:
    ExternalObject.__variants__.Base = ExternalObject



#
# type sys::Role
#
class __Role_typeof__(
    __SystemObject_typeof__,
    schema.__InheritingObject_typeof__,
    schema.__AnnotationSubject_typeof__,
):
    class __gel_reflection__(
        __SystemObject_typeof__.__gel_reflection__,
        schema.__InheritingObject_typeof__.__gel_reflection__,
        schema.__AnnotationSubject_typeof__.__gel_reflection__,
    ):
        id = UUID(int=6415088929791825864887870917823511316)
        name = SchemaPath('sys', 'Role')
        @LazyClassProperty["__schema__.ObjectType"]
        @classmethod
        def object(cls) -> __schema__.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=6415088929791825864887870917823511316),
                name='sys::Role',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __SystemObject_typeof__.__typeof__,
        schema.__InheritingObject_typeof__.__typeof__,
        schema.__AnnotationSubject_typeof__.__typeof__,
    ):
        name = TypeAliasType('name', 'std.str')
        superuser = TypeAliasType('superuser', 'std.bool')
        is_superuser = TypeAliasType('is_superuser', 'ComputedProperty[std.bool, bool]')
        password = TypeAliasType('password', 'OptionalProperty[std.str, str]')
        member_of = TypeAliasType('member_of', 'MultiLink[Role]')


class Role(
    __Role_typeof__,
    SystemObject,
    schema.InheritingObject,
    schema.AnnotationSubject,
    __gel_type_id__=UUID(int=6415088929791825864887870917823511316),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[schema.Annotation] = [],
            abstract: bool | None = None,
            inherited_fields: list[str] | None = None,
            bases: Iterable[schema.InheritingObject] = [],
            ancestors: Iterable[schema.InheritingObject] = [],
            superuser: bool,
            password: str | None = None,
            member_of: Iterable[Role] = [],
        ) -> None:
            """Create a new sys::Role instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[__schema__.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[__schema__.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[__schema__.InheritingObject] | UnspecifiedType = Unspecified,
            superuser: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            password: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            member_of: type[sys.Role] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update sys::Role instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__schema__.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__schema__.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__schema__.InheritingObject] | UnspecifiedType = Unspecified,
            superuser: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            is_superuser: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            password: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            member_of: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[sys.Role] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch sys::Role instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[__schema__.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[__schema__.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[__schema__.InheritingObject] | UnspecifiedType = Unspecified,
            superuser: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            is_superuser: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            password: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            member_of: type[sys.Role] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch sys::Role instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            internal: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            builtin: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            abstract: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            final: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            superuser: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            is_superuser: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            password: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        SystemObject.__variants__,
        schema.InheritingObject.__variants__,
        schema.AnnotationSubject.__variants__,
    ):
        class Base(
            __Role_typeof__,
            SystemObject.__variants__.Base,
            schema.InheritingObject.__variants__.Base,
            schema.AnnotationSubject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[schema.Annotation] = [],
                    abstract: bool | None = None,
                    inherited_fields: list[str] | None = None,
                    bases: Iterable[schema.InheritingObject] = [],
                    ancestors: Iterable[schema.InheritingObject] = [],
                    superuser: bool,
                    password: str | None = None,
                    member_of: Iterable[Role] = [],
                ) -> None:
                    """Create a new sys::Role instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[__schema__.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[__schema__.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[__schema__.InheritingObject] | UnspecifiedType = Unspecified,
                    superuser: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    password: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    member_of: type[sys.Role] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update sys::Role instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__schema__.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__schema__.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__schema__.InheritingObject] | UnspecifiedType = Unspecified,
                    superuser: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    is_superuser: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    password: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    member_of: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[sys.Role] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch sys::Role instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[__schema__.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[__schema__.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[__schema__.InheritingObject] | UnspecifiedType = Unspecified,
                    superuser: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    is_superuser: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    password: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    member_of: type[sys.Role] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch sys::Role instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    internal: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    builtin: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    abstract: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    final: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    superuser: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    is_superuser: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    password: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Role | Base")
    class __links__(
        SystemObject.__links__,
        schema.InheritingObject.__links__,
        schema.AnnotationSubject.__links__,
    ):
        pass

if not TYPE_CHECKING:
    Role.__variants__.Base = Role



#
# type sys::Branch
#
class __Branch_typeof__(
    __ExternalObject_typeof__,
    schema.__AnnotationSubject_typeof__,
):
    class __gel_reflection__(
        __ExternalObject_typeof__.__gel_reflection__,
        schema.__AnnotationSubject_typeof__.__gel_reflection__,
    ):
        id = UUID(int=49778529390898516016872303811592688699)
        name = SchemaPath('sys', 'Branch')
        @LazyClassProperty["__schema__.ObjectType"]
        @classmethod
        def object(cls) -> __schema__.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=49778529390898516016872303811592688699),
                name='sys::Branch',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __ExternalObject_typeof__.__typeof__,
        schema.__AnnotationSubject_typeof__.__typeof__,
    ):
        name = TypeAliasType('name', 'std.str')
        last_migration = TypeAliasType('last_migration', 'OptionalProperty[std.str, str]')


class Branch(
    __Branch_typeof__,
    ExternalObject,
    schema.AnnotationSubject,
    __gel_type_id__=UUID(int=49778529390898516016872303811592688699),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[schema.Annotation] = [],
            last_migration: str | None = None,
        ) -> None:
            """Create a new sys::Branch instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[__schema__.Annotation] | UnspecifiedType = Unspecified,
            last_migration: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update sys::Branch instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__schema__.Annotation] | UnspecifiedType = Unspecified,
            last_migration: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch sys::Branch instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[__schema__.Annotation] | UnspecifiedType = Unspecified,
            last_migration: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch sys::Branch instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            internal: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            builtin: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            last_migration: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        ExternalObject.__variants__,
        schema.AnnotationSubject.__variants__,
    ):
        class Base(
            __Branch_typeof__,
            ExternalObject.__variants__.Base,
            schema.AnnotationSubject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[schema.Annotation] = [],
                    last_migration: str | None = None,
                ) -> None:
                    """Create a new sys::Branch instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[__schema__.Annotation] | UnspecifiedType = Unspecified,
                    last_migration: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update sys::Branch instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__schema__.Annotation] | UnspecifiedType = Unspecified,
                    last_migration: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch sys::Branch instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[__schema__.Annotation] | UnspecifiedType = Unspecified,
                    last_migration: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch sys::Branch instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    internal: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    builtin: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    last_migration: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Branch | Base")
    class __links__(
        ExternalObject.__links__,
        schema.AnnotationSubject.__links__,
    ):
        pass

if not TYPE_CHECKING:
    Branch.__variants__.Base = Branch



#
# type sys::QueryStats
#
class __QueryStats_typeof__(__ExternalObject_typeof__):
    class __gel_reflection__(__ExternalObject_typeof__.__gel_reflection__):
        id = UUID(int=274580524048681063750167790732145947985)
        name = SchemaPath('sys', 'QueryStats')
        @LazyClassProperty["__schema__.ObjectType"]
        @classmethod
        def object(cls) -> __schema__.ObjectType:
            from ...schema import ObjectType
            return ObjectType(
                id=UUID(int=274580524048681063750167790732145947985),
                name='sys::QueryStats',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__ExternalObject_typeof__.__typeof__):
        query = TypeAliasType('query', 'OptionalProperty[std.str, str]')
        query_type = TypeAliasType('query_type', 'OptionalProperty[QueryType, __builtins__.str]')
        tag = TypeAliasType('tag', 'OptionalProperty[std.str, str]')
        compilation_config = TypeAliasType('compilation_config', 'OptionalProperty[std.json, str]')
        protocol_version = TypeAliasType('protocol_version', 'OptionalProperty[MajorMinor_Tuple_K20e_g, tuple[int, int]]')
        default_namespace = TypeAliasType('default_namespace', 'OptionalProperty[std.str, str]')
        namespace_aliases = TypeAliasType('namespace_aliases', 'OptionalProperty[std.json, str]')
        output_format = TypeAliasType('output_format', 'OptionalProperty[OutputFormat, __builtins__.str]')
        expect_one = TypeAliasType('expect_one', 'OptionalProperty[std.bool, bool]')
        implicit_limit = TypeAliasType('implicit_limit', 'OptionalProperty[std.int64, int]')
        inline_typeids = TypeAliasType('inline_typeids', 'OptionalProperty[std.bool, bool]')
        inline_typenames = TypeAliasType('inline_typenames', 'OptionalProperty[std.bool, bool]')
        inline_objectids = TypeAliasType('inline_objectids', 'OptionalProperty[std.bool, bool]')
        plans = TypeAliasType('plans', 'OptionalProperty[std.int64, int]')
        total_plan_time = TypeAliasType('total_plan_time', 'OptionalProperty[std.duration, timedelta]')
        min_plan_time = TypeAliasType('min_plan_time', 'OptionalProperty[std.duration, timedelta]')
        max_plan_time = TypeAliasType('max_plan_time', 'OptionalProperty[std.duration, timedelta]')
        mean_plan_time = TypeAliasType('mean_plan_time', 'OptionalProperty[std.duration, timedelta]')
        stddev_plan_time = TypeAliasType('stddev_plan_time', 'OptionalProperty[std.duration, timedelta]')
        calls = TypeAliasType('calls', 'OptionalProperty[std.int64, int]')
        total_exec_time = TypeAliasType('total_exec_time', 'OptionalProperty[std.duration, timedelta]')
        min_exec_time = TypeAliasType('min_exec_time', 'OptionalProperty[std.duration, timedelta]')
        max_exec_time = TypeAliasType('max_exec_time', 'OptionalProperty[std.duration, timedelta]')
        mean_exec_time = TypeAliasType('mean_exec_time', 'OptionalProperty[std.duration, timedelta]')
        stddev_exec_time = TypeAliasType('stddev_exec_time', 'OptionalProperty[std.duration, timedelta]')
        rows = TypeAliasType('rows', 'OptionalProperty[std.int64, int]')
        stats_since = TypeAliasType('stats_since', 'OptionalProperty[std.datetime, datetime]')
        minmax_stats_since = TypeAliasType('minmax_stats_since', 'OptionalProperty[std.datetime, datetime]')
        branch = TypeAliasType('branch', 'OptionalLink[Branch]')


class QueryStats(
    __QueryStats_typeof__,
    ExternalObject,
    __gel_type_id__=UUID(int=274580524048681063750167790732145947985),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            query: str | None = None,
            query_type: __builtins__.str | None = None,
            tag: str | None = None,
            compilation_config: str | None = None,
            protocol_version: tuple[int, int] | None = None,
            default_namespace: str | None = None,
            namespace_aliases: str | None = None,
            output_format: __builtins__.str | None = None,
            expect_one: bool | None = None,
            implicit_limit: int | None = None,
            inline_typeids: bool | None = None,
            inline_typenames: bool | None = None,
            inline_objectids: bool | None = None,
            plans: int | None = None,
            total_plan_time: timedelta | None = None,
            min_plan_time: timedelta | None = None,
            max_plan_time: timedelta | None = None,
            mean_plan_time: timedelta | None = None,
            stddev_plan_time: timedelta | None = None,
            calls: int | None = None,
            total_exec_time: timedelta | None = None,
            min_exec_time: timedelta | None = None,
            max_exec_time: timedelta | None = None,
            mean_exec_time: timedelta | None = None,
            stddev_exec_time: timedelta | None = None,
            rows: int | None = None,
            stats_since: datetime | None = None,
            minmax_stats_since: datetime | None = None,
            branch: Branch | None = None,
        ) -> None:
            """Create a new sys::QueryStats instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
            query: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            query_type: type[QueryType] | UnspecifiedType = Unspecified,
            tag: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            compilation_config: __builtins__.str | type[__std__.json] | UnspecifiedType = Unspecified,
            protocol_version: type[__std___types____.MajorMinor_Tuple_K20e_g] | UnspecifiedType = Unspecified,
            default_namespace: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            namespace_aliases: __builtins__.str | type[__std__.json] | UnspecifiedType = Unspecified,
            output_format: type[OutputFormat] | UnspecifiedType = Unspecified,
            expect_one: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            implicit_limit: __builtins_2__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            inline_typeids: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inline_typenames: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inline_objectids: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            plans: __builtins_2__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            total_plan_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            min_plan_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            max_plan_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            mean_plan_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            stddev_plan_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            calls: __builtins_2__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            total_exec_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            min_exec_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            max_exec_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            mean_exec_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            stddev_exec_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            rows: __builtins_2__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            stats_since: __datetime_1__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            minmax_stats_since: __datetime_1__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            branch: type[sys.Branch] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update sys::QueryStats instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[__std__.str]] | UnspecifiedType = Unspecified,
            query: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            query_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryType] | UnspecifiedType = Unspecified,
            tag: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            compilation_config: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.json] | UnspecifiedType = Unspecified,
            protocol_version: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std___types____.MajorMinor_Tuple_K20e_g] | UnspecifiedType = Unspecified,
            default_namespace: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            namespace_aliases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.json] | UnspecifiedType = Unspecified,
            output_format: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[OutputFormat] | UnspecifiedType = Unspecified,
            expect_one: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            implicit_limit: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
            inline_typeids: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            inline_typenames: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            inline_objectids: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            plans: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
            total_plan_time: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            min_plan_time: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            max_plan_time: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            mean_plan_time: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            stddev_plan_time: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            calls: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
            total_exec_time: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            min_exec_time: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            max_exec_time: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            mean_exec_time: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            stddev_exec_time: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
            rows: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
            stats_since: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            minmax_stats_since: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
            branch: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[sys.Branch] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch sys::QueryStats instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
            query: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            query_type: type[QueryType] | UnspecifiedType = Unspecified,
            tag: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            compilation_config: __builtins__.str | type[__std__.json] | UnspecifiedType = Unspecified,
            protocol_version: type[__std___types____.MajorMinor_Tuple_K20e_g] | UnspecifiedType = Unspecified,
            default_namespace: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            namespace_aliases: __builtins__.str | type[__std__.json] | UnspecifiedType = Unspecified,
            output_format: type[OutputFormat] | UnspecifiedType = Unspecified,
            expect_one: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            implicit_limit: __builtins_2__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            inline_typeids: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inline_typenames: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inline_objectids: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            plans: __builtins_2__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            total_plan_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            min_plan_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            max_plan_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            mean_plan_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            stddev_plan_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            calls: __builtins_2__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            total_exec_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            min_exec_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            max_exec_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            mean_exec_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            stddev_exec_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
            rows: __builtins_2__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            stats_since: __datetime_1__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            minmax_stats_since: __datetime_1__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
            branch: type[sys.Branch] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch sys::QueryStats instances from the database.
            """
            ...

        @classmethod
        def order_by(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
            id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            internal: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            builtin: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            query: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            tag: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            compilation_config: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            default_namespace: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            namespace_aliases: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            expect_one: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            implicit_limit: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            inline_typeids: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            inline_typenames: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            inline_objectids: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            plans: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            total_plan_time: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            min_plan_time: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            max_plan_time: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            mean_plan_time: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            stddev_plan_time: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            calls: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            total_exec_time: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            min_exec_time: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            max_exec_time: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            mean_exec_time: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            stddev_exec_time: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            rows: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            stats_since: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            minmax_stats_since: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(ExternalObject.__variants__):
        class Base(__QueryStats_typeof__, ExternalObject.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    query: str | None = None,
                    query_type: __builtins__.str | None = None,
                    tag: str | None = None,
                    compilation_config: str | None = None,
                    protocol_version: tuple[int, int] | None = None,
                    default_namespace: str | None = None,
                    namespace_aliases: str | None = None,
                    output_format: __builtins__.str | None = None,
                    expect_one: bool | None = None,
                    implicit_limit: int | None = None,
                    inline_typeids: bool | None = None,
                    inline_typenames: bool | None = None,
                    inline_objectids: bool | None = None,
                    plans: int | None = None,
                    total_plan_time: timedelta | None = None,
                    min_plan_time: timedelta | None = None,
                    max_plan_time: timedelta | None = None,
                    mean_plan_time: timedelta | None = None,
                    stddev_plan_time: timedelta | None = None,
                    calls: int | None = None,
                    total_exec_time: timedelta | None = None,
                    min_exec_time: timedelta | None = None,
                    max_exec_time: timedelta | None = None,
                    mean_exec_time: timedelta | None = None,
                    stddev_exec_time: timedelta | None = None,
                    rows: int | None = None,
                    stats_since: datetime | None = None,
                    minmax_stats_since: datetime | None = None,
                    branch: Branch | None = None,
                ) -> None:
                    """Create a new sys::QueryStats instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                    query: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    query_type: type[QueryType] | UnspecifiedType = Unspecified,
                    tag: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    compilation_config: __builtins__.str | type[__std__.json] | UnspecifiedType = Unspecified,
                    protocol_version: type[__std___types____.MajorMinor_Tuple_K20e_g] | UnspecifiedType = Unspecified,
                    default_namespace: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    namespace_aliases: __builtins__.str | type[__std__.json] | UnspecifiedType = Unspecified,
                    output_format: type[OutputFormat] | UnspecifiedType = Unspecified,
                    expect_one: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    implicit_limit: __builtins_2__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    inline_typeids: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inline_typenames: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inline_objectids: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    plans: __builtins_2__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    total_plan_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    min_plan_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    max_plan_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    mean_plan_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    stddev_plan_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    calls: __builtins_2__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    total_exec_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    min_exec_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    max_exec_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    mean_exec_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    stddev_exec_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    rows: __builtins_2__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    stats_since: __datetime_1__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    minmax_stats_since: __datetime_1__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    branch: type[sys.Branch] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update sys::QueryStats instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                    query: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    query_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[QueryType] | UnspecifiedType = Unspecified,
                    tag: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    compilation_config: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.json] | UnspecifiedType = Unspecified,
                    protocol_version: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std___types____.MajorMinor_Tuple_K20e_g] | UnspecifiedType = Unspecified,
                    default_namespace: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    namespace_aliases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.json] | UnspecifiedType = Unspecified,
                    output_format: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[OutputFormat] | UnspecifiedType = Unspecified,
                    expect_one: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    implicit_limit: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
                    inline_typeids: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inline_typenames: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inline_objectids: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    plans: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
                    total_plan_time: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    min_plan_time: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    max_plan_time: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    mean_plan_time: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    stddev_plan_time: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    calls: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
                    total_exec_time: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    min_exec_time: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    max_exec_time: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    mean_exec_time: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    stddev_exec_time: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.duration] | UnspecifiedType = Unspecified,
                    rows: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
                    stats_since: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    minmax_stats_since: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    branch: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[sys.Branch] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch sys::QueryStats instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    internal: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    builtin: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    computed_fields: type[Array[__std__.str]] | UnspecifiedType = Unspecified,
                    query: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    query_type: type[QueryType] | UnspecifiedType = Unspecified,
                    tag: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    compilation_config: __builtins__.str | type[__std__.json] | UnspecifiedType = Unspecified,
                    protocol_version: type[__std___types____.MajorMinor_Tuple_K20e_g] | UnspecifiedType = Unspecified,
                    default_namespace: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    namespace_aliases: __builtins__.str | type[__std__.json] | UnspecifiedType = Unspecified,
                    output_format: type[OutputFormat] | UnspecifiedType = Unspecified,
                    expect_one: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    implicit_limit: __builtins_2__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    inline_typeids: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inline_typenames: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inline_objectids: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    plans: __builtins_2__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    total_plan_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    min_plan_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    max_plan_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    mean_plan_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    stddev_plan_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    calls: __builtins_2__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    total_exec_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    min_exec_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    max_exec_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    mean_exec_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    stddev_exec_time: __datetime__.timedelta | type[__std__.duration] | UnspecifiedType = Unspecified,
                    rows: __builtins_2__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    stats_since: __datetime_1__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    minmax_stats_since: __datetime_1__.datetime | type[__std__.datetime] | UnspecifiedType = Unspecified,
                    branch: type[sys.Branch] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch sys::QueryStats instances from the database.
                    """
                    ...

                @classmethod
                def order_by(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], ExprCompatible] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str] | tuple[Callable[[type[Self]], ExprCompatible], Direction | builtins.str, EmptyDirection | builtins.str],
                    id: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    name: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    internal: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    builtin: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    query: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    tag: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    compilation_config: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    default_namespace: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    namespace_aliases: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    expect_one: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    implicit_limit: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    inline_typeids: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    inline_typenames: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    inline_objectids: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    plans: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    total_plan_time: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    min_plan_time: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    max_plan_time: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    mean_plan_time: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    stddev_plan_time: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    calls: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    total_exec_time: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    min_exec_time: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    max_exec_time: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    mean_exec_time: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    stddev_exec_time: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    rows: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    stats_since: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    minmax_stats_since: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="QueryStats | Base")
    class __links__(ExternalObject.__links__):
        pass

if not TYPE_CHECKING:
    QueryStats.__variants__.Base = QueryStats



from .. import std  # noqa: E402 F403
from ...std.__types__ import (  # noqa: E402 F403
    MajorMinorStageStage_noLocal_Tuple_SKRhXQ,
    MajorMinor_Tuple_K20e_g
)

from builtins import bool, int, str  # noqa: E402 F403
from datetime import datetime, timedelta  # noqa: E402 F403
