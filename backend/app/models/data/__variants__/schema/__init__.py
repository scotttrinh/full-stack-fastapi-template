#
# Automatically generated from Gel schema.
#
# Do not edit directly as re-generating this file will overwrite any changes.
#

from __future__ import annotations

from .. import std

from gel.models import pydantic
from gel.models.pydantic import (
    AnyEnum,
    ComputedMultiLink,
    ComputedProperty,
    Direction,
    EmptyDirection,
    ExprCompatible,
    GelLinkModel,
    LazyClassProperty,
    MultiLink,
    MultiLinkWithProps,
    OptionalComputedProperty,
    OptionalLink,
    OptionalProperty,
    PathAlias,
    ProxyModel,
    PyConstType,
    SchemaPath,
    Unspecified,
    UnspecifiedType
)

import builtins as __builtins_2__
import builtins as __builtins_1__
import builtins as builtins
import builtins as __builtins__
from builtins import list, object, tuple, type
from collections.abc import Callable, Iterable
from typing import Any, TYPE_CHECKING, TypeVar
from typing_extensions import Self, TypeAliasType
from uuid import UUID

if TYPE_CHECKING:

    from .. import std as __std__
    from ... import schema, sys as __sys__
    from ...std import __types__ as std___types__


class AccessKind(AnyEnum):
    Select = 'Select'
    UpdateRead = 'UpdateRead'
    UpdateWrite = 'UpdateWrite'
    Delete = 'Delete'
    Insert = 'Insert'


class AccessPolicyAction(AnyEnum):
    Allow = 'Allow'
    Deny = 'Deny'


class Cardinality(AnyEnum):
    One = 'One'
    Many = 'Many'


class IndexDeferrability(AnyEnum):
    Prohibited = 'Prohibited'
    Permitted = 'Permitted'
    Required = 'Required'


class MigrationGeneratedBy(AnyEnum):
    DevMode = 'DevMode'
    DDLStatement = 'DDLStatement'


class OperatorKind(AnyEnum):
    Infix = 'Infix'
    Postfix = 'Postfix'
    Prefix = 'Prefix'
    Ternary = 'Ternary'


class ParameterKind(AnyEnum):
    VariadicParam = 'VariadicParam'
    NamedOnlyParam = 'NamedOnlyParam'
    PositionalParam = 'PositionalParam'


class RewriteKind(AnyEnum):
    Update = 'Update'
    Insert = 'Insert'


class SourceDeleteAction(AnyEnum):
    DeleteTarget = 'DeleteTarget'
    Allow = 'Allow'
    DeleteTargetIfOrphan = 'DeleteTargetIfOrphan'


class TargetDeleteAction(AnyEnum):
    Restrict = 'Restrict'
    DeleteSource = 'DeleteSource'
    Allow = 'Allow'
    DeferredRestrict = 'DeferredRestrict'


class TriggerKind(AnyEnum):
    Update = 'Update'
    Delete = 'Delete'
    Insert = 'Insert'


class TriggerScope(AnyEnum):
    All = 'All'
    Each = 'Each'


class TriggerTiming(AnyEnum):
    After = 'After'
    AfterCommitOf = 'AfterCommitOf'


class TypeModifier(AnyEnum):
    SetOfType = 'SetOfType'
    OptionalType = 'OptionalType'
    SingletonType = 'SingletonType'


class Volatility(AnyEnum):
    Immutable = 'Immutable'
    Stable = 'Stable'
    Volatile = 'Volatile'
    Modifying = 'Modifying'




#
# type schema::Object
#
class __Object_typeof__(std.__BaseObject_typeof__):
    class __gel_reflection__(std.__BaseObject_typeof__.__gel_reflection__):
        id = UUID(int=67762926258550356151524041794332124377)
        name = SchemaPath('schema', 'Object')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema__
            return __schema__.ObjectType(
                id=UUID(int=67762926258550356151524041794332124377),
                name='schema::Object',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__(std.__BaseObject_typeof__.__typeof__):
        name = TypeAliasType('name', 'std.str')
        internal = TypeAliasType('internal', 'std.bool')
        builtin = TypeAliasType('builtin', 'std.bool')
        computed_fields = TypeAliasType('computed_fields', 'OptionalProperty[pydantic.Array[std.str], list[str]]')


class Object(
    __Object_typeof__,
    std.BaseObject,
    __gel_type_id__=UUID(int=67762926258550356151524041794332124377),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
        ) -> None:
            """Create a new schema::Object instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Object instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Object instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Object instances from the database.
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


    class __variants__(std.BaseObject.__variants__):
        class Base(__Object_typeof__, std.BaseObject.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                ) -> None:
                    """Create a new schema::Object instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Object instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Object instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Object instances from the database.
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


        Any = TypeVar("Any", bound="Object | Base")
    class __links__(std.BaseObject.__links__):
        pass

if not TYPE_CHECKING:
    Object.__variants__.Base = Object



#
# type schema::TupleElement
#
class __TupleElement_typeof__(std.__BaseObject_typeof__):
    class __gel_reflection__(std.__BaseObject_typeof__.__gel_reflection__):
        id = UUID(int=208358010397048077362121740569112613627)
        name = SchemaPath('schema', 'TupleElement')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema__
            return __schema__.ObjectType(
                id=UUID(int=208358010397048077362121740569112613627),
                name='schema::TupleElement',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(std.__BaseObject_typeof__.__typeof__):
        name = TypeAliasType('name', 'OptionalProperty[std.str, str]')
        type = TypeAliasType('type', 'OptionalLink[Type]')


class TupleElement(
    __TupleElement_typeof__,
    std.BaseObject,
    __gel_type_id__=UUID(int=208358010397048077362121740569112613627),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str | None = None,
            type: Type | None = None,
        ) -> None:
            """Create a new schema::TupleElement instance from keyword arguments.

            Call db.save() on the returned object to persist it in the database.
            """
            ...

        @classmethod
        def update(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::TupleElement instances in the database.
            """
            ...

        @classmethod
        def select(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: PathAlias,
            id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::TupleElement instances from the database.
            """
            ...

        @classmethod
        def filter(  # type: ignore [override, unused-ignore]
            cls,
            /,
            *exprs: Callable[[type[Self]], type[__std__.bool]],
            id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
            name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::TupleElement instances from the database.
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


    class __variants__(std.BaseObject.__variants__):
        class Base(__TupleElement_typeof__, std.BaseObject.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str | None = None,
                    type: Type | None = None,
                ) -> None:
                    """Create a new schema::TupleElement instance from keyword arguments.

                    Call db.save() on the returned object to persist it in the database.
                    """
                    ...

                @classmethod
                def update(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::TupleElement instances in the database.
                    """
                    ...

                @classmethod
                def select(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: PathAlias,
                    id: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::TupleElement instances from the database.
                    """
                    ...

                @classmethod
                def filter(  # type: ignore [override, unused-ignore]
                    cls,
                    /,
                    *exprs: Callable[[type[Self]], type[__std__.bool]],
                    id: UUID | type[__std__.uuid] | UnspecifiedType = Unspecified,
                    name: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::TupleElement instances from the database.
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


        Any = TypeVar("Any", bound="TupleElement | Base")
    class __links__(std.BaseObject.__links__):
        pass

if not TYPE_CHECKING:
    TupleElement.__variants__.Base = TupleElement



#
# type schema::AnnotationSubject
#
class __AnnotationSubject_typeof__(__Object_typeof__):
    class __gel_reflection__(__Object_typeof__.__gel_reflection__):
        id = UUID(int=200771465757710694205600005641852404014)
        name = SchemaPath('schema', 'AnnotationSubject')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema__
            return __schema__.ObjectType(
                id=UUID(int=200771465757710694205600005641852404014),
                name='schema::AnnotationSubject',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__(__Object_typeof__.__typeof__):
        annotations = TypeAliasType('annotations', 'MultiLinkWithProps[AnnotationSubject.__links__.annotations, Annotation]')


class AnnotationSubject(
    __AnnotationSubject_typeof__,
    Object,
    __gel_type_id__=UUID(int=200771465757710694205600005641852404014),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
        ) -> None:
            """Create a new schema::AnnotationSubject instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::AnnotationSubject instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::AnnotationSubject instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::AnnotationSubject instances from the database.
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


    class __variants__(Object.__variants__):
        class Base(__AnnotationSubject_typeof__, Object.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                ) -> None:
                    """Create a new schema::AnnotationSubject instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::AnnotationSubject instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::AnnotationSubject instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::AnnotationSubject instances from the database.
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


        Any = TypeVar("Any", bound="AnnotationSubject | Base")
    class __links__(Object.__links__):
        if TYPE_CHECKING:
            class annotations(
                schema.Annotation,
                ProxyModel[schema.Annotation],
            ):
                """link schema::AnnotationSubject.annotations: schema::Annotation"""
                class __lprops__(GelLinkModel):
                    owned: OptionalProperty[__std__.bool, __builtins_1__.bool]
                    is_owned: OptionalProperty[__std__.bool, __builtins_1__.bool]
                    value: OptionalProperty[__std__.str, __builtins__.str]

                def __init__(
                    self,
                    obj: schema.Annotation,
                    /,
                    *,
                    owned: __builtins_1__.bool | None = None,
                    is_owned: __builtins_1__.bool | None = None,
                    value: __builtins__.str | None = None,
                ) -> None:
                    ...

                @classmethod
                def link(
                    cls,
                    obj: schema.Annotation,
                    /,
                    *,
                    owned: __builtins_1__.bool | None = None,
                    is_owned: __builtins_1__.bool | None = None,
                    value: __builtins__.str | None = None,
                ) -> Self:
                    ...

        if not TYPE_CHECKING:
            @LazyClassProperty[type]
            @classmethod
            def annotations(cls) -> type:
                class AnnotationSubject__annotations(
                    __schema__.Annotation,
                    ProxyModel[__schema__.Annotation],
                ):
                    """link schema::AnnotationSubject.annotations: schema::Annotation"""
                    class __lprops__(GelLinkModel):
                        owned: OptionalProperty[std.bool, __builtins_1__.bool]
                        is_owned: OptionalProperty[std.bool, __builtins_1__.bool]
                        value: OptionalProperty[std.str, __builtins__.str]

                    def __init__(
                        self,
                        obj: __schema__.Annotation,
                        /,
                        *,
                        owned: __builtins_1__.bool | None = None,
                        is_owned: __builtins_1__.bool | None = None,
                        value: __builtins__.str | None = None,
                    ) -> None:
                        ProxyModel.__init__(self, obj)
                        lprops = self.__class__.__lprops__(
                            owned=owned,
                            is_owned=is_owned,
                            value=value,
                        )
                        object.__setattr__(self, "__linkprops__", lprops)

                    @classmethod
                    def link(
                        cls,
                        obj: __schema__.Annotation,
                        /,
                        *,
                        owned: __builtins_1__.bool | None = None,
                        is_owned: __builtins_1__.bool | None = None,
                        value: __builtins__.str | None = None,
                    ) -> Self:
                        return cls(
                            obj,
                            owned=owned,
                            is_owned=is_owned,
                            value=value,
                        )

                AnnotationSubject__annotations.__name__ = 'annotations'
                AnnotationSubject__annotations.__qualname__ = 'AnnotationSubject.annotations'
                return AnnotationSubject__annotations

if not TYPE_CHECKING:
    AnnotationSubject.__variants__.Base = AnnotationSubject



#
# type schema::Delta
#
class __Delta_typeof__(__Object_typeof__):
    class __gel_reflection__(__Object_typeof__.__gel_reflection__):
        id = UUID(int=267780996458575171504439478392129386302)
        name = SchemaPath('schema', 'Delta')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=267780996458575171504439478392129386302),
                name='schema::Delta',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__Object_typeof__.__typeof__):
        parents = TypeAliasType('parents', 'MultiLink[Delta]')


class Delta(
    __Delta_typeof__,
    Object,
    __gel_type_id__=UUID(int=267780996458575171504439478392129386302),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            parents: Iterable[Delta] = [],
        ) -> None:
            """Create a new schema::Delta instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            parents: type[schema.Delta] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Delta instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            parents: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Delta] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Delta instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            parents: type[schema.Delta] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Delta instances from the database.
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


    class __variants__(Object.__variants__):
        class Base(__Delta_typeof__, Object.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    parents: Iterable[Delta] = [],
                ) -> None:
                    """Create a new schema::Delta instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    parents: type[schema.Delta] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Delta instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    parents: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Delta] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Delta instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    parents: type[schema.Delta] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Delta instances from the database.
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


        Any = TypeVar("Any", bound="Delta | Base")
    class __links__(Object.__links__):
        pass

if not TYPE_CHECKING:
    Delta.__variants__.Base = Delta



#
# type schema::FutureBehavior
#
class __FutureBehavior_typeof__(__Object_typeof__):
    class __gel_reflection__(__Object_typeof__.__gel_reflection__):
        id = UUID(int=331958463269391668024806361398877540)
        name = SchemaPath('schema', 'FutureBehavior')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=331958463269391668024806361398877540),
                name='schema::FutureBehavior',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__Object_typeof__.__typeof__):
        pass


class FutureBehavior(
    __FutureBehavior_typeof__,
    Object,
    __gel_type_id__=UUID(int=331958463269391668024806361398877540),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
        ) -> None:
            """Create a new schema::FutureBehavior instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::FutureBehavior instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::FutureBehavior instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::FutureBehavior instances from the database.
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


    class __variants__(Object.__variants__):
        class Base(__FutureBehavior_typeof__, Object.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                ) -> None:
                    """Create a new schema::FutureBehavior instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::FutureBehavior instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::FutureBehavior instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::FutureBehavior instances from the database.
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


        Any = TypeVar("Any", bound="FutureBehavior | Base")
    class __links__(Object.__links__):
        pass

if not TYPE_CHECKING:
    FutureBehavior.__variants__.Base = FutureBehavior



#
# type schema::Parameter
#
class __Parameter_typeof__(__Object_typeof__):
    class __gel_reflection__(__Object_typeof__.__gel_reflection__):
        id = UUID(int=180732607306417598723908042903228099108)
        name = SchemaPath('schema', 'Parameter')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=180732607306417598723908042903228099108),
                name='schema::Parameter',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__Object_typeof__.__typeof__):
        typemod = TypeAliasType('typemod', 'TypeModifier')
        kind = TypeAliasType('kind', 'ParameterKind')
        num = TypeAliasType('num', 'std.int64')
        default = TypeAliasType('default', 'OptionalProperty[std.str, str]')
        type = TypeAliasType('type', 'OptionalLink[Type]')


class Parameter(
    __Parameter_typeof__,
    Object,
    __gel_type_id__=UUID(int=180732607306417598723908042903228099108),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            typemod: __builtins__.str,
            kind: __builtins__.str,
            num: int,
            default: str | None = None,
            type: Type | None = None,
        ) -> None:
            """Create a new schema::Parameter instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            typemod: type[TypeModifier] | UnspecifiedType = Unspecified,
            kind: type[ParameterKind] | UnspecifiedType = Unspecified,
            num: __builtins_2__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Parameter instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            typemod: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[TypeModifier] | UnspecifiedType = Unspecified,
            kind: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ParameterKind] | UnspecifiedType = Unspecified,
            num: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
            default: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Parameter instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            typemod: type[TypeModifier] | UnspecifiedType = Unspecified,
            kind: type[ParameterKind] | UnspecifiedType = Unspecified,
            num: __builtins_2__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
            default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Parameter instances from the database.
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
            num: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            default: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(Object.__variants__):
        class Base(__Parameter_typeof__, Object.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    typemod: __builtins__.str,
                    kind: __builtins__.str,
                    num: int,
                    default: str | None = None,
                    type: Type | None = None,
                ) -> None:
                    """Create a new schema::Parameter instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    typemod: type[TypeModifier] | UnspecifiedType = Unspecified,
                    kind: type[ParameterKind] | UnspecifiedType = Unspecified,
                    num: __builtins_2__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Parameter instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    typemod: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[TypeModifier] | UnspecifiedType = Unspecified,
                    kind: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[ParameterKind] | UnspecifiedType = Unspecified,
                    num: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.int64] | UnspecifiedType = Unspecified,
                    default: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Parameter instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    typemod: type[TypeModifier] | UnspecifiedType = Unspecified,
                    kind: type[ParameterKind] | UnspecifiedType = Unspecified,
                    num: __builtins_2__.int | type[__std__.int64] | UnspecifiedType = Unspecified,
                    default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Parameter instances from the database.
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
                    num: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    default: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Parameter | Base")
    class __links__(Object.__links__):
        pass

if not TYPE_CHECKING:
    Parameter.__variants__.Base = Parameter



#
# type schema::Source
#
class __Source_typeof__(__Object_typeof__):
    class __gel_reflection__(__Object_typeof__.__gel_reflection__):
        id = UUID(int=4531483172543608627442440371551189032)
        name = SchemaPath('schema', 'Source')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=4531483172543608627442440371551189032),
                name='schema::Source',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__(__Object_typeof__.__typeof__):
        pointers = TypeAliasType('pointers', 'MultiLinkWithProps[Source.__links__.pointers, Pointer]')
        indexes = TypeAliasType('indexes', 'MultiLinkWithProps[Source.__links__.indexes, Index]')


class Source(
    __Source_typeof__,
    Object,
    __gel_type_id__=UUID(int=4531483172543608627442440371551189032),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            abstract: bool | None = None,
            final: bool,
            inherited_fields: list[str] | None = None,
            bases: Iterable[InheritingObject] = [],
            ancestors: Iterable[InheritingObject] = [],
            pointers: Iterable[Pointer] = [],
            indexes: Iterable[Index] = [],
        ) -> None:
            """Create a new schema::Source instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            pointers: type[schema.Pointer] | UnspecifiedType = Unspecified,
            indexes: type[schema.Index] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Source instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            pointers: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Pointer] | UnspecifiedType = Unspecified,
            indexes: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Index] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Source instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            pointers: type[schema.Pointer] | UnspecifiedType = Unspecified,
            indexes: type[schema.Index] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Source instances from the database.
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
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(Object.__variants__):
        class Base(__Source_typeof__, Object.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    abstract: bool | None = None,
                    final: bool,
                    inherited_fields: list[str] | None = None,
                    bases: Iterable[InheritingObject] = [],
                    ancestors: Iterable[InheritingObject] = [],
                    pointers: Iterable[Pointer] = [],
                    indexes: Iterable[Index] = [],
                ) -> None:
                    """Create a new schema::Source instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    pointers: type[schema.Pointer] | UnspecifiedType = Unspecified,
                    indexes: type[schema.Index] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Source instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    pointers: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Pointer] | UnspecifiedType = Unspecified,
                    indexes: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Index] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Source instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    pointers: type[schema.Pointer] | UnspecifiedType = Unspecified,
                    indexes: type[schema.Index] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Source instances from the database.
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
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Source | Base")
    class __links__(Object.__links__):
        if TYPE_CHECKING:
            class pointers(schema.Pointer, ProxyModel[schema.Pointer]):
                """link schema::Source.pointers: schema::Pointer"""
                class __lprops__(GelLinkModel):
                    owned: OptionalProperty[__std__.bool, __builtins_1__.bool]
                    is_owned: OptionalProperty[__std__.bool, __builtins_1__.bool]

                def __init__(
                    self,
                    obj: schema.Pointer,
                    /,
                    *,
                    owned: __builtins_1__.bool | None = None,
                    is_owned: __builtins_1__.bool | None = None,
                ) -> None:
                    ...

                @classmethod
                def link(
                    cls,
                    obj: schema.Pointer,
                    /,
                    *,
                    owned: __builtins_1__.bool | None = None,
                    is_owned: __builtins_1__.bool | None = None,
                ) -> Self:
                    ...

            class indexes(schema.Index, ProxyModel[schema.Index]):
                """link schema::Source.indexes: schema::Index"""
                class __lprops__(GelLinkModel):
                    owned: OptionalProperty[__std__.bool, __builtins_1__.bool]
                    is_owned: OptionalProperty[__std__.bool, __builtins_1__.bool]

                def __init__(
                    self,
                    obj: schema.Index,
                    /,
                    *,
                    owned: __builtins_1__.bool | None = None,
                    is_owned: __builtins_1__.bool | None = None,
                ) -> None:
                    ...

                @classmethod
                def link(
                    cls,
                    obj: schema.Index,
                    /,
                    *,
                    owned: __builtins_1__.bool | None = None,
                    is_owned: __builtins_1__.bool | None = None,
                ) -> Self:
                    ...

        if not TYPE_CHECKING:
            @LazyClassProperty[type]
            @classmethod
            def pointers(cls) -> type:
                class Source__pointers(
                    __schema__.Pointer,
                    ProxyModel[__schema__.Pointer],
                ):
                    """link schema::Source.pointers: schema::Pointer"""
                    class __lprops__(GelLinkModel):
                        owned: OptionalProperty[std.bool, __builtins_1__.bool]
                        is_owned: OptionalProperty[std.bool, __builtins_1__.bool]

                    def __init__(
                        self,
                        obj: __schema__.Pointer,
                        /,
                        *,
                        owned: __builtins_1__.bool | None = None,
                        is_owned: __builtins_1__.bool | None = None,
                    ) -> None:
                        ProxyModel.__init__(self, obj)
                        lprops = self.__class__.__lprops__(
                            owned=owned,
                            is_owned=is_owned,
                        )
                        object.__setattr__(self, "__linkprops__", lprops)

                    @classmethod
                    def link(
                        cls,
                        obj: __schema__.Pointer,
                        /,
                        *,
                        owned: __builtins_1__.bool | None = None,
                        is_owned: __builtins_1__.bool | None = None,
                    ) -> Self:
                        return cls(obj, owned=owned, is_owned=is_owned)

                Source__pointers.__name__ = 'pointers'
                Source__pointers.__qualname__ = 'Source.pointers'
                return Source__pointers
            @LazyClassProperty[type]
            @classmethod
            def indexes(cls) -> type:
                class Source__indexes(
                    __schema__.Index,
                    ProxyModel[__schema__.Index],
                ):
                    """link schema::Source.indexes: schema::Index"""
                    class __lprops__(GelLinkModel):
                        owned: OptionalProperty[std.bool, __builtins_1__.bool]
                        is_owned: OptionalProperty[std.bool, __builtins_1__.bool]

                    def __init__(
                        self,
                        obj: __schema__.Index,
                        /,
                        *,
                        owned: __builtins_1__.bool | None = None,
                        is_owned: __builtins_1__.bool | None = None,
                    ) -> None:
                        ProxyModel.__init__(self, obj)
                        lprops = self.__class__.__lprops__(
                            owned=owned,
                            is_owned=is_owned,
                        )
                        object.__setattr__(self, "__linkprops__", lprops)

                    @classmethod
                    def link(
                        cls,
                        obj: __schema__.Index,
                        /,
                        *,
                        owned: __builtins_1__.bool | None = None,
                        is_owned: __builtins_1__.bool | None = None,
                    ) -> Self:
                        return cls(obj, owned=owned, is_owned=is_owned)

                Source__indexes.__name__ = 'indexes'
                Source__indexes.__qualname__ = 'Source.indexes'
                return Source__indexes

if not TYPE_CHECKING:
    Source.__variants__.Base = Source



#
# type schema::SubclassableObject
#
class __SubclassableObject_typeof__(__Object_typeof__):
    class __gel_reflection__(__Object_typeof__.__gel_reflection__):
        id = UUID(int=27059562504987325367836323013285651930)
        name = SchemaPath('schema', 'SubclassableObject')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=27059562504987325367836323013285651930),
                name='schema::SubclassableObject',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__(__Object_typeof__.__typeof__):
        abstract = TypeAliasType('abstract', 'OptionalProperty[std.bool, bool]')
        is_abstract = TypeAliasType('is_abstract', 'OptionalComputedProperty[std.bool, bool]')
        final = TypeAliasType('final', 'ComputedProperty[std.bool, bool]')
        is_final = TypeAliasType('is_final', 'ComputedProperty[std.bool, bool]')


class SubclassableObject(
    __SubclassableObject_typeof__,
    Object,
    __gel_type_id__=UUID(int=27059562504987325367836323013285651930),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            abstract: bool | None = None,
            final: bool,
        ) -> None:
            """Create a new schema::SubclassableObject instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::SubclassableObject instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::SubclassableObject instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::SubclassableObject instances from the database.
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
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(Object.__variants__):
        class Base(__SubclassableObject_typeof__, Object.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    abstract: bool | None = None,
                    final: bool,
                ) -> None:
                    """Create a new schema::SubclassableObject instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::SubclassableObject instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::SubclassableObject instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::SubclassableObject instances from the database.
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
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="SubclassableObject | Base")
    class __links__(Object.__links__):
        pass

if not TYPE_CHECKING:
    SubclassableObject.__variants__.Base = SubclassableObject



#
# type schema::VolatilitySubject
#
class __VolatilitySubject_typeof__(__Object_typeof__):
    class __gel_reflection__(__Object_typeof__.__gel_reflection__):
        id = UUID(int=315765006271294895031481864239516637073)
        name = SchemaPath('schema', 'VolatilitySubject')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=315765006271294895031481864239516637073),
                name='schema::VolatilitySubject',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__(__Object_typeof__.__typeof__):
        volatility = TypeAliasType('volatility', 'OptionalProperty[Volatility, __builtins__.str]')


class VolatilitySubject(
    __VolatilitySubject_typeof__,
    Object,
    __gel_type_id__=UUID(int=315765006271294895031481864239516637073),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            volatility: __builtins__.str | None = None,
        ) -> None:
            """Create a new schema::VolatilitySubject instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            volatility: type[Volatility] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::VolatilitySubject instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            volatility: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Volatility] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::VolatilitySubject instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            volatility: type[Volatility] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::VolatilitySubject instances from the database.
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


    class __variants__(Object.__variants__):
        class Base(__VolatilitySubject_typeof__, Object.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    volatility: __builtins__.str | None = None,
                ) -> None:
                    """Create a new schema::VolatilitySubject instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    volatility: type[Volatility] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::VolatilitySubject instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    volatility: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Volatility] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::VolatilitySubject instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    volatility: type[Volatility] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::VolatilitySubject instances from the database.
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


        Any = TypeVar("Any", bound="VolatilitySubject | Base")
    class __links__(Object.__links__):
        pass

if not TYPE_CHECKING:
    VolatilitySubject.__variants__.Base = VolatilitySubject



#
# type schema::Alias
#
class __Alias_typeof__(__AnnotationSubject_typeof__):
    class __gel_reflection__(__AnnotationSubject_typeof__.__gel_reflection__):
        id = UUID(int=89765727105434638847323116050456262054)
        name = SchemaPath('schema', 'Alias')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=89765727105434638847323116050456262054),
                name='schema::Alias',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__AnnotationSubject_typeof__.__typeof__):
        expr = TypeAliasType('expr', 'std.str')
        type = TypeAliasType('type', 'OptionalLink[Type]')


class Alias(
    __Alias_typeof__,
    AnnotationSubject,
    __gel_type_id__=UUID(int=89765727105434638847323116050456262054),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            expr: str,
            type: Type | None = None,
        ) -> None:
            """Create a new schema::Alias instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Alias instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Alias instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Alias instances from the database.
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
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(AnnotationSubject.__variants__):
        class Base(__Alias_typeof__, AnnotationSubject.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    expr: str,
                    type: Type | None = None,
                ) -> None:
                    """Create a new schema::Alias instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Alias instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Alias instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Alias instances from the database.
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
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Alias | Base")
    class __links__(AnnotationSubject.__links__):
        pass

if not TYPE_CHECKING:
    Alias.__variants__.Base = Alias



#
# type schema::CallableObject
#
class __CallableObject_typeof__(__AnnotationSubject_typeof__):
    class __gel_reflection__(__AnnotationSubject_typeof__.__gel_reflection__):
        id = UUID(int=170220000418150476267999719922415966877)
        name = SchemaPath('schema', 'CallableObject')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=170220000418150476267999719922415966877),
                name='schema::CallableObject',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__(__AnnotationSubject_typeof__.__typeof__):
        return_typemod = TypeAliasType('return_typemod', 'OptionalProperty[TypeModifier, __builtins__.str]')
        params = TypeAliasType('params', 'MultiLinkWithProps[CallableObject.__links__.params, Parameter]')
        return_type = TypeAliasType('return_type', 'OptionalLink[Type]')


class CallableObject(
    __CallableObject_typeof__,
    AnnotationSubject,
    __gel_type_id__=UUID(int=170220000418150476267999719922415966877),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            return_typemod: __builtins__.str | None = None,
            params: Iterable[Parameter] = [],
            return_type: Type | None = None,
        ) -> None:
            """Create a new schema::CallableObject instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            return_typemod: type[TypeModifier] | UnspecifiedType = Unspecified,
            params: type[schema.Parameter] | UnspecifiedType = Unspecified,
            return_type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::CallableObject instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            return_typemod: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[TypeModifier] | UnspecifiedType = Unspecified,
            params: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Parameter] | UnspecifiedType = Unspecified,
            return_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::CallableObject instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            return_typemod: type[TypeModifier] | UnspecifiedType = Unspecified,
            params: type[schema.Parameter] | UnspecifiedType = Unspecified,
            return_type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::CallableObject instances from the database.
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


    class __variants__(AnnotationSubject.__variants__):
        class Base(
            __CallableObject_typeof__,
            AnnotationSubject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    return_typemod: __builtins__.str | None = None,
                    params: Iterable[Parameter] = [],
                    return_type: Type | None = None,
                ) -> None:
                    """Create a new schema::CallableObject instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    return_typemod: type[TypeModifier] | UnspecifiedType = Unspecified,
                    params: type[schema.Parameter] | UnspecifiedType = Unspecified,
                    return_type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::CallableObject instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    return_typemod: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[TypeModifier] | UnspecifiedType = Unspecified,
                    params: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Parameter] | UnspecifiedType = Unspecified,
                    return_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::CallableObject instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    return_typemod: type[TypeModifier] | UnspecifiedType = Unspecified,
                    params: type[schema.Parameter] | UnspecifiedType = Unspecified,
                    return_type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::CallableObject instances from the database.
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


        Any = TypeVar("Any", bound="CallableObject | Base")
    class __links__(AnnotationSubject.__links__):
        if TYPE_CHECKING:
            class params(schema.Parameter, ProxyModel[schema.Parameter]):
                """link schema::CallableObject.params: schema::Parameter"""
                class __lprops__(GelLinkModel):
                    index: OptionalProperty[__std__.int64, __builtins_2__.int]

                def __init__(
                    self,
                    obj: schema.Parameter,
                    /,
                    *,
                    index: __builtins_2__.int | None = None,
                ) -> None:
                    ...

                @classmethod
                def link(
                    cls,
                    obj: schema.Parameter,
                    /,
                    *,
                    index: __builtins_2__.int | None = None,
                ) -> Self:
                    ...

        if not TYPE_CHECKING:
            @LazyClassProperty[type]
            @classmethod
            def params(cls) -> type:
                class CallableObject__params(
                    __schema__.Parameter,
                    ProxyModel[__schema__.Parameter],
                ):
                    """link schema::CallableObject.params: schema::Parameter"""
                    class __lprops__(GelLinkModel):
                        index: OptionalProperty[std.int64, __builtins_2__.int]

                    def __init__(
                        self,
                        obj: __schema__.Parameter,
                        /,
                        *,
                        index: __builtins_2__.int | None = None,
                    ) -> None:
                        ProxyModel.__init__(self, obj)
                        lprops = self.__class__.__lprops__(index=index)
                        object.__setattr__(self, "__linkprops__", lprops)

                    @classmethod
                    def link(
                        cls,
                        obj: __schema__.Parameter,
                        /,
                        *,
                        index: __builtins_2__.int | None = None,
                    ) -> Self:
                        return cls(obj, index=index)

                CallableObject__params.__name__ = 'params'
                CallableObject__params.__qualname__ = 'CallableObject.params'
                return CallableObject__params

if not TYPE_CHECKING:
    CallableObject.__variants__.Base = CallableObject



#
# type schema::Extension
#
class __Extension_typeof__(__AnnotationSubject_typeof__, __Object_typeof__):
    class __gel_reflection__(
        __AnnotationSubject_typeof__.__gel_reflection__,
        __Object_typeof__.__gel_reflection__,
    ):
        id = UUID(int=246931183695036285442200903660376250349)
        name = SchemaPath('schema', 'Extension')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=246931183695036285442200903660376250349),
                name='schema::Extension',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __AnnotationSubject_typeof__.__typeof__,
        __Object_typeof__.__typeof__,
    ):
        package = TypeAliasType('package', 'OptionalLink[sys.ExtensionPackage]')


class Extension(
    __Extension_typeof__,
    AnnotationSubject,
    Object,
    __gel_type_id__=UUID(int=246931183695036285442200903660376250349),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            package: sys.ExtensionPackage | None = None,
        ) -> None:
            """Create a new schema::Extension instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            package: type[__sys__.ExtensionPackage] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Extension instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            package: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.ExtensionPackage] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Extension instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            package: type[__sys__.ExtensionPackage] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Extension instances from the database.
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


    class __variants__(AnnotationSubject.__variants__, Object.__variants__):
        class Base(
            __Extension_typeof__,
            AnnotationSubject.__variants__.Base,
            Object.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    package: sys.ExtensionPackage | None = None,
                ) -> None:
                    """Create a new schema::Extension instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    package: type[__sys__.ExtensionPackage] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Extension instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    package: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__sys__.ExtensionPackage] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Extension instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    package: type[__sys__.ExtensionPackage] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Extension instances from the database.
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


        Any = TypeVar("Any", bound="Extension | Base")
    class __links__(AnnotationSubject.__links__, Object.__links__):
        pass

if not TYPE_CHECKING:
    Extension.__variants__.Base = Extension



#
# type schema::Global
#
class __Global_typeof__(__AnnotationSubject_typeof__):
    class __gel_reflection__(__AnnotationSubject_typeof__.__gel_reflection__):
        id = UUID(int=299290551709576802008662613040485138993)
        name = SchemaPath('schema', 'Global')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=299290551709576802008662613040485138993),
                name='schema::Global',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__AnnotationSubject_typeof__.__typeof__):
        default = TypeAliasType('default', 'OptionalProperty[std.str, str]')
        required = TypeAliasType('required', 'OptionalProperty[std.bool, bool]')
        cardinality = TypeAliasType('cardinality', 'OptionalProperty[Cardinality, __builtins__.str]')
        expr = TypeAliasType('expr', 'OptionalProperty[std.str, str]')
        target = TypeAliasType('target', 'OptionalLink[Type]')


class Global(
    __Global_typeof__,
    AnnotationSubject,
    __gel_type_id__=UUID(int=299290551709576802008662613040485138993),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            default: str | None = None,
            required: bool | None = None,
            cardinality: __builtins__.str | None = None,
            expr: str | None = None,
            target: Type | None = None,
        ) -> None:
            """Create a new schema::Global instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            required: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            cardinality: type[Cardinality] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            target: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Global instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            default: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            required: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            cardinality: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Cardinality] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            target: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Global instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            required: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            cardinality: type[Cardinality] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            target: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Global instances from the database.
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
            default: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            required: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(AnnotationSubject.__variants__):
        class Base(__Global_typeof__, AnnotationSubject.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    default: str | None = None,
                    required: bool | None = None,
                    cardinality: __builtins__.str | None = None,
                    expr: str | None = None,
                    target: Type | None = None,
                ) -> None:
                    """Create a new schema::Global instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    required: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    cardinality: type[Cardinality] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    target: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Global instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    default: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    required: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    cardinality: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Cardinality] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    target: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Global instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    required: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    cardinality: type[Cardinality] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    target: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Global instances from the database.
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
                    default: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    required: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Global | Base")
    class __links__(AnnotationSubject.__links__):
        pass

if not TYPE_CHECKING:
    Global.__variants__.Base = Global



#
# type schema::Migration
#
class __Migration_typeof__(__AnnotationSubject_typeof__, __Object_typeof__):
    class __gel_reflection__(
        __AnnotationSubject_typeof__.__gel_reflection__,
        __Object_typeof__.__gel_reflection__,
    ):
        id = UUID(int=66416194960845351792630777443783118454)
        name = SchemaPath('schema', 'Migration')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=66416194960845351792630777443783118454),
                name='schema::Migration',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __AnnotationSubject_typeof__.__typeof__,
        __Object_typeof__.__typeof__,
    ):
        script = TypeAliasType('script', 'std.str')
        sdl = TypeAliasType('sdl', 'OptionalProperty[std.str, str]')
        message = TypeAliasType('message', 'OptionalProperty[std.str, str]')
        generated_by = TypeAliasType('generated_by', 'OptionalProperty[MigrationGeneratedBy, __builtins__.str]')
        parents = TypeAliasType('parents', 'MultiLink[Migration]')


class Migration(
    __Migration_typeof__,
    AnnotationSubject,
    Object,
    __gel_type_id__=UUID(int=66416194960845351792630777443783118454),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            script: str,
            sdl: str | None = None,
            message: str | None = None,
            generated_by: __builtins__.str | None = None,
            parents: Iterable[Migration] = [],
        ) -> None:
            """Create a new schema::Migration instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            script: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            sdl: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            message: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            generated_by: type[MigrationGeneratedBy] | UnspecifiedType = Unspecified,
            parents: type[schema.Migration] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Migration instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            script: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            sdl: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            message: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            generated_by: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[MigrationGeneratedBy] | UnspecifiedType = Unspecified,
            parents: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Migration] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Migration instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            script: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            sdl: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            message: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            generated_by: type[MigrationGeneratedBy] | UnspecifiedType = Unspecified,
            parents: type[schema.Migration] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Migration instances from the database.
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
            sdl: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            message: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(AnnotationSubject.__variants__, Object.__variants__):
        class Base(
            __Migration_typeof__,
            AnnotationSubject.__variants__.Base,
            Object.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    script: str,
                    sdl: str | None = None,
                    message: str | None = None,
                    generated_by: __builtins__.str | None = None,
                    parents: Iterable[Migration] = [],
                ) -> None:
                    """Create a new schema::Migration instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    script: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    sdl: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    message: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    generated_by: type[MigrationGeneratedBy] | UnspecifiedType = Unspecified,
                    parents: type[schema.Migration] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Migration instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    script: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    sdl: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    message: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    generated_by: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[MigrationGeneratedBy] | UnspecifiedType = Unspecified,
                    parents: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Migration] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Migration instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    script: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    sdl: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    message: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    generated_by: type[MigrationGeneratedBy] | UnspecifiedType = Unspecified,
                    parents: type[schema.Migration] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Migration instances from the database.
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
                    sdl: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    message: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Migration | Base")
    class __links__(AnnotationSubject.__links__, Object.__links__):
        pass

if not TYPE_CHECKING:
    Migration.__variants__.Base = Migration



#
# type schema::Module
#
class __Module_typeof__(__AnnotationSubject_typeof__, __Object_typeof__):
    class __gel_reflection__(
        __AnnotationSubject_typeof__.__gel_reflection__,
        __Object_typeof__.__gel_reflection__,
    ):
        id = UUID(int=150233990426722901639198192952859157996)
        name = SchemaPath('schema', 'Module')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=150233990426722901639198192952859157996),
                name='schema::Module',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __AnnotationSubject_typeof__.__typeof__,
        __Object_typeof__.__typeof__,
    ):
        pass


class Module(
    __Module_typeof__,
    AnnotationSubject,
    Object,
    __gel_type_id__=UUID(int=150233990426722901639198192952859157996),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
        ) -> None:
            """Create a new schema::Module instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Module instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Module instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Module instances from the database.
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


    class __variants__(AnnotationSubject.__variants__, Object.__variants__):
        class Base(
            __Module_typeof__,
            AnnotationSubject.__variants__.Base,
            Object.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                ) -> None:
                    """Create a new schema::Module instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Module instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Module instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Module instances from the database.
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


        Any = TypeVar("Any", bound="Module | Base")
    class __links__(AnnotationSubject.__links__, Object.__links__):
        pass

if not TYPE_CHECKING:
    Module.__variants__.Base = Module



#
# type schema::InheritingObject
#
class __InheritingObject_typeof__(__SubclassableObject_typeof__):
    class __gel_reflection__(__SubclassableObject_typeof__.__gel_reflection__):
        id = UUID(int=173267341075642542569379505558814888434)
        name = SchemaPath('schema', 'InheritingObject')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=173267341075642542569379505558814888434),
                name='schema::InheritingObject',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__(__SubclassableObject_typeof__.__typeof__):
        inherited_fields = TypeAliasType('inherited_fields', 'OptionalProperty[pydantic.Array[std.str], list[str]]')
        bases = TypeAliasType('bases', 'MultiLinkWithProps[InheritingObject.__links__.bases, InheritingObject]')
        ancestors = TypeAliasType('ancestors', 'MultiLinkWithProps[InheritingObject.__links__.ancestors, InheritingObject]')


class InheritingObject(
    __InheritingObject_typeof__,
    SubclassableObject,
    __gel_type_id__=UUID(int=173267341075642542569379505558814888434),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            abstract: bool | None = None,
            final: bool,
            inherited_fields: list[str] | None = None,
            bases: Iterable[InheritingObject] = [],
            ancestors: Iterable[InheritingObject] = [],
        ) -> None:
            """Create a new schema::InheritingObject instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::InheritingObject instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::InheritingObject instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::InheritingObject instances from the database.
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
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(SubclassableObject.__variants__):
        class Base(
            __InheritingObject_typeof__,
            SubclassableObject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    abstract: bool | None = None,
                    final: bool,
                    inherited_fields: list[str] | None = None,
                    bases: Iterable[InheritingObject] = [],
                    ancestors: Iterable[InheritingObject] = [],
                ) -> None:
                    """Create a new schema::InheritingObject instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::InheritingObject instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::InheritingObject instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::InheritingObject instances from the database.
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
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="InheritingObject | Base")
    class __links__(SubclassableObject.__links__):
        if TYPE_CHECKING:
            class bases(
                schema.InheritingObject,
                ProxyModel[schema.InheritingObject],
            ):
                """link schema::InheritingObject.bases: schema::InheritingObject"""
                class __lprops__(GelLinkModel):
                    index: OptionalProperty[__std__.int64, __builtins_2__.int]

                def __init__(
                    self,
                    obj: schema.InheritingObject,
                    /,
                    *,
                    index: __builtins_2__.int | None = None,
                ) -> None:
                    ...

                @classmethod
                def link(
                    cls,
                    obj: schema.InheritingObject,
                    /,
                    *,
                    index: __builtins_2__.int | None = None,
                ) -> Self:
                    ...

            class ancestors(
                schema.InheritingObject,
                ProxyModel[schema.InheritingObject],
            ):
                """link schema::InheritingObject.ancestors: schema::InheritingObject"""
                class __lprops__(GelLinkModel):
                    index: OptionalProperty[__std__.int64, __builtins_2__.int]

                def __init__(
                    self,
                    obj: schema.InheritingObject,
                    /,
                    *,
                    index: __builtins_2__.int | None = None,
                ) -> None:
                    ...

                @classmethod
                def link(
                    cls,
                    obj: schema.InheritingObject,
                    /,
                    *,
                    index: __builtins_2__.int | None = None,
                ) -> Self:
                    ...

        if not TYPE_CHECKING:
            @LazyClassProperty[type]
            @classmethod
            def bases(cls) -> type:
                class InheritingObject__bases(
                    __schema__.InheritingObject,
                    ProxyModel[__schema__.InheritingObject],
                ):
                    """link schema::InheritingObject.bases: schema::InheritingObject"""
                    class __lprops__(GelLinkModel):
                        index: OptionalProperty[std.int64, __builtins_2__.int]

                    def __init__(
                        self,
                        obj: __schema__.InheritingObject,
                        /,
                        *,
                        index: __builtins_2__.int | None = None,
                    ) -> None:
                        ProxyModel.__init__(self, obj)
                        lprops = self.__class__.__lprops__(index=index)
                        object.__setattr__(self, "__linkprops__", lprops)

                    @classmethod
                    def link(
                        cls,
                        obj: __schema__.InheritingObject,
                        /,
                        *,
                        index: __builtins_2__.int | None = None,
                    ) -> Self:
                        return cls(obj, index=index)

                InheritingObject__bases.__name__ = 'bases'
                InheritingObject__bases.__qualname__ = 'InheritingObject.bases'
                return InheritingObject__bases
            @LazyClassProperty[type]
            @classmethod
            def ancestors(cls) -> type:
                class InheritingObject__ancestors(
                    __schema__.InheritingObject,
                    ProxyModel[__schema__.InheritingObject],
                ):
                    """link schema::InheritingObject.ancestors: schema::InheritingObject"""
                    class __lprops__(GelLinkModel):
                        index: OptionalProperty[std.int64, __builtins_2__.int]

                    def __init__(
                        self,
                        obj: __schema__.InheritingObject,
                        /,
                        *,
                        index: __builtins_2__.int | None = None,
                    ) -> None:
                        ProxyModel.__init__(self, obj)
                        lprops = self.__class__.__lprops__(index=index)
                        object.__setattr__(self, "__linkprops__", lprops)

                    @classmethod
                    def link(
                        cls,
                        obj: __schema__.InheritingObject,
                        /,
                        *,
                        index: __builtins_2__.int | None = None,
                    ) -> Self:
                        return cls(obj, index=index)

                InheritingObject__ancestors.__name__ = 'ancestors'
                InheritingObject__ancestors.__qualname__ = 'InheritingObject.ancestors'
                return InheritingObject__ancestors

if not TYPE_CHECKING:
    InheritingObject.__variants__.Base = InheritingObject



#
# type schema::Type
#
class __Type_typeof__(
    __SubclassableObject_typeof__,
    __AnnotationSubject_typeof__,
):
    class __gel_reflection__(
        __SubclassableObject_typeof__.__gel_reflection__,
        __AnnotationSubject_typeof__.__gel_reflection__,
    ):
        id = UUID(int=189275509320180683892909643730550477571)
        name = SchemaPath('schema', 'Type')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=189275509320180683892909643730550477571),
                name='schema::Type',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __SubclassableObject_typeof__.__typeof__,
        __AnnotationSubject_typeof__.__typeof__,
    ):
        expr = TypeAliasType('expr', 'OptionalProperty[std.str, str]')
        from_alias = TypeAliasType('from_alias', 'OptionalProperty[std.bool, bool]')
        is_from_alias = TypeAliasType('is_from_alias', 'OptionalComputedProperty[std.bool, bool]')


class Type(
    __Type_typeof__,
    SubclassableObject,
    AnnotationSubject,
    __gel_type_id__=UUID(int=189275509320180683892909643730550477571),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            expr: str | None = None,
            from_alias: bool | None = None,
        ) -> None:
            """Create a new schema::Type instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Type instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Type instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Type instances from the database.
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
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        SubclassableObject.__variants__,
        AnnotationSubject.__variants__,
    ):
        class Base(
            __Type_typeof__,
            SubclassableObject.__variants__.Base,
            AnnotationSubject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    expr: str | None = None,
                    from_alias: bool | None = None,
                ) -> None:
                    """Create a new schema::Type instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Type instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Type instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Type instances from the database.
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
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Type | Base")
    class __links__(SubclassableObject.__links__, AnnotationSubject.__links__):
        pass

if not TYPE_CHECKING:
    Type.__variants__.Base = Type



#
# type schema::Cast
#
class __Cast_typeof__(
    __AnnotationSubject_typeof__,
    __VolatilitySubject_typeof__,
):
    class __gel_reflection__(
        __AnnotationSubject_typeof__.__gel_reflection__,
        __VolatilitySubject_typeof__.__gel_reflection__,
    ):
        id = UUID(int=57352927458738121887507744293380160895)
        name = SchemaPath('schema', 'Cast')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=57352927458738121887507744293380160895),
                name='schema::Cast',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __AnnotationSubject_typeof__.__typeof__,
        __VolatilitySubject_typeof__.__typeof__,
    ):
        allow_implicit = TypeAliasType('allow_implicit', 'OptionalProperty[std.bool, bool]')
        allow_assignment = TypeAliasType('allow_assignment', 'OptionalProperty[std.bool, bool]')
        from_type = TypeAliasType('from_type', 'OptionalLink[Type]')
        to_type = TypeAliasType('to_type', 'OptionalLink[Type]')


class Cast(
    __Cast_typeof__,
    AnnotationSubject,
    VolatilitySubject,
    __gel_type_id__=UUID(int=57352927458738121887507744293380160895),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            volatility: __builtins__.str | None = None,
            annotations: Iterable[Annotation] = [],
            allow_implicit: bool | None = None,
            allow_assignment: bool | None = None,
            from_type: Type | None = None,
            to_type: Type | None = None,
        ) -> None:
            """Create a new schema::Cast instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            volatility: type[Volatility] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            allow_implicit: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_assignment: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            from_type: type[schema.Type] | UnspecifiedType = Unspecified,
            to_type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Cast instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            volatility: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Volatility] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            allow_implicit: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_assignment: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            from_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
            to_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Cast instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            volatility: type[Volatility] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            allow_implicit: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            allow_assignment: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            from_type: type[schema.Type] | UnspecifiedType = Unspecified,
            to_type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Cast instances from the database.
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
            allow_implicit: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            allow_assignment: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        AnnotationSubject.__variants__,
        VolatilitySubject.__variants__,
    ):
        class Base(
            __Cast_typeof__,
            AnnotationSubject.__variants__.Base,
            VolatilitySubject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    volatility: __builtins__.str | None = None,
                    annotations: Iterable[Annotation] = [],
                    allow_implicit: bool | None = None,
                    allow_assignment: bool | None = None,
                    from_type: Type | None = None,
                    to_type: Type | None = None,
                ) -> None:
                    """Create a new schema::Cast instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    volatility: type[Volatility] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    allow_implicit: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_assignment: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    from_type: type[schema.Type] | UnspecifiedType = Unspecified,
                    to_type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Cast instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    volatility: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Volatility] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    allow_implicit: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_assignment: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    from_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
                    to_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Cast instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    volatility: type[Volatility] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    allow_implicit: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    allow_assignment: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    from_type: type[schema.Type] | UnspecifiedType = Unspecified,
                    to_type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Cast instances from the database.
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
                    allow_implicit: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    allow_assignment: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Cast | Base")
    class __links__(AnnotationSubject.__links__, VolatilitySubject.__links__):
        pass

if not TYPE_CHECKING:
    Cast.__variants__.Base = Cast



#
# type schema::Function
#
class __Function_typeof__(
    __CallableObject_typeof__,
    __VolatilitySubject_typeof__,
):
    class __gel_reflection__(
        __CallableObject_typeof__.__gel_reflection__,
        __VolatilitySubject_typeof__.__gel_reflection__,
    ):
        id = UUID(int=77598660217071330185177185139856935407)
        name = SchemaPath('schema', 'Function')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=77598660217071330185177185139856935407),
                name='schema::Function',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __CallableObject_typeof__.__typeof__,
        __VolatilitySubject_typeof__.__typeof__,
    ):
        preserves_optionality = TypeAliasType('preserves_optionality', 'OptionalProperty[std.bool, bool]')
        body = TypeAliasType('body', 'OptionalProperty[std.str, str]')
        language = TypeAliasType('language', 'std.str')
        used_globals = TypeAliasType('used_globals', 'MultiLinkWithProps[Function.__links__.used_globals, Global]')


class Function(
    __Function_typeof__,
    CallableObject,
    VolatilitySubject,
    __gel_type_id__=UUID(int=77598660217071330185177185139856935407),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            volatility: __builtins__.str | None = None,
            annotations: Iterable[Annotation] = [],
            return_typemod: __builtins__.str | None = None,
            params: Iterable[Parameter] = [],
            return_type: Type | None = None,
            preserves_optionality: bool | None = None,
            body: str | None = None,
            language: str,
            used_globals: Iterable[Global] = [],
        ) -> None:
            """Create a new schema::Function instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            volatility: type[Volatility] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            return_typemod: type[TypeModifier] | UnspecifiedType = Unspecified,
            params: type[schema.Parameter] | UnspecifiedType = Unspecified,
            return_type: type[schema.Type] | UnspecifiedType = Unspecified,
            preserves_optionality: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            body: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            language: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            used_globals: type[schema.Global] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Function instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            volatility: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Volatility] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            return_typemod: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[TypeModifier] | UnspecifiedType = Unspecified,
            params: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Parameter] | UnspecifiedType = Unspecified,
            return_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
            preserves_optionality: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            body: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            language: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            used_globals: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Global] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Function instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            volatility: type[Volatility] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            return_typemod: type[TypeModifier] | UnspecifiedType = Unspecified,
            params: type[schema.Parameter] | UnspecifiedType = Unspecified,
            return_type: type[schema.Type] | UnspecifiedType = Unspecified,
            preserves_optionality: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            body: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            language: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            used_globals: type[schema.Global] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Function instances from the database.
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
            preserves_optionality: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            body: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            language: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        CallableObject.__variants__,
        VolatilitySubject.__variants__,
    ):
        class Base(
            __Function_typeof__,
            CallableObject.__variants__.Base,
            VolatilitySubject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    volatility: __builtins__.str | None = None,
                    annotations: Iterable[Annotation] = [],
                    return_typemod: __builtins__.str | None = None,
                    params: Iterable[Parameter] = [],
                    return_type: Type | None = None,
                    preserves_optionality: bool | None = None,
                    body: str | None = None,
                    language: str,
                    used_globals: Iterable[Global] = [],
                ) -> None:
                    """Create a new schema::Function instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    volatility: type[Volatility] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    return_typemod: type[TypeModifier] | UnspecifiedType = Unspecified,
                    params: type[schema.Parameter] | UnspecifiedType = Unspecified,
                    return_type: type[schema.Type] | UnspecifiedType = Unspecified,
                    preserves_optionality: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    body: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    language: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    used_globals: type[schema.Global] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Function instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    volatility: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Volatility] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    return_typemod: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[TypeModifier] | UnspecifiedType = Unspecified,
                    params: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Parameter] | UnspecifiedType = Unspecified,
                    return_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
                    preserves_optionality: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    body: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    language: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    used_globals: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Global] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Function instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    volatility: type[Volatility] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    return_typemod: type[TypeModifier] | UnspecifiedType = Unspecified,
                    params: type[schema.Parameter] | UnspecifiedType = Unspecified,
                    return_type: type[schema.Type] | UnspecifiedType = Unspecified,
                    preserves_optionality: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    body: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    language: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    used_globals: type[schema.Global] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Function instances from the database.
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
                    preserves_optionality: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    body: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    language: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Function | Base")
    class __links__(CallableObject.__links__, VolatilitySubject.__links__):
        if TYPE_CHECKING:
            class used_globals(schema.Global, ProxyModel[schema.Global]):
                """link schema::Function.used_globals: schema::Global"""
                class __lprops__(GelLinkModel):
                    index: OptionalProperty[__std__.int64, __builtins_2__.int]

                def __init__(
                    self,
                    obj: schema.Global,
                    /,
                    *,
                    index: __builtins_2__.int | None = None,
                ) -> None:
                    ...

                @classmethod
                def link(
                    cls,
                    obj: schema.Global,
                    /,
                    *,
                    index: __builtins_2__.int | None = None,
                ) -> Self:
                    ...

        if not TYPE_CHECKING:
            @LazyClassProperty[type]
            @classmethod
            def used_globals(cls) -> type:
                class Function__used_globals(
                    __schema__.Global,
                    ProxyModel[__schema__.Global],
                ):
                    """link schema::Function.used_globals: schema::Global"""
                    class __lprops__(GelLinkModel):
                        index: OptionalProperty[std.int64, __builtins_2__.int]

                    def __init__(
                        self,
                        obj: __schema__.Global,
                        /,
                        *,
                        index: __builtins_2__.int | None = None,
                    ) -> None:
                        ProxyModel.__init__(self, obj)
                        lprops = self.__class__.__lprops__(index=index)
                        object.__setattr__(self, "__linkprops__", lprops)

                    @classmethod
                    def link(
                        cls,
                        obj: __schema__.Global,
                        /,
                        *,
                        index: __builtins_2__.int | None = None,
                    ) -> Self:
                        return cls(obj, index=index)

                Function__used_globals.__name__ = 'used_globals'
                Function__used_globals.__qualname__ = 'Function.used_globals'
                return Function__used_globals

if not TYPE_CHECKING:
    Function.__variants__.Base = Function



#
# type schema::Operator
#
class __Operator_typeof__(
    __CallableObject_typeof__,
    __VolatilitySubject_typeof__,
):
    class __gel_reflection__(
        __CallableObject_typeof__.__gel_reflection__,
        __VolatilitySubject_typeof__.__gel_reflection__,
    ):
        id = UUID(int=302377796033846204813264836927507411646)
        name = SchemaPath('schema', 'Operator')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=302377796033846204813264836927507411646),
                name='schema::Operator',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __CallableObject_typeof__.__typeof__,
        __VolatilitySubject_typeof__.__typeof__,
    ):
        operator_kind = TypeAliasType('operator_kind', 'OptionalProperty[OperatorKind, __builtins__.str]')
        is_abstract = TypeAliasType('is_abstract', 'OptionalComputedProperty[std.bool, bool]')
        abstract = TypeAliasType('abstract', 'OptionalProperty[std.bool, bool]')


class Operator(
    __Operator_typeof__,
    CallableObject,
    VolatilitySubject,
    __gel_type_id__=UUID(int=302377796033846204813264836927507411646),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            volatility: __builtins__.str | None = None,
            annotations: Iterable[Annotation] = [],
            return_typemod: __builtins__.str | None = None,
            params: Iterable[Parameter] = [],
            return_type: Type | None = None,
            operator_kind: __builtins__.str | None = None,
            abstract: bool | None = None,
        ) -> None:
            """Create a new schema::Operator instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            volatility: type[Volatility] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            return_typemod: type[TypeModifier] | UnspecifiedType = Unspecified,
            params: type[schema.Parameter] | UnspecifiedType = Unspecified,
            return_type: type[schema.Type] | UnspecifiedType = Unspecified,
            operator_kind: type[OperatorKind] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Operator instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            volatility: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Volatility] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            return_typemod: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[TypeModifier] | UnspecifiedType = Unspecified,
            params: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Parameter] | UnspecifiedType = Unspecified,
            return_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
            operator_kind: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[OperatorKind] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Operator instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            volatility: type[Volatility] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            return_typemod: type[TypeModifier] | UnspecifiedType = Unspecified,
            params: type[schema.Parameter] | UnspecifiedType = Unspecified,
            return_type: type[schema.Type] | UnspecifiedType = Unspecified,
            operator_kind: type[OperatorKind] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Operator instances from the database.
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
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        CallableObject.__variants__,
        VolatilitySubject.__variants__,
    ):
        class Base(
            __Operator_typeof__,
            CallableObject.__variants__.Base,
            VolatilitySubject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    volatility: __builtins__.str | None = None,
                    annotations: Iterable[Annotation] = [],
                    return_typemod: __builtins__.str | None = None,
                    params: Iterable[Parameter] = [],
                    return_type: Type | None = None,
                    operator_kind: __builtins__.str | None = None,
                    abstract: bool | None = None,
                ) -> None:
                    """Create a new schema::Operator instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    volatility: type[Volatility] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    return_typemod: type[TypeModifier] | UnspecifiedType = Unspecified,
                    params: type[schema.Parameter] | UnspecifiedType = Unspecified,
                    return_type: type[schema.Type] | UnspecifiedType = Unspecified,
                    operator_kind: type[OperatorKind] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Operator instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    volatility: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Volatility] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    return_typemod: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[TypeModifier] | UnspecifiedType = Unspecified,
                    params: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Parameter] | UnspecifiedType = Unspecified,
                    return_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
                    operator_kind: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[OperatorKind] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Operator instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    volatility: type[Volatility] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    return_typemod: type[TypeModifier] | UnspecifiedType = Unspecified,
                    params: type[schema.Parameter] | UnspecifiedType = Unspecified,
                    return_type: type[schema.Type] | UnspecifiedType = Unspecified,
                    operator_kind: type[OperatorKind] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Operator instances from the database.
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
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Operator | Base")
    class __links__(CallableObject.__links__, VolatilitySubject.__links__):
        pass

if not TYPE_CHECKING:
    Operator.__variants__.Base = Operator



#
# type schema::AccessPolicy
#
class __AccessPolicy_typeof__(
    __InheritingObject_typeof__,
    __AnnotationSubject_typeof__,
):
    class __gel_reflection__(
        __InheritingObject_typeof__.__gel_reflection__,
        __AnnotationSubject_typeof__.__gel_reflection__,
    ):
        id = UUID(int=223674422221926051711980301232417846096)
        name = SchemaPath('schema', 'AccessPolicy')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=223674422221926051711980301232417846096),
                name='schema::AccessPolicy',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __InheritingObject_typeof__.__typeof__,
        __AnnotationSubject_typeof__.__typeof__,
    ):
        access_kinds = TypeAliasType('access_kinds', 'list[__builtins__.str]')
        condition = TypeAliasType('condition', 'OptionalProperty[std.str, str]')
        action = TypeAliasType('action', 'AccessPolicyAction')
        expr = TypeAliasType('expr', 'OptionalProperty[std.str, str]')
        errmessage = TypeAliasType('errmessage', 'OptionalProperty[std.str, str]')
        subject = TypeAliasType('subject', 'OptionalLink[ObjectType]')


class AccessPolicy(
    __AccessPolicy_typeof__,
    InheritingObject,
    AnnotationSubject,
    __gel_type_id__=UUID(int=223674422221926051711980301232417846096),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            inherited_fields: list[str] | None = None,
            bases: Iterable[InheritingObject] = [],
            ancestors: Iterable[InheritingObject] = [],
            access_kinds: Iterable[__builtins__.str] = [],
            condition: str | None = None,
            action: __builtins__.str,
            expr: str | None = None,
            errmessage: str | None = None,
            subject: ObjectType | None = None,
        ) -> None:
            """Create a new schema::AccessPolicy instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            access_kinds: type[AccessKind] | UnspecifiedType = Unspecified,
            condition: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            action: type[AccessPolicyAction] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            errmessage: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            subject: type[schema.ObjectType] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::AccessPolicy instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            access_kinds: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[AccessKind] | UnspecifiedType = Unspecified,
            condition: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            action: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[AccessPolicyAction] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            errmessage: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            subject: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.ObjectType] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::AccessPolicy instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            access_kinds: type[AccessKind] | UnspecifiedType = Unspecified,
            condition: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            action: type[AccessPolicyAction] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            errmessage: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            subject: type[schema.ObjectType] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::AccessPolicy instances from the database.
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
            condition: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            errmessage: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        InheritingObject.__variants__,
        AnnotationSubject.__variants__,
    ):
        class Base(
            __AccessPolicy_typeof__,
            InheritingObject.__variants__.Base,
            AnnotationSubject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    inherited_fields: list[str] | None = None,
                    bases: Iterable[InheritingObject] = [],
                    ancestors: Iterable[InheritingObject] = [],
                    access_kinds: Iterable[__builtins__.str] = [],
                    condition: str | None = None,
                    action: __builtins__.str,
                    expr: str | None = None,
                    errmessage: str | None = None,
                    subject: ObjectType | None = None,
                ) -> None:
                    """Create a new schema::AccessPolicy instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    access_kinds: type[AccessKind] | UnspecifiedType = Unspecified,
                    condition: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    action: type[AccessPolicyAction] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    errmessage: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    subject: type[schema.ObjectType] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::AccessPolicy instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    access_kinds: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[AccessKind] | UnspecifiedType = Unspecified,
                    condition: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    action: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[AccessPolicyAction] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    errmessage: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    subject: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.ObjectType] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::AccessPolicy instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    access_kinds: type[AccessKind] | UnspecifiedType = Unspecified,
                    condition: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    action: type[AccessPolicyAction] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    errmessage: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    subject: type[schema.ObjectType] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::AccessPolicy instances from the database.
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
                    condition: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    errmessage: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="AccessPolicy | Base")
    class __links__(InheritingObject.__links__, AnnotationSubject.__links__):
        pass

if not TYPE_CHECKING:
    AccessPolicy.__variants__.Base = AccessPolicy



#
# type schema::Annotation
#
class __Annotation_typeof__(
    __InheritingObject_typeof__,
    __AnnotationSubject_typeof__,
):
    class __gel_reflection__(
        __InheritingObject_typeof__.__gel_reflection__,
        __AnnotationSubject_typeof__.__gel_reflection__,
    ):
        id = UUID(int=52148979689992418483179854258332537093)
        name = SchemaPath('schema', 'Annotation')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=52148979689992418483179854258332537093),
                name='schema::Annotation',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __InheritingObject_typeof__.__typeof__,
        __AnnotationSubject_typeof__.__typeof__,
    ):
        inheritable = TypeAliasType('inheritable', 'OptionalProperty[std.bool, bool]')


class Annotation(
    __Annotation_typeof__,
    InheritingObject,
    AnnotationSubject,
    __gel_type_id__=UUID(int=52148979689992418483179854258332537093),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            inherited_fields: list[str] | None = None,
            bases: Iterable[InheritingObject] = [],
            ancestors: Iterable[InheritingObject] = [],
            inheritable: bool | None = None,
        ) -> None:
            """Create a new schema::Annotation instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            inheritable: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Annotation instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            inheritable: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Annotation instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            inheritable: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Annotation instances from the database.
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
            inheritable: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        InheritingObject.__variants__,
        AnnotationSubject.__variants__,
    ):
        class Base(
            __Annotation_typeof__,
            InheritingObject.__variants__.Base,
            AnnotationSubject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    inherited_fields: list[str] | None = None,
                    bases: Iterable[InheritingObject] = [],
                    ancestors: Iterable[InheritingObject] = [],
                    inheritable: bool | None = None,
                ) -> None:
                    """Create a new schema::Annotation instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    inheritable: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Annotation instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    inheritable: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Annotation instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    inheritable: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Annotation instances from the database.
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
                    inheritable: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Annotation | Base")
    class __links__(InheritingObject.__links__, AnnotationSubject.__links__):
        pass

if not TYPE_CHECKING:
    Annotation.__variants__.Base = Annotation



#
# type schema::ConsistencySubject
#
class __ConsistencySubject_typeof__(
    __InheritingObject_typeof__,
    __AnnotationSubject_typeof__,
):
    class __gel_reflection__(
        __InheritingObject_typeof__.__gel_reflection__,
        __AnnotationSubject_typeof__.__gel_reflection__,
    ):
        id = UUID(int=181100937149158556163506130951259876648)
        name = SchemaPath('schema', 'ConsistencySubject')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=181100937149158556163506130951259876648),
                name='schema::ConsistencySubject',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __InheritingObject_typeof__.__typeof__,
        __AnnotationSubject_typeof__.__typeof__,
    ):
        constraints = TypeAliasType('constraints', 'MultiLinkWithProps[ConsistencySubject.__links__.constraints, Constraint]')


class ConsistencySubject(
    __ConsistencySubject_typeof__,
    InheritingObject,
    AnnotationSubject,
    __gel_type_id__=UUID(int=181100937149158556163506130951259876648),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            inherited_fields: list[str] | None = None,
            bases: Iterable[InheritingObject] = [],
            ancestors: Iterable[InheritingObject] = [],
            constraints: Iterable[Constraint] = [],
        ) -> None:
            """Create a new schema::ConsistencySubject instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::ConsistencySubject instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            constraints: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Constraint] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::ConsistencySubject instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::ConsistencySubject instances from the database.
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
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        InheritingObject.__variants__,
        AnnotationSubject.__variants__,
    ):
        class Base(
            __ConsistencySubject_typeof__,
            InheritingObject.__variants__.Base,
            AnnotationSubject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    inherited_fields: list[str] | None = None,
                    bases: Iterable[InheritingObject] = [],
                    ancestors: Iterable[InheritingObject] = [],
                    constraints: Iterable[Constraint] = [],
                ) -> None:
                    """Create a new schema::ConsistencySubject instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::ConsistencySubject instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    constraints: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Constraint] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::ConsistencySubject instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::ConsistencySubject instances from the database.
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
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="ConsistencySubject | Base")
    class __links__(InheritingObject.__links__, AnnotationSubject.__links__):
        if TYPE_CHECKING:
            class constraints(
                schema.Constraint,
                ProxyModel[schema.Constraint],
            ):
                """link schema::ConsistencySubject.constraints: schema::Constraint"""
                class __lprops__(GelLinkModel):
                    owned: OptionalProperty[__std__.bool, __builtins_1__.bool]
                    is_owned: OptionalProperty[__std__.bool, __builtins_1__.bool]

                def __init__(
                    self,
                    obj: schema.Constraint,
                    /,
                    *,
                    owned: __builtins_1__.bool | None = None,
                    is_owned: __builtins_1__.bool | None = None,
                ) -> None:
                    ...

                @classmethod
                def link(
                    cls,
                    obj: schema.Constraint,
                    /,
                    *,
                    owned: __builtins_1__.bool | None = None,
                    is_owned: __builtins_1__.bool | None = None,
                ) -> Self:
                    ...

        if not TYPE_CHECKING:
            @LazyClassProperty[type]
            @classmethod
            def constraints(cls) -> type:
                class ConsistencySubject__constraints(
                    __schema__.Constraint,
                    ProxyModel[__schema__.Constraint],
                ):
                    """link schema::ConsistencySubject.constraints: schema::Constraint"""
                    class __lprops__(GelLinkModel):
                        owned: OptionalProperty[std.bool, __builtins_1__.bool]
                        is_owned: OptionalProperty[std.bool, __builtins_1__.bool]

                    def __init__(
                        self,
                        obj: __schema__.Constraint,
                        /,
                        *,
                        owned: __builtins_1__.bool | None = None,
                        is_owned: __builtins_1__.bool | None = None,
                    ) -> None:
                        ProxyModel.__init__(self, obj)
                        lprops = self.__class__.__lprops__(
                            owned=owned,
                            is_owned=is_owned,
                        )
                        object.__setattr__(self, "__linkprops__", lprops)

                    @classmethod
                    def link(
                        cls,
                        obj: __schema__.Constraint,
                        /,
                        *,
                        owned: __builtins_1__.bool | None = None,
                        is_owned: __builtins_1__.bool | None = None,
                    ) -> Self:
                        return cls(obj, owned=owned, is_owned=is_owned)

                ConsistencySubject__constraints.__name__ = 'constraints'
                ConsistencySubject__constraints.__qualname__ = 'ConsistencySubject.constraints'
                return ConsistencySubject__constraints

if not TYPE_CHECKING:
    ConsistencySubject.__variants__.Base = ConsistencySubject



#
# type schema::Constraint
#
class __Constraint_typeof__(
    __CallableObject_typeof__,
    __InheritingObject_typeof__,
):
    class __gel_reflection__(
        __CallableObject_typeof__.__gel_reflection__,
        __InheritingObject_typeof__.__gel_reflection__,
    ):
        id = UUID(int=195763951784768659695883964066391108399)
        name = SchemaPath('schema', 'Constraint')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=195763951784768659695883964066391108399),
                name='schema::Constraint',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __CallableObject_typeof__.__typeof__,
        __InheritingObject_typeof__.__typeof__,
    ):
        expr = TypeAliasType('expr', 'OptionalProperty[std.str, str]')
        subjectexpr = TypeAliasType('subjectexpr', 'OptionalProperty[std.str, str]')
        finalexpr = TypeAliasType('finalexpr', 'OptionalProperty[std.str, str]')
        errmessage = TypeAliasType('errmessage', 'OptionalProperty[std.str, str]')
        delegated = TypeAliasType('delegated', 'OptionalProperty[std.bool, bool]')
        except_expr = TypeAliasType('except_expr', 'OptionalProperty[std.str, str]')
        subject = TypeAliasType('subject', 'OptionalLink[ConsistencySubject]')
        params = TypeAliasType('params', 'MultiLinkWithProps[Constraint.__links__.params, Parameter]')


class Constraint(
    __Constraint_typeof__,
    CallableObject,
    InheritingObject,
    __gel_type_id__=UUID(int=195763951784768659695883964066391108399),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            inherited_fields: list[str] | None = None,
            bases: Iterable[InheritingObject] = [],
            ancestors: Iterable[InheritingObject] = [],
            return_typemod: __builtins__.str | None = None,
            params: Iterable[Parameter] = [],
            return_type: Type | None = None,
            expr: str | None = None,
            subjectexpr: str | None = None,
            finalexpr: str | None = None,
            errmessage: str | None = None,
            delegated: bool | None = None,
            except_expr: str | None = None,
            subject: ConsistencySubject | None = None,
        ) -> None:
            """Create a new schema::Constraint instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            return_typemod: type[TypeModifier] | UnspecifiedType = Unspecified,
            params: type[schema.Parameter] | UnspecifiedType = Unspecified,
            return_type: type[schema.Type] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            subjectexpr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            finalexpr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            errmessage: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            delegated: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            except_expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            subject: type[schema.ConsistencySubject] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Constraint instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            return_typemod: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[TypeModifier] | UnspecifiedType = Unspecified,
            params: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Parameter] | UnspecifiedType = Unspecified,
            return_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            subjectexpr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            finalexpr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            errmessage: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            delegated: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            except_expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            subject: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.ConsistencySubject] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Constraint instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            return_typemod: type[TypeModifier] | UnspecifiedType = Unspecified,
            params: type[schema.Parameter] | UnspecifiedType = Unspecified,
            return_type: type[schema.Type] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            subjectexpr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            finalexpr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            errmessage: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            delegated: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            except_expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            subject: type[schema.ConsistencySubject] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Constraint instances from the database.
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
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            subjectexpr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            finalexpr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            errmessage: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            delegated: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            except_expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        CallableObject.__variants__,
        InheritingObject.__variants__,
    ):
        class Base(
            __Constraint_typeof__,
            CallableObject.__variants__.Base,
            InheritingObject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    inherited_fields: list[str] | None = None,
                    bases: Iterable[InheritingObject] = [],
                    ancestors: Iterable[InheritingObject] = [],
                    return_typemod: __builtins__.str | None = None,
                    params: Iterable[Parameter] = [],
                    return_type: Type | None = None,
                    expr: str | None = None,
                    subjectexpr: str | None = None,
                    finalexpr: str | None = None,
                    errmessage: str | None = None,
                    delegated: bool | None = None,
                    except_expr: str | None = None,
                    subject: ConsistencySubject | None = None,
                ) -> None:
                    """Create a new schema::Constraint instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    return_typemod: type[TypeModifier] | UnspecifiedType = Unspecified,
                    params: type[schema.Parameter] | UnspecifiedType = Unspecified,
                    return_type: type[schema.Type] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    subjectexpr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    finalexpr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    errmessage: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    delegated: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    except_expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    subject: type[schema.ConsistencySubject] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Constraint instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    return_typemod: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[TypeModifier] | UnspecifiedType = Unspecified,
                    params: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Parameter] | UnspecifiedType = Unspecified,
                    return_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    subjectexpr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    finalexpr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    errmessage: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    delegated: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    except_expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    subject: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.ConsistencySubject] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Constraint instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    return_typemod: type[TypeModifier] | UnspecifiedType = Unspecified,
                    params: type[schema.Parameter] | UnspecifiedType = Unspecified,
                    return_type: type[schema.Type] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    subjectexpr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    finalexpr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    errmessage: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    delegated: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    except_expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    subject: type[schema.ConsistencySubject] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Constraint instances from the database.
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
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    subjectexpr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    finalexpr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    errmessage: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    delegated: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    except_expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Constraint | Base")
    class __links__(CallableObject.__links__, InheritingObject.__links__):
        if TYPE_CHECKING:
            class params(
                CallableObject.__links__.params,
                schema.Parameter,
                ProxyModel[schema.Parameter],
            ):
                """link schema::Constraint.params: schema::Parameter"""
                class __lprops__(CallableObject.__links__.params.__lprops__):
                    index: OptionalProperty[__std__.int64, __builtins_2__.int]
                    value: OptionalProperty[__std__.str, __builtins__.str]

                def __init__(
                    self,
                    obj: schema.Parameter,
                    /,
                    *,
                    index: __builtins_2__.int | None = None,
                    value: __builtins__.str | None = None,
                ) -> None:
                    ...

                @classmethod
                def link(
                    cls,
                    obj: schema.Parameter,
                    /,
                    *,
                    index: __builtins_2__.int | None = None,
                    value: __builtins__.str | None = None,
                ) -> Self:
                    ...

        if not TYPE_CHECKING:
            @LazyClassProperty[type]
            @classmethod
            def params(cls) -> type:
                class Constraint__params(
                    CallableObject.__links__.params,
                    __schema__.Parameter,
                    ProxyModel[__schema__.Parameter],
                ):
                    """link schema::Constraint.params: schema::Parameter"""
                    class __lprops__(
                        CallableObject.__links__.params.__lprops__,
                    ):
                        index: OptionalProperty[std.int64, __builtins_2__.int]
                        value: OptionalProperty[std.str, __builtins__.str]

                    def __init__(
                        self,
                        obj: __schema__.Parameter,
                        /,
                        *,
                        index: __builtins_2__.int | None = None,
                        value: __builtins__.str | None = None,
                    ) -> None:
                        ProxyModel.__init__(self, obj)
                        lprops = self.__class__.__lprops__(
                            index=index,
                            value=value,
                        )
                        object.__setattr__(self, "__linkprops__", lprops)

                    @classmethod
                    def link(
                        cls,
                        obj: __schema__.Parameter,
                        /,
                        *,
                        index: __builtins_2__.int | None = None,
                        value: __builtins__.str | None = None,
                    ) -> Self:
                        return cls(obj, index=index, value=value)

                Constraint__params.__name__ = 'params'
                Constraint__params.__qualname__ = 'Constraint.params'
                return Constraint__params

if not TYPE_CHECKING:
    Constraint.__variants__.Base = Constraint



#
# type schema::Index
#
class __Index_typeof__(
    __InheritingObject_typeof__,
    __AnnotationSubject_typeof__,
):
    class __gel_reflection__(
        __InheritingObject_typeof__.__gel_reflection__,
        __AnnotationSubject_typeof__.__gel_reflection__,
    ):
        id = UUID(int=296166827572358402527332524133223664279)
        name = SchemaPath('schema', 'Index')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=296166827572358402527332524133223664279),
                name='schema::Index',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __InheritingObject_typeof__.__typeof__,
        __AnnotationSubject_typeof__.__typeof__,
    ):
        expr = TypeAliasType('expr', 'OptionalProperty[std.str, str]')
        except_expr = TypeAliasType('except_expr', 'OptionalProperty[std.str, str]')
        deferrability = TypeAliasType('deferrability', 'OptionalProperty[IndexDeferrability, __builtins__.str]')
        deferred = TypeAliasType('deferred', 'OptionalProperty[std.bool, bool]')
        kwargs = TypeAliasType('kwargs', 'OptionalProperty[pydantic.Array[NameExpr_Tuple_9eMVFg], list[tuple[str, str]]]')
        params = TypeAliasType('params', 'MultiLinkWithProps[Index.__links__.params, Parameter]')


class Index(
    __Index_typeof__,
    InheritingObject,
    AnnotationSubject,
    __gel_type_id__=UUID(int=296166827572358402527332524133223664279),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            inherited_fields: list[str] | None = None,
            bases: Iterable[InheritingObject] = [],
            ancestors: Iterable[InheritingObject] = [],
            expr: str | None = None,
            except_expr: str | None = None,
            deferrability: __builtins__.str | None = None,
            deferred: bool | None = None,
            kwargs: list[tuple[str, str]] | None = None,
            params: Iterable[Parameter] = [],
        ) -> None:
            """Create a new schema::Index instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            except_expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            deferrability: type[IndexDeferrability] | UnspecifiedType = Unspecified,
            deferred: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            kwargs: type[pydantic.Array[std___types__.NameExpr_Tuple_9eMVFg]] | UnspecifiedType = Unspecified,
            params: type[schema.Parameter] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Index instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            except_expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            deferrability: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[IndexDeferrability] | UnspecifiedType = Unspecified,
            deferred: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            kwargs: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[std___types__.NameExpr_Tuple_9eMVFg]] | UnspecifiedType = Unspecified,
            params: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Parameter] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Index instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            except_expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            deferrability: type[IndexDeferrability] | UnspecifiedType = Unspecified,
            deferred: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            kwargs: type[pydantic.Array[std___types__.NameExpr_Tuple_9eMVFg]] | UnspecifiedType = Unspecified,
            params: type[schema.Parameter] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Index instances from the database.
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
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            except_expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            deferred: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        InheritingObject.__variants__,
        AnnotationSubject.__variants__,
    ):
        class Base(
            __Index_typeof__,
            InheritingObject.__variants__.Base,
            AnnotationSubject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    inherited_fields: list[str] | None = None,
                    bases: Iterable[InheritingObject] = [],
                    ancestors: Iterable[InheritingObject] = [],
                    expr: str | None = None,
                    except_expr: str | None = None,
                    deferrability: __builtins__.str | None = None,
                    deferred: bool | None = None,
                    kwargs: list[tuple[str, str]] | None = None,
                    params: Iterable[Parameter] = [],
                ) -> None:
                    """Create a new schema::Index instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    except_expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    deferrability: type[IndexDeferrability] | UnspecifiedType = Unspecified,
                    deferred: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    kwargs: type[pydantic.Array[std___types__.NameExpr_Tuple_9eMVFg]] | UnspecifiedType = Unspecified,
                    params: type[schema.Parameter] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Index instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    except_expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    deferrability: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[IndexDeferrability] | UnspecifiedType = Unspecified,
                    deferred: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    kwargs: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[std___types__.NameExpr_Tuple_9eMVFg]] | UnspecifiedType = Unspecified,
                    params: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Parameter] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Index instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    except_expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    deferrability: type[IndexDeferrability] | UnspecifiedType = Unspecified,
                    deferred: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    kwargs: type[pydantic.Array[std___types__.NameExpr_Tuple_9eMVFg]] | UnspecifiedType = Unspecified,
                    params: type[schema.Parameter] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Index instances from the database.
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
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    except_expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    deferred: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Index | Base")
    class __links__(InheritingObject.__links__, AnnotationSubject.__links__):
        if TYPE_CHECKING:
            class params(schema.Parameter, ProxyModel[schema.Parameter]):
                """link schema::Index.params: schema::Parameter"""
                class __lprops__(GelLinkModel):
                    index: OptionalProperty[__std__.int64, __builtins_2__.int]

                def __init__(
                    self,
                    obj: schema.Parameter,
                    /,
                    *,
                    index: __builtins_2__.int | None = None,
                ) -> None:
                    ...

                @classmethod
                def link(
                    cls,
                    obj: schema.Parameter,
                    /,
                    *,
                    index: __builtins_2__.int | None = None,
                ) -> Self:
                    ...

        if not TYPE_CHECKING:
            @LazyClassProperty[type]
            @classmethod
            def params(cls) -> type:
                class Index__params(
                    __schema__.Parameter,
                    ProxyModel[__schema__.Parameter],
                ):
                    """link schema::Index.params: schema::Parameter"""
                    class __lprops__(GelLinkModel):
                        index: OptionalProperty[std.int64, __builtins_2__.int]

                    def __init__(
                        self,
                        obj: __schema__.Parameter,
                        /,
                        *,
                        index: __builtins_2__.int | None = None,
                    ) -> None:
                        ProxyModel.__init__(self, obj)
                        lprops = self.__class__.__lprops__(index=index)
                        object.__setattr__(self, "__linkprops__", lprops)

                    @classmethod
                    def link(
                        cls,
                        obj: __schema__.Parameter,
                        /,
                        *,
                        index: __builtins_2__.int | None = None,
                    ) -> Self:
                        return cls(obj, index=index)

                Index__params.__name__ = 'params'
                Index__params.__qualname__ = 'Index.params'
                return Index__params

if not TYPE_CHECKING:
    Index.__variants__.Base = Index



#
# type schema::Rewrite
#
class __Rewrite_typeof__(
    __InheritingObject_typeof__,
    __AnnotationSubject_typeof__,
):
    class __gel_reflection__(
        __InheritingObject_typeof__.__gel_reflection__,
        __AnnotationSubject_typeof__.__gel_reflection__,
    ):
        id = UUID(int=284463082220370517579652730068569906415)
        name = SchemaPath('schema', 'Rewrite')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=284463082220370517579652730068569906415),
                name='schema::Rewrite',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __InheritingObject_typeof__.__typeof__,
        __AnnotationSubject_typeof__.__typeof__,
    ):
        kind = TypeAliasType('kind', 'TriggerKind')
        expr = TypeAliasType('expr', 'std.str')
        subject = TypeAliasType('subject', 'OptionalLink[Pointer]')


class Rewrite(
    __Rewrite_typeof__,
    InheritingObject,
    AnnotationSubject,
    __gel_type_id__=UUID(int=284463082220370517579652730068569906415),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            inherited_fields: list[str] | None = None,
            bases: Iterable[InheritingObject] = [],
            ancestors: Iterable[InheritingObject] = [],
            kind: __builtins__.str,
            expr: str,
            subject: Pointer | None = None,
        ) -> None:
            """Create a new schema::Rewrite instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            kind: type[TriggerKind] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            subject: type[schema.Pointer] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Rewrite instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            kind: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[TriggerKind] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            subject: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Pointer] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Rewrite instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            kind: type[TriggerKind] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            subject: type[schema.Pointer] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Rewrite instances from the database.
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
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        InheritingObject.__variants__,
        AnnotationSubject.__variants__,
    ):
        class Base(
            __Rewrite_typeof__,
            InheritingObject.__variants__.Base,
            AnnotationSubject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    inherited_fields: list[str] | None = None,
                    bases: Iterable[InheritingObject] = [],
                    ancestors: Iterable[InheritingObject] = [],
                    kind: __builtins__.str,
                    expr: str,
                    subject: Pointer | None = None,
                ) -> None:
                    """Create a new schema::Rewrite instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    kind: type[TriggerKind] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    subject: type[schema.Pointer] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Rewrite instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    kind: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[TriggerKind] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    subject: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Pointer] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Rewrite instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    kind: type[TriggerKind] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    subject: type[schema.Pointer] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Rewrite instances from the database.
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
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Rewrite | Base")
    class __links__(InheritingObject.__links__, AnnotationSubject.__links__):
        pass

if not TYPE_CHECKING:
    Rewrite.__variants__.Base = Rewrite



#
# type schema::Trigger
#
class __Trigger_typeof__(
    __InheritingObject_typeof__,
    __AnnotationSubject_typeof__,
):
    class __gel_reflection__(
        __InheritingObject_typeof__.__gel_reflection__,
        __AnnotationSubject_typeof__.__gel_reflection__,
    ):
        id = UUID(int=57756558562494904739428121894352067074)
        name = SchemaPath('schema', 'Trigger')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=57756558562494904739428121894352067074),
                name='schema::Trigger',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __InheritingObject_typeof__.__typeof__,
        __AnnotationSubject_typeof__.__typeof__,
    ):
        timing = TypeAliasType('timing', 'TriggerTiming')
        kinds = TypeAliasType('kinds', 'list[__builtins__.str]')
        scope = TypeAliasType('scope', 'TriggerScope')
        expr = TypeAliasType('expr', 'OptionalProperty[std.str, str]')
        condition = TypeAliasType('condition', 'OptionalProperty[std.str, str]')
        subject = TypeAliasType('subject', 'OptionalLink[ObjectType]')


class Trigger(
    __Trigger_typeof__,
    InheritingObject,
    AnnotationSubject,
    __gel_type_id__=UUID(int=57756558562494904739428121894352067074),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            inherited_fields: list[str] | None = None,
            bases: Iterable[InheritingObject] = [],
            ancestors: Iterable[InheritingObject] = [],
            timing: __builtins__.str,
            kinds: Iterable[__builtins__.str] = [],
            scope: __builtins__.str,
            expr: str | None = None,
            condition: str | None = None,
            subject: ObjectType | None = None,
        ) -> None:
            """Create a new schema::Trigger instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            timing: type[TriggerTiming] | UnspecifiedType = Unspecified,
            kinds: type[TriggerKind] | UnspecifiedType = Unspecified,
            scope: type[TriggerScope] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            condition: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            subject: type[schema.ObjectType] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Trigger instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            timing: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[TriggerTiming] | UnspecifiedType = Unspecified,
            kinds: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[TriggerKind] | UnspecifiedType = Unspecified,
            scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[TriggerScope] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            condition: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            subject: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.ObjectType] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Trigger instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            timing: type[TriggerTiming] | UnspecifiedType = Unspecified,
            kinds: type[TriggerKind] | UnspecifiedType = Unspecified,
            scope: type[TriggerScope] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            condition: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            subject: type[schema.ObjectType] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Trigger instances from the database.
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
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            condition: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        InheritingObject.__variants__,
        AnnotationSubject.__variants__,
    ):
        class Base(
            __Trigger_typeof__,
            InheritingObject.__variants__.Base,
            AnnotationSubject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    inherited_fields: list[str] | None = None,
                    bases: Iterable[InheritingObject] = [],
                    ancestors: Iterable[InheritingObject] = [],
                    timing: __builtins__.str,
                    kinds: Iterable[__builtins__.str] = [],
                    scope: __builtins__.str,
                    expr: str | None = None,
                    condition: str | None = None,
                    subject: ObjectType | None = None,
                ) -> None:
                    """Create a new schema::Trigger instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    timing: type[TriggerTiming] | UnspecifiedType = Unspecified,
                    kinds: type[TriggerKind] | UnspecifiedType = Unspecified,
                    scope: type[TriggerScope] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    condition: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    subject: type[schema.ObjectType] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Trigger instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    timing: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[TriggerTiming] | UnspecifiedType = Unspecified,
                    kinds: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[TriggerKind] | UnspecifiedType = Unspecified,
                    scope: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[TriggerScope] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    condition: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    subject: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.ObjectType] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Trigger instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    timing: type[TriggerTiming] | UnspecifiedType = Unspecified,
                    kinds: type[TriggerKind] | UnspecifiedType = Unspecified,
                    scope: type[TriggerScope] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    condition: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    subject: type[schema.ObjectType] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Trigger instances from the database.
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
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    condition: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Trigger | Base")
    class __links__(InheritingObject.__links__, AnnotationSubject.__links__):
        pass

if not TYPE_CHECKING:
    Trigger.__variants__.Base = Trigger



#
# type schema::PrimitiveType
#
class __PrimitiveType_typeof__(__Type_typeof__):
    class __gel_reflection__(__Type_typeof__.__gel_reflection__):
        id = UUID(int=289974081693672082889864807229328348553)
        name = SchemaPath('schema', 'PrimitiveType')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=289974081693672082889864807229328348553),
                name='schema::PrimitiveType',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__(__Type_typeof__.__typeof__):
        pass


class PrimitiveType(
    __PrimitiveType_typeof__,
    Type,
    __gel_type_id__=UUID(int=289974081693672082889864807229328348553),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            expr: str | None = None,
            from_alias: bool | None = None,
        ) -> None:
            """Create a new schema::PrimitiveType instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::PrimitiveType instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::PrimitiveType instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::PrimitiveType instances from the database.
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
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(Type.__variants__):
        class Base(__PrimitiveType_typeof__, Type.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    expr: str | None = None,
                    from_alias: bool | None = None,
                ) -> None:
                    """Create a new schema::PrimitiveType instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::PrimitiveType instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::PrimitiveType instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::PrimitiveType instances from the database.
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
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="PrimitiveType | Base")
    class __links__(Type.__links__):
        pass

if not TYPE_CHECKING:
    PrimitiveType.__variants__.Base = PrimitiveType



#
# type schema::PseudoType
#
class __PseudoType_typeof__(__InheritingObject_typeof__, __Type_typeof__):
    class __gel_reflection__(
        __InheritingObject_typeof__.__gel_reflection__,
        __Type_typeof__.__gel_reflection__,
    ):
        id = UUID(int=11246368220525712114260003057526016480)
        name = SchemaPath('schema', 'PseudoType')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=11246368220525712114260003057526016480),
                name='schema::PseudoType',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __InheritingObject_typeof__.__typeof__,
        __Type_typeof__.__typeof__,
    ):
        pass


class PseudoType(
    __PseudoType_typeof__,
    InheritingObject,
    Type,
    __gel_type_id__=UUID(int=11246368220525712114260003057526016480),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            expr: str | None = None,
            from_alias: bool | None = None,
            inherited_fields: list[str] | None = None,
            bases: Iterable[InheritingObject] = [],
            ancestors: Iterable[InheritingObject] = [],
        ) -> None:
            """Create a new schema::PseudoType instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::PseudoType instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::PseudoType instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::PseudoType instances from the database.
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
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(InheritingObject.__variants__, Type.__variants__):
        class Base(
            __PseudoType_typeof__,
            InheritingObject.__variants__.Base,
            Type.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    expr: str | None = None,
                    from_alias: bool | None = None,
                    inherited_fields: list[str] | None = None,
                    bases: Iterable[InheritingObject] = [],
                    ancestors: Iterable[InheritingObject] = [],
                ) -> None:
                    """Create a new schema::PseudoType instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::PseudoType instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::PseudoType instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::PseudoType instances from the database.
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
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="PseudoType | Base")
    class __links__(InheritingObject.__links__, Type.__links__):
        pass

if not TYPE_CHECKING:
    PseudoType.__variants__.Base = PseudoType



#
# type schema::ObjectType
#
class __ObjectType_typeof__(
    __Source_typeof__,
    __ConsistencySubject_typeof__,
    __InheritingObject_typeof__,
    __Type_typeof__,
    __AnnotationSubject_typeof__,
):
    class __gel_reflection__(
        __Source_typeof__.__gel_reflection__,
        __ConsistencySubject_typeof__.__gel_reflection__,
        __InheritingObject_typeof__.__gel_reflection__,
        __Type_typeof__.__gel_reflection__,
        __AnnotationSubject_typeof__.__gel_reflection__,
    ):
        id = UUID(int=51022788685504552606682066082628014243)
        name = SchemaPath('schema', 'ObjectType')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=51022788685504552606682066082628014243),
                name='schema::ObjectType',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __Source_typeof__.__typeof__,
        __ConsistencySubject_typeof__.__typeof__,
        __InheritingObject_typeof__.__typeof__,
        __Type_typeof__.__typeof__,
        __AnnotationSubject_typeof__.__typeof__,
    ):
        compound_type = TypeAliasType('compound_type', 'ComputedProperty[std.bool, bool]')
        is_compound_type = TypeAliasType('is_compound_type', 'ComputedProperty[std.bool, bool]')
        union_of = TypeAliasType('union_of', 'MultiLink[ObjectType]')
        intersection_of = TypeAliasType('intersection_of', 'MultiLink[ObjectType]')
        links = TypeAliasType('links', 'ComputedMultiLink[Link]')
        properties = TypeAliasType('properties', 'ComputedMultiLink[Property]')
        access_policies = TypeAliasType('access_policies', 'MultiLinkWithProps[ObjectType.__links__.access_policies, AccessPolicy]')
        triggers = TypeAliasType('triggers', 'MultiLinkWithProps[ObjectType.__links__.triggers, Trigger]')


class ObjectType(
    __ObjectType_typeof__,
    Source,
    ConsistencySubject,
    InheritingObject,
    Type,
    AnnotationSubject,
    __gel_type_id__=UUID(int=51022788685504552606682066082628014243),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            expr: str | None = None,
            from_alias: bool | None = None,
            inherited_fields: list[str] | None = None,
            bases: Iterable[InheritingObject] = [],
            ancestors: Iterable[InheritingObject] = [],
            constraints: Iterable[Constraint] = [],
            pointers: Iterable[Pointer] = [],
            indexes: Iterable[Index] = [],
            compound_type: bool,
            union_of: Iterable[ObjectType] = [],
            intersection_of: Iterable[ObjectType] = [],
            links: Iterable[Link] = [],
            properties: Iterable[Property] = [],
            access_policies: Iterable[AccessPolicy] = [],
            triggers: Iterable[Trigger] = [],
        ) -> None:
            """Create a new schema::ObjectType instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
            pointers: type[schema.Pointer] | UnspecifiedType = Unspecified,
            indexes: type[schema.Index] | UnspecifiedType = Unspecified,
            union_of: type[schema.ObjectType] | UnspecifiedType = Unspecified,
            intersection_of: type[schema.ObjectType] | UnspecifiedType = Unspecified,
            access_policies: type[schema.AccessPolicy] | UnspecifiedType = Unspecified,
            triggers: type[schema.Trigger] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::ObjectType instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            constraints: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Constraint] | UnspecifiedType = Unspecified,
            pointers: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Pointer] | UnspecifiedType = Unspecified,
            indexes: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Index] | UnspecifiedType = Unspecified,
            compound_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            union_of: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.ObjectType] | UnspecifiedType = Unspecified,
            intersection_of: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.ObjectType] | UnspecifiedType = Unspecified,
            links: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Link] | UnspecifiedType = Unspecified,
            properties: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Property] | UnspecifiedType = Unspecified,
            access_policies: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.AccessPolicy] | UnspecifiedType = Unspecified,
            triggers: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Trigger] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::ObjectType instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
            pointers: type[schema.Pointer] | UnspecifiedType = Unspecified,
            indexes: type[schema.Index] | UnspecifiedType = Unspecified,
            compound_type: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            union_of: type[schema.ObjectType] | UnspecifiedType = Unspecified,
            intersection_of: type[schema.ObjectType] | UnspecifiedType = Unspecified,
            links: type[schema.Link] | UnspecifiedType = Unspecified,
            properties: type[schema.Property] | UnspecifiedType = Unspecified,
            access_policies: type[schema.AccessPolicy] | UnspecifiedType = Unspecified,
            triggers: type[schema.Trigger] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::ObjectType instances from the database.
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
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            compound_type: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...

    if not TYPE_CHECKING:
        def __init__(self, /, **kwargs: Any) -> None:
            _id = kwargs.pop("id", None)
            super().__init__(**kwargs)
            object.__setattr__(self, "id", _id)


    class __variants__(
        Source.__variants__,
        ConsistencySubject.__variants__,
        InheritingObject.__variants__,
        Type.__variants__,
        AnnotationSubject.__variants__,
    ):
        class Base(
            __ObjectType_typeof__,
            Source.__variants__.Base,
            ConsistencySubject.__variants__.Base,
            InheritingObject.__variants__.Base,
            Type.__variants__.Base,
            AnnotationSubject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    expr: str | None = None,
                    from_alias: bool | None = None,
                    inherited_fields: list[str] | None = None,
                    bases: Iterable[InheritingObject] = [],
                    ancestors: Iterable[InheritingObject] = [],
                    constraints: Iterable[Constraint] = [],
                    pointers: Iterable[Pointer] = [],
                    indexes: Iterable[Index] = [],
                    compound_type: bool,
                    union_of: Iterable[ObjectType] = [],
                    intersection_of: Iterable[ObjectType] = [],
                    links: Iterable[Link] = [],
                    properties: Iterable[Property] = [],
                    access_policies: Iterable[AccessPolicy] = [],
                    triggers: Iterable[Trigger] = [],
                ) -> None:
                    """Create a new schema::ObjectType instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
                    pointers: type[schema.Pointer] | UnspecifiedType = Unspecified,
                    indexes: type[schema.Index] | UnspecifiedType = Unspecified,
                    union_of: type[schema.ObjectType] | UnspecifiedType = Unspecified,
                    intersection_of: type[schema.ObjectType] | UnspecifiedType = Unspecified,
                    access_policies: type[schema.AccessPolicy] | UnspecifiedType = Unspecified,
                    triggers: type[schema.Trigger] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::ObjectType instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    constraints: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Constraint] | UnspecifiedType = Unspecified,
                    pointers: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Pointer] | UnspecifiedType = Unspecified,
                    indexes: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Index] | UnspecifiedType = Unspecified,
                    compound_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    union_of: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.ObjectType] | UnspecifiedType = Unspecified,
                    intersection_of: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.ObjectType] | UnspecifiedType = Unspecified,
                    links: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Link] | UnspecifiedType = Unspecified,
                    properties: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Property] | UnspecifiedType = Unspecified,
                    access_policies: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.AccessPolicy] | UnspecifiedType = Unspecified,
                    triggers: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Trigger] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::ObjectType instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
                    pointers: type[schema.Pointer] | UnspecifiedType = Unspecified,
                    indexes: type[schema.Index] | UnspecifiedType = Unspecified,
                    compound_type: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    union_of: type[schema.ObjectType] | UnspecifiedType = Unspecified,
                    intersection_of: type[schema.ObjectType] | UnspecifiedType = Unspecified,
                    links: type[schema.Link] | UnspecifiedType = Unspecified,
                    properties: type[schema.Property] | UnspecifiedType = Unspecified,
                    access_policies: type[schema.AccessPolicy] | UnspecifiedType = Unspecified,
                    triggers: type[schema.Trigger] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::ObjectType instances from the database.
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
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    compound_type: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...

            if not TYPE_CHECKING:
                def __init__(self, /, **kwargs: Any) -> None:
                    _id = kwargs.pop("id", None)
                    super().__init__(**kwargs)
                    object.__setattr__(self, "id", _id)


        Any = TypeVar("Any", bound="ObjectType | Base")
    class __links__(
        Source.__links__,
        ConsistencySubject.__links__,
        InheritingObject.__links__,
        Type.__links__,
        AnnotationSubject.__links__,
    ):
        if TYPE_CHECKING:
            class access_policies(
                schema.AccessPolicy,
                ProxyModel[schema.AccessPolicy],
            ):
                """link schema::ObjectType.access_policies: schema::AccessPolicy"""
                class __lprops__(GelLinkModel):
                    owned: OptionalProperty[__std__.bool, __builtins_1__.bool]
                    is_owned: OptionalProperty[__std__.bool, __builtins_1__.bool]

                def __init__(
                    self,
                    obj: schema.AccessPolicy,
                    /,
                    *,
                    owned: __builtins_1__.bool | None = None,
                    is_owned: __builtins_1__.bool | None = None,
                ) -> None:
                    ...

                @classmethod
                def link(
                    cls,
                    obj: schema.AccessPolicy,
                    /,
                    *,
                    owned: __builtins_1__.bool | None = None,
                    is_owned: __builtins_1__.bool | None = None,
                ) -> Self:
                    ...

            class triggers(schema.Trigger, ProxyModel[schema.Trigger]):
                """link schema::ObjectType.triggers: schema::Trigger"""
                class __lprops__(GelLinkModel):
                    owned: OptionalProperty[__std__.bool, __builtins_1__.bool]
                    is_owned: OptionalProperty[__std__.bool, __builtins_1__.bool]

                def __init__(
                    self,
                    obj: schema.Trigger,
                    /,
                    *,
                    owned: __builtins_1__.bool | None = None,
                    is_owned: __builtins_1__.bool | None = None,
                ) -> None:
                    ...

                @classmethod
                def link(
                    cls,
                    obj: schema.Trigger,
                    /,
                    *,
                    owned: __builtins_1__.bool | None = None,
                    is_owned: __builtins_1__.bool | None = None,
                ) -> Self:
                    ...

        if not TYPE_CHECKING:
            @LazyClassProperty[type]
            @classmethod
            def access_policies(cls) -> type:
                class ObjectType__access_policies(
                    __schema__.AccessPolicy,
                    ProxyModel[__schema__.AccessPolicy],
                ):
                    """link schema::ObjectType.access_policies: schema::AccessPolicy"""
                    class __lprops__(GelLinkModel):
                        owned: OptionalProperty[std.bool, __builtins_1__.bool]
                        is_owned: OptionalProperty[std.bool, __builtins_1__.bool]

                    def __init__(
                        self,
                        obj: __schema__.AccessPolicy,
                        /,
                        *,
                        owned: __builtins_1__.bool | None = None,
                        is_owned: __builtins_1__.bool | None = None,
                    ) -> None:
                        ProxyModel.__init__(self, obj)
                        lprops = self.__class__.__lprops__(
                            owned=owned,
                            is_owned=is_owned,
                        )
                        object.__setattr__(self, "__linkprops__", lprops)

                    @classmethod
                    def link(
                        cls,
                        obj: __schema__.AccessPolicy,
                        /,
                        *,
                        owned: __builtins_1__.bool | None = None,
                        is_owned: __builtins_1__.bool | None = None,
                    ) -> Self:
                        return cls(obj, owned=owned, is_owned=is_owned)

                ObjectType__access_policies.__name__ = 'access_policies'
                ObjectType__access_policies.__qualname__ = 'ObjectType.access_policies'
                return ObjectType__access_policies
            @LazyClassProperty[type]
            @classmethod
            def triggers(cls) -> type:
                class ObjectType__triggers(
                    __schema__.Trigger,
                    ProxyModel[__schema__.Trigger],
                ):
                    """link schema::ObjectType.triggers: schema::Trigger"""
                    class __lprops__(GelLinkModel):
                        owned: OptionalProperty[std.bool, __builtins_1__.bool]
                        is_owned: OptionalProperty[std.bool, __builtins_1__.bool]

                    def __init__(
                        self,
                        obj: __schema__.Trigger,
                        /,
                        *,
                        owned: __builtins_1__.bool | None = None,
                        is_owned: __builtins_1__.bool | None = None,
                    ) -> None:
                        ProxyModel.__init__(self, obj)
                        lprops = self.__class__.__lprops__(
                            owned=owned,
                            is_owned=is_owned,
                        )
                        object.__setattr__(self, "__linkprops__", lprops)

                    @classmethod
                    def link(
                        cls,
                        obj: __schema__.Trigger,
                        /,
                        *,
                        owned: __builtins_1__.bool | None = None,
                        is_owned: __builtins_1__.bool | None = None,
                    ) -> Self:
                        return cls(obj, owned=owned, is_owned=is_owned)

                ObjectType__triggers.__name__ = 'triggers'
                ObjectType__triggers.__qualname__ = 'ObjectType.triggers'
                return ObjectType__triggers

if not TYPE_CHECKING:
    ObjectType.__variants__.Base = ObjectType



#
# type schema::Pointer
#
class __Pointer_typeof__(
    __ConsistencySubject_typeof__,
    __AnnotationSubject_typeof__,
):
    class __gel_reflection__(
        __ConsistencySubject_typeof__.__gel_reflection__,
        __AnnotationSubject_typeof__.__gel_reflection__,
    ):
        id = UUID(int=116815132430841301909180054634293237411)
        name = SchemaPath('schema', 'Pointer')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=116815132430841301909180054634293237411),
                name='schema::Pointer',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __ConsistencySubject_typeof__.__typeof__,
        __AnnotationSubject_typeof__.__typeof__,
    ):
        cardinality = TypeAliasType('cardinality', 'OptionalProperty[Cardinality, __builtins__.str]')
        required = TypeAliasType('required', 'OptionalProperty[std.bool, bool]')
        readonly = TypeAliasType('readonly', 'OptionalProperty[std.bool, bool]')
        default = TypeAliasType('default', 'OptionalProperty[std.str, str]')
        expr = TypeAliasType('expr', 'OptionalProperty[std.str, str]')
        secret = TypeAliasType('secret', 'OptionalProperty[std.bool, bool]')
        source = TypeAliasType('source', 'OptionalLink[Source]')
        target = TypeAliasType('target', 'OptionalLink[Type]')
        rewrites = TypeAliasType('rewrites', 'MultiLinkWithProps[Pointer.__links__.rewrites, Rewrite]')


class Pointer(
    __Pointer_typeof__,
    ConsistencySubject,
    AnnotationSubject,
    __gel_type_id__=UUID(int=116815132430841301909180054634293237411),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            inherited_fields: list[str] | None = None,
            bases: Iterable[InheritingObject] = [],
            ancestors: Iterable[InheritingObject] = [],
            constraints: Iterable[Constraint] = [],
            cardinality: __builtins__.str | None = None,
            required: bool | None = None,
            readonly: bool | None = None,
            default: str | None = None,
            expr: str | None = None,
            secret: bool | None = None,
            source: Source | None = None,
            target: Type | None = None,
            rewrites: Iterable[Rewrite] = [],
        ) -> None:
            """Create a new schema::Pointer instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
            cardinality: type[Cardinality] | UnspecifiedType = Unspecified,
            required: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            readonly: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            source: type[schema.Source] | UnspecifiedType = Unspecified,
            target: type[schema.Type] | UnspecifiedType = Unspecified,
            rewrites: type[schema.Rewrite] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Pointer instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            constraints: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Constraint] | UnspecifiedType = Unspecified,
            cardinality: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Cardinality] | UnspecifiedType = Unspecified,
            required: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            readonly: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            default: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            source: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Source] | UnspecifiedType = Unspecified,
            target: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
            rewrites: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Rewrite] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Pointer instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
            cardinality: type[Cardinality] | UnspecifiedType = Unspecified,
            required: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            readonly: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            source: type[schema.Source] | UnspecifiedType = Unspecified,
            target: type[schema.Type] | UnspecifiedType = Unspecified,
            rewrites: type[schema.Rewrite] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Pointer instances from the database.
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
            required: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            readonly: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            default: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        ConsistencySubject.__variants__,
        AnnotationSubject.__variants__,
    ):
        class Base(
            __Pointer_typeof__,
            ConsistencySubject.__variants__.Base,
            AnnotationSubject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    inherited_fields: list[str] | None = None,
                    bases: Iterable[InheritingObject] = [],
                    ancestors: Iterable[InheritingObject] = [],
                    constraints: Iterable[Constraint] = [],
                    cardinality: __builtins__.str | None = None,
                    required: bool | None = None,
                    readonly: bool | None = None,
                    default: str | None = None,
                    expr: str | None = None,
                    secret: bool | None = None,
                    source: Source | None = None,
                    target: Type | None = None,
                    rewrites: Iterable[Rewrite] = [],
                ) -> None:
                    """Create a new schema::Pointer instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
                    cardinality: type[Cardinality] | UnspecifiedType = Unspecified,
                    required: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    readonly: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    source: type[schema.Source] | UnspecifiedType = Unspecified,
                    target: type[schema.Type] | UnspecifiedType = Unspecified,
                    rewrites: type[schema.Rewrite] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Pointer instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    constraints: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Constraint] | UnspecifiedType = Unspecified,
                    cardinality: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Cardinality] | UnspecifiedType = Unspecified,
                    required: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    readonly: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    default: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    source: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Source] | UnspecifiedType = Unspecified,
                    target: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
                    rewrites: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Rewrite] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Pointer instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
                    cardinality: type[Cardinality] | UnspecifiedType = Unspecified,
                    required: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    readonly: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    source: type[schema.Source] | UnspecifiedType = Unspecified,
                    target: type[schema.Type] | UnspecifiedType = Unspecified,
                    rewrites: type[schema.Rewrite] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Pointer instances from the database.
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
                    required: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    readonly: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    default: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Pointer | Base")
    class __links__(ConsistencySubject.__links__, AnnotationSubject.__links__):
        if TYPE_CHECKING:
            class rewrites(schema.Rewrite, ProxyModel[schema.Rewrite]):
                """link schema::Pointer.rewrites: schema::Rewrite"""
                class __lprops__(GelLinkModel):
                    owned: OptionalProperty[__std__.bool, __builtins_1__.bool]
                    is_owned: OptionalProperty[__std__.bool, __builtins_1__.bool]

                def __init__(
                    self,
                    obj: schema.Rewrite,
                    /,
                    *,
                    owned: __builtins_1__.bool | None = None,
                    is_owned: __builtins_1__.bool | None = None,
                ) -> None:
                    ...

                @classmethod
                def link(
                    cls,
                    obj: schema.Rewrite,
                    /,
                    *,
                    owned: __builtins_1__.bool | None = None,
                    is_owned: __builtins_1__.bool | None = None,
                ) -> Self:
                    ...

        if not TYPE_CHECKING:
            @LazyClassProperty[type]
            @classmethod
            def rewrites(cls) -> type:
                class Pointer__rewrites(
                    __schema__.Rewrite,
                    ProxyModel[__schema__.Rewrite],
                ):
                    """link schema::Pointer.rewrites: schema::Rewrite"""
                    class __lprops__(GelLinkModel):
                        owned: OptionalProperty[std.bool, __builtins_1__.bool]
                        is_owned: OptionalProperty[std.bool, __builtins_1__.bool]

                    def __init__(
                        self,
                        obj: __schema__.Rewrite,
                        /,
                        *,
                        owned: __builtins_1__.bool | None = None,
                        is_owned: __builtins_1__.bool | None = None,
                    ) -> None:
                        ProxyModel.__init__(self, obj)
                        lprops = self.__class__.__lprops__(
                            owned=owned,
                            is_owned=is_owned,
                        )
                        object.__setattr__(self, "__linkprops__", lprops)

                    @classmethod
                    def link(
                        cls,
                        obj: __schema__.Rewrite,
                        /,
                        *,
                        owned: __builtins_1__.bool | None = None,
                        is_owned: __builtins_1__.bool | None = None,
                    ) -> Self:
                        return cls(obj, owned=owned, is_owned=is_owned)

                Pointer__rewrites.__name__ = 'rewrites'
                Pointer__rewrites.__qualname__ = 'Pointer.rewrites'
                return Pointer__rewrites

if not TYPE_CHECKING:
    Pointer.__variants__.Base = Pointer



#
# type schema::CollectionType
#
class __CollectionType_typeof__(__PrimitiveType_typeof__):
    class __gel_reflection__(__PrimitiveType_typeof__.__gel_reflection__):
        id = UUID(int=302606025822407465695339097537067301001)
        name = SchemaPath('schema', 'CollectionType')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=302606025822407465695339097537067301001),
                name='schema::CollectionType',
                builtin=True,
                internal=False,
                abstract=True,
                final=False,
                compound_type=False,
            )

    class __typeof__(__PrimitiveType_typeof__.__typeof__):
        pass


class CollectionType(
    __CollectionType_typeof__,
    PrimitiveType,
    __gel_type_id__=UUID(int=302606025822407465695339097537067301001),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            expr: str | None = None,
            from_alias: bool | None = None,
        ) -> None:
            """Create a new schema::CollectionType instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::CollectionType instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::CollectionType instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::CollectionType instances from the database.
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
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(PrimitiveType.__variants__):
        class Base(__CollectionType_typeof__, PrimitiveType.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    expr: str | None = None,
                    from_alias: bool | None = None,
                ) -> None:
                    """Create a new schema::CollectionType instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::CollectionType instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::CollectionType instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::CollectionType instances from the database.
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
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="CollectionType | Base")
    class __links__(PrimitiveType.__links__):
        pass

if not TYPE_CHECKING:
    CollectionType.__variants__.Base = CollectionType



#
# type schema::ScalarType
#
class __ScalarType_typeof__(
    __PrimitiveType_typeof__,
    __ConsistencySubject_typeof__,
    __AnnotationSubject_typeof__,
):
    class __gel_reflection__(
        __PrimitiveType_typeof__.__gel_reflection__,
        __ConsistencySubject_typeof__.__gel_reflection__,
        __AnnotationSubject_typeof__.__gel_reflection__,
    ):
        id = UUID(int=276925256413372055258128037770702872862)
        name = SchemaPath('schema', 'ScalarType')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=276925256413372055258128037770702872862),
                name='schema::ScalarType',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __PrimitiveType_typeof__.__typeof__,
        __ConsistencySubject_typeof__.__typeof__,
        __AnnotationSubject_typeof__.__typeof__,
    ):
        default = TypeAliasType('default', 'OptionalProperty[std.str, str]')
        enum_values = TypeAliasType('enum_values', 'OptionalProperty[pydantic.Array[std.str], list[str]]')
        arg_values = TypeAliasType('arg_values', 'OptionalProperty[pydantic.Array[std.str], list[str]]')


class ScalarType(
    __ScalarType_typeof__,
    PrimitiveType,
    ConsistencySubject,
    AnnotationSubject,
    __gel_type_id__=UUID(int=276925256413372055258128037770702872862),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            expr: str | None = None,
            from_alias: bool | None = None,
            inherited_fields: list[str] | None = None,
            bases: Iterable[InheritingObject] = [],
            ancestors: Iterable[InheritingObject] = [],
            constraints: Iterable[Constraint] = [],
            default: str | None = None,
            enum_values: list[str] | None = None,
            arg_values: list[str] | None = None,
        ) -> None:
            """Create a new schema::ScalarType instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
            default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            enum_values: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            arg_values: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::ScalarType instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            constraints: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Constraint] | UnspecifiedType = Unspecified,
            default: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            enum_values: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            arg_values: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::ScalarType instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
            default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            enum_values: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            arg_values: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::ScalarType instances from the database.
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
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            default: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(
        PrimitiveType.__variants__,
        ConsistencySubject.__variants__,
        AnnotationSubject.__variants__,
    ):
        class Base(
            __ScalarType_typeof__,
            PrimitiveType.__variants__.Base,
            ConsistencySubject.__variants__.Base,
            AnnotationSubject.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    expr: str | None = None,
                    from_alias: bool | None = None,
                    inherited_fields: list[str] | None = None,
                    bases: Iterable[InheritingObject] = [],
                    ancestors: Iterable[InheritingObject] = [],
                    constraints: Iterable[Constraint] = [],
                    default: str | None = None,
                    enum_values: list[str] | None = None,
                    arg_values: list[str] | None = None,
                ) -> None:
                    """Create a new schema::ScalarType instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
                    default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    enum_values: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    arg_values: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::ScalarType instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    constraints: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Constraint] | UnspecifiedType = Unspecified,
                    default: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    enum_values: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    arg_values: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::ScalarType instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
                    default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    enum_values: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    arg_values: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::ScalarType instances from the database.
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
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    default: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="ScalarType | Base")
    class __links__(
        PrimitiveType.__links__,
        ConsistencySubject.__links__,
        AnnotationSubject.__links__,
    ):
        pass

if not TYPE_CHECKING:
    ScalarType.__variants__.Base = ScalarType



#
# type schema::Link
#
class __Link_typeof__(__Pointer_typeof__, __Source_typeof__):
    class __gel_reflection__(
        __Pointer_typeof__.__gel_reflection__,
        __Source_typeof__.__gel_reflection__,
    ):
        id = UUID(int=203363928536405864267916671259475739976)
        name = SchemaPath('schema', 'Link')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=203363928536405864267916671259475739976),
                name='schema::Link',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(
        __Pointer_typeof__.__typeof__,
        __Source_typeof__.__typeof__,
    ):
        on_target_delete = TypeAliasType('on_target_delete', 'OptionalProperty[TargetDeleteAction, __builtins__.str]')
        on_source_delete = TypeAliasType('on_source_delete', 'OptionalProperty[SourceDeleteAction, __builtins__.str]')
        target = TypeAliasType('target', 'OptionalLink[ObjectType]')
        properties = TypeAliasType('properties', 'ComputedMultiLink[Property]')


class Link(
    __Link_typeof__,
    Pointer,
    Source,
    __gel_type_id__=UUID(int=203363928536405864267916671259475739976),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            inherited_fields: list[str] | None = None,
            bases: Iterable[InheritingObject] = [],
            ancestors: Iterable[InheritingObject] = [],
            pointers: Iterable[Pointer] = [],
            indexes: Iterable[Index] = [],
            constraints: Iterable[Constraint] = [],
            cardinality: __builtins__.str | None = None,
            required: bool | None = None,
            readonly: bool | None = None,
            default: str | None = None,
            expr: str | None = None,
            secret: bool | None = None,
            source: Source | None = None,
            target: ObjectType | None = None,
            rewrites: Iterable[Rewrite] = [],
            on_target_delete: __builtins__.str | None = None,
            on_source_delete: __builtins__.str | None = None,
            properties: Iterable[Property] = [],
        ) -> None:
            """Create a new schema::Link instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            pointers: type[schema.Pointer] | UnspecifiedType = Unspecified,
            indexes: type[schema.Index] | UnspecifiedType = Unspecified,
            constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
            cardinality: type[Cardinality] | UnspecifiedType = Unspecified,
            required: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            readonly: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            source: type[schema.Source] | UnspecifiedType = Unspecified,
            target: type[schema.ObjectType] | UnspecifiedType = Unspecified,
            rewrites: type[schema.Rewrite] | UnspecifiedType = Unspecified,
            on_target_delete: type[TargetDeleteAction] | UnspecifiedType = Unspecified,
            on_source_delete: type[SourceDeleteAction] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Link instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            pointers: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Pointer] | UnspecifiedType = Unspecified,
            indexes: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Index] | UnspecifiedType = Unspecified,
            constraints: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Constraint] | UnspecifiedType = Unspecified,
            cardinality: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Cardinality] | UnspecifiedType = Unspecified,
            required: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            readonly: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            default: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            source: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Source] | UnspecifiedType = Unspecified,
            target: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.ObjectType] | UnspecifiedType = Unspecified,
            rewrites: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Rewrite] | UnspecifiedType = Unspecified,
            on_target_delete: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[TargetDeleteAction] | UnspecifiedType = Unspecified,
            on_source_delete: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[SourceDeleteAction] | UnspecifiedType = Unspecified,
            properties: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Property] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Link instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            pointers: type[schema.Pointer] | UnspecifiedType = Unspecified,
            indexes: type[schema.Index] | UnspecifiedType = Unspecified,
            constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
            cardinality: type[Cardinality] | UnspecifiedType = Unspecified,
            required: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            readonly: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            source: type[schema.Source] | UnspecifiedType = Unspecified,
            target: type[schema.ObjectType] | UnspecifiedType = Unspecified,
            rewrites: type[schema.Rewrite] | UnspecifiedType = Unspecified,
            on_target_delete: type[TargetDeleteAction] | UnspecifiedType = Unspecified,
            on_source_delete: type[SourceDeleteAction] | UnspecifiedType = Unspecified,
            properties: type[schema.Property] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Link instances from the database.
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
            required: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            readonly: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            default: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(Pointer.__variants__, Source.__variants__):
        class Base(
            __Link_typeof__,
            Pointer.__variants__.Base,
            Source.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    inherited_fields: list[str] | None = None,
                    bases: Iterable[InheritingObject] = [],
                    ancestors: Iterable[InheritingObject] = [],
                    pointers: Iterable[Pointer] = [],
                    indexes: Iterable[Index] = [],
                    constraints: Iterable[Constraint] = [],
                    cardinality: __builtins__.str | None = None,
                    required: bool | None = None,
                    readonly: bool | None = None,
                    default: str | None = None,
                    expr: str | None = None,
                    secret: bool | None = None,
                    source: Source | None = None,
                    target: ObjectType | None = None,
                    rewrites: Iterable[Rewrite] = [],
                    on_target_delete: __builtins__.str | None = None,
                    on_source_delete: __builtins__.str | None = None,
                    properties: Iterable[Property] = [],
                ) -> None:
                    """Create a new schema::Link instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    pointers: type[schema.Pointer] | UnspecifiedType = Unspecified,
                    indexes: type[schema.Index] | UnspecifiedType = Unspecified,
                    constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
                    cardinality: type[Cardinality] | UnspecifiedType = Unspecified,
                    required: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    readonly: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    source: type[schema.Source] | UnspecifiedType = Unspecified,
                    target: type[schema.ObjectType] | UnspecifiedType = Unspecified,
                    rewrites: type[schema.Rewrite] | UnspecifiedType = Unspecified,
                    on_target_delete: type[TargetDeleteAction] | UnspecifiedType = Unspecified,
                    on_source_delete: type[SourceDeleteAction] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Link instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    pointers: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Pointer] | UnspecifiedType = Unspecified,
                    indexes: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Index] | UnspecifiedType = Unspecified,
                    constraints: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Constraint] | UnspecifiedType = Unspecified,
                    cardinality: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Cardinality] | UnspecifiedType = Unspecified,
                    required: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    readonly: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    default: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    source: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Source] | UnspecifiedType = Unspecified,
                    target: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.ObjectType] | UnspecifiedType = Unspecified,
                    rewrites: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Rewrite] | UnspecifiedType = Unspecified,
                    on_target_delete: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[TargetDeleteAction] | UnspecifiedType = Unspecified,
                    on_source_delete: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[SourceDeleteAction] | UnspecifiedType = Unspecified,
                    properties: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Property] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Link instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    pointers: type[schema.Pointer] | UnspecifiedType = Unspecified,
                    indexes: type[schema.Index] | UnspecifiedType = Unspecified,
                    constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
                    cardinality: type[Cardinality] | UnspecifiedType = Unspecified,
                    required: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    readonly: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    source: type[schema.Source] | UnspecifiedType = Unspecified,
                    target: type[schema.ObjectType] | UnspecifiedType = Unspecified,
                    rewrites: type[schema.Rewrite] | UnspecifiedType = Unspecified,
                    on_target_delete: type[TargetDeleteAction] | UnspecifiedType = Unspecified,
                    on_source_delete: type[SourceDeleteAction] | UnspecifiedType = Unspecified,
                    properties: type[schema.Property] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Link instances from the database.
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
                    required: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    readonly: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    default: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Link | Base")
    class __links__(Pointer.__links__, Source.__links__):
        pass

if not TYPE_CHECKING:
    Link.__variants__.Base = Link



#
# type schema::Property
#
class __Property_typeof__(__Pointer_typeof__):
    class __gel_reflection__(__Pointer_typeof__.__gel_reflection__):
        id = UUID(int=219983521560701621898641991940434680828)
        name = SchemaPath('schema', 'Property')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=219983521560701621898641991940434680828),
                name='schema::Property',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__Pointer_typeof__.__typeof__):
        pass


class Property(
    __Property_typeof__,
    Pointer,
    __gel_type_id__=UUID(int=219983521560701621898641991940434680828),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            inherited_fields: list[str] | None = None,
            bases: Iterable[InheritingObject] = [],
            ancestors: Iterable[InheritingObject] = [],
            constraints: Iterable[Constraint] = [],
            cardinality: __builtins__.str | None = None,
            required: bool | None = None,
            readonly: bool | None = None,
            default: str | None = None,
            expr: str | None = None,
            secret: bool | None = None,
            source: Source | None = None,
            target: Type | None = None,
            rewrites: Iterable[Rewrite] = [],
        ) -> None:
            """Create a new schema::Property instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
            cardinality: type[Cardinality] | UnspecifiedType = Unspecified,
            required: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            readonly: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            source: type[schema.Source] | UnspecifiedType = Unspecified,
            target: type[schema.Type] | UnspecifiedType = Unspecified,
            rewrites: type[schema.Rewrite] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Property instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            constraints: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Constraint] | UnspecifiedType = Unspecified,
            cardinality: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Cardinality] | UnspecifiedType = Unspecified,
            required: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            readonly: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            default: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            source: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Source] | UnspecifiedType = Unspecified,
            target: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
            rewrites: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Rewrite] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Property instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
            constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
            cardinality: type[Cardinality] | UnspecifiedType = Unspecified,
            required: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            readonly: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            secret: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            source: type[schema.Source] | UnspecifiedType = Unspecified,
            target: type[schema.Type] | UnspecifiedType = Unspecified,
            rewrites: type[schema.Rewrite] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Property instances from the database.
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
            required: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            readonly: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            default: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(Pointer.__variants__):
        class Base(__Property_typeof__, Pointer.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    inherited_fields: list[str] | None = None,
                    bases: Iterable[InheritingObject] = [],
                    ancestors: Iterable[InheritingObject] = [],
                    constraints: Iterable[Constraint] = [],
                    cardinality: __builtins__.str | None = None,
                    required: bool | None = None,
                    readonly: bool | None = None,
                    default: str | None = None,
                    expr: str | None = None,
                    secret: bool | None = None,
                    source: Source | None = None,
                    target: Type | None = None,
                    rewrites: Iterable[Rewrite] = [],
                ) -> None:
                    """Create a new schema::Property instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
                    cardinality: type[Cardinality] | UnspecifiedType = Unspecified,
                    required: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    readonly: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    source: type[schema.Source] | UnspecifiedType = Unspecified,
                    target: type[schema.Type] | UnspecifiedType = Unspecified,
                    rewrites: type[schema.Rewrite] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Property instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    constraints: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Constraint] | UnspecifiedType = Unspecified,
                    cardinality: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[Cardinality] | UnspecifiedType = Unspecified,
                    required: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    readonly: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    default: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    source: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Source] | UnspecifiedType = Unspecified,
                    target: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
                    rewrites: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Rewrite] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Property instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    inherited_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    bases: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    ancestors: type[schema.InheritingObject] | UnspecifiedType = Unspecified,
                    constraints: type[schema.Constraint] | UnspecifiedType = Unspecified,
                    cardinality: type[Cardinality] | UnspecifiedType = Unspecified,
                    required: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    readonly: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    default: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    secret: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    source: type[schema.Source] | UnspecifiedType = Unspecified,
                    target: type[schema.Type] | UnspecifiedType = Unspecified,
                    rewrites: type[schema.Rewrite] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Property instances from the database.
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
                    required: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    readonly: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    default: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    secret: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Property | Base")
    class __links__(Pointer.__links__):
        pass

if not TYPE_CHECKING:
    Property.__variants__.Base = Property



#
# type schema::Array
#
class __Array_typeof__(__CollectionType_typeof__):
    class __gel_reflection__(__CollectionType_typeof__.__gel_reflection__):
        id = UUID(int=53484707270343816062197209396756293927)
        name = SchemaPath('schema', 'Array')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=53484707270343816062197209396756293927),
                name='schema::Array',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__CollectionType_typeof__.__typeof__):
        dimensions = TypeAliasType('dimensions', 'OptionalProperty[pydantic.Array[std.int16], list[int]]')
        element_type = TypeAliasType('element_type', 'OptionalLink[Type]')


class Array(
    __Array_typeof__,
    CollectionType,
    __gel_type_id__=UUID(int=53484707270343816062197209396756293927),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            expr: str | None = None,
            from_alias: bool | None = None,
            dimensions: list[int] | None = None,
            element_type: Type | None = None,
        ) -> None:
            """Create a new schema::Array instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            dimensions: type[pydantic.Array[__std__.int16]] | UnspecifiedType = Unspecified,
            element_type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Array instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            dimensions: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.int16]] | UnspecifiedType = Unspecified,
            element_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Array instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            dimensions: type[pydantic.Array[__std__.int16]] | UnspecifiedType = Unspecified,
            element_type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Array instances from the database.
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
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(CollectionType.__variants__):
        class Base(__Array_typeof__, CollectionType.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    expr: str | None = None,
                    from_alias: bool | None = None,
                    dimensions: list[int] | None = None,
                    element_type: Type | None = None,
                ) -> None:
                    """Create a new schema::Array instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    dimensions: type[pydantic.Array[__std__.int16]] | UnspecifiedType = Unspecified,
                    element_type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Array instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    dimensions: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.int16]] | UnspecifiedType = Unspecified,
                    element_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Array instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    dimensions: type[pydantic.Array[__std__.int16]] | UnspecifiedType = Unspecified,
                    element_type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Array instances from the database.
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
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Array | Base")
    class __links__(CollectionType.__links__):
        pass

if not TYPE_CHECKING:
    Array.__variants__.Base = Array



#
# type schema::MultiRange
#
class __MultiRange_typeof__(__CollectionType_typeof__):
    class __gel_reflection__(__CollectionType_typeof__.__gel_reflection__):
        id = UUID(int=170204997772705628008448912071797868054)
        name = SchemaPath('schema', 'MultiRange')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=170204997772705628008448912071797868054),
                name='schema::MultiRange',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__CollectionType_typeof__.__typeof__):
        element_type = TypeAliasType('element_type', 'OptionalLink[Type]')


class MultiRange(
    __MultiRange_typeof__,
    CollectionType,
    __gel_type_id__=UUID(int=170204997772705628008448912071797868054),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            expr: str | None = None,
            from_alias: bool | None = None,
            element_type: Type | None = None,
        ) -> None:
            """Create a new schema::MultiRange instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            element_type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::MultiRange instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            element_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::MultiRange instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            element_type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::MultiRange instances from the database.
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
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(CollectionType.__variants__):
        class Base(__MultiRange_typeof__, CollectionType.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    expr: str | None = None,
                    from_alias: bool | None = None,
                    element_type: Type | None = None,
                ) -> None:
                    """Create a new schema::MultiRange instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    element_type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::MultiRange instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    element_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::MultiRange instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    element_type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::MultiRange instances from the database.
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
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="MultiRange | Base")
    class __links__(CollectionType.__links__):
        pass

if not TYPE_CHECKING:
    MultiRange.__variants__.Base = MultiRange



#
# type schema::Range
#
class __Range_typeof__(__CollectionType_typeof__):
    class __gel_reflection__(__CollectionType_typeof__.__gel_reflection__):
        id = UUID(int=272394099022298984585641659238808423105)
        name = SchemaPath('schema', 'Range')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=272394099022298984585641659238808423105),
                name='schema::Range',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__CollectionType_typeof__.__typeof__):
        element_type = TypeAliasType('element_type', 'OptionalLink[Type]')


class Range(
    __Range_typeof__,
    CollectionType,
    __gel_type_id__=UUID(int=272394099022298984585641659238808423105),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            expr: str | None = None,
            from_alias: bool | None = None,
            element_type: Type | None = None,
        ) -> None:
            """Create a new schema::Range instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            element_type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Range instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            element_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Range instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            element_type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Range instances from the database.
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
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(CollectionType.__variants__):
        class Base(__Range_typeof__, CollectionType.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    expr: str | None = None,
                    from_alias: bool | None = None,
                    element_type: Type | None = None,
                ) -> None:
                    """Create a new schema::Range instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    element_type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Range instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    element_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Range instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    element_type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Range instances from the database.
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
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Range | Base")
    class __links__(CollectionType.__links__):
        pass

if not TYPE_CHECKING:
    Range.__variants__.Base = Range



#
# type schema::Tuple
#
class __Tuple_typeof__(__CollectionType_typeof__):
    class __gel_reflection__(__CollectionType_typeof__.__gel_reflection__):
        id = UUID(int=287836478248157732887507443490326531560)
        name = SchemaPath('schema', 'Tuple')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=287836478248157732887507443490326531560),
                name='schema::Tuple',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__CollectionType_typeof__.__typeof__):
        named = TypeAliasType('named', 'std.bool')
        element_types = TypeAliasType('element_types', 'MultiLinkWithProps[Tuple.__links__.element_types, TupleElement]')


class Tuple(
    __Tuple_typeof__,
    CollectionType,
    __gel_type_id__=UUID(int=287836478248157732887507443490326531560),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            expr: str | None = None,
            from_alias: bool | None = None,
            named: bool,
            element_types: Iterable[TupleElement] = [],
        ) -> None:
            """Create a new schema::Tuple instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            named: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            element_types: type[schema.TupleElement] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::Tuple instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            named: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            element_types: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.TupleElement] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::Tuple instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            named: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            element_types: type[schema.TupleElement] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::Tuple instances from the database.
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
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            named: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(CollectionType.__variants__):
        class Base(__Tuple_typeof__, CollectionType.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    expr: str | None = None,
                    from_alias: bool | None = None,
                    named: bool,
                    element_types: Iterable[TupleElement] = [],
                ) -> None:
                    """Create a new schema::Tuple instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    named: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    element_types: type[schema.TupleElement] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::Tuple instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    named: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    element_types: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.TupleElement] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::Tuple instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    named: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    element_types: type[schema.TupleElement] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::Tuple instances from the database.
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
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    named: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="Tuple | Base")
    class __links__(CollectionType.__links__):
        if TYPE_CHECKING:
            class element_types(
                schema.TupleElement,
                ProxyModel[schema.TupleElement],
            ):
                """link schema::Tuple.element_types: schema::TupleElement"""
                class __lprops__(GelLinkModel):
                    index: OptionalProperty[__std__.int64, __builtins_2__.int]

                def __init__(
                    self,
                    obj: schema.TupleElement,
                    /,
                    *,
                    index: __builtins_2__.int | None = None,
                ) -> None:
                    ...

                @classmethod
                def link(
                    cls,
                    obj: schema.TupleElement,
                    /,
                    *,
                    index: __builtins_2__.int | None = None,
                ) -> Self:
                    ...

        if not TYPE_CHECKING:
            @LazyClassProperty[type]
            @classmethod
            def element_types(cls) -> type:
                class Tuple__element_types(
                    __schema__.TupleElement,
                    ProxyModel[__schema__.TupleElement],
                ):
                    """link schema::Tuple.element_types: schema::TupleElement"""
                    class __lprops__(GelLinkModel):
                        index: OptionalProperty[std.int64, __builtins_2__.int]

                    def __init__(
                        self,
                        obj: __schema__.TupleElement,
                        /,
                        *,
                        index: __builtins_2__.int | None = None,
                    ) -> None:
                        ProxyModel.__init__(self, obj)
                        lprops = self.__class__.__lprops__(index=index)
                        object.__setattr__(self, "__linkprops__", lprops)

                    @classmethod
                    def link(
                        cls,
                        obj: __schema__.TupleElement,
                        /,
                        *,
                        index: __builtins_2__.int | None = None,
                    ) -> Self:
                        return cls(obj, index=index)

                Tuple__element_types.__name__ = 'element_types'
                Tuple__element_types.__qualname__ = 'Tuple.element_types'
                return Tuple__element_types

if not TYPE_CHECKING:
    Tuple.__variants__.Base = Tuple



#
# type schema::ArrayExprAlias
#
class __ArrayExprAlias_typeof__(__Array_typeof__):
    class __gel_reflection__(__Array_typeof__.__gel_reflection__):
        id = UUID(int=61590213175760747272592738068582400723)
        name = SchemaPath('schema', 'ArrayExprAlias')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=61590213175760747272592738068582400723),
                name='schema::ArrayExprAlias',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__Array_typeof__.__typeof__):
        pass


class ArrayExprAlias(
    __ArrayExprAlias_typeof__,
    Array,
    __gel_type_id__=UUID(int=61590213175760747272592738068582400723),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            expr: str | None = None,
            from_alias: bool | None = None,
            dimensions: list[int] | None = None,
            element_type: Type | None = None,
        ) -> None:
            """Create a new schema::ArrayExprAlias instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            dimensions: type[pydantic.Array[__std__.int16]] | UnspecifiedType = Unspecified,
            element_type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::ArrayExprAlias instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            dimensions: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.int16]] | UnspecifiedType = Unspecified,
            element_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::ArrayExprAlias instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            dimensions: type[pydantic.Array[__std__.int16]] | UnspecifiedType = Unspecified,
            element_type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::ArrayExprAlias instances from the database.
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
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(Array.__variants__):
        class Base(__ArrayExprAlias_typeof__, Array.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    expr: str | None = None,
                    from_alias: bool | None = None,
                    dimensions: list[int] | None = None,
                    element_type: Type | None = None,
                ) -> None:
                    """Create a new schema::ArrayExprAlias instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    dimensions: type[pydantic.Array[__std__.int16]] | UnspecifiedType = Unspecified,
                    element_type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::ArrayExprAlias instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    dimensions: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.int16]] | UnspecifiedType = Unspecified,
                    element_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::ArrayExprAlias instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    dimensions: type[pydantic.Array[__std__.int16]] | UnspecifiedType = Unspecified,
                    element_type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::ArrayExprAlias instances from the database.
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
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="ArrayExprAlias | Base")
    class __links__(Array.__links__):
        pass

if not TYPE_CHECKING:
    ArrayExprAlias.__variants__.Base = ArrayExprAlias



#
# type schema::MultiRangeExprAlias
#
class __MultiRangeExprAlias_typeof__(__MultiRange_typeof__):
    class __gel_reflection__(__MultiRange_typeof__.__gel_reflection__):
        id = UUID(int=224883386490687742483367914857266351077)
        name = SchemaPath('schema', 'MultiRangeExprAlias')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=224883386490687742483367914857266351077),
                name='schema::MultiRangeExprAlias',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__MultiRange_typeof__.__typeof__):
        pass


class MultiRangeExprAlias(
    __MultiRangeExprAlias_typeof__,
    MultiRange,
    __gel_type_id__=UUID(int=224883386490687742483367914857266351077),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            expr: str | None = None,
            from_alias: bool | None = None,
            element_type: Type | None = None,
        ) -> None:
            """Create a new schema::MultiRangeExprAlias instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            element_type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::MultiRangeExprAlias instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            element_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::MultiRangeExprAlias instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            element_type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::MultiRangeExprAlias instances from the database.
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
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(MultiRange.__variants__):
        class Base(
            __MultiRangeExprAlias_typeof__,
            MultiRange.__variants__.Base,
        ):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    expr: str | None = None,
                    from_alias: bool | None = None,
                    element_type: Type | None = None,
                ) -> None:
                    """Create a new schema::MultiRangeExprAlias instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    element_type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::MultiRangeExprAlias instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    element_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::MultiRangeExprAlias instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    element_type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::MultiRangeExprAlias instances from the database.
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
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="MultiRangeExprAlias | Base")
    class __links__(MultiRange.__links__):
        pass

if not TYPE_CHECKING:
    MultiRangeExprAlias.__variants__.Base = MultiRangeExprAlias



#
# type schema::RangeExprAlias
#
class __RangeExprAlias_typeof__(__Range_typeof__):
    class __gel_reflection__(__Range_typeof__.__gel_reflection__):
        id = UUID(int=250410383444011926837054666695611053661)
        name = SchemaPath('schema', 'RangeExprAlias')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=250410383444011926837054666695611053661),
                name='schema::RangeExprAlias',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__Range_typeof__.__typeof__):
        pass


class RangeExprAlias(
    __RangeExprAlias_typeof__,
    Range,
    __gel_type_id__=UUID(int=250410383444011926837054666695611053661),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            expr: str | None = None,
            from_alias: bool | None = None,
            element_type: Type | None = None,
        ) -> None:
            """Create a new schema::RangeExprAlias instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            element_type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::RangeExprAlias instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            element_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::RangeExprAlias instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            element_type: type[schema.Type] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::RangeExprAlias instances from the database.
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
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(Range.__variants__):
        class Base(__RangeExprAlias_typeof__, Range.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    expr: str | None = None,
                    from_alias: bool | None = None,
                    element_type: Type | None = None,
                ) -> None:
                    """Create a new schema::RangeExprAlias instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    element_type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::RangeExprAlias instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    element_type: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Type] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::RangeExprAlias instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    element_type: type[schema.Type] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::RangeExprAlias instances from the database.
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
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="RangeExprAlias | Base")
    class __links__(Range.__links__):
        pass

if not TYPE_CHECKING:
    RangeExprAlias.__variants__.Base = RangeExprAlias



#
# type schema::TupleExprAlias
#
class __TupleExprAlias_typeof__(__Tuple_typeof__):
    class __gel_reflection__(__Tuple_typeof__.__gel_reflection__):
        id = UUID(int=243852543501794655710671212006669279835)
        name = SchemaPath('schema', 'TupleExprAlias')
        @LazyClassProperty["schema.ObjectType"]
        @classmethod
        def object(cls) -> schema.ObjectType:
            from ... import schema as __schema_1__
            return __schema_1__.ObjectType(
                id=UUID(int=243852543501794655710671212006669279835),
                name='schema::TupleExprAlias',
                builtin=True,
                internal=False,
                abstract=False,
                final=False,
                compound_type=False,
            )

    class __typeof__(__Tuple_typeof__.__typeof__):
        pass


class TupleExprAlias(
    __TupleExprAlias_typeof__,
    Tuple,
    __gel_type_id__=UUID(int=243852543501794655710671212006669279835),
):
    if TYPE_CHECKING:
        def __init__(
            self,
            /,
            *,
            id: UUID,
            name: str,
            internal: bool,
            builtin: bool,
            computed_fields: list[str] | None = None,
            annotations: Iterable[Annotation] = [],
            abstract: bool | None = None,
            final: bool,
            expr: str | None = None,
            from_alias: bool | None = None,
            named: bool,
            element_types: Iterable[TupleElement] = [],
        ) -> None:
            """Create a new schema::TupleExprAlias instance from keyword arguments.

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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            named: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            element_types: type[schema.TupleElement] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Update schema::TupleExprAlias instances in the database.
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
            computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            named: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
            element_types: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.TupleElement] | UnspecifiedType = Unspecified,
            **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
        ) -> type[Self]:
            """Fetch schema::TupleExprAlias instances from the database.
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
            computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
            annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
            abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
            from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            named: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
            element_types: type[schema.TupleElement] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Fetch schema::TupleExprAlias instances from the database.
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
            expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
            named: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
        ) -> type[Self]:
            """Specify the sort order for the selection"""
            ...


    class __variants__(Tuple.__variants__):
        class Base(__TupleExprAlias_typeof__, Tuple.__variants__.Base):
            if TYPE_CHECKING:
                def __init__(
                    self,
                    /,
                    *,
                    id: UUID,
                    name: str,
                    internal: bool,
                    builtin: bool,
                    computed_fields: list[str] | None = None,
                    annotations: Iterable[Annotation] = [],
                    abstract: bool | None = None,
                    final: bool,
                    expr: str | None = None,
                    from_alias: bool | None = None,
                    named: bool,
                    element_types: Iterable[TupleElement] = [],
                ) -> None:
                    """Create a new schema::TupleExprAlias instance from keyword arguments.

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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    named: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    element_types: type[schema.TupleElement] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Update schema::TupleExprAlias instances in the database.
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
                    computed_fields: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    named: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[__std__.bool] | UnspecifiedType = Unspecified,
                    element_types: builtins.bool | Callable[[type[Self]], ExprCompatible] | ExprCompatible | type[schema.TupleElement] | UnspecifiedType = Unspecified,
                    **computed: Callable[[type[Self]], ExprCompatible] | ExprCompatible | PyConstType,
                ) -> type[Self]:
                    """Fetch schema::TupleExprAlias instances from the database.
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
                    computed_fields: type[pydantic.Array[__std__.str]] | UnspecifiedType = Unspecified,
                    annotations: type[schema.Annotation] | UnspecifiedType = Unspecified,
                    abstract: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    final: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    expr: __builtins__.str | type[__std__.str] | UnspecifiedType = Unspecified,
                    from_alias: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    named: __builtins_1__.bool | type[__std__.bool] | UnspecifiedType = Unspecified,
                    element_types: type[schema.TupleElement] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Fetch schema::TupleExprAlias instances from the database.
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
                    expr: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    from_alias: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                    named: Direction | builtins.str | builtins.str | builtins.bool | tuple[Direction | builtins.str, EmptyDirection | builtins.str] | UnspecifiedType = Unspecified,
                ) -> type[Self]:
                    """Specify the sort order for the selection"""
                    ...


        Any = TypeVar("Any", bound="TupleExprAlias | Base")
    class __links__(Tuple.__links__):
        pass

if not TYPE_CHECKING:
    TupleExprAlias.__variants__.Base = TupleExprAlias



from .. import sys  # noqa: E402 F403
from ... import schema as __schema__  # noqa: E402 F403
from ...std.__types__ import NameExpr_Tuple_9eMVFg  # noqa: E402 F403

from builtins import bool, int, str  # noqa: E402 F403
