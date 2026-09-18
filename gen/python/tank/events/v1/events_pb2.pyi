from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tank.blocks.v1 import blocks_pb2 as _blocks_pb2
from tank.message.v1 import message_pb2 as _message_pb2
from tank.presence.v1 import presence_pb2 as _presence_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Envelope(_message.Message):
    __slots__ = ("id", "workspace_id", "type", "subject", "occurred_at", "trace_parent", "payload")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    TRACE_PARENT_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    type: str
    subject: str
    occurred_at: _timestamp_pb2.Timestamp
    trace_parent: str
    payload: _any_pb2.Any
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., type: _Optional[str] = ..., subject: _Optional[str] = ..., occurred_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., trace_parent: _Optional[str] = ..., payload: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class MessageCreated(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _message_pb2.Message
    def __init__(self, message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class MessageUpdated(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _message_pb2.Message
    def __init__(self, message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class MessageDeleted(_message.Message):
    __slots__ = ("message_id", "channel_id", "thread_root_id")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    channel_id: str
    thread_root_id: str
    def __init__(self, message_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ...) -> None: ...

class ReactionAdded(_message.Message):
    __slots__ = ("message_id", "user_id", "emoji")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    user_id: str
    emoji: str
    def __init__(self, message_id: _Optional[str] = ..., user_id: _Optional[str] = ..., emoji: _Optional[str] = ...) -> None: ...

class ReactionRemoved(_message.Message):
    __slots__ = ("message_id", "user_id", "emoji")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    user_id: str
    emoji: str
    def __init__(self, message_id: _Optional[str] = ..., user_id: _Optional[str] = ..., emoji: _Optional[str] = ...) -> None: ...

class ReadStateUpdated(_message.Message):
    __slots__ = ("user_id", "channel_id", "last_read_seq", "thread_root_id", "last_read_thread_seq")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_READ_SEQ_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_READ_THREAD_SEQ_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    channel_id: str
    last_read_seq: int
    thread_root_id: str
    last_read_thread_seq: int
    def __init__(self, user_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., last_read_seq: _Optional[int] = ..., thread_root_id: _Optional[str] = ..., last_read_thread_seq: _Optional[int] = ...) -> None: ...

class ChannelUpdated(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class ChannelMembershipChanged(_message.Message):
    __slots__ = ("channel_id", "user_id", "joined")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    JOINED_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    user_id: str
    joined: bool
    def __init__(self, channel_id: _Optional[str] = ..., user_id: _Optional[str] = ..., joined: bool = ...) -> None: ...

class CardAction(_message.Message):
    __slots__ = ("action",)
    ACTION_FIELD_NUMBER: _ClassVar[int]
    action: _blocks_pb2.BlockAction
    def __init__(self, action: _Optional[_Union[_blocks_pb2.BlockAction, _Mapping]] = ...) -> None: ...

class AppCommand(_message.Message):
    __slots__ = ("command", "text", "user_id", "channel_id", "thread_root_id")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    command: str
    text: str
    user_id: str
    channel_id: str
    thread_root_id: str
    def __init__(self, command: _Optional[str] = ..., text: _Optional[str] = ..., user_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ...) -> None: ...

class PresenceChanged(_message.Message):
    __slots__ = ("presence",)
    PRESENCE_FIELD_NUMBER: _ClassVar[int]
    presence: _presence_pb2.Presence
    def __init__(self, presence: _Optional[_Union[_presence_pb2.Presence, _Mapping]] = ...) -> None: ...

class Typing(_message.Message):
    __slots__ = ("channel_id", "user_id", "thread_root_id")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    user_id: str
    thread_root_id: str
    def __init__(self, channel_id: _Optional[str] = ..., user_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ...) -> None: ...

class AgentStatus(_message.Message):
    __slots__ = ("channel_id", "thread_root_id", "run_id", "status")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    thread_root_id: str
    run_id: str
    status: str
    def __init__(self, channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., run_id: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class NotificationCreated(_message.Message):
    __slots__ = ("notification_id", "kind", "message_id", "channel_id", "actor_id")
    NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    notification_id: str
    kind: str
    message_id: str
    channel_id: str
    actor_id: str
    def __init__(self, notification_id: _Optional[str] = ..., kind: _Optional[str] = ..., message_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., actor_id: _Optional[str] = ...) -> None: ...
