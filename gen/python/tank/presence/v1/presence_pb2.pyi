from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PresenceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRESENCE_STATUS_UNSPECIFIED: _ClassVar[PresenceStatus]
    PRESENCE_STATUS_ACTIVE: _ClassVar[PresenceStatus]
    PRESENCE_STATUS_AWAY: _ClassVar[PresenceStatus]
    PRESENCE_STATUS_DND: _ClassVar[PresenceStatus]
    PRESENCE_STATUS_ARMOR: _ClassVar[PresenceStatus]
PRESENCE_STATUS_UNSPECIFIED: PresenceStatus
PRESENCE_STATUS_ACTIVE: PresenceStatus
PRESENCE_STATUS_AWAY: PresenceStatus
PRESENCE_STATUS_DND: PresenceStatus
PRESENCE_STATUS_ARMOR: PresenceStatus

class Presence(_message.Message):
    __slots__ = ("user_id", "status", "last_seen", "custom_status_text", "custom_status_emoji", "status_expires_at")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_STATUS_TEXT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_STATUS_EMOJI_FIELD_NUMBER: _ClassVar[int]
    STATUS_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    status: PresenceStatus
    last_seen: _timestamp_pb2.Timestamp
    custom_status_text: str
    custom_status_emoji: str
    status_expires_at: _timestamp_pb2.Timestamp
    def __init__(self, user_id: _Optional[str] = ..., status: _Optional[_Union[PresenceStatus, str]] = ..., last_seen: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., custom_status_text: _Optional[str] = ..., custom_status_emoji: _Optional[str] = ..., status_expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SetStatusRequest(_message.Message):
    __slots__ = ("status", "custom_status_text", "custom_status_emoji", "expires_at", "workspace_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_STATUS_TEXT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_STATUS_EMOJI_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    status: PresenceStatus
    custom_status_text: str
    custom_status_emoji: str
    expires_at: _timestamp_pb2.Timestamp
    workspace_id: str
    def __init__(self, status: _Optional[_Union[PresenceStatus, str]] = ..., custom_status_text: _Optional[str] = ..., custom_status_emoji: _Optional[str] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., workspace_id: _Optional[str] = ...) -> None: ...

class SetStatusResponse(_message.Message):
    __slots__ = ("presence",)
    PRESENCE_FIELD_NUMBER: _ClassVar[int]
    presence: Presence
    def __init__(self, presence: _Optional[_Union[Presence, _Mapping]] = ...) -> None: ...

class GetPresenceRequest(_message.Message):
    __slots__ = ("user_ids", "workspace_id")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    workspace_id: str
    def __init__(self, user_ids: _Optional[_Iterable[str]] = ..., workspace_id: _Optional[str] = ...) -> None: ...

class GetPresenceResponse(_message.Message):
    __slots__ = ("presences",)
    PRESENCES_FIELD_NUMBER: _ClassVar[int]
    presences: _containers.RepeatedCompositeFieldContainer[Presence]
    def __init__(self, presences: _Optional[_Iterable[_Union[Presence, _Mapping]]] = ...) -> None: ...
