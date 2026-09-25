from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tank.message.v1 import message_pb2 as _message_pb2
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
    MARK_TYPE_WAITING_ON: _ClassVar[MarkType]
    MARK_TYPE_ARTIFACT: _ClassVar[MarkType]
    MARK_TYPE_EVENT: _ClassVar[MarkType]
    MARK_TYPE_UNANSWERED_QUESTION: _ClassVar[MarkType]

class ArtifactKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARTIFACT_KIND_UNSPECIFIED: _ClassVar[ArtifactKind]
    ARTIFACT_KIND_FILE: _ClassVar[ArtifactKind]
    ARTIFACT_KIND_LINK: _ClassVar[ArtifactKind]
    ARTIFACT_KIND_CODE: _ClassVar[ArtifactKind]

class MarkStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MARK_STATUS_UNSPECIFIED: _ClassVar[MarkStatus]
    MARK_STATUS_OPEN: _ClassVar[MarkStatus]
    MARK_STATUS_RESOLVED: _ClassVar[MarkStatus]
    MARK_STATUS_DISMISSED: _ClassVar[MarkStatus]

class Lane(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LANE_UNSPECIFIED: _ClassVar[Lane]
    LANE_STRUCTURE: _ClassVar[Lane]
    LANE_MESSAGE: _ClassVar[Lane]
    LANE_PERSONAL: _ClassVar[Lane]

class WaitingDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WAITING_DIRECTION_UNSPECIFIED: _ClassVar[WaitingDirection]
    WAITING_DIRECTION_ON_ME: _ClassVar[WaitingDirection]
    WAITING_DIRECTION_BY_ME: _ClassVar[WaitingDirection]
MARK_TYPE_UNSPECIFIED: MarkType
MARK_TYPE_MENTION: MarkType
MARK_TYPE_OWN_MESSAGE: MarkType
MARK_TYPE_READ_HORIZON: MarkType
MARK_TYPE_SEARCH_HIT: MarkType
MARK_TYPE_WAITING_ON: MarkType
MARK_TYPE_ARTIFACT: MarkType
MARK_TYPE_EVENT: MarkType
MARK_TYPE_UNANSWERED_QUESTION: MarkType
ARTIFACT_KIND_UNSPECIFIED: ArtifactKind
ARTIFACT_KIND_FILE: ArtifactKind
ARTIFACT_KIND_LINK: ArtifactKind
ARTIFACT_KIND_CODE: ArtifactKind
MARK_STATUS_UNSPECIFIED: MarkStatus
MARK_STATUS_OPEN: MarkStatus
MARK_STATUS_RESOLVED: MarkStatus
MARK_STATUS_DISMISSED: MarkStatus
LANE_UNSPECIFIED: Lane
LANE_STRUCTURE: Lane
LANE_MESSAGE: Lane
LANE_PERSONAL: Lane
WAITING_DIRECTION_UNSPECIFIED: WaitingDirection
WAITING_DIRECTION_ON_ME: WaitingDirection
WAITING_DIRECTION_BY_ME: WaitingDirection

class Mark(_message.Message):
    __slots__ = ("id", "channel_id", "message_id", "channel_seq", "type", "lane", "elevation", "preview", "created_at", "status", "waiting_on_user_ids", "created_by_user_id", "resolved_at", "detail", "url", "artifact_kind", "survey")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_SEQ_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LANE_FIELD_NUMBER: _ClassVar[int]
    ELEVATION_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    WAITING_ON_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_AT_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_KIND_FIELD_NUMBER: _ClassVar[int]
    SURVEY_FIELD_NUMBER: _ClassVar[int]
    id: str
    channel_id: str
    message_id: str
    channel_seq: int
    type: MarkType
    lane: Lane
    elevation: int
    preview: str
    created_at: _timestamp_pb2.Timestamp
    status: MarkStatus
    waiting_on_user_ids: _containers.RepeatedScalarFieldContainer[str]
    created_by_user_id: str
    resolved_at: _timestamp_pb2.Timestamp
    detail: str
    url: str
    artifact_kind: ArtifactKind
    survey: SurveyOrigin
    def __init__(self, id: _Optional[str] = ..., channel_id: _Optional[str] = ..., message_id: _Optional[str] = ..., channel_seq: _Optional[int] = ..., type: _Optional[_Union[MarkType, str]] = ..., lane: _Optional[_Union[Lane, str]] = ..., elevation: _Optional[int] = ..., preview: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[MarkStatus, str]] = ..., waiting_on_user_ids: _Optional[_Iterable[str]] = ..., created_by_user_id: _Optional[str] = ..., resolved_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., detail: _Optional[str] = ..., url: _Optional[str] = ..., artifact_kind: _Optional[_Union[ArtifactKind, str]] = ..., survey: _Optional[_Union[SurveyOrigin, _Mapping]] = ...) -> None: ...

class SurveyOrigin(_message.Message):
    __slots__ = ("extractor", "version", "model", "confidence")
    EXTRACTOR_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    extractor: str
    version: str
    model: str
    confidence: float
    def __init__(self, extractor: _Optional[str] = ..., version: _Optional[str] = ..., model: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

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

class FlagWaitingOnRequest(_message.Message):
    __slots__ = ("message_id", "user_ids")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, message_id: _Optional[str] = ..., user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class FlagWaitingOnResponse(_message.Message):
    __slots__ = ("mark",)
    MARK_FIELD_NUMBER: _ClassVar[int]
    mark: Mark
    def __init__(self, mark: _Optional[_Union[Mark, _Mapping]] = ...) -> None: ...

class ResolveWaitingOnRequest(_message.Message):
    __slots__ = ("mark_id", "dismiss")
    MARK_ID_FIELD_NUMBER: _ClassVar[int]
    DISMISS_FIELD_NUMBER: _ClassVar[int]
    mark_id: str
    dismiss: bool
    def __init__(self, mark_id: _Optional[str] = ..., dismiss: bool = ...) -> None: ...

class ResolveWaitingOnResponse(_message.Message):
    __slots__ = ("mark",)
    MARK_FIELD_NUMBER: _ClassVar[int]
    mark: Mark
    def __init__(self, mark: _Optional[_Union[Mark, _Mapping]] = ...) -> None: ...

class ListWaitingOnRequest(_message.Message):
    __slots__ = ("workspace_id", "direction", "include_closed")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CLOSED_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    direction: WaitingDirection
    include_closed: bool
    def __init__(self, workspace_id: _Optional[str] = ..., direction: _Optional[_Union[WaitingDirection, str]] = ..., include_closed: bool = ...) -> None: ...

class WaitingOnItem(_message.Message):
    __slots__ = ("mark", "message")
    MARK_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    mark: Mark
    message: _message_pb2.Message
    def __init__(self, mark: _Optional[_Union[Mark, _Mapping]] = ..., message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class RecordEventRequest(_message.Message):
    __slots__ = ("channel_id", "kind", "detail", "url", "dedupe_key")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    DEDUPE_KEY_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    kind: str
    detail: str
    url: str
    dedupe_key: str
    def __init__(self, channel_id: _Optional[str] = ..., kind: _Optional[str] = ..., detail: _Optional[str] = ..., url: _Optional[str] = ..., dedupe_key: _Optional[str] = ...) -> None: ...

class RecordEventResponse(_message.Message):
    __slots__ = ("mark",)
    MARK_FIELD_NUMBER: _ClassVar[int]
    mark: Mark
    def __init__(self, mark: _Optional[_Union[Mark, _Mapping]] = ...) -> None: ...

class ListWaitingOnResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[WaitingOnItem]
    def __init__(self, items: _Optional[_Iterable[_Union[WaitingOnItem, _Mapping]]] = ...) -> None: ...
