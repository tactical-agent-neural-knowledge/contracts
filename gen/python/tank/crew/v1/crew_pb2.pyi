from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Treads(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TREADS_UNSPECIFIED: _ClassVar[Treads]
    TREADS_ALL: _ClassVar[Treads]
    TREADS_SELECTED: _ClassVar[Treads]

class Activity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTIVITY_UNSPECIFIED: _ClassVar[Activity]
    ACTIVITY_MENTIONED: _ClassVar[Activity]
    ACTIVITY_LOW: _ClassVar[Activity]
    ACTIVITY_NORMAL: _ClassVar[Activity]
    ACTIVITY_HIGH: _ClassVar[Activity]
TREADS_UNSPECIFIED: Treads
TREADS_ALL: Treads
TREADS_SELECTED: Treads
ACTIVITY_UNSPECIFIED: Activity
ACTIVITY_MENTIONED: Activity
ACTIVITY_LOW: Activity
ACTIVITY_NORMAL: Activity
ACTIVITY_HIGH: Activity

class Member(_message.Message):
    __slots__ = ("id", "agent_id", "principal_id", "role", "title", "handle", "skill", "enabled", "treads", "channel_ids", "activity", "daily_cap_usd", "concurrent_cap", "model", "spend_today_usd", "spend_month_usd", "runs_today", "running_now")
    ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    TREADS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    DAILY_CAP_USD_FIELD_NUMBER: _ClassVar[int]
    CONCURRENT_CAP_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SPEND_TODAY_USD_FIELD_NUMBER: _ClassVar[int]
    SPEND_MONTH_USD_FIELD_NUMBER: _ClassVar[int]
    RUNS_TODAY_FIELD_NUMBER: _ClassVar[int]
    RUNNING_NOW_FIELD_NUMBER: _ClassVar[int]
    id: str
    agent_id: str
    principal_id: str
    role: str
    title: str
    handle: str
    skill: str
    enabled: bool
    treads: Treads
    channel_ids: _containers.RepeatedScalarFieldContainer[str]
    activity: Activity
    daily_cap_usd: float
    concurrent_cap: int
    model: str
    spend_today_usd: float
    spend_month_usd: float
    runs_today: int
    running_now: int
    def __init__(self, id: _Optional[str] = ..., agent_id: _Optional[str] = ..., principal_id: _Optional[str] = ..., role: _Optional[str] = ..., title: _Optional[str] = ..., handle: _Optional[str] = ..., skill: _Optional[str] = ..., enabled: bool = ..., treads: _Optional[_Union[Treads, str]] = ..., channel_ids: _Optional[_Iterable[str]] = ..., activity: _Optional[_Union[Activity, str]] = ..., daily_cap_usd: _Optional[float] = ..., concurrent_cap: _Optional[int] = ..., model: _Optional[str] = ..., spend_today_usd: _Optional[float] = ..., spend_month_usd: _Optional[float] = ..., runs_today: _Optional[int] = ..., running_now: _Optional[int] = ...) -> None: ...

class Preset(_message.Message):
    __slots__ = ("role", "title", "handle", "skill", "summary")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    role: str
    title: str
    handle: str
    skill: str
    summary: str
    def __init__(self, role: _Optional[str] = ..., title: _Optional[str] = ..., handle: _Optional[str] = ..., skill: _Optional[str] = ..., summary: _Optional[str] = ...) -> None: ...

class ListCrewRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListCrewResponse(_message.Message):
    __slots__ = ("members", "presets", "can_manage")
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    PRESETS_FIELD_NUMBER: _ClassVar[int]
    CAN_MANAGE_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedCompositeFieldContainer[Member]
    presets: _containers.RepeatedCompositeFieldContainer[Preset]
    can_manage: bool
    def __init__(self, members: _Optional[_Iterable[_Union[Member, _Mapping]]] = ..., presets: _Optional[_Iterable[_Union[Preset, _Mapping]]] = ..., can_manage: bool = ...) -> None: ...

class AddMemberRequest(_message.Message):
    __slots__ = ("workspace_id", "role", "title", "handle", "skill")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    role: str
    title: str
    handle: str
    skill: str
    def __init__(self, workspace_id: _Optional[str] = ..., role: _Optional[str] = ..., title: _Optional[str] = ..., handle: _Optional[str] = ..., skill: _Optional[str] = ...) -> None: ...

class AddMemberResponse(_message.Message):
    __slots__ = ("member",)
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: Member
    def __init__(self, member: _Optional[_Union[Member, _Mapping]] = ...) -> None: ...

class UpdateMemberRequest(_message.Message):
    __slots__ = ("workspace_id", "member")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    member: Member
    def __init__(self, workspace_id: _Optional[str] = ..., member: _Optional[_Union[Member, _Mapping]] = ...) -> None: ...

class UpdateMemberResponse(_message.Message):
    __slots__ = ("member",)
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: Member
    def __init__(self, member: _Optional[_Union[Member, _Mapping]] = ...) -> None: ...

class RemoveMemberRequest(_message.Message):
    __slots__ = ("workspace_id", "member_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    member_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., member_id: _Optional[str] = ...) -> None: ...

class RemoveMemberResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
