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
    __slots__ = ("name", "kind", "size", "cpu", "memory", "public", "min", "max", "schedule", "timeout_seconds", "volume", "ready", "desired", "paused", "last_run_at", "last_run_result", "storage", "extensions", "scratch_gi")
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
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    SCRATCH_GI_FIELD_NUMBER: _ClassVar[int]
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
    storage: str
    extensions: _containers.RepeatedScalarFieldContainer[str]
    scratch_gi: int
    def __init__(self, name: _Optional[str] = ..., kind: _Optional[str] = ..., size: _Optional[str] = ..., cpu: _Optional[str] = ..., memory: _Optional[str] = ..., public: bool = ..., min: _Optional[int] = ..., max: _Optional[int] = ..., schedule: _Optional[str] = ..., timeout_seconds: _Optional[int] = ..., volume: _Optional[str] = ..., ready: _Optional[int] = ..., desired: _Optional[int] = ..., paused: bool = ..., last_run_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_run_result: _Optional[str] = ..., storage: _Optional[str] = ..., extensions: _Optional[_Iterable[str]] = ..., scratch_gi: _Optional[int] = ...) -> None: ...

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
    __slots__ = ("resources", "estimate", "pending", "secrets", "can_manage", "month_cents", "cap_cents", "capped", "can_set_cap", "previews", "secrets_set", "library", "env_keys")
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    PENDING_FIELD_NUMBER: _ClassVar[int]
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    CAN_MANAGE_FIELD_NUMBER: _ClassVar[int]
    MONTH_CENTS_FIELD_NUMBER: _ClassVar[int]
    CAP_CENTS_FIELD_NUMBER: _ClassVar[int]
    CAPPED_FIELD_NUMBER: _ClassVar[int]
    CAN_SET_CAP_FIELD_NUMBER: _ClassVar[int]
    PREVIEWS_FIELD_NUMBER: _ClassVar[int]
    SECRETS_SET_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_FIELD_NUMBER: _ClassVar[int]
    ENV_KEYS_FIELD_NUMBER: _ClassVar[int]
    resources: _containers.RepeatedCompositeFieldContainer[Resource]
    estimate: Cost
    pending: PendingBuild
    secrets: _containers.RepeatedScalarFieldContainer[str]
    can_manage: bool
    month_cents: int
    cap_cents: int
    capped: bool
    can_set_cap: bool
    previews: _containers.RepeatedCompositeFieldContainer[Preview]
    secrets_set: _containers.RepeatedScalarFieldContainer[str]
    library: _containers.RepeatedScalarFieldContainer[str]
    env_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, resources: _Optional[_Iterable[_Union[Resource, _Mapping]]] = ..., estimate: _Optional[_Union[Cost, _Mapping]] = ..., pending: _Optional[_Union[PendingBuild, _Mapping]] = ..., secrets: _Optional[_Iterable[str]] = ..., can_manage: bool = ..., month_cents: _Optional[int] = ..., cap_cents: _Optional[int] = ..., capped: bool = ..., can_set_cap: bool = ..., previews: _Optional[_Iterable[_Union[Preview, _Mapping]]] = ..., secrets_set: _Optional[_Iterable[str]] = ..., library: _Optional[_Iterable[str]] = ..., env_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class Preview(_message.Message):
    __slots__ = ("pull_request", "url", "build", "expires_at")
    PULL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    pull_request: int
    url: str
    build: str
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, pull_request: _Optional[int] = ..., url: _Optional[str] = ..., build: _Optional[str] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

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

class SetCapRequest(_message.Message):
    __slots__ = ("channel_id", "cap_cents")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CAP_CENTS_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    cap_cents: int
    def __init__(self, channel_id: _Optional[str] = ..., cap_cents: _Optional[int] = ...) -> None: ...

class SetCapResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HostedProduct(_message.Message):
    __slots__ = ("channel_id", "channel_name", "slug", "url", "awake", "month_cents", "cap_cents", "capped")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    AWAKE_FIELD_NUMBER: _ClassVar[int]
    MONTH_CENTS_FIELD_NUMBER: _ClassVar[int]
    CAP_CENTS_FIELD_NUMBER: _ClassVar[int]
    CAPPED_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    channel_name: str
    slug: str
    url: str
    awake: bool
    month_cents: int
    cap_cents: int
    capped: bool
    def __init__(self, channel_id: _Optional[str] = ..., channel_name: _Optional[str] = ..., slug: _Optional[str] = ..., url: _Optional[str] = ..., awake: bool = ..., month_cents: _Optional[int] = ..., cap_cents: _Optional[int] = ..., capped: bool = ...) -> None: ...

class ListHostingRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListHostingResponse(_message.Message):
    __slots__ = ("products", "month_cents", "allowance_cents", "can_set")
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    MONTH_CENTS_FIELD_NUMBER: _ClassVar[int]
    ALLOWANCE_CENTS_FIELD_NUMBER: _ClassVar[int]
    CAN_SET_FIELD_NUMBER: _ClassVar[int]
    products: _containers.RepeatedCompositeFieldContainer[HostedProduct]
    month_cents: int
    allowance_cents: int
    can_set: bool
    def __init__(self, products: _Optional[_Iterable[_Union[HostedProduct, _Mapping]]] = ..., month_cents: _Optional[int] = ..., allowance_cents: _Optional[int] = ..., can_set: bool = ...) -> None: ...

class SetAllowanceRequest(_message.Message):
    __slots__ = ("workspace_id", "allowance_cents")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOWANCE_CENTS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    allowance_cents: int
    def __init__(self, workspace_id: _Optional[str] = ..., allowance_cents: _Optional[int] = ...) -> None: ...

class SetAllowanceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExportProductRequest(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class ExportProductResponse(_message.Message):
    __slots__ = ("filename", "content")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    filename: str
    content: str
    def __init__(self, filename: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class SetSecretRequest(_message.Message):
    __slots__ = ("channel_id", "name", "value")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    name: str
    value: str
    def __init__(self, channel_id: _Optional[str] = ..., name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class SetSecretResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResourceChange(_message.Message):
    __slots__ = ("kind", "name", "remove", "size", "min", "max", "schedule", "storage", "extensions", "command", "scratch", "timeout", "value")
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    SCRATCH_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    name: str
    remove: bool
    size: str
    min: int
    max: int
    schedule: str
    storage: str
    extensions: _containers.RepeatedScalarFieldContainer[str]
    command: _containers.RepeatedScalarFieldContainer[str]
    scratch: str
    timeout: str
    value: str
    def __init__(self, kind: _Optional[str] = ..., name: _Optional[str] = ..., remove: bool = ..., size: _Optional[str] = ..., min: _Optional[int] = ..., max: _Optional[int] = ..., schedule: _Optional[str] = ..., storage: _Optional[str] = ..., extensions: _Optional[_Iterable[str]] = ..., command: _Optional[_Iterable[str]] = ..., scratch: _Optional[str] = ..., timeout: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class PreviewChangeRequest(_message.Message):
    __slots__ = ("channel_id", "change", "text")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    change: ResourceChange
    text: str
    def __init__(self, channel_id: _Optional[str] = ..., change: _Optional[_Union[ResourceChange, _Mapping]] = ..., text: _Optional[str] = ...) -> None: ...

class PreviewChangeResponse(_message.Message):
    __slots__ = ("text", "before", "after", "problems", "needs_owner", "can_apply")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    NEEDS_OWNER_FIELD_NUMBER: _ClassVar[int]
    CAN_APPLY_FIELD_NUMBER: _ClassVar[int]
    text: str
    before: Cost
    after: Cost
    problems: _containers.RepeatedScalarFieldContainer[str]
    needs_owner: bool
    can_apply: bool
    def __init__(self, text: _Optional[str] = ..., before: _Optional[_Union[Cost, _Mapping]] = ..., after: _Optional[_Union[Cost, _Mapping]] = ..., problems: _Optional[_Iterable[str]] = ..., needs_owner: bool = ..., can_apply: bool = ...) -> None: ...

class ApplyChangeRequest(_message.Message):
    __slots__ = ("channel_id", "change", "text", "accepted_total_cents")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_TOTAL_CENTS_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    change: ResourceChange
    text: str
    accepted_total_cents: int
    def __init__(self, channel_id: _Optional[str] = ..., change: _Optional[_Union[ResourceChange, _Mapping]] = ..., text: _Optional[str] = ..., accepted_total_cents: _Optional[int] = ...) -> None: ...

class ApplyChangeResponse(_message.Message):
    __slots__ = ("commit_sha", "estimate", "live")
    COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    LIVE_FIELD_NUMBER: _ClassVar[int]
    commit_sha: str
    estimate: Cost
    live: bool
    def __init__(self, commit_sha: _Optional[str] = ..., estimate: _Optional[_Union[Cost, _Mapping]] = ..., live: bool = ...) -> None: ...

class GetSpecTextRequest(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class GetSpecTextResponse(_message.Message):
    __slots__ = ("text", "can_edit")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    CAN_EDIT_FIELD_NUMBER: _ClassVar[int]
    text: str
    can_edit: bool
    def __init__(self, text: _Optional[str] = ..., can_edit: bool = ...) -> None: ...
