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

class Resource(_message.Message):
    __slots__ = ("name", "kind", "size", "cpu", "memory", "public", "min", "max", "schedule", "timeout_seconds", "volume", "ready", "desired", "paused", "last_run_at", "last_run_result")
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    READY_FIELD_NUMBER: _ClassVar[int]
    DESIRED_FIELD_NUMBER: _ClassVar[int]
    PAUSED_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_RESULT_FIELD_NUMBER: _ClassVar[int]
    name: str
    kind: str
    size: str
    cpu: str
    memory: str
    public: bool
    min: int
    max: int
    schedule: str
    timeout_seconds: int
    volume: str
    ready: int
    desired: int
    paused: bool
    last_run_at: _timestamp_pb2.Timestamp
    last_run_result: str
    def __init__(self, name: _Optional[str] = ..., kind: _Optional[str] = ..., size: _Optional[str] = ..., cpu: _Optional[str] = ..., memory: _Optional[str] = ..., public: bool = ..., min: _Optional[int] = ..., max: _Optional[int] = ..., schedule: _Optional[str] = ..., timeout_seconds: _Optional[int] = ..., volume: _Optional[str] = ..., ready: _Optional[int] = ..., desired: _Optional[int] = ..., paused: bool = ..., last_run_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_run_result: _Optional[str] = ...) -> None: ...

class Cost(_message.Message):
    __slots__ = ("base_cents", "overage_cents", "total_cents", "lines")
    BASE_CENTS_FIELD_NUMBER: _ClassVar[int]
    OVERAGE_CENTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CENTS_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    base_cents: int
    overage_cents: int
    total_cents: int
    lines: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base_cents: _Optional[int] = ..., overage_cents: _Optional[int] = ..., total_cents: _Optional[int] = ..., lines: _Optional[_Iterable[str]] = ...) -> None: ...

class PendingBuild(_message.Message):
    __slots__ = ("sha", "reason", "problems", "estimate", "at", "can_approve")
    SHA_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    CAN_APPROVE_FIELD_NUMBER: _ClassVar[int]
    sha: str
    reason: str
    problems: _containers.RepeatedScalarFieldContainer[str]
    estimate: Cost
    at: _timestamp_pb2.Timestamp
    can_approve: bool
    def __init__(self, sha: _Optional[str] = ..., reason: _Optional[str] = ..., problems: _Optional[_Iterable[str]] = ..., estimate: _Optional[_Union[Cost, _Mapping]] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., can_approve: bool = ...) -> None: ...

class GetResourcesRequest(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class GetResourcesResponse(_message.Message):
    __slots__ = ("resources", "estimate", "pending", "secrets", "can_manage")
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    PENDING_FIELD_NUMBER: _ClassVar[int]
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    CAN_MANAGE_FIELD_NUMBER: _ClassVar[int]
    resources: _containers.RepeatedCompositeFieldContainer[Resource]
    estimate: Cost
    pending: PendingBuild
    secrets: _containers.RepeatedScalarFieldContainer[str]
    can_manage: bool
    def __init__(self, resources: _Optional[_Iterable[_Union[Resource, _Mapping]]] = ..., estimate: _Optional[_Union[Cost, _Mapping]] = ..., pending: _Optional[_Union[PendingBuild, _Mapping]] = ..., secrets: _Optional[_Iterable[str]] = ..., can_manage: bool = ...) -> None: ...

class ApproveBuildRequest(_message.Message):
    __slots__ = ("channel_id", "sha")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SHA_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    sha: str
    def __init__(self, channel_id: _Optional[str] = ..., sha: _Optional[str] = ...) -> None: ...

class ApproveBuildResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OperateRequest(_message.Message):
    __slots__ = ("channel_id", "action", "process")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PROCESS_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    action: str
    process: str
    def __init__(self, channel_id: _Optional[str] = ..., action: _Optional[str] = ..., process: _Optional[str] = ...) -> None: ...

class OperateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Change(_message.Message):
    __slots__ = ("sha", "message", "at")
    SHA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    sha: str
    message: str
    at: _timestamp_pb2.Timestamp
    def __init__(self, sha: _Optional[str] = ..., message: _Optional[str] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListChangesRequest(_message.Message):
    __slots__ = ("channel_id", "limit")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    limit: int
    def __init__(self, channel_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListChangesResponse(_message.Message):
    __slots__ = ("changes",)
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[Change]
    def __init__(self, changes: _Optional[_Iterable[_Union[Change, _Mapping]]] = ...) -> None: ...

class RollbackRequest(_message.Message):
    __slots__ = ("channel_id", "sha")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SHA_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    sha: str
    def __init__(self, channel_id: _Optional[str] = ..., sha: _Optional[str] = ...) -> None: ...

class RollbackResponse(_message.Message):
    __slots__ = ("applied", "reason", "problems", "estimate")
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    applied: bool
    reason: str
    problems: _containers.RepeatedScalarFieldContainer[str]
    estimate: Cost
    def __init__(self, applied: bool = ..., reason: _Optional[str] = ..., problems: _Optional[_Iterable[str]] = ..., estimate: _Optional[_Union[Cost, _Mapping]] = ...) -> None: ...

class UpdateResourceRequest(_message.Message):
    __slots__ = ("channel_id", "name", "size", "min", "max", "schedule")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    name: str
    size: str
    min: int
    max: int
    schedule: str
    def __init__(self, channel_id: _Optional[str] = ..., name: _Optional[str] = ..., size: _Optional[str] = ..., min: _Optional[int] = ..., max: _Optional[int] = ..., schedule: _Optional[str] = ...) -> None: ...

class UpdateResourceResponse(_message.Message):
    __slots__ = ("estimate",)
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    estimate: Cost
    def __init__(self, estimate: _Optional[_Union[Cost, _Mapping]] = ...) -> None: ...
