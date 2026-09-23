from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MarkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MARK_TYPE_UNSPECIFIED: _ClassVar[MarkType]
    MARK_TYPE_MENTION: _ClassVar[MarkType]
    MARK_TYPE_OWN_MESSAGE: _ClassVar[MarkType]
    MARK_TYPE_READ_HORIZON: _ClassVar[MarkType]
    MARK_TYPE_SEARCH_HIT: _ClassVar[MarkType]

class Lane(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LANE_UNSPECIFIED: _ClassVar[Lane]
    LANE_STRUCTURE: _ClassVar[Lane]
    LANE_MESSAGE: _ClassVar[Lane]
    LANE_PERSONAL: _ClassVar[Lane]
MARK_TYPE_UNSPECIFIED: MarkType
MARK_TYPE_MENTION: MarkType
MARK_TYPE_OWN_MESSAGE: MarkType
MARK_TYPE_READ_HORIZON: MarkType
MARK_TYPE_SEARCH_HIT: MarkType
LANE_UNSPECIFIED: Lane
LANE_STRUCTURE: Lane
LANE_MESSAGE: Lane
LANE_PERSONAL: Lane

class Mark(_message.Message):
    __slots__ = ("id", "channel_id", "message_id", "channel_seq", "type", "lane", "elevation", "preview", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_SEQ_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LANE_FIELD_NUMBER: _ClassVar[int]
    ELEVATION_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    channel_id: str
    message_id: str
    channel_seq: int
    type: MarkType
    lane: Lane
    elevation: int
    preview: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., channel_id: _Optional[str] = ..., message_id: _Optional[str] = ..., channel_seq: _Optional[int] = ..., type: _Optional[_Union[MarkType, str]] = ..., lane: _Optional[_Union[Lane, str]] = ..., elevation: _Optional[int] = ..., preview: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListMarksRequest(_message.Message):
    __slots__ = ("channel_id", "types")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    types: _containers.RepeatedScalarFieldContainer[MarkType]
    def __init__(self, channel_id: _Optional[str] = ..., types: _Optional[_Iterable[_Union[MarkType, str]]] = ...) -> None: ...

class ListMarksResponse(_message.Message):
    __slots__ = ("marks", "last_seq")
    MARKS_FIELD_NUMBER: _ClassVar[int]
    LAST_SEQ_FIELD_NUMBER: _ClassVar[int]
    marks: _containers.RepeatedCompositeFieldContainer[Mark]
    last_seq: int
    def __init__(self, marks: _Optional[_Iterable[_Union[Mark, _Mapping]]] = ..., last_seq: _Optional[int] = ...) -> None: ...
