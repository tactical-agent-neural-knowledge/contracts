from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tank.agent.v1 import agent_pb2 as _agent_pb2
from tank.blocks.v1 import blocks_pb2 as _blocks_pb2
from tank.board.v1 import board_pb2 as _board_pb2
from tank.books.v1 import books_pb2 as _books_pb2
from tank.canvas.v1 import canvas_pb2 as _canvas_pb2
from tank.social.v1 import social_pb2 as _social_pb2
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
    INBOX_KIND_HANDOFF: _ClassVar[InboxKind]
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
INBOX_KIND_HANDOFF: InboxKind

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
    __slots__ = ("mode", "tools_deny", "network_allowed_hosts", "default_model", "subagent_model", "max_turns", "max_budget_usd", "rules", "tools_gate_destructive")
    MODE_FIELD_NUMBER: _ClassVar[int]
    TOOLS_DENY_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ALLOWED_HOSTS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MODEL_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_MODEL_FIELD_NUMBER: _ClassVar[int]
    MAX_TURNS_FIELD_NUMBER: _ClassVar[int]
    MAX_BUDGET_USD_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    TOOLS_GATE_DESTRUCTIVE_FIELD_NUMBER: _ClassVar[int]
    mode: str
    tools_deny: _containers.RepeatedScalarFieldContainer[str]
    network_allowed_hosts: _containers.RepeatedScalarFieldContainer[str]
    default_model: str
    subagent_model: str
    max_turns: int
    max_budget_usd: float
    rules: _containers.RepeatedScalarFieldContainer[str]
    tools_gate_destructive: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, mode: _Optional[str] = ..., tools_deny: _Optional[_Iterable[str]] = ..., network_allowed_hosts: _Optional[_Iterable[str]] = ..., default_model: _Optional[str] = ..., subagent_model: _Optional[str] = ..., max_turns: _Optional[int] = ..., max_budget_usd: _Optional[float] = ..., rules: _Optional[_Iterable[str]] = ..., tools_gate_destructive: _Optional[_Iterable[str]] = ...) -> None: ...

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
    __slots__ = ("run_id", "workspace_id", "channel_id", "thread_root_id", "agent_id", "agent_name", "requested_by", "phase", "instructions", "thread_excerpt", "repo", "base_branch", "branch", "toolchain", "policy", "operating_rules", "approved_plan", "sdk_session_id", "workspace_dir", "git_remote_url", "attachments", "repo_access", "product_run", "channel_purpose", "channel_goal", "agent_title", "agent_skill", "skip_neural_knowledge", "task_class", "workbench_board_id", "tread_brief", "tread_plan", "mode", "team", "parent_run_id", "handoff", "envelope_left")
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
    REPO_ACCESS_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_RUN_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_PURPOSE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_GOAL_FIELD_NUMBER: _ClassVar[int]
    AGENT_TITLE_FIELD_NUMBER: _ClassVar[int]
    AGENT_SKILL_FIELD_NUMBER: _ClassVar[int]
    SKIP_NEURAL_KNOWLEDGE_FIELD_NUMBER: _ClassVar[int]
    TASK_CLASS_FIELD_NUMBER: _ClassVar[int]
    WORKBENCH_BOARD_ID_FIELD_NUMBER: _ClassVar[int]
    TREAD_BRIEF_FIELD_NUMBER: _ClassVar[int]
    TREAD_PLAN_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    PARENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    HANDOFF_FIELD_NUMBER: _ClassVar[int]
    ENVELOPE_LEFT_FIELD_NUMBER: _ClassVar[int]
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
    repo_access: _containers.RepeatedCompositeFieldContainer[RepoAccess]
    product_run: bool
    channel_purpose: str
    channel_goal: str
    agent_title: str
    agent_skill: str
    skip_neural_knowledge: bool
    task_class: str
    workbench_board_id: str
    tread_brief: str
    tread_plan: _agent_pb2.TreadPlan
    mode: str
    team: TeamContext
    parent_run_id: str
    handoff: Handoff
    envelope_left: Envelope
    def __init__(self, run_id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., agent_name: _Optional[str] = ..., requested_by: _Optional[str] = ..., phase: _Optional[_Union[RunPhase, str]] = ..., instructions: _Optional[str] = ..., thread_excerpt: _Optional[_Iterable[_Union[ThreadMessage, _Mapping]]] = ..., repo: _Optional[str] = ..., base_branch: _Optional[str] = ..., branch: _Optional[str] = ..., toolchain: _Optional[str] = ..., policy: _Optional[_Union[PolicySummary, _Mapping]] = ..., operating_rules: _Optional[str] = ..., approved_plan: _Optional[_Union[ApprovedPlan, _Mapping]] = ..., sdk_session_id: _Optional[str] = ..., workspace_dir: _Optional[str] = ..., git_remote_url: _Optional[str] = ..., attachments: _Optional[_Iterable[_Union[Attachment, _Mapping]]] = ..., repo_access: _Optional[_Iterable[_Union[RepoAccess, _Mapping]]] = ..., product_run: bool = ..., channel_purpose: _Optional[str] = ..., channel_goal: _Optional[str] = ..., agent_title: _Optional[str] = ..., agent_skill: _Optional[str] = ..., skip_neural_knowledge: bool = ..., task_class: _Optional[str] = ..., workbench_board_id: _Optional[str] = ..., tread_brief: _Optional[str] = ..., tread_plan: _Optional[_Union[_agent_pb2.TreadPlan, _Mapping]] = ..., mode: _Optional[str] = ..., team: _Optional[_Union[TeamContext, _Mapping]] = ..., parent_run_id: _Optional[str] = ..., handoff: _Optional[_Union[Handoff, _Mapping]] = ..., envelope_left: _Optional[_Union[Envelope, _Mapping]] = ...) -> None: ...

class TeamContext(_message.Message):
    __slots__ = ("team_id", "name", "handle", "purpose", "members", "member_id", "coordinator", "board_id", "paused", "cap_note")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    COORDINATOR_FIELD_NUMBER: _ClassVar[int]
    BOARD_ID_FIELD_NUMBER: _ClassVar[int]
    PAUSED_FIELD_NUMBER: _ClassVar[int]
    CAP_NOTE_FIELD_NUMBER: _ClassVar[int]
    team_id: str
    name: str
    handle: str
    purpose: str
    members: _containers.RepeatedCompositeFieldContainer[TeamMember]
    member_id: str
    coordinator: bool
    board_id: str
    paused: bool
    cap_note: str
    def __init__(self, team_id: _Optional[str] = ..., name: _Optional[str] = ..., handle: _Optional[str] = ..., purpose: _Optional[str] = ..., members: _Optional[_Iterable[_Union[TeamMember, _Mapping]]] = ..., member_id: _Optional[str] = ..., coordinator: bool = ..., board_id: _Optional[str] = ..., paused: bool = ..., cap_note: _Optional[str] = ...) -> None: ...

class ClaimItem(_message.Message):
    __slots__ = ("kind", "key")
    KIND_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    kind: str
    key: str
    def __init__(self, kind: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class HeldClaim(_message.Message):
    __slots__ = ("item", "run_id", "title", "ask", "since")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ASK_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    item: ClaimItem
    run_id: str
    title: str
    ask: str
    since: _timestamp_pb2.Timestamp
    def __init__(self, item: _Optional[_Union[ClaimItem, _Mapping]] = ..., run_id: _Optional[str] = ..., title: _Optional[str] = ..., ask: _Optional[str] = ..., since: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ClaimRequest(_message.Message):
    __slots__ = ("items", "note")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ClaimItem]
    note: str
    def __init__(self, items: _Optional[_Iterable[_Union[ClaimItem, _Mapping]]] = ..., note: _Optional[str] = ...) -> None: ...

class ClaimResponse(_message.Message):
    __slots__ = ("granted", "held")
    GRANTED_FIELD_NUMBER: _ClassVar[int]
    HELD_FIELD_NUMBER: _ClassVar[int]
    granted: _containers.RepeatedCompositeFieldContainer[ClaimItem]
    held: _containers.RepeatedCompositeFieldContainer[HeldClaim]
    def __init__(self, granted: _Optional[_Iterable[_Union[ClaimItem, _Mapping]]] = ..., held: _Optional[_Iterable[_Union[HeldClaim, _Mapping]]] = ...) -> None: ...

class ReleaseClaimsRequest(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ClaimItem]
    def __init__(self, items: _Optional[_Iterable[_Union[ClaimItem, _Mapping]]] = ...) -> None: ...

class ReleaseClaimsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CheckClaimRequest(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: ClaimItem
    def __init__(self, item: _Optional[_Union[ClaimItem, _Mapping]] = ...) -> None: ...

class CheckClaimResponse(_message.Message):
    __slots__ = ("ok", "held")
    OK_FIELD_NUMBER: _ClassVar[int]
    HELD_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    held: HeldClaim
    def __init__(self, ok: bool = ..., held: _Optional[_Union[HeldClaim, _Mapping]] = ...) -> None: ...

class ListClaimsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListClaimsResponse(_message.Message):
    __slots__ = ("mine", "others")
    MINE_FIELD_NUMBER: _ClassVar[int]
    OTHERS_FIELD_NUMBER: _ClassVar[int]
    mine: _containers.RepeatedCompositeFieldContainer[HeldClaim]
    others: _containers.RepeatedCompositeFieldContainer[HeldClaim]
    def __init__(self, mine: _Optional[_Iterable[_Union[HeldClaim, _Mapping]]] = ..., others: _Optional[_Iterable[_Union[HeldClaim, _Mapping]]] = ...) -> None: ...

class TeamMember(_message.Message):
    __slots__ = ("member_id", "agent_id", "title", "handle", "coordinator", "triggers", "delegate", "delegate_to", "envelope", "enabled", "is_me", "person", "user_id", "record")
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    COORDINATOR_FIELD_NUMBER: _ClassVar[int]
    TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    DELEGATE_FIELD_NUMBER: _ClassVar[int]
    DELEGATE_TO_FIELD_NUMBER: _ClassVar[int]
    ENVELOPE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_ME_FIELD_NUMBER: _ClassVar[int]
    PERSON_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    agent_id: str
    title: str
    handle: str
    coordinator: bool
    triggers: _containers.RepeatedScalarFieldContainer[str]
    delegate: bool
    delegate_to: _containers.RepeatedScalarFieldContainer[str]
    envelope: Envelope
    enabled: bool
    is_me: bool
    person: bool
    user_id: str
    record: str
    def __init__(self, member_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., title: _Optional[str] = ..., handle: _Optional[str] = ..., coordinator: bool = ..., triggers: _Optional[_Iterable[str]] = ..., delegate: bool = ..., delegate_to: _Optional[_Iterable[str]] = ..., envelope: _Optional[_Union[Envelope, _Mapping]] = ..., enabled: bool = ..., is_me: bool = ..., person: bool = ..., user_id: _Optional[str] = ..., record: _Optional[str] = ...) -> None: ...

class Envelope(_message.Message):
    __slots__ = ("usd", "turns", "minutes")
    USD_FIELD_NUMBER: _ClassVar[int]
    TURNS_FIELD_NUMBER: _ClassVar[int]
    MINUTES_FIELD_NUMBER: _ClassVar[int]
    usd: float
    turns: int
    minutes: int
    def __init__(self, usd: _Optional[float] = ..., turns: _Optional[int] = ..., minutes: _Optional[int] = ...) -> None: ...

class Handoff(_message.Message):
    __slots__ = ("ask", "return_shape", "acceptance_check", "envelope", "from_title", "to_title")
    ASK_FIELD_NUMBER: _ClassVar[int]
    RETURN_SHAPE_FIELD_NUMBER: _ClassVar[int]
    ACCEPTANCE_CHECK_FIELD_NUMBER: _ClassVar[int]
    ENVELOPE_FIELD_NUMBER: _ClassVar[int]
    FROM_TITLE_FIELD_NUMBER: _ClassVar[int]
    TO_TITLE_FIELD_NUMBER: _ClassVar[int]
    ask: str
    return_shape: str
    acceptance_check: str
    envelope: Envelope
    from_title: str
    to_title: str
    def __init__(self, ask: _Optional[str] = ..., return_shape: _Optional[str] = ..., acceptance_check: _Optional[str] = ..., envelope: _Optional[_Union[Envelope, _Mapping]] = ..., from_title: _Optional[str] = ..., to_title: _Optional[str] = ...) -> None: ...

class HandoffStatus(_message.Message):
    __slots__ = ("child_run_id", "member_id", "title", "handle", "state", "cost_usd", "envelope", "handoff", "result", "thread_root_id", "verdict", "verdict_note", "quorum_with", "person_user_id", "deadline")
    CHILD_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COST_USD_FIELD_NUMBER: _ClassVar[int]
    ENVELOPE_FIELD_NUMBER: _ClassVar[int]
    HANDOFF_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    VERDICT_NOTE_FIELD_NUMBER: _ClassVar[int]
    QUORUM_WITH_FIELD_NUMBER: _ClassVar[int]
    PERSON_USER_ID_FIELD_NUMBER: _ClassVar[int]
    DEADLINE_FIELD_NUMBER: _ClassVar[int]
    child_run_id: str
    member_id: str
    title: str
    handle: str
    state: str
    cost_usd: float
    envelope: Envelope
    handoff: Handoff
    result: str
    thread_root_id: str
    verdict: str
    verdict_note: str
    quorum_with: str
    person_user_id: str
    deadline: _timestamp_pb2.Timestamp
    def __init__(self, child_run_id: _Optional[str] = ..., member_id: _Optional[str] = ..., title: _Optional[str] = ..., handle: _Optional[str] = ..., state: _Optional[str] = ..., cost_usd: _Optional[float] = ..., envelope: _Optional[_Union[Envelope, _Mapping]] = ..., handoff: _Optional[_Union[Handoff, _Mapping]] = ..., result: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., verdict: _Optional[str] = ..., verdict_note: _Optional[str] = ..., quorum_with: _Optional[str] = ..., person_user_id: _Optional[str] = ..., deadline: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DelegateRequest(_message.Message):
    __slots__ = ("member_handle", "ask", "return_shape", "acceptance_check", "envelope", "quorum_handle", "deadline_minutes")
    MEMBER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ASK_FIELD_NUMBER: _ClassVar[int]
    RETURN_SHAPE_FIELD_NUMBER: _ClassVar[int]
    ACCEPTANCE_CHECK_FIELD_NUMBER: _ClassVar[int]
    ENVELOPE_FIELD_NUMBER: _ClassVar[int]
    QUORUM_HANDLE_FIELD_NUMBER: _ClassVar[int]
    DEADLINE_MINUTES_FIELD_NUMBER: _ClassVar[int]
    member_handle: str
    ask: str
    return_shape: str
    acceptance_check: str
    envelope: Envelope
    quorum_handle: str
    deadline_minutes: int
    def __init__(self, member_handle: _Optional[str] = ..., ask: _Optional[str] = ..., return_shape: _Optional[str] = ..., acceptance_check: _Optional[str] = ..., envelope: _Optional[_Union[Envelope, _Mapping]] = ..., quorum_handle: _Optional[str] = ..., deadline_minutes: _Optional[int] = ...) -> None: ...

class DelegateResponse(_message.Message):
    __slots__ = ("child_run_id", "thread_root_id", "envelope", "envelope_left", "quorum_child_run_id", "already")
    CHILD_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    ENVELOPE_FIELD_NUMBER: _ClassVar[int]
    ENVELOPE_LEFT_FIELD_NUMBER: _ClassVar[int]
    QUORUM_CHILD_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ALREADY_FIELD_NUMBER: _ClassVar[int]
    child_run_id: str
    thread_root_id: str
    envelope: Envelope
    envelope_left: Envelope
    quorum_child_run_id: str
    already: str
    def __init__(self, child_run_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., envelope: _Optional[_Union[Envelope, _Mapping]] = ..., envelope_left: _Optional[_Union[Envelope, _Mapping]] = ..., quorum_child_run_id: _Optional[str] = ..., already: _Optional[str] = ...) -> None: ...

class AcceptHandoffRequest(_message.Message):
    __slots__ = ("child_run_id", "accepted", "note")
    CHILD_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    child_run_id: str
    accepted: bool
    note: str
    def __init__(self, child_run_id: _Optional[str] = ..., accepted: bool = ..., note: _Optional[str] = ...) -> None: ...

class AcceptHandoffResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListHandoffsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListHandoffsResponse(_message.Message):
    __slots__ = ("handoffs", "envelope_left")
    HANDOFFS_FIELD_NUMBER: _ClassVar[int]
    ENVELOPE_LEFT_FIELD_NUMBER: _ClassVar[int]
    handoffs: _containers.RepeatedCompositeFieldContainer[HandoffStatus]
    envelope_left: Envelope
    def __init__(self, handoffs: _Optional[_Iterable[_Union[HandoffStatus, _Mapping]]] = ..., envelope_left: _Optional[_Union[Envelope, _Mapping]] = ...) -> None: ...

class GetRunContextRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetRunContextResponse(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: RunContext
    def __init__(self, context: _Optional[_Union[RunContext, _Mapping]] = ...) -> None: ...

class RepoAccess(_message.Message):
    __slots__ = ("repo", "access")
    REPO_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    repo: str
    access: str
    def __init__(self, repo: _Optional[str] = ..., access: _Optional[str] = ...) -> None: ...

class GetGitCredentialRequest(_message.Message):
    __slots__ = ("scope", "repo")
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    REPO_FIELD_NUMBER: _ClassVar[int]
    scope: str
    repo: str
    def __init__(self, scope: _Optional[str] = ..., repo: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("text", "client_msg_id", "also_send_to_tread")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_MSG_ID_FIELD_NUMBER: _ClassVar[int]
    ALSO_SEND_TO_TREAD_FIELD_NUMBER: _ClassVar[int]
    text: str
    client_msg_id: str
    also_send_to_tread: bool
    def __init__(self, text: _Optional[str] = ..., client_msg_id: _Optional[str] = ..., also_send_to_tread: bool = ...) -> None: ...

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
    __slots__ = ("name", "mime", "content", "caption", "deliver")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MIME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CAPTION_FIELD_NUMBER: _ClassVar[int]
    DELIVER_FIELD_NUMBER: _ClassVar[int]
    name: str
    mime: str
    content: bytes
    caption: str
    deliver: bool
    def __init__(self, name: _Optional[str] = ..., mime: _Optional[str] = ..., content: _Optional[bytes] = ..., caption: _Optional[str] = ..., deliver: bool = ...) -> None: ...

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

class UpdateTreadPlanRequest(_message.Message):
    __slots__ = ("title", "source", "items", "replace_all")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    REPLACE_ALL_FIELD_NUMBER: _ClassVar[int]
    title: str
    source: str
    items: _containers.RepeatedCompositeFieldContainer[_agent_pb2.TreadPlanItem]
    replace_all: bool
    def __init__(self, title: _Optional[str] = ..., source: _Optional[str] = ..., items: _Optional[_Iterable[_Union[_agent_pb2.TreadPlanItem, _Mapping]]] = ..., replace_all: bool = ...) -> None: ...

class UpdateTreadPlanResponse(_message.Message):
    __slots__ = ("plan",)
    PLAN_FIELD_NUMBER: _ClassVar[int]
    plan: _agent_pb2.TreadPlan
    def __init__(self, plan: _Optional[_Union[_agent_pb2.TreadPlan, _Mapping]] = ...) -> None: ...

class UpdatePlanStepsRequest(_message.Message):
    __slots__ = ("steps",)
    STEPS_FIELD_NUMBER: _ClassVar[int]
    steps: _containers.RepeatedCompositeFieldContainer[PlanStepUpdate]
    def __init__(self, steps: _Optional[_Iterable[_Union[PlanStepUpdate, _Mapping]]] = ...) -> None: ...

class PlanStepUpdate(_message.Message):
    __slots__ = ("id", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: _blocks_pb2.StepStatus
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[_blocks_pb2.StepStatus, str]] = ...) -> None: ...

class UpdatePlanStepsResponse(_message.Message):
    __slots__ = ("unknown_ids",)
    UNKNOWN_IDS_FIELD_NUMBER: _ClassVar[int]
    unknown_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, unknown_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ReportCompletionRequest(_message.Message):
    __slots__ = ("done", "remaining", "blocked")
    DONE_FIELD_NUMBER: _ClassVar[int]
    REMAINING_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_FIELD_NUMBER: _ClassVar[int]
    done: _containers.RepeatedScalarFieldContainer[str]
    remaining: _containers.RepeatedScalarFieldContainer[str]
    blocked: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, done: _Optional[_Iterable[str]] = ..., remaining: _Optional[_Iterable[str]] = ..., blocked: _Optional[_Iterable[str]] = ...) -> None: ...

class ReportCompletionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReadProductRequest(_message.Message):
    __slots__ = ("tail_lines", "pull_request")
    TAIL_LINES_FIELD_NUMBER: _ClassVar[int]
    PULL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    tail_lines: int
    pull_request: int
    def __init__(self, tail_lines: _Optional[int] = ..., pull_request: _Optional[int] = ...) -> None: ...

class ReadProductResponse(_message.Message):
    __slots__ = ("slug", "state", "logs", "note")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    slug: str
    state: ProductState
    logs: str
    note: str
    def __init__(self, slug: _Optional[str] = ..., state: _Optional[_Union[ProductState, _Mapping]] = ..., logs: _Optional[str] = ..., note: _Optional[str] = ...) -> None: ...

class CheckLiveRequest(_message.Message):
    __slots__ = ("path", "viewport_width", "viewport_height", "expect_sha", "pull_request")
    PATH_FIELD_NUMBER: _ClassVar[int]
    VIEWPORT_WIDTH_FIELD_NUMBER: _ClassVar[int]
    VIEWPORT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    EXPECT_SHA_FIELD_NUMBER: _ClassVar[int]
    PULL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    path: str
    viewport_width: int
    viewport_height: int
    expect_sha: str
    pull_request: int
    def __init__(self, path: _Optional[str] = ..., viewport_width: _Optional[int] = ..., viewport_height: _Optional[int] = ..., expect_sha: _Optional[str] = ..., pull_request: _Optional[int] = ...) -> None: ...

class CheckLiveResponse(_message.Message):
    __slots__ = ("url", "status", "build_sha", "deployed", "title", "text_length", "errors", "screenshot_png", "note")
    URL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BUILD_SHA_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    SCREENSHOT_PNG_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    url: str
    status: int
    build_sha: str
    deployed: bool
    title: str
    text_length: int
    errors: _containers.RepeatedScalarFieldContainer[str]
    screenshot_png: bytes
    note: str
    def __init__(self, url: _Optional[str] = ..., status: _Optional[int] = ..., build_sha: _Optional[str] = ..., deployed: bool = ..., title: _Optional[str] = ..., text_length: _Optional[int] = ..., errors: _Optional[_Iterable[str]] = ..., screenshot_png: _Optional[bytes] = ..., note: _Optional[str] = ...) -> None: ...

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

class BoardResearchRequest(_message.Message):
    __slots__ = ("query", "limit")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    query: str
    limit: int
    def __init__(self, query: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ResearchHit(_message.Message):
    __slots__ = ("product", "slug", "url", "industry", "stage", "excerpt")
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    INDUSTRY_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    EXCERPT_FIELD_NUMBER: _ClassVar[int]
    product: str
    slug: str
    url: str
    industry: str
    stage: str
    excerpt: str
    def __init__(self, product: _Optional[str] = ..., slug: _Optional[str] = ..., url: _Optional[str] = ..., industry: _Optional[str] = ..., stage: _Optional[str] = ..., excerpt: _Optional[str] = ...) -> None: ...

class BoardResearchResponse(_message.Message):
    __slots__ = ("hits",)
    HITS_FIELD_NUMBER: _ClassVar[int]
    hits: _containers.RepeatedCompositeFieldContainer[ResearchHit]
    def __init__(self, hits: _Optional[_Iterable[_Union[ResearchHit, _Mapping]]] = ...) -> None: ...

class RepoFile(_message.Message):
    __slots__ = ("path", "content")
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    path: str
    content: str
    def __init__(self, path: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class CommitFilesRequest(_message.Message):
    __slots__ = ("files", "message", "build")
    FILES_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[RepoFile]
    message: str
    build: bool
    def __init__(self, files: _Optional[_Iterable[_Union[RepoFile, _Mapping]]] = ..., message: _Optional[str] = ..., build: bool = ...) -> None: ...

class CommitFilesResponse(_message.Message):
    __slots__ = ("committed",)
    COMMITTED_FIELD_NUMBER: _ClassVar[int]
    committed: int
    def __init__(self, committed: _Optional[int] = ...) -> None: ...

class SetBrandRequest(_message.Message):
    __slots__ = ("icon_svg", "primary", "secondary", "background", "accent", "tagline")
    ICON_SVG_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    ACCENT_FIELD_NUMBER: _ClassVar[int]
    TAGLINE_FIELD_NUMBER: _ClassVar[int]
    icon_svg: str
    primary: str
    secondary: str
    background: str
    accent: str
    tagline: str
    def __init__(self, icon_svg: _Optional[str] = ..., primary: _Optional[str] = ..., secondary: _Optional[str] = ..., background: _Optional[str] = ..., accent: _Optional[str] = ..., tagline: _Optional[str] = ...) -> None: ...

class SetBrandResponse(_message.Message):
    __slots__ = ("icon_url",)
    ICON_URL_FIELD_NUMBER: _ClassVar[int]
    icon_url: str
    def __init__(self, icon_url: _Optional[str] = ...) -> None: ...

class SetLandingRequest(_message.Message):
    __slots__ = ("html",)
    HTML_FIELD_NUMBER: _ClassVar[int]
    html: str
    def __init__(self, html: _Optional[str] = ...) -> None: ...

class SetLandingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RecordFindingRequest(_message.Message):
    __slots__ = ("tool", "kind", "value", "amount", "unit", "quote", "url")
    TOOL_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    QUOTE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    tool: str
    kind: str
    value: str
    amount: float
    unit: str
    quote: str
    url: str
    def __init__(self, tool: _Optional[str] = ..., kind: _Optional[str] = ..., value: _Optional[str] = ..., amount: _Optional[float] = ..., unit: _Optional[str] = ..., quote: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class RecordFindingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BooksSummaryRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BooksSummaryResponse(_message.Message):
    __slots__ = ("enabled", "summary", "open_invoices", "customers")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    OPEN_INVOICES_FIELD_NUMBER: _ClassVar[int]
    CUSTOMERS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    summary: _books_pb2.CashSummary
    open_invoices: _containers.RepeatedCompositeFieldContainer[_books_pb2.Invoice]
    customers: _containers.RepeatedCompositeFieldContainer[_books_pb2.Customer]
    def __init__(self, enabled: bool = ..., summary: _Optional[_Union[_books_pb2.CashSummary, _Mapping]] = ..., open_invoices: _Optional[_Iterable[_Union[_books_pb2.Invoice, _Mapping]]] = ..., customers: _Optional[_Iterable[_Union[_books_pb2.Customer, _Mapping]]] = ...) -> None: ...

class BooksCreateInvoiceRequest(_message.Message):
    __slots__ = ("customer_name", "lines", "tax_cents", "due_days", "notes", "send")
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    TAX_CENTS_FIELD_NUMBER: _ClassVar[int]
    DUE_DAYS_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    SEND_FIELD_NUMBER: _ClassVar[int]
    customer_name: str
    lines: _containers.RepeatedCompositeFieldContainer[_books_pb2.InvoiceLine]
    tax_cents: int
    due_days: int
    notes: str
    send: bool
    def __init__(self, customer_name: _Optional[str] = ..., lines: _Optional[_Iterable[_Union[_books_pb2.InvoiceLine, _Mapping]]] = ..., tax_cents: _Optional[int] = ..., due_days: _Optional[int] = ..., notes: _Optional[str] = ..., send: bool = ...) -> None: ...

class BooksCreateInvoiceResponse(_message.Message):
    __slots__ = ("invoice",)
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: _books_pb2.Invoice
    def __init__(self, invoice: _Optional[_Union[_books_pb2.Invoice, _Mapping]] = ...) -> None: ...

class BooksRecordExpenseRequest(_message.Message):
    __slots__ = ("vendor", "category", "amount_cents", "notes", "receipt_file_id")
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    vendor: str
    category: str
    amount_cents: int
    notes: str
    receipt_file_id: str
    def __init__(self, vendor: _Optional[str] = ..., category: _Optional[str] = ..., amount_cents: _Optional[int] = ..., notes: _Optional[str] = ..., receipt_file_id: _Optional[str] = ...) -> None: ...

class BooksRecordExpenseResponse(_message.Message):
    __slots__ = ("expense",)
    EXPENSE_FIELD_NUMBER: _ClassVar[int]
    expense: _books_pb2.Expense
    def __init__(self, expense: _Optional[_Union[_books_pb2.Expense, _Mapping]] = ...) -> None: ...

class BooksRecordPaymentRequest(_message.Message):
    __slots__ = ("invoice_number", "amount_cents", "method", "reference")
    INVOICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    invoice_number: str
    amount_cents: int
    method: str
    reference: str
    def __init__(self, invoice_number: _Optional[str] = ..., amount_cents: _Optional[int] = ..., method: _Optional[str] = ..., reference: _Optional[str] = ...) -> None: ...

class BooksRecordPaymentResponse(_message.Message):
    __slots__ = ("invoice",)
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: _books_pb2.Invoice
    def __init__(self, invoice: _Optional[_Union[_books_pb2.Invoice, _Mapping]] = ...) -> None: ...

class BooksReportRequest(_message.Message):
    __slots__ = ("period",)
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    period: str
    def __init__(self, period: _Optional[str] = ...) -> None: ...

class SocialAccountsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SocialAccountsResponse(_message.Message):
    __slots__ = ("enabled", "review_required", "accounts", "voice")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    REVIEW_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    VOICE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    review_required: bool
    accounts: _containers.RepeatedCompositeFieldContainer[_social_pb2.Account]
    voice: str
    def __init__(self, enabled: bool = ..., review_required: bool = ..., accounts: _Optional[_Iterable[_Union[_social_pb2.Account, _Mapping]]] = ..., voice: _Optional[str] = ...) -> None: ...

class SocialCreatePostRequest(_message.Message):
    __slots__ = ("platform", "text", "file_ids")
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    platform: _social_pb2.Platform
    text: str
    file_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, platform: _Optional[_Union[_social_pb2.Platform, str]] = ..., text: _Optional[str] = ..., file_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class SocialCreatePostResponse(_message.Message):
    __slots__ = ("post", "needs_review")
    POST_FIELD_NUMBER: _ClassVar[int]
    NEEDS_REVIEW_FIELD_NUMBER: _ClassVar[int]
    post: _social_pb2.Post
    needs_review: bool
    def __init__(self, post: _Optional[_Union[_social_pb2.Post, _Mapping]] = ..., needs_review: bool = ...) -> None: ...

class SocialPublishPostRequest(_message.Message):
    __slots__ = ("post_id",)
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    def __init__(self, post_id: _Optional[str] = ...) -> None: ...

class SocialPublishPostResponse(_message.Message):
    __slots__ = ("post",)
    POST_FIELD_NUMBER: _ClassVar[int]
    post: _social_pb2.Post
    def __init__(self, post: _Optional[_Union[_social_pb2.Post, _Mapping]] = ...) -> None: ...

class WriteUpThreadRequest(_message.Message):
    __slots__ = ("title",)
    TITLE_FIELD_NUMBER: _ClassVar[int]
    title: str
    def __init__(self, title: _Optional[str] = ...) -> None: ...

class WriteUpThreadResponse(_message.Message):
    __slots__ = ("canvas_id", "title", "blocks", "decisions")
    CANVAS_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    DECISIONS_FIELD_NUMBER: _ClassVar[int]
    canvas_id: str
    title: str
    blocks: int
    decisions: int
    def __init__(self, canvas_id: _Optional[str] = ..., title: _Optional[str] = ..., blocks: _Optional[int] = ..., decisions: _Optional[int] = ...) -> None: ...

class ReadCanvasRequest(_message.Message):
    __slots__ = ("canvas_id",)
    CANVAS_ID_FIELD_NUMBER: _ClassVar[int]
    canvas_id: str
    def __init__(self, canvas_id: _Optional[str] = ...) -> None: ...

class ReadCanvasResponse(_message.Message):
    __slots__ = ("canvas",)
    CANVAS_FIELD_NUMBER: _ClassVar[int]
    canvas: _canvas_pb2.Canvas
    def __init__(self, canvas: _Optional[_Union[_canvas_pb2.Canvas, _Mapping]] = ...) -> None: ...

class AskCanvasRequest(_message.Message):
    __slots__ = ("question", "limit")
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    question: str
    limit: int
    def __init__(self, question: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class AskCanvasResponse(_message.Message):
    __slots__ = ("summary", "answers")
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    ANSWERS_FIELD_NUMBER: _ClassVar[int]
    summary: str
    answers: _containers.RepeatedCompositeFieldContainer[_canvas_pb2.Answer]
    def __init__(self, summary: _Optional[str] = ..., answers: _Optional[_Iterable[_Union[_canvas_pb2.Answer, _Mapping]]] = ...) -> None: ...

class BooksReportResponse(_message.Message):
    __slots__ = ("enabled", "report")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    REPORT_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    report: _books_pb2.Report
    def __init__(self, enabled: bool = ..., report: _Optional[_Union[_books_pb2.Report, _Mapping]] = ...) -> None: ...

class ListBoardsRequest(_message.Message):
    __slots__ = ("limit",)
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    limit: int
    def __init__(self, limit: _Optional[int] = ...) -> None: ...

class BoardListing(_message.Message):
    __slots__ = ("board_id", "title", "objects", "app_frames")
    BOARD_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    APP_FRAMES_FIELD_NUMBER: _ClassVar[int]
    board_id: str
    title: str
    objects: int
    app_frames: int
    def __init__(self, board_id: _Optional[str] = ..., title: _Optional[str] = ..., objects: _Optional[int] = ..., app_frames: _Optional[int] = ...) -> None: ...

class ListBoardsResponse(_message.Message):
    __slots__ = ("boards",)
    BOARDS_FIELD_NUMBER: _ClassVar[int]
    boards: _containers.RepeatedCompositeFieldContainer[BoardListing]
    def __init__(self, boards: _Optional[_Iterable[_Union[BoardListing, _Mapping]]] = ...) -> None: ...

class ReadBoardRequest(_message.Message):
    __slots__ = ("board_id",)
    BOARD_ID_FIELD_NUMBER: _ClassVar[int]
    board_id: str
    def __init__(self, board_id: _Optional[str] = ...) -> None: ...

class ReadBoardResponse(_message.Message):
    __slots__ = ("board",)
    BOARD_FIELD_NUMBER: _ClassVar[int]
    board: _board_pb2.Board
    def __init__(self, board: _Optional[_Union[_board_pb2.Board, _Mapping]] = ...) -> None: ...

class BoardShape(_message.Message):
    __slots__ = ("id", "kind", "x", "y", "w", "h", "text", "fill", "parent_id", "from_id", "to_id", "file_id", "status", "app")
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    H_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    FILL_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_ID_FIELD_NUMBER: _ClassVar[int]
    TO_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    APP_FIELD_NUMBER: _ClassVar[int]
    id: str
    kind: str
    x: float
    y: float
    w: float
    h: float
    text: str
    fill: str
    parent_id: str
    from_id: str
    to_id: str
    file_id: str
    status: str
    app: AppFrameSpec
    def __init__(self, id: _Optional[str] = ..., kind: _Optional[str] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., w: _Optional[float] = ..., h: _Optional[float] = ..., text: _Optional[str] = ..., fill: _Optional[str] = ..., parent_id: _Optional[str] = ..., from_id: _Optional[str] = ..., to_id: _Optional[str] = ..., file_id: _Optional[str] = ..., status: _Optional[str] = ..., app: _Optional[_Union[AppFrameSpec, _Mapping]] = ...) -> None: ...

class AppFrameSpec(_message.Message):
    __slots__ = ("repo", "ref", "path", "viewport_width", "viewport_height")
    REPO_FIELD_NUMBER: _ClassVar[int]
    REF_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    VIEWPORT_WIDTH_FIELD_NUMBER: _ClassVar[int]
    VIEWPORT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    repo: str
    ref: str
    path: str
    viewport_width: int
    viewport_height: int
    def __init__(self, repo: _Optional[str] = ..., ref: _Optional[str] = ..., path: _Optional[str] = ..., viewport_width: _Optional[int] = ..., viewport_height: _Optional[int] = ...) -> None: ...

class WorkbenchStep(_message.Message):
    __slots__ = ("id", "title", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    status: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class WorkbenchStepsRequest(_message.Message):
    __slots__ = ("steps",)
    STEPS_FIELD_NUMBER: _ClassVar[int]
    steps: _containers.RepeatedCompositeFieldContainer[WorkbenchStep]
    def __init__(self, steps: _Optional[_Iterable[_Union[WorkbenchStep, _Mapping]]] = ...) -> None: ...

class WorkbenchStepsResponse(_message.Message):
    __slots__ = ("board_id",)
    BOARD_ID_FIELD_NUMBER: _ClassVar[int]
    board_id: str
    def __init__(self, board_id: _Optional[str] = ...) -> None: ...

class WorkbenchShowRequest(_message.Message):
    __slots__ = ("kind", "file_ids", "app", "text", "diagram", "title")
    KIND_FIELD_NUMBER: _ClassVar[int]
    FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    APP_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    DIAGRAM_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    file_ids: _containers.RepeatedScalarFieldContainer[str]
    app: AppFrameSpec
    text: str
    diagram: str
    title: str
    def __init__(self, kind: _Optional[str] = ..., file_ids: _Optional[_Iterable[str]] = ..., app: _Optional[_Union[AppFrameSpec, _Mapping]] = ..., text: _Optional[str] = ..., diagram: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class WorkbenchShowResponse(_message.Message):
    __slots__ = ("board_id", "object_ids")
    BOARD_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    board_id: str
    object_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, board_id: _Optional[str] = ..., object_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class DrawOnBoardRequest(_message.Message):
    __slots__ = ("board_id", "shapes", "delete_ids", "base_revs")
    class BaseRevsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    BOARD_ID_FIELD_NUMBER: _ClassVar[int]
    SHAPES_FIELD_NUMBER: _ClassVar[int]
    DELETE_IDS_FIELD_NUMBER: _ClassVar[int]
    BASE_REVS_FIELD_NUMBER: _ClassVar[int]
    board_id: str
    shapes: _containers.RepeatedCompositeFieldContainer[BoardShape]
    delete_ids: _containers.RepeatedScalarFieldContainer[str]
    base_revs: _containers.ScalarMap[str, int]
    def __init__(self, board_id: _Optional[str] = ..., shapes: _Optional[_Iterable[_Union[BoardShape, _Mapping]]] = ..., delete_ids: _Optional[_Iterable[str]] = ..., base_revs: _Optional[_Mapping[str, int]] = ...) -> None: ...

class DrawOnBoardResponse(_message.Message):
    __slots__ = ("object_ids", "objects", "conflict_ids", "conflict_note")
    OBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_IDS_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_NOTE_FIELD_NUMBER: _ClassVar[int]
    object_ids: _containers.RepeatedScalarFieldContainer[str]
    objects: int
    conflict_ids: _containers.RepeatedScalarFieldContainer[str]
    conflict_note: str
    def __init__(self, object_ids: _Optional[_Iterable[str]] = ..., objects: _Optional[int] = ..., conflict_ids: _Optional[_Iterable[str]] = ..., conflict_note: _Optional[str] = ...) -> None: ...

class ArrangeBoardRequest(_message.Message):
    __slots__ = ("board_id", "object_ids", "layout", "gap", "columns", "base_revs")
    class BaseRevsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    BOARD_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_FIELD_NUMBER: _ClassVar[int]
    GAP_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    BASE_REVS_FIELD_NUMBER: _ClassVar[int]
    board_id: str
    object_ids: _containers.RepeatedScalarFieldContainer[str]
    layout: str
    gap: float
    columns: int
    base_revs: _containers.ScalarMap[str, int]
    def __init__(self, board_id: _Optional[str] = ..., object_ids: _Optional[_Iterable[str]] = ..., layout: _Optional[str] = ..., gap: _Optional[float] = ..., columns: _Optional[int] = ..., base_revs: _Optional[_Mapping[str, int]] = ...) -> None: ...

class ArrangeBoardResponse(_message.Message):
    __slots__ = ("moved", "note", "conflict_ids", "conflict_note")
    MOVED_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_IDS_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_NOTE_FIELD_NUMBER: _ClassVar[int]
    moved: int
    note: str
    conflict_ids: _containers.RepeatedScalarFieldContainer[str]
    conflict_note: str
    def __init__(self, moved: _Optional[int] = ..., note: _Optional[str] = ..., conflict_ids: _Optional[_Iterable[str]] = ..., conflict_note: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("seq", "kind", "user_id", "user_name", "text", "gate_id", "decision", "card_id", "at", "handoff")
    SEQ_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    GATE_ID_FIELD_NUMBER: _ClassVar[int]
    DECISION_FIELD_NUMBER: _ClassVar[int]
    CARD_ID_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    HANDOFF_FIELD_NUMBER: _ClassVar[int]
    seq: int
    kind: InboxKind
    user_id: str
    user_name: str
    text: str
    gate_id: str
    decision: str
    card_id: str
    at: _timestamp_pb2.Timestamp
    handoff: HandoffStatus
    def __init__(self, seq: _Optional[int] = ..., kind: _Optional[_Union[InboxKind, str]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., text: _Optional[str] = ..., gate_id: _Optional[str] = ..., decision: _Optional[str] = ..., card_id: _Optional[str] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., handoff: _Optional[_Union[HandoffStatus, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("workspace_id", "channel_id", "thread_root_id", "agent_id", "requested_by", "instructions", "mode", "repo", "skip_neural_knowledge")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    REPO_FIELD_NUMBER: _ClassVar[int]
    SKIP_NEURAL_KNOWLEDGE_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    thread_root_id: str
    agent_id: str
    requested_by: str
    instructions: str
    mode: str
    repo: str
    skip_neural_knowledge: bool
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., requested_by: _Optional[str] = ..., instructions: _Optional[str] = ..., mode: _Optional[str] = ..., repo: _Optional[str] = ..., skip_neural_knowledge: bool = ...) -> None: ...

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

class RefreshNeuralKnowledgeRequest(_message.Message):
    __slots__ = ("workspace_id", "repo", "requested_by")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    REPO_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    repo: str
    requested_by: str
    def __init__(self, workspace_id: _Optional[str] = ..., repo: _Optional[str] = ..., requested_by: _Optional[str] = ...) -> None: ...

class RefreshNeuralKnowledgeResponse(_message.Message):
    __slots__ = ("channel_id", "thread_root_id", "started")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    thread_root_id: str
    started: bool
    def __init__(self, channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., started: bool = ...) -> None: ...

class OpenThreadRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id", "text")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    text: str
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class OpenThreadResponse(_message.Message):
    __slots__ = ("thread_root_id",)
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    thread_root_id: str
    def __init__(self, thread_root_id: _Optional[str] = ...) -> None: ...

class SetUpPreviewWorkflowRequest(_message.Message):
    __slots__ = ("workspace_id", "repos", "base_branch", "api_url", "secret_name", "branch")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    REPOS_FIELD_NUMBER: _ClassVar[int]
    BASE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    API_URL_FIELD_NUMBER: _ClassVar[int]
    SECRET_NAME_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    repos: _containers.RepeatedScalarFieldContainer[str]
    base_branch: str
    api_url: str
    secret_name: str
    branch: str
    def __init__(self, workspace_id: _Optional[str] = ..., repos: _Optional[_Iterable[str]] = ..., base_branch: _Optional[str] = ..., api_url: _Optional[str] = ..., secret_name: _Optional[str] = ..., branch: _Optional[str] = ...) -> None: ...

class PreviewWorkflowResult(_message.Message):
    __slots__ = ("repo", "status", "pull_request_url", "branch", "base_branch", "workflow_path", "reason")
    REPO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PULL_REQUEST_URL_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    BASE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_PATH_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    repo: str
    status: str
    pull_request_url: str
    branch: str
    base_branch: str
    workflow_path: str
    reason: str
    def __init__(self, repo: _Optional[str] = ..., status: _Optional[str] = ..., pull_request_url: _Optional[str] = ..., branch: _Optional[str] = ..., base_branch: _Optional[str] = ..., workflow_path: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class SetUpPreviewWorkflowResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[PreviewWorkflowResult]
    def __init__(self, results: _Optional[_Iterable[_Union[PreviewWorkflowResult, _Mapping]]] = ...) -> None: ...

class RegisterDeploymentRequest(_message.Message):
    __slots__ = ("workspace_id", "slug", "repo", "description")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    REPO_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    slug: str
    repo: str
    description: str
    def __init__(self, workspace_id: _Optional[str] = ..., slug: _Optional[str] = ..., repo: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class RegisterDeploymentResponse(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class GetDeploymentRequest(_message.Message):
    __slots__ = ("slug",)
    SLUG_FIELD_NUMBER: _ClassVar[int]
    slug: str
    def __init__(self, slug: _Optional[str] = ...) -> None: ...

class ProductProcess(_message.Message):
    __slots__ = ("name", "kind", "size", "cpu", "memory", "port", "public", "min", "max", "schedule", "timeout_seconds", "command", "volume", "scratch_gi")
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    SCRATCH_GI_FIELD_NUMBER: _ClassVar[int]
    name: str
    kind: str
    size: str
    cpu: str
    memory: str
    port: int
    public: bool
    min: int
    max: int
    schedule: str
    timeout_seconds: int
    command: _containers.RepeatedScalarFieldContainer[str]
    volume: str
    scratch_gi: int
    def __init__(self, name: _Optional[str] = ..., kind: _Optional[str] = ..., size: _Optional[str] = ..., cpu: _Optional[str] = ..., memory: _Optional[str] = ..., port: _Optional[int] = ..., public: bool = ..., min: _Optional[int] = ..., max: _Optional[int] = ..., schedule: _Optional[str] = ..., timeout_seconds: _Optional[int] = ..., command: _Optional[_Iterable[str]] = ..., volume: _Optional[str] = ..., scratch_gi: _Optional[int] = ...) -> None: ...

class ProductParts(_message.Message):
    __slots__ = ("databases", "cache_size", "buckets", "datasets", "library")
    DATABASES_FIELD_NUMBER: _ClassVar[int]
    CACHE_SIZE_FIELD_NUMBER: _ClassVar[int]
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    DATASETS_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_FIELD_NUMBER: _ClassVar[int]
    databases: _containers.RepeatedCompositeFieldContainer[ProductDatabase]
    cache_size: str
    buckets: _containers.RepeatedScalarFieldContainer[str]
    datasets: _containers.RepeatedScalarFieldContainer[str]
    library: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, databases: _Optional[_Iterable[_Union[ProductDatabase, _Mapping]]] = ..., cache_size: _Optional[str] = ..., buckets: _Optional[_Iterable[str]] = ..., datasets: _Optional[_Iterable[str]] = ..., library: _Optional[_Iterable[str]] = ...) -> None: ...

class ProductDatabase(_message.Message):
    __slots__ = ("name", "size", "storage", "extensions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    size: str
    storage: str
    extensions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., size: _Optional[str] = ..., storage: _Optional[str] = ..., extensions: _Optional[_Iterable[str]] = ...) -> None: ...

class ProductSpecChange(_message.Message):
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

class PreviewProductSpecRequest(_message.Message):
    __slots__ = ("slug", "change", "text")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    slug: str
    change: ProductSpecChange
    text: str
    def __init__(self, slug: _Optional[str] = ..., change: _Optional[_Union[ProductSpecChange, _Mapping]] = ..., text: _Optional[str] = ...) -> None: ...

class PreviewProductSpecResponse(_message.Message):
    __slots__ = ("text", "before", "after", "problems")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    text: str
    before: ProductCost
    after: ProductCost
    problems: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, text: _Optional[str] = ..., before: _Optional[_Union[ProductCost, _Mapping]] = ..., after: _Optional[_Union[ProductCost, _Mapping]] = ..., problems: _Optional[_Iterable[str]] = ...) -> None: ...

class ApplyProductSpecRequest(_message.Message):
    __slots__ = ("slug", "change", "text", "author_name", "author_email", "accepted_total_cents", "accepted_by")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_EMAIL_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_TOTAL_CENTS_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_BY_FIELD_NUMBER: _ClassVar[int]
    slug: str
    change: ProductSpecChange
    text: str
    author_name: str
    author_email: str
    accepted_total_cents: int
    accepted_by: str
    def __init__(self, slug: _Optional[str] = ..., change: _Optional[_Union[ProductSpecChange, _Mapping]] = ..., text: _Optional[str] = ..., author_name: _Optional[str] = ..., author_email: _Optional[str] = ..., accepted_total_cents: _Optional[int] = ..., accepted_by: _Optional[str] = ...) -> None: ...

class ApplyProductSpecResponse(_message.Message):
    __slots__ = ("commit_sha", "estimate", "live")
    COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    LIVE_FIELD_NUMBER: _ClassVar[int]
    commit_sha: str
    estimate: ProductCost
    live: bool
    def __init__(self, commit_sha: _Optional[str] = ..., estimate: _Optional[_Union[ProductCost, _Mapping]] = ..., live: bool = ...) -> None: ...

class GetProductSpecTextRequest(_message.Message):
    __slots__ = ("slug",)
    SLUG_FIELD_NUMBER: _ClassVar[int]
    slug: str
    def __init__(self, slug: _Optional[str] = ...) -> None: ...

class GetProductSpecTextResponse(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class ProductCost(_message.Message):
    __slots__ = ("base_cents", "overage_cents", "lines")
    BASE_CENTS_FIELD_NUMBER: _ClassVar[int]
    OVERAGE_CENTS_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    base_cents: int
    overage_cents: int
    lines: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base_cents: _Optional[int] = ..., overage_cents: _Optional[int] = ..., lines: _Optional[_Iterable[str]] = ...) -> None: ...

class PendingBuild(_message.Message):
    __slots__ = ("sha", "reason", "problems", "estimate", "at", "processes")
    SHA_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    PROCESSES_FIELD_NUMBER: _ClassVar[int]
    sha: str
    reason: str
    problems: _containers.RepeatedScalarFieldContainer[str]
    estimate: ProductCost
    at: str
    processes: _containers.RepeatedCompositeFieldContainer[ProductProcess]
    def __init__(self, sha: _Optional[str] = ..., reason: _Optional[str] = ..., problems: _Optional[_Iterable[str]] = ..., estimate: _Optional[_Union[ProductCost, _Mapping]] = ..., at: _Optional[str] = ..., processes: _Optional[_Iterable[_Union[ProductProcess, _Mapping]]] = ...) -> None: ...

class ProcessState(_message.Message):
    __slots__ = ("name", "kind", "desired", "ready", "suspended", "last_run_at", "last_run_result")
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    DESIRED_FIELD_NUMBER: _ClassVar[int]
    READY_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_RESULT_FIELD_NUMBER: _ClassVar[int]
    name: str
    kind: str
    desired: int
    ready: int
    suspended: bool
    last_run_at: str
    last_run_result: str
    def __init__(self, name: _Optional[str] = ..., kind: _Optional[str] = ..., desired: _Optional[int] = ..., ready: _Optional[int] = ..., suspended: bool = ..., last_run_at: _Optional[str] = ..., last_run_result: _Optional[str] = ...) -> None: ...

class JobRun(_message.Message):
    __slots__ = ("job", "id")
    JOB_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    job: str
    id: str
    def __init__(self, job: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class ProductChange(_message.Message):
    __slots__ = ("sha", "message", "at", "image_tag")
    SHA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    sha: str
    message: str
    at: str
    image_tag: str
    def __init__(self, sha: _Optional[str] = ..., message: _Optional[str] = ..., at: _Optional[str] = ..., image_tag: _Optional[str] = ...) -> None: ...

class ValidateSpecRequest(_message.Message):
    __slots__ = ("tank_yaml",)
    TANK_YAML_FIELD_NUMBER: _ClassVar[int]
    tank_yaml: str
    def __init__(self, tank_yaml: _Optional[str] = ...) -> None: ...

class ValidateSpecResponse(_message.Message):
    __slots__ = ("ok", "problems", "estimate", "processes")
    OK_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    PROCESSES_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    problems: _containers.RepeatedScalarFieldContainer[str]
    estimate: ProductCost
    processes: _containers.RepeatedCompositeFieldContainer[ProductProcess]
    def __init__(self, ok: bool = ..., problems: _Optional[_Iterable[str]] = ..., estimate: _Optional[_Union[ProductCost, _Mapping]] = ..., processes: _Optional[_Iterable[_Union[ProductProcess, _Mapping]]] = ...) -> None: ...

class GetProductSpecRequest(_message.Message):
    __slots__ = ("slug",)
    SLUG_FIELD_NUMBER: _ClassVar[int]
    slug: str
    def __init__(self, slug: _Optional[str] = ...) -> None: ...

class GetProductSpecResponse(_message.Message):
    __slots__ = ("processes", "estimate", "pending", "restarted_at", "paused", "runs", "env_keys", "secrets", "previews", "secrets_set", "parts")
    PROCESSES_FIELD_NUMBER: _ClassVar[int]
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    PENDING_FIELD_NUMBER: _ClassVar[int]
    RESTARTED_AT_FIELD_NUMBER: _ClassVar[int]
    PAUSED_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    ENV_KEYS_FIELD_NUMBER: _ClassVar[int]
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    PREVIEWS_FIELD_NUMBER: _ClassVar[int]
    SECRETS_SET_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    processes: _containers.RepeatedCompositeFieldContainer[ProductProcess]
    estimate: ProductCost
    pending: PendingBuild
    restarted_at: str
    paused: _containers.RepeatedScalarFieldContainer[str]
    runs: _containers.RepeatedCompositeFieldContainer[JobRun]
    env_keys: _containers.RepeatedScalarFieldContainer[str]
    secrets: _containers.RepeatedScalarFieldContainer[str]
    previews: _containers.RepeatedCompositeFieldContainer[ProductPreview]
    secrets_set: _containers.RepeatedScalarFieldContainer[str]
    parts: ProductParts
    def __init__(self, processes: _Optional[_Iterable[_Union[ProductProcess, _Mapping]]] = ..., estimate: _Optional[_Union[ProductCost, _Mapping]] = ..., pending: _Optional[_Union[PendingBuild, _Mapping]] = ..., restarted_at: _Optional[str] = ..., paused: _Optional[_Iterable[str]] = ..., runs: _Optional[_Iterable[_Union[JobRun, _Mapping]]] = ..., env_keys: _Optional[_Iterable[str]] = ..., secrets: _Optional[_Iterable[str]] = ..., previews: _Optional[_Iterable[_Union[ProductPreview, _Mapping]]] = ..., secrets_set: _Optional[_Iterable[str]] = ..., parts: _Optional[_Union[ProductParts, _Mapping]] = ...) -> None: ...

class ProductPreview(_message.Message):
    __slots__ = ("pull_request", "url", "image_tag", "expires_at")
    PULL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    pull_request: int
    url: str
    image_tag: str
    expires_at: str
    def __init__(self, pull_request: _Optional[int] = ..., url: _Optional[str] = ..., image_tag: _Optional[str] = ..., expires_at: _Optional[str] = ...) -> None: ...

class ApproveProductBuildRequest(_message.Message):
    __slots__ = ("slug", "sha", "by")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    SHA_FIELD_NUMBER: _ClassVar[int]
    BY_FIELD_NUMBER: _ClassVar[int]
    slug: str
    sha: str
    by: str
    def __init__(self, slug: _Optional[str] = ..., sha: _Optional[str] = ..., by: _Optional[str] = ...) -> None: ...

class ApproveProductBuildResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OperateProductRequest(_message.Message):
    __slots__ = ("slug", "action", "process", "by")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PROCESS_FIELD_NUMBER: _ClassVar[int]
    BY_FIELD_NUMBER: _ClassVar[int]
    slug: str
    action: str
    process: str
    by: str
    def __init__(self, slug: _Optional[str] = ..., action: _Optional[str] = ..., process: _Optional[str] = ..., by: _Optional[str] = ...) -> None: ...

class OperateProductResponse(_message.Message):
    __slots__ = ("run_id",)
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class ListProductChangesRequest(_message.Message):
    __slots__ = ("slug", "limit")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    slug: str
    limit: int
    def __init__(self, slug: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListProductChangesResponse(_message.Message):
    __slots__ = ("changes",)
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[ProductChange]
    def __init__(self, changes: _Optional[_Iterable[_Union[ProductChange, _Mapping]]] = ...) -> None: ...

class RollbackProductRequest(_message.Message):
    __slots__ = ("slug", "sha", "by")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    SHA_FIELD_NUMBER: _ClassVar[int]
    BY_FIELD_NUMBER: _ClassVar[int]
    slug: str
    sha: str
    by: str
    def __init__(self, slug: _Optional[str] = ..., sha: _Optional[str] = ..., by: _Optional[str] = ...) -> None: ...

class RollbackProductResponse(_message.Message):
    __slots__ = ("applied", "reason", "problems", "estimate")
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    applied: bool
    reason: str
    problems: _containers.RepeatedScalarFieldContainer[str]
    estimate: ProductCost
    def __init__(self, applied: bool = ..., reason: _Optional[str] = ..., problems: _Optional[_Iterable[str]] = ..., estimate: _Optional[_Union[ProductCost, _Mapping]] = ...) -> None: ...

class SetProductSecretRequest(_message.Message):
    __slots__ = ("slug", "name", "value")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    slug: str
    name: str
    value: str
    def __init__(self, slug: _Optional[str] = ..., name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class SetProductSecretResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExportProductRequest(_message.Message):
    __slots__ = ("slug",)
    SLUG_FIELD_NUMBER: _ClassVar[int]
    slug: str
    def __init__(self, slug: _Optional[str] = ...) -> None: ...

class ExportProductResponse(_message.Message):
    __slots__ = ("compose_yaml", "image")
    COMPOSE_YAML_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    compose_yaml: str
    image: str
    def __init__(self, compose_yaml: _Optional[str] = ..., image: _Optional[str] = ...) -> None: ...

class UpdateProductSpecRequest(_message.Message):
    __slots__ = ("slug", "process", "size", "min", "max", "schedule", "author_name", "author_email")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    PROCESS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_EMAIL_FIELD_NUMBER: _ClassVar[int]
    slug: str
    process: str
    size: str
    min: int
    max: int
    schedule: str
    author_name: str
    author_email: str
    def __init__(self, slug: _Optional[str] = ..., process: _Optional[str] = ..., size: _Optional[str] = ..., min: _Optional[int] = ..., max: _Optional[int] = ..., schedule: _Optional[str] = ..., author_name: _Optional[str] = ..., author_email: _Optional[str] = ...) -> None: ...

class UpdateProductSpecResponse(_message.Message):
    __slots__ = ("commit_sha", "estimate")
    COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    commit_sha: str
    estimate: ProductCost
    def __init__(self, commit_sha: _Optional[str] = ..., estimate: _Optional[_Union[ProductCost, _Mapping]] = ...) -> None: ...

class ProductState(_message.Message):
    __slots__ = ("phase", "image_tag", "replicas", "ready", "restarts", "last_exit_reason", "last_exit_code", "started_at", "disk_bytes", "cpu_limit", "memory_limit", "events", "processes")
    PHASE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    READY_FIELD_NUMBER: _ClassVar[int]
    RESTARTS_FIELD_NUMBER: _ClassVar[int]
    LAST_EXIT_REASON_FIELD_NUMBER: _ClassVar[int]
    LAST_EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    DISK_BYTES_FIELD_NUMBER: _ClassVar[int]
    CPU_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    PROCESSES_FIELD_NUMBER: _ClassVar[int]
    phase: str
    image_tag: str
    replicas: int
    ready: int
    restarts: int
    last_exit_reason: str
    last_exit_code: int
    started_at: str
    disk_bytes: int
    cpu_limit: str
    memory_limit: str
    events: _containers.RepeatedCompositeFieldContainer[ProductEvent]
    processes: _containers.RepeatedCompositeFieldContainer[ProcessState]
    def __init__(self, phase: _Optional[str] = ..., image_tag: _Optional[str] = ..., replicas: _Optional[int] = ..., ready: _Optional[int] = ..., restarts: _Optional[int] = ..., last_exit_reason: _Optional[str] = ..., last_exit_code: _Optional[int] = ..., started_at: _Optional[str] = ..., disk_bytes: _Optional[int] = ..., cpu_limit: _Optional[str] = ..., memory_limit: _Optional[str] = ..., events: _Optional[_Iterable[_Union[ProductEvent, _Mapping]]] = ..., processes: _Optional[_Iterable[_Union[ProcessState, _Mapping]]] = ...) -> None: ...

class ProductEvent(_message.Message):
    __slots__ = ("at", "type", "reason", "message")
    AT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    at: str
    type: str
    reason: str
    message: str
    def __init__(self, at: _Optional[str] = ..., type: _Optional[str] = ..., reason: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class CheckProductPageRequest(_message.Message):
    __slots__ = ("slug", "path")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    slug: str
    path: str
    def __init__(self, slug: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class CheckProductPageResponse(_message.Message):
    __slots__ = ("check",)
    CHECK_FIELD_NUMBER: _ClassVar[int]
    check: CheckLiveResponse
    def __init__(self, check: _Optional[_Union[CheckLiveResponse, _Mapping]] = ...) -> None: ...

class GetProductStateRequest(_message.Message):
    __slots__ = ("slug", "tail_lines")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    TAIL_LINES_FIELD_NUMBER: _ClassVar[int]
    slug: str
    tail_lines: int
    def __init__(self, slug: _Optional[str] = ..., tail_lines: _Optional[int] = ...) -> None: ...

class GetProductStateResponse(_message.Message):
    __slots__ = ("state", "logs")
    STATE_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    state: ProductState
    logs: str
    def __init__(self, state: _Optional[_Union[ProductState, _Mapping]] = ..., logs: _Optional[str] = ...) -> None: ...

class GetDeploymentResponse(_message.Message):
    __slots__ = ("repo", "url", "image_tag", "replicas", "workflow_present", "managed")
    REPO_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_PRESENT_FIELD_NUMBER: _ClassVar[int]
    MANAGED_FIELD_NUMBER: _ClassVar[int]
    repo: str
    url: str
    image_tag: str
    replicas: int
    workflow_present: bool
    managed: bool
    def __init__(self, repo: _Optional[str] = ..., url: _Optional[str] = ..., image_tag: _Optional[str] = ..., replicas: _Optional[int] = ..., workflow_present: bool = ..., managed: bool = ...) -> None: ...

class SetProductReplicasRequest(_message.Message):
    __slots__ = ("slug", "replicas", "reason")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    slug: str
    replicas: int
    reason: str
    def __init__(self, slug: _Optional[str] = ..., replicas: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...

class SetProductReplicasResponse(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class CreateProductRepoRequest(_message.Message):
    __slots__ = ("workspace_id", "slug", "description")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    slug: str
    description: str
    def __init__(self, workspace_id: _Optional[str] = ..., slug: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CreateProductRepoResponse(_message.Message):
    __slots__ = ("repo",)
    REPO_FIELD_NUMBER: _ClassVar[int]
    repo: str
    def __init__(self, repo: _Optional[str] = ...) -> None: ...

class CommitProductFilesRequest(_message.Message):
    __slots__ = ("slug", "files", "message", "build")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    slug: str
    files: _containers.RepeatedCompositeFieldContainer[RepoFile]
    message: str
    build: bool
    def __init__(self, slug: _Optional[str] = ..., files: _Optional[_Iterable[_Union[RepoFile, _Mapping]]] = ..., message: _Optional[str] = ..., build: bool = ...) -> None: ...

class CommitProductFilesResponse(_message.Message):
    __slots__ = ("committed",)
    COMMITTED_FIELD_NUMBER: _ClassVar[int]
    committed: int
    def __init__(self, committed: _Optional[int] = ...) -> None: ...

class BindChannelRepoRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id", "repo", "base_branch", "toolchain", "hosted", "requested_by")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    REPO_FIELD_NUMBER: _ClassVar[int]
    BASE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    TOOLCHAIN_FIELD_NUMBER: _ClassVar[int]
    HOSTED_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    repo: str
    base_branch: str
    toolchain: str
    hosted: bool
    requested_by: str
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., repo: _Optional[str] = ..., base_branch: _Optional[str] = ..., toolchain: _Optional[str] = ..., hosted: bool = ..., requested_by: _Optional[str] = ...) -> None: ...

class BindChannelRepoResponse(_message.Message):
    __slots__ = ("repo", "base_branch", "toolchain", "previous_repo")
    REPO_FIELD_NUMBER: _ClassVar[int]
    BASE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    TOOLCHAIN_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_REPO_FIELD_NUMBER: _ClassVar[int]
    repo: str
    base_branch: str
    toolchain: str
    previous_repo: str
    def __init__(self, repo: _Optional[str] = ..., base_branch: _Optional[str] = ..., toolchain: _Optional[str] = ..., previous_repo: _Optional[str] = ...) -> None: ...

class UnbindChannelRepoRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id", "requested_by")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    requested_by: str
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., requested_by: _Optional[str] = ...) -> None: ...

class UnbindChannelRepoResponse(_message.Message):
    __slots__ = ("removed",)
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    removed: bool
    def __init__(self, removed: bool = ...) -> None: ...

class RepoAccessEntry(_message.Message):
    __slots__ = ("repo", "access")
    REPO_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    repo: str
    access: str
    def __init__(self, repo: _Optional[str] = ..., access: _Optional[str] = ...) -> None: ...

class SetChannelRepoAccessRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id", "entries", "requested_by")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    entries: _containers.RepeatedCompositeFieldContainer[RepoAccessEntry]
    requested_by: str
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[RepoAccessEntry, _Mapping]]] = ..., requested_by: _Optional[str] = ...) -> None: ...

class SetChannelRepoAccessResponse(_message.Message):
    __slots__ = ("entries", "added")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    ADDED_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[RepoAccessEntry]
    added: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, entries: _Optional[_Iterable[_Union[RepoAccessEntry, _Mapping]]] = ..., added: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateGitHubConnectStateRequest(_message.Message):
    __slots__ = ("workspace_id", "created_by", "ttl_seconds")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    TTL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    created_by: str
    ttl_seconds: int
    def __init__(self, workspace_id: _Optional[str] = ..., created_by: _Optional[str] = ..., ttl_seconds: _Optional[int] = ...) -> None: ...

class CreateGitHubConnectStateResponse(_message.Message):
    __slots__ = ("state_token", "expires_at")
    STATE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    state_token: str
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, state_token: _Optional[str] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SetChannelAgentSettingsRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id", "settings", "requested_by")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    settings: _agent_pb2.TreadSettings
    requested_by: str
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., settings: _Optional[_Union[_agent_pb2.TreadSettings, _Mapping]] = ..., requested_by: _Optional[str] = ...) -> None: ...

class SetChannelAgentSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _agent_pb2.TreadSettings
    def __init__(self, settings: _Optional[_Union[_agent_pb2.TreadSettings, _Mapping]] = ...) -> None: ...

class SetWorkspaceAgentPolicyRequest(_message.Message):
    __slots__ = ("workspace_id", "policy", "requested_by")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    policy: bytes
    requested_by: str
    def __init__(self, workspace_id: _Optional[str] = ..., policy: _Optional[bytes] = ..., requested_by: _Optional[str] = ...) -> None: ...

class SetWorkspaceAgentPolicyResponse(_message.Message):
    __slots__ = ("policy",)
    POLICY_FIELD_NUMBER: _ClassVar[int]
    policy: bytes
    def __init__(self, policy: _Optional[bytes] = ...) -> None: ...

class ArenaTurnRequest(_message.Message):
    __slots__ = ("environment_id", "round_id", "product_workspace_id", "system", "user", "max_tokens")
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ROUND_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    environment_id: str
    round_id: str
    product_workspace_id: str
    system: str
    user: str
    max_tokens: int
    def __init__(self, environment_id: _Optional[str] = ..., round_id: _Optional[str] = ..., product_workspace_id: _Optional[str] = ..., system: _Optional[str] = ..., user: _Optional[str] = ..., max_tokens: _Optional[int] = ...) -> None: ...

class ArenaTurnResponse(_message.Message):
    __slots__ = ("text", "model", "prompt_hash", "input_tokens", "output_tokens")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    PROMPT_HASH_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    text: str
    model: str
    prompt_hash: str
    input_tokens: int
    output_tokens: int
    def __init__(self, text: _Optional[str] = ..., model: _Optional[str] = ..., prompt_hash: _Optional[str] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ...) -> None: ...

class ReadRepoRequest(_message.Message):
    __slots__ = ("workspace_id", "repo", "ref", "path", "tree", "max_bytes")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    REPO_FIELD_NUMBER: _ClassVar[int]
    REF_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TREE_FIELD_NUMBER: _ClassVar[int]
    MAX_BYTES_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    repo: str
    ref: str
    path: str
    tree: bool
    max_bytes: int
    def __init__(self, workspace_id: _Optional[str] = ..., repo: _Optional[str] = ..., ref: _Optional[str] = ..., path: _Optional[str] = ..., tree: bool = ..., max_bytes: _Optional[int] = ...) -> None: ...

class ReadRepoResponse(_message.Message):
    __slots__ = ("sha", "content", "paths", "status", "reason", "truncated")
    SHA_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    sha: str
    content: bytes
    paths: _containers.RepeatedScalarFieldContainer[str]
    status: str
    reason: str
    truncated: bool
    def __init__(self, sha: _Optional[str] = ..., content: _Optional[bytes] = ..., paths: _Optional[_Iterable[str]] = ..., status: _Optional[str] = ..., reason: _Optional[str] = ..., truncated: bool = ...) -> None: ...

class BuildPreviewRequest(_message.Message):
    __slots__ = ("workspace_id", "repo", "ref")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    REPO_FIELD_NUMBER: _ClassVar[int]
    REF_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    repo: str
    ref: str
    def __init__(self, workspace_id: _Optional[str] = ..., repo: _Optional[str] = ..., ref: _Optional[str] = ...) -> None: ...

class BuildPreviewResponse(_message.Message):
    __slots__ = ("state", "url", "sha", "reason", "framework")
    STATE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    SHA_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
    state: str
    url: str
    sha: str
    reason: str
    framework: str
    def __init__(self, state: _Optional[str] = ..., url: _Optional[str] = ..., sha: _Optional[str] = ..., reason: _Optional[str] = ..., framework: _Optional[str] = ...) -> None: ...

class OpenSetupPullRequestRequest(_message.Message):
    __slots__ = ("workspace_id", "repo", "verify_token", "bridge_tag")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    REPO_FIELD_NUMBER: _ClassVar[int]
    VERIFY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_TAG_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    repo: str
    verify_token: str
    bridge_tag: str
    def __init__(self, workspace_id: _Optional[str] = ..., repo: _Optional[str] = ..., verify_token: _Optional[str] = ..., bridge_tag: _Optional[str] = ...) -> None: ...

class OpenSetupPullRequestResponse(_message.Message):
    __slots__ = ("url", "state", "framework", "files", "note")
    URL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    url: str
    state: str
    framework: str
    files: _containers.RepeatedScalarFieldContainer[str]
    note: str
    def __init__(self, url: _Optional[str] = ..., state: _Optional[str] = ..., framework: _Optional[str] = ..., files: _Optional[_Iterable[str]] = ..., note: _Optional[str] = ...) -> None: ...

class ReadElementAtRequest(_message.Message):
    __slots__ = ("url", "viewport_width", "viewport_height", "x", "y")
    URL_FIELD_NUMBER: _ClassVar[int]
    VIEWPORT_WIDTH_FIELD_NUMBER: _ClassVar[int]
    VIEWPORT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    url: str
    viewport_width: int
    viewport_height: int
    x: float
    y: float
    def __init__(self, url: _Optional[str] = ..., viewport_width: _Optional[int] = ..., viewport_height: _Optional[int] = ..., x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class ReadElementAtResponse(_message.Message):
    __slots__ = ("tag", "text", "test_id", "classes", "selector", "x", "y", "w", "h", "note")
    TAG_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TEST_ID_FIELD_NUMBER: _ClassVar[int]
    CLASSES_FIELD_NUMBER: _ClassVar[int]
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    H_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    tag: str
    text: str
    test_id: str
    classes: _containers.RepeatedScalarFieldContainer[str]
    selector: str
    x: float
    y: float
    w: float
    h: float
    note: str
    def __init__(self, tag: _Optional[str] = ..., text: _Optional[str] = ..., test_id: _Optional[str] = ..., classes: _Optional[_Iterable[str]] = ..., selector: _Optional[str] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., w: _Optional[float] = ..., h: _Optional[float] = ..., note: _Optional[str] = ...) -> None: ...

class MergeChangeRequest(_message.Message):
    __slots__ = ("workspace_id", "thread_root_id", "sha")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    SHA_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    thread_root_id: str
    sha: str
    def __init__(self, workspace_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., sha: _Optional[str] = ...) -> None: ...

class MergeChangeResponse(_message.Message):
    __slots__ = ("merged", "pull_request_url", "note")
    MERGED_FIELD_NUMBER: _ClassVar[int]
    PULL_REQUEST_URL_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    merged: bool
    pull_request_url: str
    note: str
    def __init__(self, merged: bool = ..., pull_request_url: _Optional[str] = ..., note: _Optional[str] = ...) -> None: ...
