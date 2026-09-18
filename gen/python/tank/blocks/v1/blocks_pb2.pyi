from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tank.message.v1 import richtext_pb2 as _richtext_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ButtonStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BUTTON_STYLE_UNSPECIFIED: _ClassVar[ButtonStyle]
    BUTTON_STYLE_PRIMARY: _ClassVar[ButtonStyle]
    BUTTON_STYLE_DANGER: _ClassVar[ButtonStyle]

class StepStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STEP_STATUS_UNSPECIFIED: _ClassVar[StepStatus]
    STEP_STATUS_PENDING: _ClassVar[StepStatus]
    STEP_STATUS_RUNNING: _ClassVar[StepStatus]
    STEP_STATUS_DONE: _ClassVar[StepStatus]
    STEP_STATUS_FAILED: _ClassVar[StepStatus]
    STEP_STATUS_SKIPPED: _ClassVar[StepStatus]

class CheckState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHECK_STATE_UNSPECIFIED: _ClassVar[CheckState]
    CHECK_STATE_QUEUED: _ClassVar[CheckState]
    CHECK_STATE_RUNNING: _ClassVar[CheckState]
    CHECK_STATE_SUCCESS: _ClassVar[CheckState]
    CHECK_STATE_FAILURE: _ClassVar[CheckState]
    CHECK_STATE_CANCELLED: _ClassVar[CheckState]

class GateKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GATE_KIND_UNSPECIFIED: _ClassVar[GateKind]
    GATE_KIND_PLAN: _ClassVar[GateKind]
    GATE_KIND_SCOPE_CHANGE: _ClassVar[GateKind]
    GATE_KIND_MERGE: _ClassVar[GateKind]
    GATE_KIND_DEPLOY: _ClassVar[GateKind]
    GATE_KIND_DESTRUCTIVE_TOOL: _ClassVar[GateKind]
    GATE_KIND_BUDGET_INCREASE: _ClassVar[GateKind]
BUTTON_STYLE_UNSPECIFIED: ButtonStyle
BUTTON_STYLE_PRIMARY: ButtonStyle
BUTTON_STYLE_DANGER: ButtonStyle
STEP_STATUS_UNSPECIFIED: StepStatus
STEP_STATUS_PENDING: StepStatus
STEP_STATUS_RUNNING: StepStatus
STEP_STATUS_DONE: StepStatus
STEP_STATUS_FAILED: StepStatus
STEP_STATUS_SKIPPED: StepStatus
CHECK_STATE_UNSPECIFIED: CheckState
CHECK_STATE_QUEUED: CheckState
CHECK_STATE_RUNNING: CheckState
CHECK_STATE_SUCCESS: CheckState
CHECK_STATE_FAILURE: CheckState
CHECK_STATE_CANCELLED: CheckState
GATE_KIND_UNSPECIFIED: GateKind
GATE_KIND_PLAN: GateKind
GATE_KIND_SCOPE_CHANGE: GateKind
GATE_KIND_MERGE: GateKind
GATE_KIND_DEPLOY: GateKind
GATE_KIND_DESTRUCTIVE_TOOL: GateKind
GATE_KIND_BUDGET_INCREASE: GateKind

class Blocks(_message.Message):
    __slots__ = ("blocks",)
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    blocks: _containers.RepeatedCompositeFieldContainer[Block]
    def __init__(self, blocks: _Optional[_Iterable[_Union[Block, _Mapping]]] = ...) -> None: ...

class Block(_message.Message):
    __slots__ = ("block_id", "header", "section", "context", "divider", "actions", "plan_card", "diff_preview", "ci_status", "approval_prompt", "tool_log", "file_preview", "status_card")
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SECTION_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DIVIDER_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    PLAN_CARD_FIELD_NUMBER: _ClassVar[int]
    DIFF_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    CI_STATUS_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_PROMPT_FIELD_NUMBER: _ClassVar[int]
    TOOL_LOG_FIELD_NUMBER: _ClassVar[int]
    FILE_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    STATUS_CARD_FIELD_NUMBER: _ClassVar[int]
    block_id: str
    header: Header
    section: Section
    context: Context
    divider: Divider
    actions: Actions
    plan_card: PlanCard
    diff_preview: DiffPreview
    ci_status: CiStatus
    approval_prompt: ApprovalPrompt
    tool_log: ToolLog
    file_preview: FilePreview
    status_card: StatusCard
    def __init__(self, block_id: _Optional[str] = ..., header: _Optional[_Union[Header, _Mapping]] = ..., section: _Optional[_Union[Section, _Mapping]] = ..., context: _Optional[_Union[Context, _Mapping]] = ..., divider: _Optional[_Union[Divider, _Mapping]] = ..., actions: _Optional[_Union[Actions, _Mapping]] = ..., plan_card: _Optional[_Union[PlanCard, _Mapping]] = ..., diff_preview: _Optional[_Union[DiffPreview, _Mapping]] = ..., ci_status: _Optional[_Union[CiStatus, _Mapping]] = ..., approval_prompt: _Optional[_Union[ApprovalPrompt, _Mapping]] = ..., tool_log: _Optional[_Union[ToolLog, _Mapping]] = ..., file_preview: _Optional[_Union[FilePreview, _Mapping]] = ..., status_card: _Optional[_Union[StatusCard, _Mapping]] = ...) -> None: ...

class Header(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class Section(_message.Message):
    __slots__ = ("text", "fields", "accessory")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ACCESSORY_FIELD_NUMBER: _ClassVar[int]
    text: _richtext_pb2.RichText
    fields: _containers.RepeatedCompositeFieldContainer[Field]
    accessory: Button
    def __init__(self, text: _Optional[_Union[_richtext_pb2.RichText, _Mapping]] = ..., fields: _Optional[_Iterable[_Union[Field, _Mapping]]] = ..., accessory: _Optional[_Union[Button, _Mapping]] = ...) -> None: ...

class Field(_message.Message):
    __slots__ = ("label", "value")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    label: str
    value: str
    def __init__(self, label: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class Context(_message.Message):
    __slots__ = ("elements",)
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    elements: _containers.RepeatedCompositeFieldContainer[_richtext_pb2.RichText]
    def __init__(self, elements: _Optional[_Iterable[_Union[_richtext_pb2.RichText, _Mapping]]] = ...) -> None: ...

class Divider(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Button(_message.Message):
    __slots__ = ("action_id", "text", "value", "style", "url", "confirm")
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    STYLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_FIELD_NUMBER: _ClassVar[int]
    action_id: str
    text: str
    value: str
    style: ButtonStyle
    url: str
    confirm: Confirm
    def __init__(self, action_id: _Optional[str] = ..., text: _Optional[str] = ..., value: _Optional[str] = ..., style: _Optional[_Union[ButtonStyle, str]] = ..., url: _Optional[str] = ..., confirm: _Optional[_Union[Confirm, _Mapping]] = ...) -> None: ...

class Confirm(_message.Message):
    __slots__ = ("title", "text", "confirm", "deny")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_FIELD_NUMBER: _ClassVar[int]
    DENY_FIELD_NUMBER: _ClassVar[int]
    title: str
    text: str
    confirm: str
    deny: str
    def __init__(self, title: _Optional[str] = ..., text: _Optional[str] = ..., confirm: _Optional[str] = ..., deny: _Optional[str] = ...) -> None: ...

class Actions(_message.Message):
    __slots__ = ("buttons",)
    BUTTONS_FIELD_NUMBER: _ClassVar[int]
    buttons: _containers.RepeatedCompositeFieldContainer[Button]
    def __init__(self, buttons: _Optional[_Iterable[_Union[Button, _Mapping]]] = ...) -> None: ...

class PlanStep(_message.Message):
    __slots__ = ("id", "title", "status", "files")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    status: StepStatus
    files: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., status: _Optional[_Union[StepStatus, str]] = ..., files: _Optional[_Iterable[str]] = ...) -> None: ...

class PlanCard(_message.Message):
    __slots__ = ("summary", "steps", "risks", "questions", "approver_ids", "plan_hash", "version")
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    RISKS_FIELD_NUMBER: _ClassVar[int]
    QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    APPROVER_IDS_FIELD_NUMBER: _ClassVar[int]
    PLAN_HASH_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    summary: str
    steps: _containers.RepeatedCompositeFieldContainer[PlanStep]
    risks: _containers.RepeatedScalarFieldContainer[str]
    questions: _containers.RepeatedScalarFieldContainer[str]
    approver_ids: _containers.RepeatedScalarFieldContainer[str]
    plan_hash: str
    version: int
    def __init__(self, summary: _Optional[str] = ..., steps: _Optional[_Iterable[_Union[PlanStep, _Mapping]]] = ..., risks: _Optional[_Iterable[str]] = ..., questions: _Optional[_Iterable[str]] = ..., approver_ids: _Optional[_Iterable[str]] = ..., plan_hash: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class DiffFile(_message.Message):
    __slots__ = ("path", "additions", "deletions", "hunk_preview")
    PATH_FIELD_NUMBER: _ClassVar[int]
    ADDITIONS_FIELD_NUMBER: _ClassVar[int]
    DELETIONS_FIELD_NUMBER: _ClassVar[int]
    HUNK_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    path: str
    additions: int
    deletions: int
    hunk_preview: str
    def __init__(self, path: _Optional[str] = ..., additions: _Optional[int] = ..., deletions: _Optional[int] = ..., hunk_preview: _Optional[str] = ...) -> None: ...

class DiffPreview(_message.Message):
    __slots__ = ("commit_sha", "compare_url", "files", "total_additions", "total_deletions")
    COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
    COMPARE_URL_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ADDITIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DELETIONS_FIELD_NUMBER: _ClassVar[int]
    commit_sha: str
    compare_url: str
    files: _containers.RepeatedCompositeFieldContainer[DiffFile]
    total_additions: int
    total_deletions: int
    def __init__(self, commit_sha: _Optional[str] = ..., compare_url: _Optional[str] = ..., files: _Optional[_Iterable[_Union[DiffFile, _Mapping]]] = ..., total_additions: _Optional[int] = ..., total_deletions: _Optional[int] = ...) -> None: ...

class Check(_message.Message):
    __slots__ = ("name", "state", "url", "failure_excerpt")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    FAILURE_EXCERPT_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: CheckState
    url: str
    failure_excerpt: str
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[CheckState, str]] = ..., url: _Optional[str] = ..., failure_excerpt: _Optional[str] = ...) -> None: ...

class CiStatus(_message.Message):
    __slots__ = ("head_sha", "checks", "pr_url", "pr_number")
    HEAD_SHA_FIELD_NUMBER: _ClassVar[int]
    CHECKS_FIELD_NUMBER: _ClassVar[int]
    PR_URL_FIELD_NUMBER: _ClassVar[int]
    PR_NUMBER_FIELD_NUMBER: _ClassVar[int]
    head_sha: str
    checks: _containers.RepeatedCompositeFieldContainer[Check]
    pr_url: str
    pr_number: int
    def __init__(self, head_sha: _Optional[str] = ..., checks: _Optional[_Iterable[_Union[Check, _Mapping]]] = ..., pr_url: _Optional[str] = ..., pr_number: _Optional[int] = ...) -> None: ...

class ApprovalPrompt(_message.Message):
    __slots__ = ("gate_id", "kind", "subject", "approver_ids", "min_approvals", "expires_at", "decided", "decision")
    GATE_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    APPROVER_IDS_FIELD_NUMBER: _ClassVar[int]
    MIN_APPROVALS_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    DECIDED_FIELD_NUMBER: _ClassVar[int]
    DECISION_FIELD_NUMBER: _ClassVar[int]
    gate_id: str
    kind: GateKind
    subject: str
    approver_ids: _containers.RepeatedScalarFieldContainer[str]
    min_approvals: int
    expires_at: _timestamp_pb2.Timestamp
    decided: bool
    decision: str
    def __init__(self, gate_id: _Optional[str] = ..., kind: _Optional[_Union[GateKind, str]] = ..., subject: _Optional[str] = ..., approver_ids: _Optional[_Iterable[str]] = ..., min_approvals: _Optional[int] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., decided: bool = ..., decision: _Optional[str] = ...) -> None: ...

class ToolLogEntry(_message.Message):
    __slots__ = ("at", "tool", "summary", "ok")
    AT_FIELD_NUMBER: _ClassVar[int]
    TOOL_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    OK_FIELD_NUMBER: _ClassVar[int]
    at: _timestamp_pb2.Timestamp
    tool: str
    summary: str
    ok: bool
    def __init__(self, at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., tool: _Optional[str] = ..., summary: _Optional[str] = ..., ok: bool = ...) -> None: ...

class ToolLog(_message.Message):
    __slots__ = ("phase", "tool_calls", "files_edited", "recent", "run_panel_url")
    PHASE_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    FILES_EDITED_FIELD_NUMBER: _ClassVar[int]
    RECENT_FIELD_NUMBER: _ClassVar[int]
    RUN_PANEL_URL_FIELD_NUMBER: _ClassVar[int]
    phase: str
    tool_calls: int
    files_edited: int
    recent: _containers.RepeatedCompositeFieldContainer[ToolLogEntry]
    run_panel_url: str
    def __init__(self, phase: _Optional[str] = ..., tool_calls: _Optional[int] = ..., files_edited: _Optional[int] = ..., recent: _Optional[_Iterable[_Union[ToolLogEntry, _Mapping]]] = ..., run_panel_url: _Optional[str] = ...) -> None: ...

class FilePreview(_message.Message):
    __slots__ = ("file_id", "name", "mime", "size", "thumbnail_url")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MIME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_URL_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    name: str
    mime: str
    size: int
    thumbnail_url: str
    def __init__(self, file_id: _Optional[str] = ..., name: _Optional[str] = ..., mime: _Optional[str] = ..., size: _Optional[int] = ..., thumbnail_url: _Optional[str] = ...) -> None: ...

class StatusCard(_message.Message):
    __slots__ = ("run_id", "state", "detail", "branch", "cost_usd", "started_at", "run_panel_url")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    COST_USD_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    RUN_PANEL_URL_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    state: str
    detail: str
    branch: str
    cost_usd: float
    started_at: _timestamp_pb2.Timestamp
    run_panel_url: str
    def __init__(self, run_id: _Optional[str] = ..., state: _Optional[str] = ..., detail: _Optional[str] = ..., branch: _Optional[str] = ..., cost_usd: _Optional[float] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., run_panel_url: _Optional[str] = ...) -> None: ...

class BlockAction(_message.Message):
    __slots__ = ("message_id", "block_id", "action_id", "value", "user_id", "at")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    block_id: str
    action_id: str
    value: str
    user_id: str
    at: _timestamp_pb2.Timestamp
    def __init__(self, message_id: _Optional[str] = ..., block_id: _Optional[str] = ..., action_id: _Optional[str] = ..., value: _Optional[str] = ..., user_id: _Optional[str] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
