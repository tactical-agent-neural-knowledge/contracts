from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RunState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RUN_STATE_UNSPECIFIED: _ClassVar[RunState]
    RUN_STATE_REQUESTED: _ClassVar[RunState]
    RUN_STATE_ADMITTED: _ClassVar[RunState]
    RUN_STATE_PROVISIONING: _ClassVar[RunState]
    RUN_STATE_PLANNING: _ClassVar[RunState]
    RUN_STATE_AWAITING_PLAN_APPROVAL: _ClassVar[RunState]
    RUN_STATE_IMPLEMENTING: _ClassVar[RunState]
    RUN_STATE_PUSHED: _ClassVar[RunState]
    RUN_STATE_CI_WATCHING: _ClassVar[RunState]
    RUN_STATE_PR_OPEN: _ClassVar[RunState]
    RUN_STATE_AWAITING_MERGE_APPROVAL: _ClassVar[RunState]
    RUN_STATE_MERGED: _ClassVar[RunState]
    RUN_STATE_VERIFYING_DEPLOY: _ClassVar[RunState]
    RUN_STATE_DONE: _ClassVar[RunState]
    RUN_STATE_CANCELLED: _ClassVar[RunState]
    RUN_STATE_FAILED: _ClassVar[RunState]
    RUN_STATE_BUDGET_EXHAUSTED: _ClassVar[RunState]
    RUN_STATE_TIMED_OUT: _ClassVar[RunState]
    RUN_STATE_APPROVAL_EXPIRED: _ClassVar[RunState]
RUN_STATE_UNSPECIFIED: RunState
RUN_STATE_REQUESTED: RunState
RUN_STATE_ADMITTED: RunState
RUN_STATE_PROVISIONING: RunState
RUN_STATE_PLANNING: RunState
RUN_STATE_AWAITING_PLAN_APPROVAL: RunState
RUN_STATE_IMPLEMENTING: RunState
RUN_STATE_PUSHED: RunState
RUN_STATE_CI_WATCHING: RunState
RUN_STATE_PR_OPEN: RunState
RUN_STATE_AWAITING_MERGE_APPROVAL: RunState
RUN_STATE_MERGED: RunState
RUN_STATE_VERIFYING_DEPLOY: RunState
RUN_STATE_DONE: RunState
RUN_STATE_CANCELLED: RunState
RUN_STATE_FAILED: RunState
RUN_STATE_BUDGET_EXHAUSTED: RunState
RUN_STATE_TIMED_OUT: RunState
RUN_STATE_APPROVAL_EXPIRED: RunState

class Agent(_message.Message):
    __slots__ = ("id", "workspace_id", "principal_id", "name", "scopes")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    principal_id: str
    name: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., principal_id: _Optional[str] = ..., name: _Optional[str] = ..., scopes: _Optional[_Iterable[str]] = ...) -> None: ...

class Run(_message.Message):
    __slots__ = ("id", "workspace_id", "channel_id", "thread_root_id", "agent_id", "requested_by", "state", "branch", "pr_url", "cost_usd", "status_message_id", "started_at", "ended_at", "plan_hash", "pending_gate_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    PR_URL_FIELD_NUMBER: _ClassVar[int]
    COST_USD_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    PLAN_HASH_FIELD_NUMBER: _ClassVar[int]
    PENDING_GATE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    channel_id: str
    thread_root_id: str
    agent_id: str
    requested_by: str
    state: RunState
    branch: str
    pr_url: str
    cost_usd: float
    status_message_id: str
    started_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    plan_hash: str
    pending_gate_id: str
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., requested_by: _Optional[str] = ..., state: _Optional[_Union[RunState, str]] = ..., branch: _Optional[str] = ..., pr_url: _Optional[str] = ..., cost_usd: _Optional[float] = ..., status_message_id: _Optional[str] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., plan_hash: _Optional[str] = ..., pending_gate_id: _Optional[str] = ...) -> None: ...

class StartRunRequest(_message.Message):
    __slots__ = ("thread_root_id", "agent_id", "instructions", "requested_by")
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    thread_root_id: str
    agent_id: str
    instructions: str
    requested_by: str
    def __init__(self, thread_root_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., instructions: _Optional[str] = ..., requested_by: _Optional[str] = ...) -> None: ...

class StartRunResponse(_message.Message):
    __slots__ = ("run", "agent_session_token", "token_expires_at")
    RUN_FIELD_NUMBER: _ClassVar[int]
    AGENT_SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    run: Run
    agent_session_token: str
    token_expires_at: _timestamp_pb2.Timestamp
    def __init__(self, run: _Optional[_Union[Run, _Mapping]] = ..., agent_session_token: _Optional[str] = ..., token_expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StopRunRequest(_message.Message):
    __slots__ = ("run_id", "reason")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    reason: str
    def __init__(self, run_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class StopRunResponse(_message.Message):
    __slots__ = ("run",)
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: Run
    def __init__(self, run: _Optional[_Union[Run, _Mapping]] = ...) -> None: ...

class HeartbeatRequest(_message.Message):
    __slots__ = ("run_id",)
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class HeartbeatResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetStatusRequest(_message.Message):
    __slots__ = ("run_id", "state", "status", "branch", "pr_url", "cost_usd")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    PR_URL_FIELD_NUMBER: _ClassVar[int]
    COST_USD_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    state: RunState
    status: str
    branch: str
    pr_url: str
    cost_usd: float
    def __init__(self, run_id: _Optional[str] = ..., state: _Optional[_Union[RunState, str]] = ..., status: _Optional[str] = ..., branch: _Optional[str] = ..., pr_url: _Optional[str] = ..., cost_usd: _Optional[float] = ...) -> None: ...

class SetStatusResponse(_message.Message):
    __slots__ = ("run",)
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: Run
    def __init__(self, run: _Optional[_Union[Run, _Mapping]] = ...) -> None: ...

class SetProductBrandRequest(_message.Message):
    __slots__ = ("run_id", "icon_svg", "primary", "secondary", "background", "accent", "tagline")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ICON_SVG_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    ACCENT_FIELD_NUMBER: _ClassVar[int]
    TAGLINE_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    icon_svg: str
    primary: str
    secondary: str
    background: str
    accent: str
    tagline: str
    def __init__(self, run_id: _Optional[str] = ..., icon_svg: _Optional[str] = ..., primary: _Optional[str] = ..., secondary: _Optional[str] = ..., background: _Optional[str] = ..., accent: _Optional[str] = ..., tagline: _Optional[str] = ...) -> None: ...

class SetProductBrandResponse(_message.Message):
    __slots__ = ("icon_url",)
    ICON_URL_FIELD_NUMBER: _ClassVar[int]
    icon_url: str
    def __init__(self, icon_url: _Optional[str] = ...) -> None: ...

class SetProductLandingRequest(_message.Message):
    __slots__ = ("run_id", "html")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    HTML_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    html: str
    def __init__(self, run_id: _Optional[str] = ..., html: _Optional[str] = ...) -> None: ...

class SetProductLandingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RecordProductFindingRequest(_message.Message):
    __slots__ = ("run_id", "tool", "kind", "value", "amount", "unit", "quote", "url")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    QUOTE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    tool: str
    kind: str
    value: str
    amount: float
    unit: str
    quote: str
    url: str
    def __init__(self, run_id: _Optional[str] = ..., tool: _Optional[str] = ..., kind: _Optional[str] = ..., value: _Optional[str] = ..., amount: _Optional[float] = ..., unit: _Optional[str] = ..., quote: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class RecordProductFindingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetRunRequest(_message.Message):
    __slots__ = ("run_id",)
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class GetRunResponse(_message.Message):
    __slots__ = ("run",)
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: Run
    def __init__(self, run: _Optional[_Union[Run, _Mapping]] = ...) -> None: ...

class ListRunsRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id", "thread_root_id", "cursor", "limit")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    thread_root_id: str
    cursor: str
    limit: int
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., cursor: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListRunsResponse(_message.Message):
    __slots__ = ("runs", "next_cursor")
    RUNS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    runs: _containers.RepeatedCompositeFieldContainer[Run]
    next_cursor: str
    def __init__(self, runs: _Optional[_Iterable[_Union[Run, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class ListAgentsRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListAgentsResponse(_message.Message):
    __slots__ = ("agents",)
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    agents: _containers.RepeatedCompositeFieldContainer[Agent]
    def __init__(self, agents: _Optional[_Iterable[_Union[Agent, _Mapping]]] = ...) -> None: ...

class RepoBinding(_message.Message):
    __slots__ = ("repo", "base_branch", "toolchain")
    REPO_FIELD_NUMBER: _ClassVar[int]
    BASE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    TOOLCHAIN_FIELD_NUMBER: _ClassVar[int]
    repo: str
    base_branch: str
    toolchain: str
    def __init__(self, repo: _Optional[str] = ..., base_branch: _Optional[str] = ..., toolchain: _Optional[str] = ...) -> None: ...

class RepoAccess(_message.Message):
    __slots__ = ("repo", "access")
    REPO_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    repo: str
    access: str
    def __init__(self, repo: _Optional[str] = ..., access: _Optional[str] = ...) -> None: ...

class RepoConnection(_message.Message):
    __slots__ = ("connected", "account_login", "repos", "binding", "can_manage", "access", "premium", "hosting_available", "deployment")
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_LOGIN_FIELD_NUMBER: _ClassVar[int]
    REPOS_FIELD_NUMBER: _ClassVar[int]
    BINDING_FIELD_NUMBER: _ClassVar[int]
    CAN_MANAGE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    PREMIUM_FIELD_NUMBER: _ClassVar[int]
    HOSTING_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    connected: bool
    account_login: str
    repos: _containers.RepeatedScalarFieldContainer[str]
    binding: RepoBinding
    can_manage: bool
    access: _containers.RepeatedCompositeFieldContainer[RepoAccess]
    premium: bool
    hosting_available: bool
    deployment: TreadDeployment
    def __init__(self, connected: bool = ..., account_login: _Optional[str] = ..., repos: _Optional[_Iterable[str]] = ..., binding: _Optional[_Union[RepoBinding, _Mapping]] = ..., can_manage: bool = ..., access: _Optional[_Iterable[_Union[RepoAccess, _Mapping]]] = ..., premium: bool = ..., hosting_available: bool = ..., deployment: _Optional[_Union[TreadDeployment, _Mapping]] = ...) -> None: ...

class SetRepoAccessRequest(_message.Message):
    __slots__ = ("channel_id", "access")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    access: _containers.RepeatedCompositeFieldContainer[RepoAccess]
    def __init__(self, channel_id: _Optional[str] = ..., access: _Optional[_Iterable[_Union[RepoAccess, _Mapping]]] = ...) -> None: ...

class SetRepoAccessResponse(_message.Message):
    __slots__ = ("access",)
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    access: _containers.RepeatedCompositeFieldContainer[RepoAccess]
    def __init__(self, access: _Optional[_Iterable[_Union[RepoAccess, _Mapping]]] = ...) -> None: ...

class TreadSettings(_message.Message):
    __slots__ = ("concurrent_runs", "auto_accept_plans", "max_run_usd", "daily_usd", "pull_requests", "pr_reviewer_ids", "read_neural_knowledge")
    CONCURRENT_RUNS_FIELD_NUMBER: _ClassVar[int]
    AUTO_ACCEPT_PLANS_FIELD_NUMBER: _ClassVar[int]
    MAX_RUN_USD_FIELD_NUMBER: _ClassVar[int]
    DAILY_USD_FIELD_NUMBER: _ClassVar[int]
    PULL_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    PR_REVIEWER_IDS_FIELD_NUMBER: _ClassVar[int]
    READ_NEURAL_KNOWLEDGE_FIELD_NUMBER: _ClassVar[int]
    concurrent_runs: int
    auto_accept_plans: bool
    max_run_usd: float
    daily_usd: float
    pull_requests: str
    pr_reviewer_ids: _containers.RepeatedScalarFieldContainer[str]
    read_neural_knowledge: bool
    def __init__(self, concurrent_runs: _Optional[int] = ..., auto_accept_plans: bool = ..., max_run_usd: _Optional[float] = ..., daily_usd: _Optional[float] = ..., pull_requests: _Optional[str] = ..., pr_reviewer_ids: _Optional[_Iterable[str]] = ..., read_neural_knowledge: bool = ...) -> None: ...

class HourBucket(_message.Message):
    __slots__ = ("hour", "runs", "spend_usd")
    HOUR_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    SPEND_USD_FIELD_NUMBER: _ClassVar[int]
    hour: _timestamp_pb2.Timestamp
    runs: int
    spend_usd: float
    def __init__(self, hour: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., runs: _Optional[int] = ..., spend_usd: _Optional[float] = ...) -> None: ...

class TreadMetrics(_message.Message):
    __slots__ = ("spend_today_usd", "spend_month_usd", "runs_today", "runs_month", "success_rate_30d", "hours", "workspace_spend_today_usd", "workspace_spend_month_usd", "running_now", "avg_run_minutes_30d")
    SPEND_TODAY_USD_FIELD_NUMBER: _ClassVar[int]
    SPEND_MONTH_USD_FIELD_NUMBER: _ClassVar[int]
    RUNS_TODAY_FIELD_NUMBER: _ClassVar[int]
    RUNS_MONTH_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_RATE_30D_FIELD_NUMBER: _ClassVar[int]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_SPEND_TODAY_USD_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_SPEND_MONTH_USD_FIELD_NUMBER: _ClassVar[int]
    RUNNING_NOW_FIELD_NUMBER: _ClassVar[int]
    AVG_RUN_MINUTES_30D_FIELD_NUMBER: _ClassVar[int]
    spend_today_usd: float
    spend_month_usd: float
    runs_today: int
    runs_month: int
    success_rate_30d: float
    hours: _containers.RepeatedCompositeFieldContainer[HourBucket]
    workspace_spend_today_usd: float
    workspace_spend_month_usd: float
    running_now: int
    avg_run_minutes_30d: float
    def __init__(self, spend_today_usd: _Optional[float] = ..., spend_month_usd: _Optional[float] = ..., runs_today: _Optional[int] = ..., runs_month: _Optional[int] = ..., success_rate_30d: _Optional[float] = ..., hours: _Optional[_Iterable[_Union[HourBucket, _Mapping]]] = ..., workspace_spend_today_usd: _Optional[float] = ..., workspace_spend_month_usd: _Optional[float] = ..., running_now: _Optional[int] = ..., avg_run_minutes_30d: _Optional[float] = ...) -> None: ...

class GetTreadSwitchboardRequest(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class GetTreadSwitchboardResponse(_message.Message):
    __slots__ = ("metrics", "settings", "can_manage")
    METRICS_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CAN_MANAGE_FIELD_NUMBER: _ClassVar[int]
    metrics: TreadMetrics
    settings: TreadSettings
    can_manage: bool
    def __init__(self, metrics: _Optional[_Union[TreadMetrics, _Mapping]] = ..., settings: _Optional[_Union[TreadSettings, _Mapping]] = ..., can_manage: bool = ...) -> None: ...

class SetTreadSettingsRequest(_message.Message):
    __slots__ = ("channel_id", "settings")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    settings: TreadSettings
    def __init__(self, channel_id: _Optional[str] = ..., settings: _Optional[_Union[TreadSettings, _Mapping]] = ...) -> None: ...

class SetTreadSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: TreadSettings
    def __init__(self, settings: _Optional[_Union[TreadSettings, _Mapping]] = ...) -> None: ...

class GetRepoConnectionRequest(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class GetRepoConnectionResponse(_message.Message):
    __slots__ = ("connection",)
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    connection: RepoConnection
    def __init__(self, connection: _Optional[_Union[RepoConnection, _Mapping]] = ...) -> None: ...

class StartGitHubConnectRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class StartGitHubConnectResponse(_message.Message):
    __slots__ = ("install_url",)
    INSTALL_URL_FIELD_NUMBER: _ClassVar[int]
    install_url: str
    def __init__(self, install_url: _Optional[str] = ...) -> None: ...

class BindRepoRequest(_message.Message):
    __slots__ = ("channel_id", "repo", "base_branch", "toolchain")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    REPO_FIELD_NUMBER: _ClassVar[int]
    BASE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    TOOLCHAIN_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    repo: str
    base_branch: str
    toolchain: str
    def __init__(self, channel_id: _Optional[str] = ..., repo: _Optional[str] = ..., base_branch: _Optional[str] = ..., toolchain: _Optional[str] = ...) -> None: ...

class BindRepoResponse(_message.Message):
    __slots__ = ("binding",)
    BINDING_FIELD_NUMBER: _ClassVar[int]
    binding: RepoBinding
    def __init__(self, binding: _Optional[_Union[RepoBinding, _Mapping]] = ...) -> None: ...

class UnbindRepoRequest(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class UnbindRepoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TreadDeployment(_message.Message):
    __slots__ = ("slug", "repo", "url", "awake", "updated_at")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    REPO_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    AWAKE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    slug: str
    repo: str
    url: str
    awake: bool
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, slug: _Optional[str] = ..., repo: _Optional[str] = ..., url: _Optional[str] = ..., awake: bool = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateTreadRepoRequest(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class CreateTreadRepoResponse(_message.Message):
    __slots__ = ("binding", "deployment")
    BINDING_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    binding: RepoBinding
    deployment: TreadDeployment
    def __init__(self, binding: _Optional[_Union[RepoBinding, _Mapping]] = ..., deployment: _Optional[_Union[TreadDeployment, _Mapping]] = ...) -> None: ...

class SetTreadDeploymentRequest(_message.Message):
    __slots__ = ("channel_id", "awake")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    AWAKE_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    awake: bool
    def __init__(self, channel_id: _Optional[str] = ..., awake: bool = ...) -> None: ...

class SetTreadDeploymentResponse(_message.Message):
    __slots__ = ("deployment",)
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    deployment: TreadDeployment
    def __init__(self, deployment: _Optional[_Union[TreadDeployment, _Mapping]] = ...) -> None: ...
