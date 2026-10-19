from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROLE_UNSPECIFIED: _ClassVar[Role]
    ROLE_USER: _ClassVar[Role]
    ROLE_ASSISTANT: _ClassVar[Role]
ROLE_UNSPECIFIED: Role
ROLE_USER: Role
ROLE_ASSISTANT: Role

class Conversation(_message.Message):
    __slots__ = ("id", "title", "created_at", "updated_at", "preview", "pinned")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    PINNED_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    preview: str
    pinned: bool
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., preview: _Optional[str] = ..., pinned: bool = ...) -> None: ...

class Attachment(_message.Message):
    __slots__ = ("id", "name", "mime", "data", "size")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MIME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    mime: str
    data: bytes
    size: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., mime: _Optional[str] = ..., data: _Optional[bytes] = ..., size: _Optional[int] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ("id", "conversation_id", "role", "text", "attachments", "created_at", "stop_reason", "input_tokens", "output_tokens", "rating")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STOP_REASON_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    id: str
    conversation_id: str
    role: Role
    text: str
    attachments: _containers.RepeatedCompositeFieldContainer[Attachment]
    created_at: _timestamp_pb2.Timestamp
    stop_reason: str
    input_tokens: int
    output_tokens: int
    rating: int
    def __init__(self, id: _Optional[str] = ..., conversation_id: _Optional[str] = ..., role: _Optional[_Union[Role, str]] = ..., text: _Optional[str] = ..., attachments: _Optional[_Iterable[_Union[Attachment, _Mapping]]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., stop_reason: _Optional[str] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., rating: _Optional[int] = ...) -> None: ...

class ListConversationsRequest(_message.Message):
    __slots__ = ("query", "limit")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    query: str
    limit: int
    def __init__(self, query: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListConversationsResponse(_message.Message):
    __slots__ = ("conversations",)
    CONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    conversations: _containers.RepeatedCompositeFieldContainer[Conversation]
    def __init__(self, conversations: _Optional[_Iterable[_Union[Conversation, _Mapping]]] = ...) -> None: ...

class GetConversationRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetConversationResponse(_message.Message):
    __slots__ = ("conversation", "messages")
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    conversation: Conversation
    messages: _containers.RepeatedCompositeFieldContainer[Message]
    def __init__(self, conversation: _Optional[_Union[Conversation, _Mapping]] = ..., messages: _Optional[_Iterable[_Union[Message, _Mapping]]] = ...) -> None: ...

class CreateConversationRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateConversationResponse(_message.Message):
    __slots__ = ("conversation",)
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    conversation: Conversation
    def __init__(self, conversation: _Optional[_Union[Conversation, _Mapping]] = ...) -> None: ...

class UpdateConversationRequest(_message.Message):
    __slots__ = ("id", "title", "set_title", "pinned", "set_pinned")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SET_TITLE_FIELD_NUMBER: _ClassVar[int]
    PINNED_FIELD_NUMBER: _ClassVar[int]
    SET_PINNED_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    set_title: bool
    pinned: bool
    set_pinned: bool
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., set_title: bool = ..., pinned: bool = ..., set_pinned: bool = ...) -> None: ...

class UpdateConversationResponse(_message.Message):
    __slots__ = ("conversation",)
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    conversation: Conversation
    def __init__(self, conversation: _Optional[_Union[Conversation, _Mapping]] = ...) -> None: ...

class DeleteConversationRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteConversationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendMessageRequest(_message.Message):
    __slots__ = ("conversation_id", "text", "attachments", "regenerate_message_id", "replace_message_id")
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    REGENERATE_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    REPLACE_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    text: str
    attachments: _containers.RepeatedCompositeFieldContainer[Attachment]
    regenerate_message_id: str
    replace_message_id: str
    def __init__(self, conversation_id: _Optional[str] = ..., text: _Optional[str] = ..., attachments: _Optional[_Iterable[_Union[Attachment, _Mapping]]] = ..., regenerate_message_id: _Optional[str] = ..., replace_message_id: _Optional[str] = ...) -> None: ...

class SendMessageResponse(_message.Message):
    __slots__ = ("started", "delta", "done", "title")
    STARTED_FIELD_NUMBER: _ClassVar[int]
    DELTA_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    started: Started
    delta: str
    done: Message
    title: str
    def __init__(self, started: _Optional[_Union[Started, _Mapping]] = ..., delta: _Optional[str] = ..., done: _Optional[_Union[Message, _Mapping]] = ..., title: _Optional[str] = ...) -> None: ...

class Started(_message.Message):
    __slots__ = ("conversation", "user_message", "assistant_message_id")
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ASSISTANT_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    conversation: Conversation
    user_message: Message
    assistant_message_id: str
    def __init__(self, conversation: _Optional[_Union[Conversation, _Mapping]] = ..., user_message: _Optional[_Union[Message, _Mapping]] = ..., assistant_message_id: _Optional[str] = ...) -> None: ...

class RateMessageRequest(_message.Message):
    __slots__ = ("message_id", "rating")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    rating: int
    def __init__(self, message_id: _Optional[str] = ..., rating: _Optional[int] = ...) -> None: ...

class RateMessageResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSettingsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: Settings
    def __init__(self, settings: _Optional[_Union[Settings, _Mapping]] = ...) -> None: ...

class Settings(_message.Message):
    __slots__ = ("instructions", "model_label")
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    MODEL_LABEL_FIELD_NUMBER: _ClassVar[int]
    instructions: str
    model_label: str
    def __init__(self, instructions: _Optional[str] = ..., model_label: _Optional[str] = ...) -> None: ...

class UpdateSettingsRequest(_message.Message):
    __slots__ = ("instructions",)
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    instructions: str
    def __init__(self, instructions: _Optional[str] = ...) -> None: ...

class UpdateSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: Settings
    def __init__(self, settings: _Optional[_Union[Settings, _Mapping]] = ...) -> None: ...
