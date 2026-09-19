from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tank.events.v1 import events_pb2 as _events_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ERROR_CODE_UNSPECIFIED: _ClassVar[ErrorCode]
    ERROR_CODE_UNAUTHENTICATED: _ClassVar[ErrorCode]
    ERROR_CODE_SLOW_CONSUMER: _ClassVar[ErrorCode]
    ERROR_CODE_BAD_FRAME: _ClassVar[ErrorCode]
    ERROR_CODE_RATE_LIMITED: _ClassVar[ErrorCode]
ERROR_CODE_UNSPECIFIED: ErrorCode
ERROR_CODE_UNAUTHENTICATED: ErrorCode
ERROR_CODE_SLOW_CONSUMER: ErrorCode
ERROR_CODE_BAD_FRAME: ErrorCode
ERROR_CODE_RATE_LIMITED: ErrorCode

class Hello(_message.Message):
    __slots__ = ("access_token", "workspace_ids", "capabilities")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_IDS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    workspace_ids: _containers.RepeatedScalarFieldContainer[str]
    capabilities: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, access_token: _Optional[str] = ..., workspace_ids: _Optional[_Iterable[str]] = ..., capabilities: _Optional[_Iterable[str]] = ...) -> None: ...

class Resume(_message.Message):
    __slots__ = ("session_id", "resume_token", "cursors")
    class CursorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CURSORS_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    resume_token: str
    cursors: _containers.ScalarMap[str, int]
    def __init__(self, session_id: _Optional[str] = ..., resume_token: _Optional[str] = ..., cursors: _Optional[_Mapping[str, int]] = ...) -> None: ...

class Subscribe(_message.Message):
    __slots__ = ("channel_ids", "thread_root_ids")
    CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_IDS_FIELD_NUMBER: _ClassVar[int]
    channel_ids: _containers.RepeatedScalarFieldContainer[str]
    thread_root_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, channel_ids: _Optional[_Iterable[str]] = ..., thread_root_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class Unsubscribe(_message.Message):
    __slots__ = ("channel_ids", "thread_root_ids")
    CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_IDS_FIELD_NUMBER: _ClassVar[int]
    channel_ids: _containers.RepeatedScalarFieldContainer[str]
    thread_root_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, channel_ids: _Optional[_Iterable[str]] = ..., thread_root_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class PresenceSubscribe(_message.Message):
    __slots__ = ("user_ids",)
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class TypingFrame(_message.Message):
    __slots__ = ("channel_id", "thread_root_id")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    thread_root_id: str
    def __init__(self, channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ...) -> None: ...

class Focus(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class Ping(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClientFrame(_message.Message):
    __slots__ = ("hello", "resume", "subscribe", "unsubscribe", "presence_subscribe", "typing", "focus", "ping")
    HELLO_FIELD_NUMBER: _ClassVar[int]
    RESUME_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_FIELD_NUMBER: _ClassVar[int]
    UNSUBSCRIBE_FIELD_NUMBER: _ClassVar[int]
    PRESENCE_SUBSCRIBE_FIELD_NUMBER: _ClassVar[int]
    TYPING_FIELD_NUMBER: _ClassVar[int]
    FOCUS_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    hello: Hello
    resume: Resume
    subscribe: Subscribe
    unsubscribe: Unsubscribe
    presence_subscribe: PresenceSubscribe
    typing: TypingFrame
    focus: Focus
    ping: Ping
    def __init__(self, hello: _Optional[_Union[Hello, _Mapping]] = ..., resume: _Optional[_Union[Resume, _Mapping]] = ..., subscribe: _Optional[_Union[Subscribe, _Mapping]] = ..., unsubscribe: _Optional[_Union[Unsubscribe, _Mapping]] = ..., presence_subscribe: _Optional[_Union[PresenceSubscribe, _Mapping]] = ..., typing: _Optional[_Union[TypingFrame, _Mapping]] = ..., focus: _Optional[_Union[Focus, _Mapping]] = ..., ping: _Optional[_Union[Ping, _Mapping]] = ...) -> None: ...

class Ready(_message.Message):
    __slots__ = ("session_id", "resume_token", "heartbeat_interval_ms", "server_time")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_INTERVAL_MS_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIME_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    resume_token: str
    heartbeat_interval_ms: int
    server_time: _timestamp_pb2.Timestamp
    def __init__(self, session_id: _Optional[str] = ..., resume_token: _Optional[str] = ..., heartbeat_interval_ms: _Optional[int] = ..., server_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Resumed(_message.Message):
    __slots__ = ("replayed",)
    REPLAYED_FIELD_NUMBER: _ClassVar[int]
    replayed: int
    def __init__(self, replayed: _Optional[int] = ...) -> None: ...

class ResyncRequired(_message.Message):
    __slots__ = ("reason", "workspace_id")
    REASON_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    reason: str
    workspace_id: str
    def __init__(self, reason: _Optional[str] = ..., workspace_id: _Optional[str] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("cursor", "envelope")
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    ENVELOPE_FIELD_NUMBER: _ClassVar[int]
    cursor: int
    envelope: _events_pb2.Envelope
    def __init__(self, cursor: _Optional[int] = ..., envelope: _Optional[_Union[_events_pb2.Envelope, _Mapping]] = ...) -> None: ...

class Pong(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Error(_message.Message):
    __slots__ = ("code", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: ErrorCode
    message: str
    def __init__(self, code: _Optional[_Union[ErrorCode, str]] = ..., message: _Optional[str] = ...) -> None: ...

class ServerFrame(_message.Message):
    __slots__ = ("ready", "resumed", "resync_required", "event", "pong", "error", "typing", "presence", "agent_status")
    READY_FIELD_NUMBER: _ClassVar[int]
    RESUMED_FIELD_NUMBER: _ClassVar[int]
    RESYNC_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    PONG_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TYPING_FIELD_NUMBER: _ClassVar[int]
    PRESENCE_FIELD_NUMBER: _ClassVar[int]
    AGENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    ready: Ready
    resumed: Resumed
    resync_required: ResyncRequired
    event: Event
    pong: Pong
    error: Error
    typing: _events_pb2.Typing
    presence: _events_pb2.PresenceChanged
    agent_status: _events_pb2.AgentStatus
    def __init__(self, ready: _Optional[_Union[Ready, _Mapping]] = ..., resumed: _Optional[_Union[Resumed, _Mapping]] = ..., resync_required: _Optional[_Union[ResyncRequired, _Mapping]] = ..., event: _Optional[_Union[Event, _Mapping]] = ..., pong: _Optional[_Union[Pong, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ..., typing: _Optional[_Union[_events_pb2.Typing, _Mapping]] = ..., presence: _Optional[_Union[_events_pb2.PresenceChanged, _Mapping]] = ..., agent_status: _Optional[_Union[_events_pb2.AgentStatus, _Mapping]] = ...) -> None: ...
