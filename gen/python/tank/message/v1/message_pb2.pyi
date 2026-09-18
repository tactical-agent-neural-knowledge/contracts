from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tank.auth.v1 import auth_pb2 as _auth_pb2
from tank.blocks.v1 import blocks_pb2 as _blocks_pb2
from tank.richtext.v1 import richtext_pb2 as _richtext_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MESSAGE_KIND_UNSPECIFIED: _ClassVar[MessageKind]
    MESSAGE_KIND_MESSAGE: _ClassVar[MessageKind]
    MESSAGE_KIND_SYSTEM: _ClassVar[MessageKind]
    MESSAGE_KIND_AGENT_EVENT: _ClassVar[MessageKind]
    MESSAGE_KIND_BOT: _ClassVar[MessageKind]
MESSAGE_KIND_UNSPECIFIED: MessageKind
MESSAGE_KIND_MESSAGE: MessageKind
MESSAGE_KIND_SYSTEM: MessageKind
MESSAGE_KIND_AGENT_EVENT: MessageKind
MESSAGE_KIND_BOT: MessageKind

class Reaction(_message.Message):
    __slots__ = ("emoji", "count", "user_ids", "reacted")
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    REACTED_FIELD_NUMBER: _ClassVar[int]
    emoji: str
    count: int
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    reacted: bool
    def __init__(self, emoji: _Optional[str] = ..., count: _Optional[int] = ..., user_ids: _Optional[_Iterable[str]] = ..., reacted: bool = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ("id", "workspace_id", "channel_id", "channel_seq", "thread_root_id", "thread_seq", "author_id", "author_kind", "kind", "client_msg_id", "text", "rich_text", "blocks", "mention_ids", "file_ids", "reactions", "edited_at", "deleted_at", "reply_count", "last_reply_at", "reply_user_ids", "metadata", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_SEQ_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_SEQ_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_KIND_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    CLIENT_MSG_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    MENTION_IDS_FIELD_NUMBER: _ClassVar[int]
    FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    REACTIONS_FIELD_NUMBER: _ClassVar[int]
    EDITED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    REPLY_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_REPLY_AT_FIELD_NUMBER: _ClassVar[int]
    REPLY_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    channel_id: str
    channel_seq: int
    thread_root_id: str
    thread_seq: int
    author_id: str
    author_kind: _auth_pb2.PrincipalKind
    kind: MessageKind
    client_msg_id: str
    text: str
    rich_text: _richtext_pb2.RichText
    blocks: _blocks_pb2.Blocks
    mention_ids: _containers.RepeatedScalarFieldContainer[str]
    file_ids: _containers.RepeatedScalarFieldContainer[str]
    reactions: _containers.RepeatedCompositeFieldContainer[Reaction]
    edited_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    reply_count: int
    last_reply_at: _timestamp_pb2.Timestamp
    reply_user_ids: _containers.RepeatedScalarFieldContainer[str]
    metadata: _struct_pb2.Struct
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., channel_seq: _Optional[int] = ..., thread_root_id: _Optional[str] = ..., thread_seq: _Optional[int] = ..., author_id: _Optional[str] = ..., author_kind: _Optional[_Union[_auth_pb2.PrincipalKind, str]] = ..., kind: _Optional[_Union[MessageKind, str]] = ..., client_msg_id: _Optional[str] = ..., text: _Optional[str] = ..., rich_text: _Optional[_Union[_richtext_pb2.RichText, _Mapping]] = ..., blocks: _Optional[_Union[_blocks_pb2.Blocks, _Mapping]] = ..., mention_ids: _Optional[_Iterable[str]] = ..., file_ids: _Optional[_Iterable[str]] = ..., reactions: _Optional[_Iterable[_Union[Reaction, _Mapping]]] = ..., edited_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., reply_count: _Optional[int] = ..., last_reply_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., reply_user_ids: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PostMessageRequest(_message.Message):
    __slots__ = ("channel_id", "thread_root_id", "client_msg_id", "text", "rich_text", "blocks", "file_ids", "kind", "metadata", "also_send_to_channel", "ephemeral", "ephemeral_user_id")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_MSG_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ALSO_SEND_TO_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    EPHEMERAL_FIELD_NUMBER: _ClassVar[int]
    EPHEMERAL_USER_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    thread_root_id: str
    client_msg_id: str
    text: str
    rich_text: _richtext_pb2.RichText
    blocks: _blocks_pb2.Blocks
    file_ids: _containers.RepeatedScalarFieldContainer[str]
    kind: MessageKind
    metadata: _struct_pb2.Struct
    also_send_to_channel: bool
    ephemeral: bool
    ephemeral_user_id: str
    def __init__(self, channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., client_msg_id: _Optional[str] = ..., text: _Optional[str] = ..., rich_text: _Optional[_Union[_richtext_pb2.RichText, _Mapping]] = ..., blocks: _Optional[_Union[_blocks_pb2.Blocks, _Mapping]] = ..., file_ids: _Optional[_Iterable[str]] = ..., kind: _Optional[_Union[MessageKind, str]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., also_send_to_channel: bool = ..., ephemeral: bool = ..., ephemeral_user_id: _Optional[str] = ...) -> None: ...

class PostMessageResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: Message
    def __init__(self, message: _Optional[_Union[Message, _Mapping]] = ...) -> None: ...

class UpdateMessageRequest(_message.Message):
    __slots__ = ("message_id", "text", "rich_text", "blocks", "metadata", "stream_seq")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STREAM_SEQ_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    text: str
    rich_text: _richtext_pb2.RichText
    blocks: _blocks_pb2.Blocks
    metadata: _struct_pb2.Struct
    stream_seq: int
    def __init__(self, message_id: _Optional[str] = ..., text: _Optional[str] = ..., rich_text: _Optional[_Union[_richtext_pb2.RichText, _Mapping]] = ..., blocks: _Optional[_Union[_blocks_pb2.Blocks, _Mapping]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., stream_seq: _Optional[int] = ...) -> None: ...

class UpdateMessageResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: Message
    def __init__(self, message: _Optional[_Union[Message, _Mapping]] = ...) -> None: ...

class DeleteMessageRequest(_message.Message):
    __slots__ = ("message_id",)
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    def __init__(self, message_id: _Optional[str] = ...) -> None: ...

class DeleteMessageResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListMessagesRequest(_message.Message):
    __slots__ = ("channel_id", "before_seq", "after_seq", "limit", "kinds")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_SEQ_FIELD_NUMBER: _ClassVar[int]
    AFTER_SEQ_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    KINDS_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    before_seq: int
    after_seq: int
    limit: int
    kinds: _containers.RepeatedScalarFieldContainer[MessageKind]
    def __init__(self, channel_id: _Optional[str] = ..., before_seq: _Optional[int] = ..., after_seq: _Optional[int] = ..., limit: _Optional[int] = ..., kinds: _Optional[_Iterable[_Union[MessageKind, str]]] = ...) -> None: ...

class ListMessagesResponse(_message.Message):
    __slots__ = ("messages", "has_more")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[Message]
    has_more: bool
    def __init__(self, messages: _Optional[_Iterable[_Union[Message, _Mapping]]] = ..., has_more: bool = ...) -> None: ...

class GetThreadRequest(_message.Message):
    __slots__ = ("thread_root_id", "after_thread_seq", "limit")
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    AFTER_THREAD_SEQ_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    thread_root_id: str
    after_thread_seq: int
    limit: int
    def __init__(self, thread_root_id: _Optional[str] = ..., after_thread_seq: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class GetThreadResponse(_message.Message):
    __slots__ = ("root", "replies", "has_more")
    ROOT_FIELD_NUMBER: _ClassVar[int]
    REPLIES_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    root: Message
    replies: _containers.RepeatedCompositeFieldContainer[Message]
    has_more: bool
    def __init__(self, root: _Optional[_Union[Message, _Mapping]] = ..., replies: _Optional[_Iterable[_Union[Message, _Mapping]]] = ..., has_more: bool = ...) -> None: ...

class MarkReadRequest(_message.Message):
    __slots__ = ("channel_id", "seq", "thread_root_id", "thread_seq")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SEQ_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_SEQ_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    seq: int
    thread_root_id: str
    thread_seq: int
    def __init__(self, channel_id: _Optional[str] = ..., seq: _Optional[int] = ..., thread_root_id: _Optional[str] = ..., thread_seq: _Optional[int] = ...) -> None: ...

class MarkReadResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddReactionRequest(_message.Message):
    __slots__ = ("message_id", "emoji")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    emoji: str
    def __init__(self, message_id: _Optional[str] = ..., emoji: _Optional[str] = ...) -> None: ...

class AddReactionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveReactionRequest(_message.Message):
    __slots__ = ("message_id", "emoji")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    emoji: str
    def __init__(self, message_id: _Optional[str] = ..., emoji: _Optional[str] = ...) -> None: ...

class RemoveReactionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubscribeThreadRequest(_message.Message):
    __slots__ = ("thread_root_id", "subscribed")
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    thread_root_id: str
    subscribed: bool
    def __init__(self, thread_root_id: _Optional[str] = ..., subscribed: bool = ...) -> None: ...

class SubscribeThreadResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PostBlockActionRequest(_message.Message):
    __slots__ = ("action",)
    ACTION_FIELD_NUMBER: _ClassVar[int]
    action: _blocks_pb2.BlockAction
    def __init__(self, action: _Optional[_Union[_blocks_pb2.BlockAction, _Mapping]] = ...) -> None: ...

class PostBlockActionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
