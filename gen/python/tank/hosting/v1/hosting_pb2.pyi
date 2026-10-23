from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetProductRequest(_message.Message):
    __slots__ = ("channel_id", "tail_lines")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TAIL_LINES_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    tail_lines: int
    def __init__(self, channel_id: _Optional[str] = ..., tail_lines: _Optional[int] = ...) -> None: ...

class GetProductResponse(_message.Message):
    __slots__ = ("product", "logs", "events")
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    product: Product
    logs: str
    events: _containers.RepeatedCompositeFieldContainer[ProductEvent]
    def __init__(self, product: _Optional[_Union[Product, _Mapping]] = ..., logs: _Optional[str] = ..., events: _Optional[_Iterable[_Union[ProductEvent, _Mapping]]] = ...) -> None: ...

class Product(_message.Message):
    __slots__ = ("slug", "repo", "url", "awake", "status", "image_tag", "restarts", "last_exit_reason", "started_at", "cpu_limit", "memory_limit", "disk_bytes", "can_manage", "managed", "updated_at")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    REPO_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    AWAKE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    RESTARTS_FIELD_NUMBER: _ClassVar[int]
    LAST_EXIT_REASON_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    CPU_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    DISK_BYTES_FIELD_NUMBER: _ClassVar[int]
    CAN_MANAGE_FIELD_NUMBER: _ClassVar[int]
    MANAGED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    slug: str
    repo: str
    url: str
    awake: bool
    status: str
    image_tag: str
    restarts: int
    last_exit_reason: str
    started_at: _timestamp_pb2.Timestamp
    cpu_limit: str
    memory_limit: str
    disk_bytes: int
    can_manage: bool
    managed: bool
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, slug: _Optional[str] = ..., repo: _Optional[str] = ..., url: _Optional[str] = ..., awake: bool = ..., status: _Optional[str] = ..., image_tag: _Optional[str] = ..., restarts: _Optional[int] = ..., last_exit_reason: _Optional[str] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cpu_limit: _Optional[str] = ..., memory_limit: _Optional[str] = ..., disk_bytes: _Optional[int] = ..., can_manage: bool = ..., managed: bool = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ProductEvent(_message.Message):
    __slots__ = ("at", "type", "reason", "message")
    AT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    at: _timestamp_pb2.Timestamp
    type: str
    reason: str
    message: str
    def __init__(self, at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., type: _Optional[str] = ..., reason: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class CheckProductRequest(_message.Message):
    __slots__ = ("channel_id", "path")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    path: str
    def __init__(self, channel_id: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class CheckProductResponse(_message.Message):
    __slots__ = ("check",)
    CHECK_FIELD_NUMBER: _ClassVar[int]
    check: LiveCheck
    def __init__(self, check: _Optional[_Union[LiveCheck, _Mapping]] = ...) -> None: ...

class LiveCheck(_message.Message):
    __slots__ = ("url", "status", "build_sha", "title", "text_length", "errors", "screenshot_png", "checked_at", "note")
    URL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BUILD_SHA_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    SCREENSHOT_PNG_FIELD_NUMBER: _ClassVar[int]
    CHECKED_AT_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    url: str
    status: int
    build_sha: str
    title: str
    text_length: int
    errors: _containers.RepeatedScalarFieldContainer[str]
    screenshot_png: bytes
    checked_at: _timestamp_pb2.Timestamp
    note: str
    def __init__(self, url: _Optional[str] = ..., status: _Optional[int] = ..., build_sha: _Optional[str] = ..., title: _Optional[str] = ..., text_length: _Optional[int] = ..., errors: _Optional[_Iterable[str]] = ..., screenshot_png: _Optional[bytes] = ..., checked_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., note: _Optional[str] = ...) -> None: ...
