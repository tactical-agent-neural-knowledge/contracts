from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tank.agent.v1 import agent_pb2 as _agent_pb2
from tank.blocks.v1 import blocks_pb2 as _blocks_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RunPhase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RUN_PHASE_UNSPECIFIED: _ClassVar[RunPhase]
    RUN_PHASE_PLANNING: _ClassVar[RunPhase]
    RUN_PHASE_IMPLEMENTING: _ClassVar[RunPhase]

class RunEventKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RUN_EVENT_KIND_UNSPECIFIED: _ClassVar[RunEventKind]
    RUN_EVENT_KIND_ASSISTANT_DELTA: _ClassVar[RunEventKind]
    RUN_EVENT_KIND_TOOL_CALL: _ClassVar[RunEventKind]
    RUN_EVENT_KIND_TOOL_RESULT: _ClassVar[RunEventKind]
    RUN_EVENT_KIND_PERMISSION_REQUEST: _ClassVar[RunEventKind]
    RUN_EVENT_KIND_RESULT: _ClassVar[RunEventKind]
    RUN_EVENT_KIND_USAGE: _ClassVar[RunEventKind]
    RUN_EVENT_KIND_STATUS: _ClassVar[RunEventKind]
    RUN_EVENT_KIND_LOG: _ClassVar[RunEventKind]

class InboxKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INBOX_KIND_UNSPECIFIED: _ClassVar[InboxKind]
    INBOX_KIND_STEER: _ClassVar[InboxKind]
    INBOX_KIND_APPROVAL: _ClassVar[InboxKind]
    INBOX_KIND_ANSWER: _ClassVar[InboxKind]
    INBOX_KIND_CANCEL: _ClassVar[InboxKind]
RUN_PHASE_UNSPECIFIED: RunPhase
RUN_PHASE_PLANNING: RunPhase
RUN_PHASE_IMPLEMENTING: RunPhase
RUN_EVENT_KIND_UNSPECIFIED: RunEventKind
RUN_EVENT_KIND_ASSISTANT_DELTA: RunEventKind
RUN_EVENT_KIND_TOOL_CALL: RunEventKind
RUN_EVENT_KIND_TOOL_RESULT: RunEventKind
RUN_EVENT_KIND_PERMISSION_REQUEST: RunEventKind
RUN_EVENT_KIND_RESULT: RunEventKind
RUN_EVENT_KIND_USAGE: RunEventKind
RUN_EVENT_KIND_STATUS: RunEventKind
RUN_EVENT_KIND_LOG: RunEventKind
INBOX_KIND_UNSPECIFIED: InboxKind
INBOX_KIND_STEER: InboxKind
INBOX_KIND_APPROVAL: InboxKind
INBOX_KIND_ANSWER: InboxKind
INBOX_KIND_CANCEL: InboxKind

class Attachment(_message.Message):
    __slots__ = ("file_id", "name", "mime", "size", "message_id")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MIME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    name: str
    mime: str
    size: int
    message_id: str
    def __init__(self, file_id: _Optional[str] = ..., name: _Optional[str] = ..., mime: _Optional[str] = ..., size: _Optional[int] = ..., message_id: _Optional[str] = ...) -> None: ...

class ThreadMessage(_message.Message):
    __slots__ = ("message_id", "author_id", "author_name", "author_kind", "text", "created_at", "attachments")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_KIND_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    author_id: str
    author_name: str
    author_kind: str
    text: str
    created_at: _timestamp_pb2.Timestamp
    attachments: _containers.RepeatedCompositeFieldContainer[Attachment]
    def __init__(self, message_id: _Optional[str] = ..., author_id: _Optional[str] = ..., author_name: _Optional[str] = ..., author_kind: _Optional[str] = ..., text: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., attachments: _Optional[_Iterable[_Union[Attachment, _Mapping]]] = ...) -> None: ...

class PolicySummary(_message.Message):
    __slots__ = ("mode", "tools_deny", "network_allowed_hosts", "default_model", "subagent_model", "max_turns", "max_budget_usd", "rules")
    MODE_FIELD_NUMBER: _ClassVar[int]
    TOOLS_DENY_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ALLOWED_HOSTS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MODEL_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_MODEL_FIELD_NUMBER: _ClassVar[int]
    MAX_TURNS_FIELD_NUMBER: _ClassVar[int]
    MAX_BUDGET_USD_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    mode: str
    tools_deny: _containers.RepeatedScalarFieldContainer[str]
    network_allowed_hosts: _containers.RepeatedScalarFieldContainer[str]
    default_model: str
    subagent_model: str
    max_turns: int
    max_budget_usd: float
    rules: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, mode: _Optional[str] = ..., tools_deny: _Optional[_Iterable[str]] = ..., network_allowed_hosts: _Optional[_Iterable[str]] = ..., default_model: _Optional[str] = ..., subagent_model: _Optional[str] = ..., max_turns: _Optional[int] = ..., max_budget_usd: _Optional[float] = ..., rules: _Optional[_Iterable[str]] = ...) -> None: ...

class ApprovedPlan(_message.Message):
    __slots__ = ("plan_hash", "summary", "steps", "risks", "approved_by", "approved_at", "feedback")
    PLAN_HASH_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    RISKS_FIELD_NUMBER: _ClassVar[int]
    APPROVED_BY_FIELD_NUMBER: _ClassVar[int]
    APPROVED_AT_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    plan_hash: str
    summary: str
    steps: _containers.RepeatedCompositeFieldContainer[_blocks_pb2.PlanStep]
    risks: _containers.RepeatedScalarFieldContainer[str]
    approved_by: str
    approved_at: _timestamp_pb2.Timestamp
    feedback: str
    def __init__(self, plan_hash: _Optional[str] = ..., summary: _Optional[str] = ..., steps: _Optional[_Iterable[_Union[_blocks_pb2.PlanStep, _Mapping]]] = ..., risks: _Optional[_Iterable[str]] = ..., approved_by: _Optional[str] = ..., approved_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., feedback: _Optional[str] = ...) -> None: ...

class RunContext(_message.Message):
    __slots__ = ("run_id", "workspace_id", "channel_id", "thread_root_id", "agent_id", "agent_name", "requested_by", "phase", "instructions", "thread_excerpt", "repo", "base_branch", "branch", "toolchain", "policy", "operating_rules", "approved_plan", "sdk_session_id", "workspace_dir", "git_remote_url", "attachments")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    THREAD_EXCERPT_FIELD_NUMBER: _ClassVar[int]
    REPO_FIELD_NUMBER: _ClassVar[int]
    BASE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    TOOLCHAIN_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    OPERATING_RULES_FIELD_NUMBER: _ClassVar[int]
    APPROVED_PLAN_FIELD_NUMBER: _ClassVar[int]
    SDK_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_DIR_FIELD_NUMBER: _ClassVar[int]
    GIT_REMOTE_URL_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    workspace_id: str
    channel_id: str
    thread_root_id: str
    agent_id: str
    agent_name: str
    requested_by: str
    phase: RunPhase
    instructions: str
    thread_excerpt: _containers.RepeatedCompositeFieldContainer[ThreadMessage]
    repo: str
    base_branch: str
    branch: str
    toolchain: str
    policy: PolicySummary
    operating_rules: str
    approved_plan: ApprovedPlan
    sdk_session_id: str
    workspace_dir: str
    git_remote_url: str
    attachments: _containers.RepeatedCompositeFieldContainer[Attachment]
    def __init__(self, run_id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., agent_name: _Optional[str] = ..., requested_by: _Optional[str] = ..., phase: _Optional[_Union[RunPhase, str]] = ..., instructions: _Optional[str] = ..., thread_excerpt: _Optional[_Iterable[_Union[ThreadMessage, _Mapping]]] = ..., repo: _Optional[str] = ..., base_branch: _Optional[str] = ..., branch: _Optional[str] = ..., toolchain: _Optional[str] = ..., policy: _Optional[_Union[PolicySummary, _Mapping]] = ..., operating_rules: _Optional[str] = ..., approved_plan: _Optional[_Union[ApprovedPlan, _Mapping]] = ..., sdk_session_id: _Optional[str] = ..., workspace_dir: _Optional[str] = ..., git_remote_url: _Optional[str] = ..., attachments: _Optional[_Iterable[_Union[Attachment, _Mapping]]] = ...) -> None: ...

class GetRunContextRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetRunContextResponse(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: RunContext
    def __init__(self, context: _Optional[_Union[RunContext, _Mapping]] = ...) -> None: ...

class GetGitCredentialRequest(_message.Message):
    __slots__ = ("scope",)
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    scope: str
    def __init__(self, scope: _Optional[str] = ...) -> None: ...

class GetGitCredentialResponse(_message.Message):
    __slots__ = ("username", "password", "expires_at", "remote_url")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    REMOTE_URL_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    expires_at: _timestamp_pb2.Timestamp
    remote_url: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., remote_url: _Optional[str] = ...) -> None: ...

class PostToThreadRequest(_message.Message):
    __slots__ = ("text", "client_msg_id")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_MSG_ID_FIELD_NUMBER: _ClassVar[int]
    text: str
    client_msg_id: str
    def __init__(self, text: _Optional[str] = ..., client_msg_id: _Optional[str] = ...) -> None: ...

class PostToThreadResponse(_message.Message):
    __slots__ = ("message_id",)
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    def __init__(self, message_id: _Optional[str] = ...) -> None: ...

class PostPlanRequest(_message.Message):
    __slots__ = ("summary", "steps", "risks", "questions", "preview_file_ids")
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    RISKS_FIELD_NUMBER: _ClassVar[int]
    QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    summary: str
    steps: _containers.RepeatedCompositeFieldContainer[_blocks_pb2.PlanStep]
    risks: _containers.RepeatedScalarFieldContainer[str]
    questions: _containers.RepeatedScalarFieldContainer[str]
    preview_file_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, summary: _Optional[str] = ..., steps: _Optional[_Iterable[_Union[_blocks_pb2.PlanStep, _Mapping]]] = ..., risks: _Optional[_Iterable[str]] = ..., questions: _Optional[_Iterable[str]] = ..., preview_file_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class PostPlanResponse(_message.Message):
    __slots__ = ("card_id", "gate_id", "plan_hash")
    CARD_ID_FIELD_NUMBER: _ClassVar[int]
    GATE_ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_HASH_FIELD_NUMBER: _ClassVar[int]
    card_id: str
    gate_id: str
    plan_hash: str
    def __init__(self, card_id: _Optional[str] = ..., gate_id: _Optional[str] = ..., plan_hash: _Optional[str] = ...) -> None: ...

class AttachArtifactRequest(_message.Message):
    __slots__ = ("name", "mime", "content", "caption")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MIME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CAPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    mime: str
    content: bytes
    caption: str
    def __init__(self, name: _Optional[str] = ..., mime: _Optional[str] = ..., content: _Optional[bytes] = ..., caption: _Optional[str] = ...) -> None: ...

class AttachArtifactResponse(_message.Message):
    __slots__ = ("file_id",)
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    def __init__(self, file_id: _Optional[str] = ...) -> None: ...

class GetAttachmentRequest(_message.Message):
    __slots__ = ("file_id",)
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    def __init__(self, file_id: _Optional[str] = ...) -> None: ...

class GetAttachmentResponse(_message.Message):
    __slots__ = ("attachment", "chunk")
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    attachment: Attachment
    chunk: bytes
    def __init__(self, attachment: _Optional[_Union[Attachment, _Mapping]] = ..., chunk: _Optional[bytes] = ...) -> None: ...

class UpdateCardRequest(_message.Message):
    __slots__ = ("card_id", "blocks", "text")
    CARD_ID_FIELD_NUMBER: _ClassVar[int]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    card_id: str
    blocks: _blocks_pb2.Blocks
    text: str
    def __init__(self, card_id: _Optional[str] = ..., blocks: _Optional[_Union[_blocks_pb2.Blocks, _Mapping]] = ..., text: _Optional[str] = ...) -> None: ...

class UpdateCardResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AskForApprovalRequest(_message.Message):
    __slots__ = ("kind", "subject", "reason")
    KIND_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    kind: _blocks_pb2.GateKind
    subject: str
    reason: str
    def __init__(self, kind: _Optional[_Union[_blocks_pb2.GateKind, str]] = ..., subject: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class AskForApprovalResponse(_message.Message):
    __slots__ = ("gate_id", "decision", "feedback")
    GATE_ID_FIELD_NUMBER: _ClassVar[int]
    DECISION_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    gate_id: str
    decision: str
    feedback: str
    def __init__(self, gate_id: _Optional[str] = ..., decision: _Optional[str] = ..., feedback: _Optional[str] = ...) -> None: ...

class AskQuestionRequest(_message.Message):
    __slots__ = ("question", "options", "multi_select")
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    MULTI_SELECT_FIELD_NUMBER: _ClassVar[int]
    question: str
    options: _containers.RepeatedScalarFieldContainer[str]
    multi_select: bool
    def __init__(self, question: _Optional[str] = ..., options: _Optional[_Iterable[str]] = ..., multi_select: bool = ...) -> None: ...

class AskQuestionResponse(_message.Message):
    __slots__ = ("card_id", "answer")
    CARD_ID_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    card_id: str
    answer: str
    def __init__(self, card_id: _Optional[str] = ..., answer: _Optional[str] = ...) -> None: ...

class ReportStatusRequest(_message.Message):
    __slots__ = ("status", "detail")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    status: str
    detail: str
    def __init__(self, status: _Optional[str] = ..., detail: _Optional[str] = ...) -> None: ...

class ReportStatusResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReadThreadRequest(_message.Message):
    __slots__ = ("after_thread_seq", "limit")
    AFTER_THREAD_SEQ_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    after_thread_seq: int
    limit: int
    def __init__(self, after_thread_seq: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class ReadThreadResponse(_message.Message):
    __slots__ = ("messages",)
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[ThreadMessage]
    def __init__(self, messages: _Optional[_Iterable[_Union[ThreadMessage, _Mapping]]] = ...) -> None: ...

class OpenPullRequestRequest(_message.Message):
    __slots__ = ("title", "body", "head_sha", "draft")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    HEAD_SHA_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    title: str
    body: str
    head_sha: str
    draft: bool
    def __init__(self, title: _Optional[str] = ..., body: _Optional[str] = ..., head_sha: _Optional[str] = ..., draft: bool = ...) -> None: ...

class OpenPullRequestResponse(_message.Message):
    __slots__ = ("pr_url", "pr_number")
    PR_URL_FIELD_NUMBER: _ClassVar[int]
    PR_NUMBER_FIELD_NUMBER: _ClassVar[int]
    pr_url: str
    pr_number: int
    def __init__(self, pr_url: _Optional[str] = ..., pr_number: _Optional[int] = ...) -> None: ...

class RequestCiWatchRequest(_message.Message):
    __slots__ = ("head_sha", "workflows")
    HEAD_SHA_FIELD_NUMBER: _ClassVar[int]
    WORKFLOWS_FIELD_NUMBER: _ClassVar[int]
    head_sha: str
    workflows: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, head_sha: _Optional[str] = ..., workflows: _Optional[_Iterable[str]] = ...) -> None: ...

class RequestCiWatchResponse(_message.Message):
    __slots__ = ("watch_id",)
    WATCH_ID_FIELD_NUMBER: _ClassVar[int]
    watch_id: str
    def __init__(self, watch_id: _Optional[str] = ...) -> None: ...

class GetCiFailureRequest(_message.Message):
    __slots__ = ("head_sha",)
    HEAD_SHA_FIELD_NUMBER: _ClassVar[int]
    head_sha: str
    def __init__(self, head_sha: _Optional[str] = ...) -> None: ...

class GetCiFailureResponse(_message.Message):
    __slots__ = ("complete", "green", "checks", "failed_log_excerpt")
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    GREEN_FIELD_NUMBER: _ClassVar[int]
    CHECKS_FIELD_NUMBER: _ClassVar[int]
    FAILED_LOG_EXCERPT_FIELD_NUMBER: _ClassVar[int]
    complete: bool
    green: bool
    checks: _containers.RepeatedCompositeFieldContainer[_blocks_pb2.Check]
    failed_log_excerpt: str
    def __init__(self, complete: bool = ..., green: bool = ..., checks: _Optional[_Iterable[_Union[_blocks_pb2.Check, _Mapping]]] = ..., failed_log_excerpt: _Optional[str] = ...) -> None: ...

class RecordDecisionRequest(_message.Message):
    __slots__ = ("title", "body", "tags")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    title: str
    body: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, title: _Optional[str] = ..., body: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class RecordDecisionResponse(_message.Message):
    __slots__ = ("decision_id",)
    DECISION_ID_FIELD_NUMBER: _ClassVar[int]
    decision_id: str
    def __init__(self, decision_id: _Optional[str] = ...) -> None: ...

class RememberRequest(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class RememberResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Usage(_message.Message):
    __slots__ = ("input_tokens", "output_tokens", "cache_read_input_tokens", "cache_creation_input_tokens", "cost_usd", "model")
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_READ_INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_CREATION_INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    COST_USD_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    input_tokens: int
    output_tokens: int
    cache_read_input_tokens: int
    cache_creation_input_tokens: int
    cost_usd: float
    model: str
    def __init__(self, input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., cache_read_input_tokens: _Optional[int] = ..., cache_creation_input_tokens: _Optional[int] = ..., cost_usd: _Optional[float] = ..., model: _Optional[str] = ...) -> None: ...

class RunEvent(_message.Message):
    __slots__ = ("seq", "at", "kind", "sdk_session_id", "text", "tool_name", "tool_use_id", "tool_input", "tool_output", "tool_output_sha256", "is_error", "usage", "result_subtype", "num_turns", "duration_ms")
    SEQ_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SDK_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    TOOL_USE_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_INPUT_FIELD_NUMBER: _ClassVar[int]
    TOOL_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    TOOL_OUTPUT_SHA256_FIELD_NUMBER: _ClassVar[int]
    IS_ERROR_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_TURNS_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    seq: int
    at: _timestamp_pb2.Timestamp
    kind: RunEventKind
    sdk_session_id: str
    text: str
    tool_name: str
    tool_use_id: str
    tool_input: _struct_pb2.Struct
    tool_output: str
    tool_output_sha256: str
    is_error: bool
    usage: Usage
    result_subtype: str
    num_turns: int
    duration_ms: int
    def __init__(self, seq: _Optional[int] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., kind: _Optional[_Union[RunEventKind, str]] = ..., sdk_session_id: _Optional[str] = ..., text: _Optional[str] = ..., tool_name: _Optional[str] = ..., tool_use_id: _Optional[str] = ..., tool_input: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., tool_output: _Optional[str] = ..., tool_output_sha256: _Optional[str] = ..., is_error: bool = ..., usage: _Optional[_Union[Usage, _Mapping]] = ..., result_subtype: _Optional[str] = ..., num_turns: _Optional[int] = ..., duration_ms: _Optional[int] = ...) -> None: ...

class StreamEventsRequest(_message.Message):
    __slots__ = ("event",)
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: RunEvent
    def __init__(self, event: _Optional[_Union[RunEvent, _Mapping]] = ...) -> None: ...

class StreamEventsResponse(_message.Message):
    __slots__ = ("accepted",)
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    accepted: int
    def __init__(self, accepted: _Optional[int] = ...) -> None: ...

class SessionEntry(_message.Message):
    __slots__ = ("session_id", "project_key", "subpath", "seq", "entry_uuid", "payload", "created_at")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_KEY_FIELD_NUMBER: _ClassVar[int]
    SUBPATH_FIELD_NUMBER: _ClassVar[int]
    SEQ_FIELD_NUMBER: _ClassVar[int]
    ENTRY_UUID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    project_key: str
    subpath: str
    seq: int
    entry_uuid: str
    payload: bytes
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, session_id: _Optional[str] = ..., project_key: _Optional[str] = ..., subpath: _Optional[str] = ..., seq: _Optional[int] = ..., entry_uuid: _Optional[str] = ..., payload: _Optional[bytes] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SessionSummary(_message.Message):
    __slots__ = ("session_id", "mtime_ms", "data")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    MTIME_MS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    mtime_ms: int
    data: _struct_pb2.Struct
    def __init__(self, session_id: _Optional[str] = ..., mtime_ms: _Optional[int] = ..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class SessionStorePutRequest(_message.Message):
    __slots__ = ("entries", "summary")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[SessionEntry]
    summary: SessionSummary
    def __init__(self, entries: _Optional[_Iterable[_Union[SessionEntry, _Mapping]]] = ..., summary: _Optional[_Union[SessionSummary, _Mapping]] = ...) -> None: ...

class SessionStorePutResponse(_message.Message):
    __slots__ = ("written",)
    WRITTEN_FIELD_NUMBER: _ClassVar[int]
    written: int
    def __init__(self, written: _Optional[int] = ...) -> None: ...

class SessionStoreListRequest(_message.Message):
    __slots__ = ("session_id", "project_key", "subpath", "after_seq", "limit")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_KEY_FIELD_NUMBER: _ClassVar[int]
    SUBPATH_FIELD_NUMBER: _ClassVar[int]
    AFTER_SEQ_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    project_key: str
    subpath: str
    after_seq: int
    limit: int
    def __init__(self, session_id: _Optional[str] = ..., project_key: _Optional[str] = ..., subpath: _Optional[str] = ..., after_seq: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class SessionStoreListResponse(_message.Message):
    __slots__ = ("entries", "has_more", "found")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[SessionEntry]
    has_more: bool
    found: bool
    def __init__(self, entries: _Optional[_Iterable[_Union[SessionEntry, _Mapping]]] = ..., has_more: bool = ..., found: bool = ...) -> None: ...

class SessionStoreListSessionsRequest(_message.Message):
    __slots__ = ("project_key",)
    PROJECT_KEY_FIELD_NUMBER: _ClassVar[int]
    project_key: str
    def __init__(self, project_key: _Optional[str] = ...) -> None: ...

class SessionStoreListSessionsResponse(_message.Message):
    __slots__ = ("sessions",)
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[SessionSummary]
    def __init__(self, sessions: _Optional[_Iterable[_Union[SessionSummary, _Mapping]]] = ...) -> None: ...

class SessionStoreListSubkeysRequest(_message.Message):
    __slots__ = ("session_id", "project_key")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_KEY_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    project_key: str
    def __init__(self, session_id: _Optional[str] = ..., project_key: _Optional[str] = ...) -> None: ...

class SessionStoreListSubkeysResponse(_message.Message):
    __slots__ = ("subpaths",)
    SUBPATHS_FIELD_NUMBER: _ClassVar[int]
    subpaths: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, subpaths: _Optional[_Iterable[str]] = ...) -> None: ...

class SessionStoreDeleteRequest(_message.Message):
    __slots__ = ("session_id", "project_key", "subpath")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_KEY_FIELD_NUMBER: _ClassVar[int]
    SUBPATH_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    project_key: str
    subpath: str
    def __init__(self, session_id: _Optional[str] = ..., project_key: _Optional[str] = ..., subpath: _Optional[str] = ...) -> None: ...

class SessionStoreDeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InboxItem(_message.Message):
    __slots__ = ("seq", "kind", "user_id", "user_name", "text", "gate_id", "decision", "card_id", "at")
    SEQ_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    GATE_ID_FIELD_NUMBER: _ClassVar[int]
    DECISION_FIELD_NUMBER: _ClassVar[int]
    CARD_ID_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    seq: int
    kind: InboxKind
    user_id: str
    user_name: str
    text: str
    gate_id: str
    decision: str
    card_id: str
    at: _timestamp_pb2.Timestamp
    def __init__(self, seq: _Optional[int] = ..., kind: _Optional[_Union[InboxKind, str]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., text: _Optional[str] = ..., gate_id: _Optional[str] = ..., decision: _Optional[str] = ..., card_id: _Optional[str] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PollInboxRequest(_message.Message):
    __slots__ = ("after_seq", "wait_ms")
    AFTER_SEQ_FIELD_NUMBER: _ClassVar[int]
    WAIT_MS_FIELD_NUMBER: _ClassVar[int]
    after_seq: int
    wait_ms: int
    def __init__(self, after_seq: _Optional[int] = ..., wait_ms: _Optional[int] = ...) -> None: ...

class PollInboxResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[InboxItem]
    def __init__(self, items: _Optional[_Iterable[_Union[InboxItem, _Mapping]]] = ...) -> None: ...

class StartRunRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id", "thread_root_id", "agent_id", "requested_by", "instructions")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    thread_root_id: str
    agent_id: str
    requested_by: str
    instructions: str
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., requested_by: _Optional[str] = ..., instructions: _Optional[str] = ...) -> None: ...

class StartRunResponse(_message.Message):
    __slots__ = ("run",)
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: _agent_pb2.Run
    def __init__(self, run: _Optional[_Union[_agent_pb2.Run, _Mapping]] = ...) -> None: ...

class GetRunRequest(_message.Message):
    __slots__ = ("run_id",)
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class GetRunResponse(_message.Message):
    __slots__ = ("run", "sdk_session_id", "head_sha", "gates")
    RUN_FIELD_NUMBER: _ClassVar[int]
    SDK_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    HEAD_SHA_FIELD_NUMBER: _ClassVar[int]
    GATES_FIELD_NUMBER: _ClassVar[int]
    run: _agent_pb2.Run
    sdk_session_id: str
    head_sha: str
    gates: _containers.RepeatedCompositeFieldContainer[Gate]
    def __init__(self, run: _Optional[_Union[_agent_pb2.Run, _Mapping]] = ..., sdk_session_id: _Optional[str] = ..., head_sha: _Optional[str] = ..., gates: _Optional[_Iterable[_Union[Gate, _Mapping]]] = ...) -> None: ...

class Gate(_message.Message):
    __slots__ = ("id", "kind", "subject_hash", "required_approvers", "min_approvals", "expires_at", "decision", "decisions")
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_HASH_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_APPROVERS_FIELD_NUMBER: _ClassVar[int]
    MIN_APPROVALS_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    DECISION_FIELD_NUMBER: _ClassVar[int]
    DECISIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    kind: _blocks_pb2.GateKind
    subject_hash: str
    required_approvers: _containers.RepeatedScalarFieldContainer[str]
    min_approvals: int
    expires_at: _timestamp_pb2.Timestamp
    decision: str
    decisions: _containers.RepeatedCompositeFieldContainer[GateDecision]
    def __init__(self, id: _Optional[str] = ..., kind: _Optional[_Union[_blocks_pb2.GateKind, str]] = ..., subject_hash: _Optional[str] = ..., required_approvers: _Optional[_Iterable[str]] = ..., min_approvals: _Optional[int] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., decision: _Optional[str] = ..., decisions: _Optional[_Iterable[_Union[GateDecision, _Mapping]]] = ...) -> None: ...

class GateDecision(_message.Message):
    __slots__ = ("user_id", "decision", "feedback", "at")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DECISION_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    decision: str
    feedback: str
    at: _timestamp_pb2.Timestamp
    def __init__(self, user_id: _Optional[str] = ..., decision: _Optional[str] = ..., feedback: _Optional[str] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListRunsRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id", "thread_root_id", "limit")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    thread_root_id: str
    limit: int
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListRunsResponse(_message.Message):
    __slots__ = ("runs",)
    RUNS_FIELD_NUMBER: _ClassVar[int]
    runs: _containers.RepeatedCompositeFieldContainer[_agent_pb2.Run]
    def __init__(self, runs: _Optional[_Iterable[_Union[_agent_pb2.Run, _Mapping]]] = ...) -> None: ...

class DecideGateRequest(_message.Message):
    __slots__ = ("run_id", "gate_id", "user_id", "decision", "feedback")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    GATE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DECISION_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    gate_id: str
    user_id: str
    decision: str
    feedback: str
    def __init__(self, run_id: _Optional[str] = ..., gate_id: _Optional[str] = ..., user_id: _Optional[str] = ..., decision: _Optional[str] = ..., feedback: _Optional[str] = ...) -> None: ...

class DecideGateResponse(_message.Message):
    __slots__ = ("gate",)
    GATE_FIELD_NUMBER: _ClassVar[int]
    gate: Gate
    def __init__(self, gate: _Optional[_Union[Gate, _Mapping]] = ...) -> None: ...

class SteerRunRequest(_message.Message):
    __slots__ = ("run_id", "user_id", "text")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    user_id: str
    text: str
    def __init__(self, run_id: _Optional[str] = ..., user_id: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class SteerRunResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelRunRequest(_message.Message):
    __slots__ = ("run_id", "user_id", "reason")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    user_id: str
    reason: str
    def __init__(self, run_id: _Optional[str] = ..., user_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class CancelRunResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRunEventsRequest(_message.Message):
    __slots__ = ("run_id", "after_seq", "limit")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    AFTER_SEQ_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    after_seq: int
    limit: int
    def __init__(self, run_id: _Optional[str] = ..., after_seq: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class ListRunEventsResponse(_message.Message):
    __slots__ = ("events", "has_more")
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[RunEvent]
    has_more: bool
    def __init__(self, events: _Optional[_Iterable[_Union[RunEvent, _Mapping]]] = ..., has_more: bool = ...) -> None: ...
