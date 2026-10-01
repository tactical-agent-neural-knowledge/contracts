from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProductSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCT_SORT_UNSPECIFIED: _ClassVar[ProductSort]
    PRODUCT_SORT_NEWEST: _ClassVar[ProductSort]
    PRODUCT_SORT_FURTHEST_ALONG: _ClassVar[ProductSort]
    PRODUCT_SORT_CHEAPEST: _ClassVar[ProductSort]
    PRODUCT_SORT_MOST_EXPENSIVE: _ClassVar[ProductSort]
    PRODUCT_SORT_MOST_VIEWED: _ClassVar[ProductSort]
PRODUCT_SORT_UNSPECIFIED: ProductSort
PRODUCT_SORT_NEWEST: ProductSort
PRODUCT_SORT_FURTHEST_ALONG: ProductSort
PRODUCT_SORT_CHEAPEST: ProductSort
PRODUCT_SORT_MOST_EXPENSIVE: ProductSort
PRODUCT_SORT_MOST_VIEWED: ProductSort

class ProductCard(_message.Message):
    __slots__ = ("workspace_id", "slug", "name", "description", "industry", "buyer", "price_cents", "agent_minutes", "work_delivered", "agent_active", "created_at", "last_worked_at", "available", "watched", "view_count")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INDUSTRY_FIELD_NUMBER: _ClassVar[int]
    BUYER_FIELD_NUMBER: _ClassVar[int]
    PRICE_CENTS_FIELD_NUMBER: _ClassVar[int]
    AGENT_MINUTES_FIELD_NUMBER: _ClassVar[int]
    WORK_DELIVERED_FIELD_NUMBER: _ClassVar[int]
    AGENT_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_WORKED_AT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    WATCHED_FIELD_NUMBER: _ClassVar[int]
    VIEW_COUNT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    slug: str
    name: str
    description: str
    industry: str
    buyer: str
    price_cents: int
    agent_minutes: int
    work_delivered: int
    agent_active: bool
    created_at: _timestamp_pb2.Timestamp
    last_worked_at: _timestamp_pb2.Timestamp
    available: bool
    watched: bool
    view_count: int
    def __init__(self, workspace_id: _Optional[str] = ..., slug: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., industry: _Optional[str] = ..., buyer: _Optional[str] = ..., price_cents: _Optional[int] = ..., agent_minutes: _Optional[int] = ..., work_delivered: _Optional[int] = ..., agent_active: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_worked_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., available: bool = ..., watched: bool = ..., view_count: _Optional[int] = ...) -> None: ...

class ListProductsRequest(_message.Message):
    __slots__ = ("sort", "industry", "query", "watched_only", "portfolio_id", "cursor", "limit")
    SORT_FIELD_NUMBER: _ClassVar[int]
    INDUSTRY_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    WATCHED_ONLY_FIELD_NUMBER: _ClassVar[int]
    PORTFOLIO_ID_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    sort: ProductSort
    industry: str
    query: str
    watched_only: bool
    portfolio_id: str
    cursor: str
    limit: int
    def __init__(self, sort: _Optional[_Union[ProductSort, str]] = ..., industry: _Optional[str] = ..., query: _Optional[str] = ..., watched_only: bool = ..., portfolio_id: _Optional[str] = ..., cursor: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListProductsResponse(_message.Message):
    __slots__ = ("products", "next_cursor", "total", "industries")
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    INDUSTRIES_FIELD_NUMBER: _ClassVar[int]
    products: _containers.RepeatedCompositeFieldContainer[ProductCard]
    next_cursor: str
    total: int
    industries: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, products: _Optional[_Iterable[_Union[ProductCard, _Mapping]]] = ..., next_cursor: _Optional[str] = ..., total: _Optional[int] = ..., industries: _Optional[_Iterable[str]] = ...) -> None: ...

class WatchProductRequest(_message.Message):
    __slots__ = ("workspace_id", "watched")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    WATCHED_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    watched: bool
    def __init__(self, workspace_id: _Optional[str] = ..., watched: bool = ...) -> None: ...

class WatchProductResponse(_message.Message):
    __slots__ = ("product",)
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    product: ProductCard
    def __init__(self, product: _Optional[_Union[ProductCard, _Mapping]] = ...) -> None: ...

class Portfolio(_message.Message):
    __slots__ = ("id", "name", "note", "product_count", "value_cents", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_COUNT_FIELD_NUMBER: _ClassVar[int]
    VALUE_CENTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    note: str
    product_count: int
    value_cents: int
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., note: _Optional[str] = ..., product_count: _Optional[int] = ..., value_cents: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListPortfoliosRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPortfoliosResponse(_message.Message):
    __slots__ = ("portfolios",)
    PORTFOLIOS_FIELD_NUMBER: _ClassVar[int]
    portfolios: _containers.RepeatedCompositeFieldContainer[Portfolio]
    def __init__(self, portfolios: _Optional[_Iterable[_Union[Portfolio, _Mapping]]] = ...) -> None: ...

class CreatePortfolioRequest(_message.Message):
    __slots__ = ("name", "note")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    name: str
    note: str
    def __init__(self, name: _Optional[str] = ..., note: _Optional[str] = ...) -> None: ...

class CreatePortfolioResponse(_message.Message):
    __slots__ = ("portfolio",)
    PORTFOLIO_FIELD_NUMBER: _ClassVar[int]
    portfolio: Portfolio
    def __init__(self, portfolio: _Optional[_Union[Portfolio, _Mapping]] = ...) -> None: ...

class RenamePortfolioRequest(_message.Message):
    __slots__ = ("id", "name", "note")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    note: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., note: _Optional[str] = ...) -> None: ...

class RenamePortfolioResponse(_message.Message):
    __slots__ = ("portfolio",)
    PORTFOLIO_FIELD_NUMBER: _ClassVar[int]
    portfolio: Portfolio
    def __init__(self, portfolio: _Optional[_Union[Portfolio, _Mapping]] = ...) -> None: ...

class DeletePortfolioRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeletePortfolioResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetPortfolioProductRequest(_message.Message):
    __slots__ = ("portfolio_id", "workspace_id", "included")
    PORTFOLIO_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_FIELD_NUMBER: _ClassVar[int]
    portfolio_id: str
    workspace_id: str
    included: bool
    def __init__(self, portfolio_id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., included: bool = ...) -> None: ...

class SetPortfolioProductResponse(_message.Message):
    __slots__ = ("portfolio",)
    PORTFOLIO_FIELD_NUMBER: _ClassVar[int]
    portfolio: Portfolio
    def __init__(self, portfolio: _Optional[_Union[Portfolio, _Mapping]] = ...) -> None: ...

class RecordProductViewRequest(_message.Message):
    __slots__ = ("slug", "referrer")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    REFERRER_FIELD_NUMBER: _ClassVar[int]
    slug: str
    referrer: str
    def __init__(self, slug: _Optional[str] = ..., referrer: _Optional[str] = ...) -> None: ...

class RecordProductViewResponse(_message.Message):
    __slots__ = ("view_count",)
    VIEW_COUNT_FIELD_NUMBER: _ClassVar[int]
    view_count: int
    def __init__(self, view_count: _Optional[int] = ...) -> None: ...

class Stat(_message.Message):
    __slots__ = ("key", "label", "value", "unit", "sample", "note")
    KEY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    key: str
    label: str
    value: float
    unit: str
    sample: int
    note: str
    def __init__(self, key: _Optional[str] = ..., label: _Optional[str] = ..., value: _Optional[float] = ..., unit: _Optional[str] = ..., sample: _Optional[int] = ..., note: _Optional[str] = ...) -> None: ...

class Tally(_message.Message):
    __slots__ = ("name", "count", "share")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SHARE_FIELD_NUMBER: _ClassVar[int]
    name: str
    count: int
    share: float
    def __init__(self, name: _Optional[str] = ..., count: _Optional[int] = ..., share: _Optional[float] = ...) -> None: ...

class BoardStatsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BoardStatsResponse(_message.Message):
    __slots__ = ("computed_at", "headline", "all", "industries", "stages", "sources")
    COMPUTED_AT_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    INDUSTRIES_FIELD_NUMBER: _ClassVar[int]
    STAGES_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    computed_at: _timestamp_pb2.Timestamp
    headline: _containers.RepeatedCompositeFieldContainer[Stat]
    all: _containers.RepeatedCompositeFieldContainer[Stat]
    industries: _containers.RepeatedCompositeFieldContainer[Tally]
    stages: _containers.RepeatedCompositeFieldContainer[Tally]
    sources: _containers.RepeatedCompositeFieldContainer[Tally]
    def __init__(self, computed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., headline: _Optional[_Iterable[_Union[Stat, _Mapping]]] = ..., all: _Optional[_Iterable[_Union[Stat, _Mapping]]] = ..., industries: _Optional[_Iterable[_Union[Tally, _Mapping]]] = ..., stages: _Optional[_Iterable[_Union[Tally, _Mapping]]] = ..., sources: _Optional[_Iterable[_Union[Tally, _Mapping]]] = ...) -> None: ...
