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
SEAT_UNSPECIFIED: Seat
SEAT_COORDINATOR: Seat
SEAT_SPECIALIST: Seat

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
    __slots__ = ("id", "agent_id", "principal_id", "seat", "title", "handle", "prompt", "models", "tools", "delegate", "delegate_to", "triggers", "envelope", "enabled", "spend_today_usd", "spend_month_usd", "runs_today", "running_now")
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
    def __init__(self, id: _Optional[str] = ..., agent_id: _Optional[str] = ..., principal_id: _Optional[str] = ..., seat: _Optional[_Union[Seat, str]] = ..., title: _Optional[str] = ..., handle: _Optional[str] = ..., prompt: _Optional[str] = ..., models: _Optional[_Iterable[str]] = ..., tools: _Optional[_Union[ToolPolicy, _Mapping]] = ..., delegate: bool = ..., delegate_to: _Optional[_Iterable[str]] = ..., triggers: _Optional[_Iterable[str]] = ..., envelope: _Optional[_Union[Envelope, _Mapping]] = ..., enabled: bool = ..., spend_today_usd: _Optional[float] = ..., spend_month_usd: _Optional[float] = ..., runs_today: _Optional[int] = ..., running_now: _Optional[int] = ...) -> None: ...

class Team(_message.Message):
    __slots__ = ("id", "workspace_id", "name", "handle", "purpose", "members", "channel_ids", "daily_cap_usd", "concurrent_cap", "envelope", "spend_today_usd", "spend_month_usd", "runs_today", "running_now", "created_at", "updated_at", "created_by")
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
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., name: _Optional[str] = ..., handle: _Optional[str] = ..., purpose: _Optional[str] = ..., members: _Optional[_Iterable[_Union[Member, _Mapping]]] = ..., channel_ids: _Optional[_Iterable[str]] = ..., daily_cap_usd: _Optional[float] = ..., concurrent_cap: _Optional[int] = ..., envelope: _Optional[_Union[Envelope, _Mapping]] = ..., spend_today_usd: _Optional[float] = ..., spend_month_usd: _Optional[float] = ..., runs_today: _Optional[int] = ..., running_now: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ...) -> None: ...

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
