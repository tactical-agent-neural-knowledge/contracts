from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tank.ai.v1 import ai_pb2 as _ai_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApiKey(_message.Message):
    __slots__ = ("id", "name", "last4", "created_at", "last_used_at", "created_by")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LAST4_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    last4: str
    created_at: _timestamp_pb2.Timestamp
    last_used_at: _timestamp_pb2.Timestamp
    created_by: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., last4: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_used_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ...) -> None: ...

class ListApiKeysRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListApiKeysResponse(_message.Message):
    __slots__ = ("keys",)
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[ApiKey]
    def __init__(self, keys: _Optional[_Iterable[_Union[ApiKey, _Mapping]]] = ...) -> None: ...

class CreateApiKeyRequest(_message.Message):
    __slots__ = ("workspace_id", "name")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    name: str
    def __init__(self, workspace_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CreateApiKeyResponse(_message.Message):
    __slots__ = ("key", "secret")
    KEY_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    key: ApiKey
    secret: str
    def __init__(self, key: _Optional[_Union[ApiKey, _Mapping]] = ..., secret: _Optional[str] = ...) -> None: ...

class RevokeApiKeyRequest(_message.Message):
    __slots__ = ("workspace_id", "key_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    key_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., key_id: _Optional[str] = ...) -> None: ...

class RevokeApiKeyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UsageDay(_message.Message):
    __slots__ = ("day", "key_id", "requests", "input_tokens", "output_tokens", "charge_usd")
    DAY_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CHARGE_USD_FIELD_NUMBER: _ClassVar[int]
    day: str
    key_id: str
    requests: int
    input_tokens: int
    output_tokens: int
    charge_usd: float
    def __init__(self, day: _Optional[str] = ..., key_id: _Optional[str] = ..., requests: _Optional[int] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., charge_usd: _Optional[float] = ...) -> None: ...

class GetApiUsageRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class GetApiUsageResponse(_message.Message):
    __slots__ = ("days", "requests", "input_tokens", "output_tokens", "charge_usd")
    DAYS_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CHARGE_USD_FIELD_NUMBER: _ClassVar[int]
    days: _containers.RepeatedCompositeFieldContainer[UsageDay]
    requests: int
    input_tokens: int
    output_tokens: int
    charge_usd: float
    def __init__(self, days: _Optional[_Iterable[_Union[UsageDay, _Mapping]]] = ..., requests: _Optional[int] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., charge_usd: _Optional[float] = ...) -> None: ...

class ChatMessage(_message.Message):
    __slots__ = ("role", "text", "attachments")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    role: str
    text: str
    attachments: _containers.RepeatedCompositeFieldContainer[_ai_pb2.Attachment]
    def __init__(self, role: _Optional[str] = ..., text: _Optional[str] = ..., attachments: _Optional[_Iterable[_Union[_ai_pb2.Attachment, _Mapping]]] = ...) -> None: ...

class ChatRequest(_message.Message):
    __slots__ = ("messages", "instructions", "look_up")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    LOOK_UP_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[ChatMessage]
    instructions: str
    look_up: bool
    def __init__(self, messages: _Optional[_Iterable[_Union[ChatMessage, _Mapping]]] = ..., instructions: _Optional[str] = ..., look_up: bool = ...) -> None: ...

class ChatDone(_message.Message):
    __slots__ = ("id", "stop_reason", "input_tokens", "output_tokens", "charge_usd")
    ID_FIELD_NUMBER: _ClassVar[int]
    STOP_REASON_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CHARGE_USD_FIELD_NUMBER: _ClassVar[int]
    id: str
    stop_reason: str
    input_tokens: int
    output_tokens: int
    charge_usd: float
    def __init__(self, id: _Optional[str] = ..., stop_reason: _Optional[str] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., charge_usd: _Optional[float] = ...) -> None: ...

class ChatResponse(_message.Message):
    __slots__ = ("delta", "done")
    DELTA_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    delta: str
    done: ChatDone
    def __init__(self, delta: _Optional[str] = ..., done: _Optional[_Union[ChatDone, _Mapping]] = ...) -> None: ...
