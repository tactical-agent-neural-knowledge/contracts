from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HuddleParticipant(_message.Message):
    __slots__ = ("user_id", "joined_at", "muted")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    JOINED_AT_FIELD_NUMBER: _ClassVar[int]
    MUTED_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    joined_at: _timestamp_pb2.Timestamp
    muted: bool
    def __init__(self, user_id: _Optional[str] = ..., joined_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., muted: bool = ...) -> None: ...

class Huddle(_message.Message):
    __slots__ = ("channel_id", "workspace_id", "room_name", "started_by", "started_at", "ended_at", "participants")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    STARTED_BY_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    workspace_id: str
    room_name: str
    started_by: str
    started_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    participants: _containers.RepeatedCompositeFieldContainer[HuddleParticipant]
    def __init__(self, channel_id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., room_name: _Optional[str] = ..., started_by: _Optional[str] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., participants: _Optional[_Iterable[_Union[HuddleParticipant, _Mapping]]] = ...) -> None: ...

class JoinHuddleRequest(_message.Message):
    __slots__ = ("channel_id", "audio_only")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_ONLY_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    audio_only: bool
    def __init__(self, channel_id: _Optional[str] = ..., audio_only: bool = ...) -> None: ...

class JoinHuddleResponse(_message.Message):
    __slots__ = ("url", "token", "room_name", "expires_at", "huddle")
    URL_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    HUDDLE_FIELD_NUMBER: _ClassVar[int]
    url: str
    token: str
    room_name: str
    expires_at: _timestamp_pb2.Timestamp
    huddle: Huddle
    def __init__(self, url: _Optional[str] = ..., token: _Optional[str] = ..., room_name: _Optional[str] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., huddle: _Optional[_Union[Huddle, _Mapping]] = ...) -> None: ...

class LeaveHuddleRequest(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class LeaveHuddleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetHuddleRequest(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class GetHuddleResponse(_message.Message):
    __slots__ = ("huddle",)
    HUDDLE_FIELD_NUMBER: _ClassVar[int]
    huddle: Huddle
    def __init__(self, huddle: _Optional[_Union[Huddle, _Mapping]] = ...) -> None: ...

class ListActiveHuddlesRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListActiveHuddlesResponse(_message.Message):
    __slots__ = ("huddles",)
    HUDDLES_FIELD_NUMBER: _ClassVar[int]
    huddles: _containers.RepeatedCompositeFieldContainer[Huddle]
    def __init__(self, huddles: _Optional[_Iterable[_Union[Huddle, _Mapping]]] = ...) -> None: ...
