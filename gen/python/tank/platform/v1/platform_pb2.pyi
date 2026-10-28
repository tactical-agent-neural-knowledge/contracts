from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgentureRow(_message.Message):
    __slots__ = ("workspace_id", "slug", "name", "description", "enabled", "weight", "next_due_at", "last_run_at", "runs", "last_error", "agent_minutes", "live_run_id", "live_state", "spend_usd", "price_cents", "claimed", "auto_approve")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    NEXT_DUE_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_AT_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    AGENT_MINUTES_FIELD_NUMBER: _ClassVar[int]
    LIVE_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    LIVE_STATE_FIELD_NUMBER: _ClassVar[int]
    SPEND_USD_FIELD_NUMBER: _ClassVar[int]
    PRICE_CENTS_FIELD_NUMBER: _ClassVar[int]
    CLAIMED_FIELD_NUMBER: _ClassVar[int]
    AUTO_APPROVE_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    slug: str
    name: str
    description: str
    enabled: bool
    weight: int
    next_due_at: _timestamp_pb2.Timestamp
    last_run_at: _timestamp_pb2.Timestamp
    runs: int
    last_error: str
    agent_minutes: int
    live_run_id: str
    live_state: str
    spend_usd: float
    price_cents: int
    claimed: bool
    auto_approve: bool
    def __init__(self, workspace_id: _Optional[str] = ..., slug: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., enabled: bool = ..., weight: _Optional[int] = ..., next_due_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_run_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., runs: _Optional[int] = ..., last_error: _Optional[str] = ..., agent_minutes: _Optional[int] = ..., live_run_id: _Optional[str] = ..., live_state: _Optional[str] = ..., spend_usd: _Optional[float] = ..., price_cents: _Optional[int] = ..., claimed: bool = ..., auto_approve: bool = ...) -> None: ...

class ListAgenturesRequest(_message.Message):
    __slots__ = ("query", "limit", "offset")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    query: str
    limit: int
    offset: int
    def __init__(self, query: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListAgenturesResponse(_message.Message):
    __slots__ = ("agentures", "total", "summary")
    AGENTURES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    agentures: _containers.RepeatedCompositeFieldContainer[AgentureRow]
    total: int
    summary: BoardSummary
    def __init__(self, agentures: _Optional[_Iterable[_Union[AgentureRow, _Mapping]]] = ..., total: _Optional[int] = ..., summary: _Optional[_Union[BoardSummary, _Mapping]] = ...) -> None: ...

class BoardSummary(_message.Message):
    __slots__ = ("in_flight", "max_concurrent", "enabled", "killed", "auto_default", "hours_from", "hours_to", "hours_zone", "hours_days", "unclaimed", "agent_minutes_24h", "spend_usd_24h", "spend_usd_total", "spend_usd_1h", "spend_usd_3h")
    IN_FLIGHT_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    KILLED_FIELD_NUMBER: _ClassVar[int]
    AUTO_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    HOURS_FROM_FIELD_NUMBER: _ClassVar[int]
    HOURS_TO_FIELD_NUMBER: _ClassVar[int]
    HOURS_ZONE_FIELD_NUMBER: _ClassVar[int]
    HOURS_DAYS_FIELD_NUMBER: _ClassVar[int]
    UNCLAIMED_FIELD_NUMBER: _ClassVar[int]
    AGENT_MINUTES_24H_FIELD_NUMBER: _ClassVar[int]
    SPEND_USD_24H_FIELD_NUMBER: _ClassVar[int]
    SPEND_USD_TOTAL_FIELD_NUMBER: _ClassVar[int]
    SPEND_USD_1H_FIELD_NUMBER: _ClassVar[int]
    SPEND_USD_3H_FIELD_NUMBER: _ClassVar[int]
    in_flight: int
    max_concurrent: int
    enabled: bool
    killed: bool
    auto_default: bool
    hours_from: int
    hours_to: int
    hours_zone: str
    hours_days: _containers.RepeatedScalarFieldContainer[int]
    unclaimed: int
    agent_minutes_24h: int
    spend_usd_24h: float
    spend_usd_total: float
    spend_usd_1h: float
    spend_usd_3h: float
    def __init__(self, in_flight: _Optional[int] = ..., max_concurrent: _Optional[int] = ..., enabled: bool = ..., killed: bool = ..., auto_default: bool = ..., hours_from: _Optional[int] = ..., hours_to: _Optional[int] = ..., hours_zone: _Optional[str] = ..., hours_days: _Optional[_Iterable[int]] = ..., unclaimed: _Optional[int] = ..., agent_minutes_24h: _Optional[int] = ..., spend_usd_24h: _Optional[float] = ..., spend_usd_total: _Optional[float] = ..., spend_usd_1h: _Optional[float] = ..., spend_usd_3h: _Optional[float] = ...) -> None: ...

class SetAllocationRequest(_message.Message):
    __slots__ = ("workspace_id", "enabled", "weight", "run_now", "auto_approve")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    RUN_NOW_FIELD_NUMBER: _ClassVar[int]
    AUTO_APPROVE_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    enabled: bool
    weight: int
    run_now: bool
    auto_approve: bool
    def __init__(self, workspace_id: _Optional[str] = ..., enabled: bool = ..., weight: _Optional[int] = ..., run_now: bool = ..., auto_approve: bool = ...) -> None: ...

class SetAllocationResponse(_message.Message):
    __slots__ = ("agenture",)
    AGENTURE_FIELD_NUMBER: _ClassVar[int]
    agenture: AgentureRow
    def __init__(self, agenture: _Optional[_Union[AgentureRow, _Mapping]] = ...) -> None: ...

class SetBoardSettingsRequest(_message.Message):
    __slots__ = ("max_concurrent", "killed", "auto_default", "hours_from", "hours_to", "hours_zone", "hours_days")
    MAX_CONCURRENT_FIELD_NUMBER: _ClassVar[int]
    KILLED_FIELD_NUMBER: _ClassVar[int]
    AUTO_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    HOURS_FROM_FIELD_NUMBER: _ClassVar[int]
    HOURS_TO_FIELD_NUMBER: _ClassVar[int]
    HOURS_ZONE_FIELD_NUMBER: _ClassVar[int]
    HOURS_DAYS_FIELD_NUMBER: _ClassVar[int]
    max_concurrent: int
    killed: bool
    auto_default: bool
    hours_from: int
    hours_to: int
    hours_zone: str
    hours_days: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, max_concurrent: _Optional[int] = ..., killed: bool = ..., auto_default: bool = ..., hours_from: _Optional[int] = ..., hours_to: _Optional[int] = ..., hours_zone: _Optional[str] = ..., hours_days: _Optional[_Iterable[int]] = ...) -> None: ...

class SetBoardSettingsResponse(_message.Message):
    __slots__ = ("summary",)
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    summary: BoardSummary
    def __init__(self, summary: _Optional[_Union[BoardSummary, _Mapping]] = ...) -> None: ...

class StopRunRequest(_message.Message):
    __slots__ = ("run_id", "reason")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    reason: str
    def __init__(self, run_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class StopRunResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MergeProposal(_message.Message):
    __slots__ = ("id", "absorbed_slug", "absorbed_name", "absorbed_summary", "survivor_slug", "survivor_name", "survivor_summary", "similarity", "status", "auto", "proposed_at", "done_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ABSORBED_SLUG_FIELD_NUMBER: _ClassVar[int]
    ABSORBED_NAME_FIELD_NUMBER: _ClassVar[int]
    ABSORBED_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SURVIVOR_SLUG_FIELD_NUMBER: _ClassVar[int]
    SURVIVOR_NAME_FIELD_NUMBER: _ClassVar[int]
    SURVIVOR_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SIMILARITY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AUTO_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_AT_FIELD_NUMBER: _ClassVar[int]
    DONE_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    absorbed_slug: str
    absorbed_name: str
    absorbed_summary: str
    survivor_slug: str
    survivor_name: str
    survivor_summary: str
    similarity: float
    status: str
    auto: bool
    proposed_at: _timestamp_pb2.Timestamp
    done_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., absorbed_slug: _Optional[str] = ..., absorbed_name: _Optional[str] = ..., absorbed_summary: _Optional[str] = ..., survivor_slug: _Optional[str] = ..., survivor_name: _Optional[str] = ..., survivor_summary: _Optional[str] = ..., similarity: _Optional[float] = ..., status: _Optional[str] = ..., auto: bool = ..., proposed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., done_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListMergesRequest(_message.Message):
    __slots__ = ("include_decided",)
    INCLUDE_DECIDED_FIELD_NUMBER: _ClassVar[int]
    include_decided: bool
    def __init__(self, include_decided: bool = ...) -> None: ...

class ListMergesResponse(_message.Message):
    __slots__ = ("merges",)
    MERGES_FIELD_NUMBER: _ClassVar[int]
    merges: _containers.RepeatedCompositeFieldContainer[MergeProposal]
    def __init__(self, merges: _Optional[_Iterable[_Union[MergeProposal, _Mapping]]] = ...) -> None: ...

class DecideMergeRequest(_message.Message):
    __slots__ = ("id", "approve")
    ID_FIELD_NUMBER: _ClassVar[int]
    APPROVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    approve: bool
    def __init__(self, id: _Optional[str] = ..., approve: bool = ...) -> None: ...

class DecideMergeResponse(_message.Message):
    __slots__ = ("merge",)
    MERGE_FIELD_NUMBER: _ClassVar[int]
    merge: MergeProposal
    def __init__(self, merge: _Optional[_Union[MergeProposal, _Mapping]] = ...) -> None: ...

class DropCandidate(_message.Message):
    __slots__ = ("workspace_id", "slug", "name", "industry", "score", "reasons")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INDUSTRY_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    REASONS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    slug: str
    name: str
    industry: str
    score: int
    reasons: str
    def __init__(self, workspace_id: _Optional[str] = ..., slug: _Optional[str] = ..., name: _Optional[str] = ..., industry: _Optional[str] = ..., score: _Optional[int] = ..., reasons: _Optional[str] = ...) -> None: ...

class ListDropCandidatesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListDropCandidatesResponse(_message.Message):
    __slots__ = ("candidates", "day")
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    candidates: _containers.RepeatedCompositeFieldContainer[DropCandidate]
    day: str
    def __init__(self, candidates: _Optional[_Iterable[_Union[DropCandidate, _Mapping]]] = ..., day: _Optional[str] = ...) -> None: ...

class UserRow(_message.Message):
    __slots__ = ("id", "display_name", "email", "kind", "created_at", "last_login_at", "last_active_at", "workspaces", "super_admin")
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_LOGIN_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    WORKSPACES_FIELD_NUMBER: _ClassVar[int]
    SUPER_ADMIN_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    email: str
    kind: str
    created_at: _timestamp_pb2.Timestamp
    last_login_at: _timestamp_pb2.Timestamp
    last_active_at: _timestamp_pb2.Timestamp
    workspaces: int
    super_admin: bool
    def __init__(self, id: _Optional[str] = ..., display_name: _Optional[str] = ..., email: _Optional[str] = ..., kind: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_login_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_active_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., workspaces: _Optional[int] = ..., super_admin: bool = ...) -> None: ...

class SearchUsersRequest(_message.Message):
    __slots__ = ("query", "limit", "offset", "include_machines", "sort")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_MACHINES_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    query: str
    limit: int
    offset: int
    include_machines: bool
    sort: str
    def __init__(self, query: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ..., include_machines: bool = ..., sort: _Optional[str] = ...) -> None: ...

class SearchUsersResponse(_message.Message):
    __slots__ = ("users", "total")
    USERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[UserRow]
    total: int
    def __init__(self, users: _Optional[_Iterable[_Union[UserRow, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...

class Membership(_message.Message):
    __slots__ = ("workspace_id", "slug", "name", "role", "joined_at", "last_active_at", "deactivated", "plan")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    JOINED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATED_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    slug: str
    name: str
    role: str
    joined_at: _timestamp_pb2.Timestamp
    last_active_at: _timestamp_pb2.Timestamp
    deactivated: bool
    plan: str
    def __init__(self, workspace_id: _Optional[str] = ..., slug: _Optional[str] = ..., name: _Optional[str] = ..., role: _Optional[str] = ..., joined_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_active_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deactivated: bool = ..., plan: _Optional[str] = ...) -> None: ...

class LoginRow(_message.Message):
    __slots__ = ("at", "kind", "client", "live")
    AT_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    LIVE_FIELD_NUMBER: _ClassVar[int]
    at: _timestamp_pb2.Timestamp
    kind: str
    client: str
    live: bool
    def __init__(self, at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., kind: _Optional[str] = ..., client: _Optional[str] = ..., live: bool = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ("user", "memberships", "logins")
    USER_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIPS_FIELD_NUMBER: _ClassVar[int]
    LOGINS_FIELD_NUMBER: _ClassVar[int]
    user: UserRow
    memberships: _containers.RepeatedCompositeFieldContainer[Membership]
    logins: _containers.RepeatedCompositeFieldContainer[LoginRow]
    def __init__(self, user: _Optional[_Union[UserRow, _Mapping]] = ..., memberships: _Optional[_Iterable[_Union[Membership, _Mapping]]] = ..., logins: _Optional[_Iterable[_Union[LoginRow, _Mapping]]] = ...) -> None: ...

class WorkspaceRow(_message.Message):
    __slots__ = ("id", "slug", "name", "kind", "plan", "addons", "people", "created_at", "last_active_at", "owner_email", "agent_runs_30d", "agent_cost_usd_30d", "agent_billed_cents_month")
    ID_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    ADDONS_FIELD_NUMBER: _ClassVar[int]
    PEOPLE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    OWNER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    AGENT_RUNS_30D_FIELD_NUMBER: _ClassVar[int]
    AGENT_COST_USD_30D_FIELD_NUMBER: _ClassVar[int]
    AGENT_BILLED_CENTS_MONTH_FIELD_NUMBER: _ClassVar[int]
    id: str
    slug: str
    name: str
    kind: str
    plan: str
    addons: _containers.RepeatedScalarFieldContainer[str]
    people: int
    created_at: _timestamp_pb2.Timestamp
    last_active_at: _timestamp_pb2.Timestamp
    owner_email: str
    agent_runs_30d: int
    agent_cost_usd_30d: float
    agent_billed_cents_month: int
    def __init__(self, id: _Optional[str] = ..., slug: _Optional[str] = ..., name: _Optional[str] = ..., kind: _Optional[str] = ..., plan: _Optional[str] = ..., addons: _Optional[_Iterable[str]] = ..., people: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_active_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., owner_email: _Optional[str] = ..., agent_runs_30d: _Optional[int] = ..., agent_cost_usd_30d: _Optional[float] = ..., agent_billed_cents_month: _Optional[int] = ...) -> None: ...

class SearchWorkspacesRequest(_message.Message):
    __slots__ = ("query", "limit", "offset", "sort", "kind", "plan")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    query: str
    limit: int
    offset: int
    sort: str
    kind: str
    plan: str
    def __init__(self, query: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ..., sort: _Optional[str] = ..., kind: _Optional[str] = ..., plan: _Optional[str] = ...) -> None: ...

class SearchWorkspacesResponse(_message.Message):
    __slots__ = ("workspaces", "total")
    WORKSPACES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    workspaces: _containers.RepeatedCompositeFieldContainer[WorkspaceRow]
    total: int
    def __init__(self, workspaces: _Optional[_Iterable[_Union[WorkspaceRow, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...

class MemberRow(_message.Message):
    __slots__ = ("user_id", "display_name", "email", "kind", "role", "joined_at", "last_login_at", "last_active_at", "deactivated")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    JOINED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_LOGIN_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATED_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    display_name: str
    email: str
    kind: str
    role: str
    joined_at: _timestamp_pb2.Timestamp
    last_login_at: _timestamp_pb2.Timestamp
    last_active_at: _timestamp_pb2.Timestamp
    deactivated: bool
    def __init__(self, user_id: _Optional[str] = ..., display_name: _Optional[str] = ..., email: _Optional[str] = ..., kind: _Optional[str] = ..., role: _Optional[str] = ..., joined_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_login_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_active_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deactivated: bool = ...) -> None: ...

class Feature(_message.Message):
    __slots__ = ("key", "label", "on", "since")
    KEY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ON_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    key: str
    label: str
    on: bool
    since: _timestamp_pb2.Timestamp
    def __init__(self, key: _Optional[str] = ..., label: _Optional[str] = ..., on: bool = ..., since: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Subscription(_message.Message):
    __slots__ = ("product", "provider", "status", "seats", "period_end")
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SEATS_FIELD_NUMBER: _ClassVar[int]
    PERIOD_END_FIELD_NUMBER: _ClassVar[int]
    product: str
    provider: str
    status: str
    seats: int
    period_end: str
    def __init__(self, product: _Optional[str] = ..., provider: _Optional[str] = ..., status: _Optional[str] = ..., seats: _Optional[int] = ..., period_end: _Optional[str] = ...) -> None: ...

class DailyCount(_message.Message):
    __slots__ = ("day", "messages", "active_people", "agent_runs", "agent_cost_usd", "new_people", "new_workspaces")
    DAY_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_PEOPLE_FIELD_NUMBER: _ClassVar[int]
    AGENT_RUNS_FIELD_NUMBER: _ClassVar[int]
    AGENT_COST_USD_FIELD_NUMBER: _ClassVar[int]
    NEW_PEOPLE_FIELD_NUMBER: _ClassVar[int]
    NEW_WORKSPACES_FIELD_NUMBER: _ClassVar[int]
    day: str
    messages: int
    active_people: int
    agent_runs: int
    agent_cost_usd: float
    new_people: int
    new_workspaces: int
    def __init__(self, day: _Optional[str] = ..., messages: _Optional[int] = ..., active_people: _Optional[int] = ..., agent_runs: _Optional[int] = ..., agent_cost_usd: _Optional[float] = ..., new_people: _Optional[int] = ..., new_workspaces: _Optional[int] = ...) -> None: ...

class AgentRunRow(_message.Message):
    __slots__ = ("id", "agent_name", "state", "started_at", "ended_at", "minutes", "cost_usd")
    ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    MINUTES_FIELD_NUMBER: _ClassVar[int]
    COST_USD_FIELD_NUMBER: _ClassVar[int]
    id: str
    agent_name: str
    state: str
    started_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    minutes: int
    cost_usd: float
    def __init__(self, id: _Optional[str] = ..., agent_name: _Optional[str] = ..., state: _Optional[str] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., minutes: _Optional[int] = ..., cost_usd: _Optional[float] = ...) -> None: ...

class AgentUsage(_message.Message):
    __slots__ = ("runs_30d", "failed_30d", "minutes_30d", "cost_usd_30d", "cost_usd_month", "billed_cents_month", "cap_cents", "recent", "agents")
    RUNS_30D_FIELD_NUMBER: _ClassVar[int]
    FAILED_30D_FIELD_NUMBER: _ClassVar[int]
    MINUTES_30D_FIELD_NUMBER: _ClassVar[int]
    COST_USD_30D_FIELD_NUMBER: _ClassVar[int]
    COST_USD_MONTH_FIELD_NUMBER: _ClassVar[int]
    BILLED_CENTS_MONTH_FIELD_NUMBER: _ClassVar[int]
    CAP_CENTS_FIELD_NUMBER: _ClassVar[int]
    RECENT_FIELD_NUMBER: _ClassVar[int]
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    runs_30d: int
    failed_30d: int
    minutes_30d: int
    cost_usd_30d: float
    cost_usd_month: float
    billed_cents_month: int
    cap_cents: int
    recent: _containers.RepeatedCompositeFieldContainer[AgentRunRow]
    agents: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, runs_30d: _Optional[int] = ..., failed_30d: _Optional[int] = ..., minutes_30d: _Optional[int] = ..., cost_usd_30d: _Optional[float] = ..., cost_usd_month: _Optional[float] = ..., billed_cents_month: _Optional[int] = ..., cap_cents: _Optional[int] = ..., recent: _Optional[_Iterable[_Union[AgentRunRow, _Mapping]]] = ..., agents: _Optional[_Iterable[str]] = ...) -> None: ...

class WorkspaceCounts(_message.Message):
    __slots__ = ("treads", "messages", "files", "boards", "pages")
    TREADS_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    BOARDS_FIELD_NUMBER: _ClassVar[int]
    PAGES_FIELD_NUMBER: _ClassVar[int]
    treads: int
    messages: int
    files: int
    boards: int
    pages: int
    def __init__(self, treads: _Optional[int] = ..., messages: _Optional[int] = ..., files: _Optional[int] = ..., boards: _Optional[int] = ..., pages: _Optional[int] = ...) -> None: ...

class GetWorkspaceRequest(_message.Message):
    __slots__ = ("workspace_id", "slug")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    slug: str
    def __init__(self, workspace_id: _Optional[str] = ..., slug: _Optional[str] = ...) -> None: ...

class GetWorkspaceResponse(_message.Message):
    __slots__ = ("workspace", "members", "features", "subscriptions", "agent_usage", "days", "counts")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    AGENT_USAGE_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    COUNTS_FIELD_NUMBER: _ClassVar[int]
    workspace: WorkspaceRow
    members: _containers.RepeatedCompositeFieldContainer[MemberRow]
    features: _containers.RepeatedCompositeFieldContainer[Feature]
    subscriptions: _containers.RepeatedCompositeFieldContainer[Subscription]
    agent_usage: AgentUsage
    days: _containers.RepeatedCompositeFieldContainer[DailyCount]
    counts: WorkspaceCounts
    def __init__(self, workspace: _Optional[_Union[WorkspaceRow, _Mapping]] = ..., members: _Optional[_Iterable[_Union[MemberRow, _Mapping]]] = ..., features: _Optional[_Iterable[_Union[Feature, _Mapping]]] = ..., subscriptions: _Optional[_Iterable[_Union[Subscription, _Mapping]]] = ..., agent_usage: _Optional[_Union[AgentUsage, _Mapping]] = ..., days: _Optional[_Iterable[_Union[DailyCount, _Mapping]]] = ..., counts: _Optional[_Union[WorkspaceCounts, _Mapping]] = ...) -> None: ...

class GetOverviewRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetOverviewResponse(_message.Message):
    __slots__ = ("people", "people_new_7d", "people_active_1d", "people_active_7d", "workspaces", "workspaces_new_7d", "premium", "agent_cost_usd_month", "agent_runs_30d", "days", "caller_is_root", "most_active")
    PEOPLE_FIELD_NUMBER: _ClassVar[int]
    PEOPLE_NEW_7D_FIELD_NUMBER: _ClassVar[int]
    PEOPLE_ACTIVE_1D_FIELD_NUMBER: _ClassVar[int]
    PEOPLE_ACTIVE_7D_FIELD_NUMBER: _ClassVar[int]
    WORKSPACES_FIELD_NUMBER: _ClassVar[int]
    WORKSPACES_NEW_7D_FIELD_NUMBER: _ClassVar[int]
    PREMIUM_FIELD_NUMBER: _ClassVar[int]
    AGENT_COST_USD_MONTH_FIELD_NUMBER: _ClassVar[int]
    AGENT_RUNS_30D_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    CALLER_IS_ROOT_FIELD_NUMBER: _ClassVar[int]
    MOST_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    people: int
    people_new_7d: int
    people_active_1d: int
    people_active_7d: int
    workspaces: int
    workspaces_new_7d: int
    premium: int
    agent_cost_usd_month: float
    agent_runs_30d: int
    days: _containers.RepeatedCompositeFieldContainer[DailyCount]
    caller_is_root: bool
    most_active: _containers.RepeatedCompositeFieldContainer[WorkspaceRow]
    def __init__(self, people: _Optional[int] = ..., people_new_7d: _Optional[int] = ..., people_active_1d: _Optional[int] = ..., people_active_7d: _Optional[int] = ..., workspaces: _Optional[int] = ..., workspaces_new_7d: _Optional[int] = ..., premium: _Optional[int] = ..., agent_cost_usd_month: _Optional[float] = ..., agent_runs_30d: _Optional[int] = ..., days: _Optional[_Iterable[_Union[DailyCount, _Mapping]]] = ..., caller_is_root: bool = ..., most_active: _Optional[_Iterable[_Union[WorkspaceRow, _Mapping]]] = ...) -> None: ...

class SuperAdminRow(_message.Message):
    __slots__ = ("user_id", "email", "display_name", "root", "added_by_email", "added_at")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ROOT_FIELD_NUMBER: _ClassVar[int]
    ADDED_BY_EMAIL_FIELD_NUMBER: _ClassVar[int]
    ADDED_AT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    email: str
    display_name: str
    root: bool
    added_by_email: str
    added_at: _timestamp_pb2.Timestamp
    def __init__(self, user_id: _Optional[str] = ..., email: _Optional[str] = ..., display_name: _Optional[str] = ..., root: bool = ..., added_by_email: _Optional[str] = ..., added_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListSuperAdminsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSuperAdminsResponse(_message.Message):
    __slots__ = ("admins", "caller_is_root")
    ADMINS_FIELD_NUMBER: _ClassVar[int]
    CALLER_IS_ROOT_FIELD_NUMBER: _ClassVar[int]
    admins: _containers.RepeatedCompositeFieldContainer[SuperAdminRow]
    caller_is_root: bool
    def __init__(self, admins: _Optional[_Iterable[_Union[SuperAdminRow, _Mapping]]] = ..., caller_is_root: bool = ...) -> None: ...

class AddSuperAdminRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class AddSuperAdminResponse(_message.Message):
    __slots__ = ("admins",)
    ADMINS_FIELD_NUMBER: _ClassVar[int]
    admins: _containers.RepeatedCompositeFieldContainer[SuperAdminRow]
    def __init__(self, admins: _Optional[_Iterable[_Union[SuperAdminRow, _Mapping]]] = ...) -> None: ...

class RemoveSuperAdminRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class RemoveSuperAdminResponse(_message.Message):
    __slots__ = ("admins",)
    ADMINS_FIELD_NUMBER: _ClassVar[int]
    admins: _containers.RepeatedCompositeFieldContainer[SuperAdminRow]
    def __init__(self, admins: _Optional[_Iterable[_Union[SuperAdminRow, _Mapping]]] = ...) -> None: ...
