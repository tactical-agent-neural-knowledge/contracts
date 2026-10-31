from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Seat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEAT_UNSPECIFIED: _ClassVar[Seat]
    SEAT_COORDINATOR: _ClassVar[Seat]
    SEAT_SPECIALIST: _ClassVar[Seat]
    SEAT_PERSON: _ClassVar[Seat]
SEAT_UNSPECIFIED: Seat
SEAT_COORDINATOR: Seat
SEAT_SPECIALIST: Seat
SEAT_PERSON: Seat

class ToolPolicy(_message.Message):
    __slots__ = ("allow", "deny")
    ALLOW_FIELD_NUMBER: _ClassVar[int]
    DENY_FIELD_NUMBER: _ClassVar[int]
    allow: _containers.RepeatedScalarFieldContainer[str]
    deny: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, allow: _Optional[_Iterable[str]] = ..., deny: _Optional[_Iterable[str]] = ...) -> None: ...

class Envelope(_message.Message):
    __slots__ = ("usd", "turns", "minutes")
    USD_FIELD_NUMBER: _ClassVar[int]
    TURNS_FIELD_NUMBER: _ClassVar[int]
    MINUTES_FIELD_NUMBER: _ClassVar[int]
    usd: float
    turns: int
    minutes: int
    def __init__(self, usd: _Optional[float] = ..., turns: _Optional[int] = ..., minutes: _Optional[int] = ...) -> None: ...

class Member(_message.Message):
    __slots__ = ("id", "agent_id", "principal_id", "seat", "title", "handle", "prompt", "models", "tools", "delegate", "delegate_to", "triggers", "envelope", "enabled", "spend_today_usd", "spend_month_usd", "runs_today", "running_now", "user_id", "record")
    ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    SEAT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    DELEGATE_FIELD_NUMBER: _ClassVar[int]
    DELEGATE_TO_FIELD_NUMBER: _ClassVar[int]
    TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    ENVELOPE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SPEND_TODAY_USD_FIELD_NUMBER: _ClassVar[int]
    SPEND_MONTH_USD_FIELD_NUMBER: _ClassVar[int]
    RUNS_TODAY_FIELD_NUMBER: _ClassVar[int]
    RUNNING_NOW_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    id: str
    agent_id: str
    principal_id: str
    seat: Seat
    title: str
    handle: str
    prompt: str
    models: _containers.RepeatedScalarFieldContainer[str]
    tools: ToolPolicy
    delegate: bool
    delegate_to: _containers.RepeatedScalarFieldContainer[str]
    triggers: _containers.RepeatedScalarFieldContainer[str]
    envelope: Envelope
    enabled: bool
    spend_today_usd: float
    spend_month_usd: float
    runs_today: int
    running_now: int
    user_id: str
    record: MemberRecord
    def __init__(self, id: _Optional[str] = ..., agent_id: _Optional[str] = ..., principal_id: _Optional[str] = ..., seat: _Optional[_Union[Seat, str]] = ..., title: _Optional[str] = ..., handle: _Optional[str] = ..., prompt: _Optional[str] = ..., models: _Optional[_Iterable[str]] = ..., tools: _Optional[_Union[ToolPolicy, _Mapping]] = ..., delegate: bool = ..., delegate_to: _Optional[_Iterable[str]] = ..., triggers: _Optional[_Iterable[str]] = ..., envelope: _Optional[_Union[Envelope, _Mapping]] = ..., enabled: bool = ..., spend_today_usd: _Optional[float] = ..., spend_month_usd: _Optional[float] = ..., runs_today: _Optional[int] = ..., running_now: _Optional[int] = ..., user_id: _Optional[str] = ..., record: _Optional[_Union[MemberRecord, _Mapping]] = ...) -> None: ...

class MemberRecord(_message.Message):
    __slots__ = ("finished", "failed", "accepted", "rejected", "avg_cost_usd", "avg_minutes", "kinds")
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    AVG_COST_USD_FIELD_NUMBER: _ClassVar[int]
    AVG_MINUTES_FIELD_NUMBER: _ClassVar[int]
    KINDS_FIELD_NUMBER: _ClassVar[int]
    finished: int
    failed: int
    accepted: int
    rejected: int
    avg_cost_usd: float
    avg_minutes: float
    kinds: _containers.RepeatedCompositeFieldContainer[KindRecord]
    def __init__(self, finished: _Optional[int] = ..., failed: _Optional[int] = ..., accepted: _Optional[int] = ..., rejected: _Optional[int] = ..., avg_cost_usd: _Optional[float] = ..., avg_minutes: _Optional[float] = ..., kinds: _Optional[_Iterable[_Union[KindRecord, _Mapping]]] = ...) -> None: ...

class KindRecord(_message.Message):
    __slots__ = ("kind", "finished", "failed", "accepted", "rejected")
    KIND_FIELD_NUMBER: _ClassVar[int]
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    kind: str
    finished: int
    failed: int
    accepted: int
    rejected: int
    def __init__(self, kind: _Optional[str] = ..., finished: _Optional[int] = ..., failed: _Optional[int] = ..., accepted: _Optional[int] = ..., rejected: _Optional[int] = ...) -> None: ...

class Team(_message.Message):
    __slots__ = ("id", "workspace_id", "name", "handle", "purpose", "members", "channel_ids", "daily_cap_usd", "concurrent_cap", "envelope", "spend_today_usd", "spend_month_usd", "runs_today", "running_now", "created_at", "updated_at", "created_by", "board_id", "paused", "claims", "slo")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    DAILY_CAP_USD_FIELD_NUMBER: _ClassVar[int]
    CONCURRENT_CAP_FIELD_NUMBER: _ClassVar[int]
    ENVELOPE_FIELD_NUMBER: _ClassVar[int]
    SPEND_TODAY_USD_FIELD_NUMBER: _ClassVar[int]
    SPEND_MONTH_USD_FIELD_NUMBER: _ClassVar[int]
    RUNS_TODAY_FIELD_NUMBER: _ClassVar[int]
    RUNNING_NOW_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    BOARD_ID_FIELD_NUMBER: _ClassVar[int]
    PAUSED_FIELD_NUMBER: _ClassVar[int]
    CLAIMS_FIELD_NUMBER: _ClassVar[int]
    SLO_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    name: str
    handle: str
    purpose: str
    members: _containers.RepeatedCompositeFieldContainer[Member]
    channel_ids: _containers.RepeatedScalarFieldContainer[str]
    daily_cap_usd: float
    concurrent_cap: int
    envelope: Envelope
    spend_today_usd: float
    spend_month_usd: float
    runs_today: int
    running_now: int
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    created_by: str
    board_id: str
    paused: bool
    claims: _containers.RepeatedCompositeFieldContainer[Claim]
    slo: TeamSlo
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., name: _Optional[str] = ..., handle: _Optional[str] = ..., purpose: _Optional[str] = ..., members: _Optional[_Iterable[_Union[Member, _Mapping]]] = ..., channel_ids: _Optional[_Iterable[str]] = ..., daily_cap_usd: _Optional[float] = ..., concurrent_cap: _Optional[int] = ..., envelope: _Optional[_Union[Envelope, _Mapping]] = ..., spend_today_usd: _Optional[float] = ..., spend_month_usd: _Optional[float] = ..., runs_today: _Optional[int] = ..., running_now: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., board_id: _Optional[str] = ..., paused: bool = ..., claims: _Optional[_Iterable[_Union[Claim, _Mapping]]] = ..., slo: _Optional[_Union[TeamSlo, _Mapping]] = ...) -> None: ...

class Claim(_message.Message):
    __slots__ = ("kind", "key", "run_id", "title", "ask", "since")
    KIND_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ASK_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    key: str
    run_id: str
    title: str
    ask: str
    since: _timestamp_pb2.Timestamp
    def __init__(self, kind: _Optional[str] = ..., key: _Optional[str] = ..., run_id: _Optional[str] = ..., title: _Optional[str] = ..., ask: _Optional[str] = ..., since: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TeamSlo(_message.Message):
    __slots__ = ("first_result_minutes_p50", "run_minutes_p95", "finished_30d", "failed_30d", "stalled_now", "accepted_rate_30d", "near_cap")
    FIRST_RESULT_MINUTES_P50_FIELD_NUMBER: _ClassVar[int]
    RUN_MINUTES_P95_FIELD_NUMBER: _ClassVar[int]
    FINISHED_30D_FIELD_NUMBER: _ClassVar[int]
    FAILED_30D_FIELD_NUMBER: _ClassVar[int]
    STALLED_NOW_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_RATE_30D_FIELD_NUMBER: _ClassVar[int]
    NEAR_CAP_FIELD_NUMBER: _ClassVar[int]
    first_result_minutes_p50: float
    run_minutes_p95: float
    finished_30d: int
    failed_30d: int
    stalled_now: int
    accepted_rate_30d: float
    near_cap: bool
    def __init__(self, first_result_minutes_p50: _Optional[float] = ..., run_minutes_p95: _Optional[float] = ..., finished_30d: _Optional[int] = ..., failed_30d: _Optional[int] = ..., stalled_now: _Optional[int] = ..., accepted_rate_30d: _Optional[float] = ..., near_cap: bool = ...) -> None: ...

class SetTeamPauseRequest(_message.Message):
    __slots__ = ("workspace_id", "team_id", "paused")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    PAUSED_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    team_id: str
    paused: bool
    def __init__(self, workspace_id: _Optional[str] = ..., team_id: _Optional[str] = ..., paused: bool = ...) -> None: ...

class SetTeamPauseResponse(_message.Message):
    __slots__ = ("team",)
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: Team
    def __init__(self, team: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...

class StopTeamRequest(_message.Message):
    __slots__ = ("workspace_id", "team_id", "reason")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    team_id: str
    reason: str
    def __init__(self, workspace_id: _Optional[str] = ..., team_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class StopTeamResponse(_message.Message):
    __slots__ = ("team", "stopped")
    TEAM_FIELD_NUMBER: _ClassVar[int]
    STOPPED_FIELD_NUMBER: _ClassVar[int]
    team: Team
    stopped: int
    def __init__(self, team: _Optional[_Union[Team, _Mapping]] = ..., stopped: _Optional[int] = ...) -> None: ...

class Template(_message.Message):
    __slots__ = ("key", "name", "summary", "team")
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    key: str
    name: str
    summary: str
    team: Team
    def __init__(self, key: _Optional[str] = ..., name: _Optional[str] = ..., summary: _Optional[str] = ..., team: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...

class ListTeamsRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class ListTeamsResponse(_message.Message):
    __slots__ = ("teams", "templates", "can_manage")
    TEAMS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    CAN_MANAGE_FIELD_NUMBER: _ClassVar[int]
    teams: _containers.RepeatedCompositeFieldContainer[Team]
    templates: _containers.RepeatedCompositeFieldContainer[Template]
    can_manage: bool
    def __init__(self, teams: _Optional[_Iterable[_Union[Team, _Mapping]]] = ..., templates: _Optional[_Iterable[_Union[Template, _Mapping]]] = ..., can_manage: bool = ...) -> None: ...

class GetTeamRequest(_message.Message):
    __slots__ = ("workspace_id", "team_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    team_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., team_id: _Optional[str] = ...) -> None: ...

class GetTeamResponse(_message.Message):
    __slots__ = ("team",)
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: Team
    def __init__(self, team: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...

class CreateTeamRequest(_message.Message):
    __slots__ = ("workspace_id", "name", "handle", "purpose", "template_key", "members", "channel_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_KEY_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    name: str
    handle: str
    purpose: str
    template_key: str
    members: _containers.RepeatedCompositeFieldContainer[Member]
    channel_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., name: _Optional[str] = ..., handle: _Optional[str] = ..., purpose: _Optional[str] = ..., template_key: _Optional[str] = ..., members: _Optional[_Iterable[_Union[Member, _Mapping]]] = ..., channel_id: _Optional[str] = ...) -> None: ...

class CreateTeamResponse(_message.Message):
    __slots__ = ("team",)
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: Team
    def __init__(self, team: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...

class UpdateTeamRequest(_message.Message):
    __slots__ = ("workspace_id", "team")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    team: Team
    def __init__(self, workspace_id: _Optional[str] = ..., team: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...

class UpdateTeamResponse(_message.Message):
    __slots__ = ("team",)
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: Team
    def __init__(self, team: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...

class DeleteTeamRequest(_message.Message):
    __slots__ = ("workspace_id", "team_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    team_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., team_id: _Optional[str] = ...) -> None: ...

class DeleteTeamResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AttachTeamRequest(_message.Message):
    __slots__ = ("workspace_id", "team_id", "channel_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    team_id: str
    channel_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., team_id: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class AttachTeamResponse(_message.Message):
    __slots__ = ("team",)
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: Team
    def __init__(self, team: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...

class DetachTeamRequest(_message.Message):
    __slots__ = ("workspace_id", "team_id", "channel_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    team_id: str
    channel_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., team_id: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class DetachTeamResponse(_message.Message):
    __slots__ = ("team",)
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: Team
    def __init__(self, team: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...

class ExportTeamRequest(_message.Message):
    __slots__ = ("workspace_id", "team_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    team_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., team_id: _Optional[str] = ...) -> None: ...

class ExportTeamResponse(_message.Message):
    __slots__ = ("yaml",)
    YAML_FIELD_NUMBER: _ClassVar[int]
    yaml: str
    def __init__(self, yaml: _Optional[str] = ...) -> None: ...

class ImportTeamRequest(_message.Message):
    __slots__ = ("workspace_id", "yaml", "channel_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    YAML_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    yaml: str
    channel_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., yaml: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class ImportTeamResponse(_message.Message):
    __slots__ = ("team",)
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: Team
    def __init__(self, team: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...
