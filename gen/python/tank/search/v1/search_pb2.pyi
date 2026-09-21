from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tank.message.v1 import message_pb2 as _message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HasFilter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HAS_FILTER_UNSPECIFIED: _ClassVar[HasFilter]
    HAS_FILTER_FILES: _ClassVar[HasFilter]
    HAS_FILTER_LINKS: _ClassVar[HasFilter]
    HAS_FILTER_REACTIONS: _ClassVar[HasFilter]
    HAS_FILTER_BLOCKS: _ClassVar[HasFilter]
HAS_FILTER_UNSPECIFIED: HasFilter
HAS_FILTER_FILES: HasFilter
HAS_FILTER_LINKS: HasFilter
HAS_FILTER_REACTIONS: HasFilter
HAS_FILTER_BLOCKS: HasFilter

class SearchFilters(_message.Message):
    __slots__ = ("from_user_ids", "in_channel_ids", "has", "before", "after")
    FROM_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    IN_CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    HAS_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    from_user_ids: _containers.RepeatedScalarFieldContainer[str]
    in_channel_ids: _containers.RepeatedScalarFieldContainer[str]
    has: _containers.RepeatedScalarFieldContainer[HasFilter]
    before: _timestamp_pb2.Timestamp
    after: _timestamp_pb2.Timestamp
    def __init__(self, from_user_ids: _Optional[_Iterable[str]] = ..., in_channel_ids: _Optional[_Iterable[str]] = ..., has: _Optional[_Iterable[_Union[HasFilter, str]]] = ..., before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SearchRequest(_message.Message):
    __slots__ = ("workspace_id", "query", "filters", "cursor", "limit", "q", "semantic")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    Q_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    query: str
    filters: SearchFilters
    cursor: str
    limit: int
    q: str
    semantic: bool
    def __init__(self, workspace_id: _Optional[str] = ..., query: _Optional[str] = ..., filters: _Optional[_Union[SearchFilters, _Mapping]] = ..., cursor: _Optional[str] = ..., limit: _Optional[int] = ..., q: _Optional[str] = ..., semantic: bool = ...) -> None: ...

class SearchHit(_message.Message):
    __slots__ = ("message", "channel_id", "highlights", "score")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    HIGHLIGHTS_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    message: _message_pb2.Message
    channel_id: str
    highlights: _containers.RepeatedScalarFieldContainer[str]
    score: float
    def __init__(self, message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ..., channel_id: _Optional[str] = ..., highlights: _Optional[_Iterable[str]] = ..., score: _Optional[float] = ...) -> None: ...

class SearchResponse(_message.Message):
    __slots__ = ("hits", "next_cursor", "total_estimate", "parsed_filters", "parsed_query", "semantic_used")
    HITS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    PARSED_FILTERS_FIELD_NUMBER: _ClassVar[int]
    PARSED_QUERY_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_USED_FIELD_NUMBER: _ClassVar[int]
    hits: _containers.RepeatedCompositeFieldContainer[SearchHit]
    next_cursor: str
    total_estimate: int
    parsed_filters: SearchFilters
    parsed_query: str
    semantic_used: bool
    def __init__(self, hits: _Optional[_Iterable[_Union[SearchHit, _Mapping]]] = ..., next_cursor: _Optional[str] = ..., total_estimate: _Optional[int] = ..., parsed_filters: _Optional[_Union[SearchFilters, _Mapping]] = ..., parsed_query: _Optional[str] = ..., semantic_used: bool = ...) -> None: ...
