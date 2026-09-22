from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tank.channel.v1 import channel_pb2 as _channel_pb2
from tank.workspace.v1 import workspace_pb2 as _workspace_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Permission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PERMISSION_UNSPECIFIED: _ClassVar[Permission]
    PERMISSION_EVERYONE: _ClassVar[Permission]
    PERMISSION_MEMBERS: _ClassVar[Permission]
    PERMISSION_ADMINS: _ClassVar[Permission]
    PERMISSION_OWNERS: _ClassVar[Permission]

class ExportState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXPORT_STATE_UNSPECIFIED: _ClassVar[ExportState]
    EXPORT_STATE_PENDING: _ClassVar[ExportState]
    EXPORT_STATE_RUNNING: _ClassVar[ExportState]
    EXPORT_STATE_READY: _ClassVar[ExportState]
    EXPORT_STATE_FAILED: _ClassVar[ExportState]
    EXPORT_STATE_EXPIRED: _ClassVar[ExportState]
PERMISSION_UNSPECIFIED: Permission
PERMISSION_EVERYONE: Permission
PERMISSION_MEMBERS: Permission
PERMISSION_ADMINS: Permission
PERMISSION_OWNERS: Permission
EXPORT_STATE_UNSPECIFIED: ExportState
EXPORT_STATE_PENDING: ExportState
EXPORT_STATE_RUNNING: ExportState
EXPORT_STATE_READY: ExportState
EXPORT_STATE_FAILED: ExportState
EXPORT_STATE_EXPIRED: ExportState

class ListMembersRequest(_message.Message):
    __slots__ = ("workspace_id", "cursor", "limit", "role", "deactivated", "search")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATED_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    cursor: str
    limit: int
    role: _workspace_pb2.Role
    deactivated: bool
    search: str
    def __init__(self, workspace_id: _Optional[str] = ..., cursor: _Optional[str] = ..., limit: _Optional[int] = ..., role: _Optional[_Union[_workspace_pb2.Role, str]] = ..., deactivated: bool = ..., search: _Optional[str] = ...) -> None: ...

class ListMembersResponse(_message.Message):
    __slots__ = ("members", "next_cursor", "total")
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedCompositeFieldContainer[_workspace_pb2.Member]
    next_cursor: str
    total: int
    def __init__(self, members: _Optional[_Iterable[_Union[_workspace_pb2.Member, _Mapping]]] = ..., next_cursor: _Optional[str] = ..., total: _Optional[int] = ...) -> None: ...

class SetMemberRoleRequest(_message.Message):
    __slots__ = ("workspace_id", "user_id", "role")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    user_id: str
    role: _workspace_pb2.Role
    def __init__(self, workspace_id: _Optional[str] = ..., user_id: _Optional[str] = ..., role: _Optional[_Union[_workspace_pb2.Role, str]] = ...) -> None: ...

class SetMemberRoleResponse(_message.Message):
    __slots__ = ("member",)
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: _workspace_pb2.Member
    def __init__(self, member: _Optional[_Union[_workspace_pb2.Member, _Mapping]] = ...) -> None: ...

class DeactivateMemberRequest(_message.Message):
    __slots__ = ("workspace_id", "user_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    user_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class DeactivateMemberResponse(_message.Message):
    __slots__ = ("member",)
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: _workspace_pb2.Member
    def __init__(self, member: _Optional[_Union[_workspace_pb2.Member, _Mapping]] = ...) -> None: ...

class ReactivateMemberRequest(_message.Message):
    __slots__ = ("workspace_id", "user_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    user_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class ReactivateMemberResponse(_message.Message):
    __slots__ = ("member",)
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: _workspace_pb2.Member
    def __init__(self, member: _Optional[_Union[_workspace_pb2.Member, _Mapping]] = ...) -> None: ...

class RemoveMemberRequest(_message.Message):
    __slots__ = ("workspace_id", "user_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    user_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class RemoveMemberResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Invite(_message.Message):
    __slots__ = ("id", "workspace_id", "email", "role", "invited_by", "created_at", "expires_at", "consumed_at", "revoked_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    INVITED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    CONSUMED_AT_FIELD_NUMBER: _ClassVar[int]
    REVOKED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    email: str
    role: _workspace_pb2.Role
    invited_by: str
    created_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    consumed_at: _timestamp_pb2.Timestamp
    revoked_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., email: _Optional[str] = ..., role: _Optional[_Union[_workspace_pb2.Role, str]] = ..., invited_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., consumed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., revoked_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListInvitesRequest(_message.Message):
    __slots__ = ("workspace_id", "cursor", "limit", "include_inactive")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    cursor: str
    limit: int
    include_inactive: bool
    def __init__(self, workspace_id: _Optional[str] = ..., cursor: _Optional[str] = ..., limit: _Optional[int] = ..., include_inactive: bool = ...) -> None: ...

class ListInvitesResponse(_message.Message):
    __slots__ = ("invites", "next_cursor")
    INVITES_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    invites: _containers.RepeatedCompositeFieldContainer[Invite]
    next_cursor: str
    def __init__(self, invites: _Optional[_Iterable[_Union[Invite, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class RevokeInviteRequest(_message.Message):
    __slots__ = ("workspace_id", "invite_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    INVITE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    invite_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., invite_id: _Optional[str] = ...) -> None: ...

class RevokeInviteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChannelCounts(_message.Message):
    __slots__ = ("public", "private", "archived", "dm")
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    DM_FIELD_NUMBER: _ClassVar[int]
    public: int
    private: int
    archived: int
    dm: int
    def __init__(self, public: _Optional[int] = ..., private: _Optional[int] = ..., archived: _Optional[int] = ..., dm: _Optional[int] = ...) -> None: ...

class ListChannelsAdminRequest(_message.Message):
    __slots__ = ("workspace_id", "cursor", "limit", "type", "include_archived", "search")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    cursor: str
    limit: int
    type: _channel_pb2.ChannelType
    include_archived: bool
    search: str
    def __init__(self, workspace_id: _Optional[str] = ..., cursor: _Optional[str] = ..., limit: _Optional[int] = ..., type: _Optional[_Union[_channel_pb2.ChannelType, str]] = ..., include_archived: bool = ..., search: _Optional[str] = ...) -> None: ...

class ListChannelsAdminResponse(_message.Message):
    __slots__ = ("channels", "next_cursor", "counts")
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    COUNTS_FIELD_NUMBER: _ClassVar[int]
    channels: _containers.RepeatedCompositeFieldContainer[_channel_pb2.Channel]
    next_cursor: str
    counts: ChannelCounts
    def __init__(self, channels: _Optional[_Iterable[_Union[_channel_pb2.Channel, _Mapping]]] = ..., next_cursor: _Optional[str] = ..., counts: _Optional[_Union[ChannelCounts, _Mapping]] = ...) -> None: ...

class AdminArchiveChannelRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id", "archived")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    archived: bool
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., archived: bool = ...) -> None: ...

class AdminArchiveChannelResponse(_message.Message):
    __slots__ = ("channel",)
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: _channel_pb2.Channel
    def __init__(self, channel: _Optional[_Union[_channel_pb2.Channel, _Mapping]] = ...) -> None: ...

class AdminSetChannelMembersRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id", "add_user_ids", "remove_user_ids")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ADD_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    add_user_ids: _containers.RepeatedScalarFieldContainer[str]
    remove_user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., add_user_ids: _Optional[_Iterable[str]] = ..., remove_user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class AdminSetChannelMembersResponse(_message.Message):
    __slots__ = ("channel", "added", "removed")
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    ADDED_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    channel: _channel_pb2.Channel
    added: int
    removed: int
    def __init__(self, channel: _Optional[_Union[_channel_pb2.Channel, _Mapping]] = ..., added: _Optional[int] = ..., removed: _Optional[int] = ...) -> None: ...

class RetentionPolicy(_message.Message):
    __slots__ = ("public_days", "private_days", "dm_days", "mpdm_days")
    PUBLIC_DAYS_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_DAYS_FIELD_NUMBER: _ClassVar[int]
    DM_DAYS_FIELD_NUMBER: _ClassVar[int]
    MPDM_DAYS_FIELD_NUMBER: _ClassVar[int]
    public_days: int
    private_days: int
    dm_days: int
    mpdm_days: int
    def __init__(self, public_days: _Optional[int] = ..., private_days: _Optional[int] = ..., dm_days: _Optional[int] = ..., mpdm_days: _Optional[int] = ...) -> None: ...

class WorkspaceSettings(_message.Message):
    __slots__ = ("workspace_id", "name", "icon_file_id", "default_channel_ids", "who_can_create_channels", "who_can_invite", "retention", "allow_guests", "require_sso", "legal_hold", "updated_at")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    WHO_CAN_CREATE_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    WHO_CAN_INVITE_FIELD_NUMBER: _ClassVar[int]
    RETENTION_FIELD_NUMBER: _ClassVar[int]
    ALLOW_GUESTS_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_SSO_FIELD_NUMBER: _ClassVar[int]
    LEGAL_HOLD_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    name: str
    icon_file_id: str
    default_channel_ids: _containers.RepeatedScalarFieldContainer[str]
    who_can_create_channels: Permission
    who_can_invite: Permission
    retention: RetentionPolicy
    allow_guests: bool
    require_sso: bool
    legal_hold: bool
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, workspace_id: _Optional[str] = ..., name: _Optional[str] = ..., icon_file_id: _Optional[str] = ..., default_channel_ids: _Optional[_Iterable[str]] = ..., who_can_create_channels: _Optional[_Union[Permission, str]] = ..., who_can_invite: _Optional[_Union[Permission, str]] = ..., retention: _Optional[_Union[RetentionPolicy, _Mapping]] = ..., allow_guests: bool = ..., require_sso: bool = ..., legal_hold: bool = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetWorkspaceSettingsRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class GetWorkspaceSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: WorkspaceSettings
    def __init__(self, settings: _Optional[_Union[WorkspaceSettings, _Mapping]] = ...) -> None: ...

class UpdateWorkspaceSettingsRequest(_message.Message):
    __slots__ = ("workspace_id", "settings", "update_mask")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    settings: WorkspaceSettings
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, workspace_id: _Optional[str] = ..., settings: _Optional[_Union[WorkspaceSettings, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateWorkspaceSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: WorkspaceSettings
    def __init__(self, settings: _Optional[_Union[WorkspaceSettings, _Mapping]] = ...) -> None: ...

class AuditEntry(_message.Message):
    __slots__ = ("id", "workspace_id", "actor_id", "actor_kind", "action", "target_type", "target_id", "metadata_json", "ip", "user_agent", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_KIND_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_JSON_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    actor_id: str
    actor_kind: str
    action: str
    target_type: str
    target_id: str
    metadata_json: str
    ip: str
    user_agent: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., actor_id: _Optional[str] = ..., actor_kind: _Optional[str] = ..., action: _Optional[str] = ..., target_type: _Optional[str] = ..., target_id: _Optional[str] = ..., metadata_json: _Optional[str] = ..., ip: _Optional[str] = ..., user_agent: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListAuditLogRequest(_message.Message):
    __slots__ = ("workspace_id", "cursor", "limit", "actor_id", "action", "since", "until")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    cursor: str
    limit: int
    actor_id: str
    action: str
    since: _timestamp_pb2.Timestamp
    until: _timestamp_pb2.Timestamp
    def __init__(self, workspace_id: _Optional[str] = ..., cursor: _Optional[str] = ..., limit: _Optional[int] = ..., actor_id: _Optional[str] = ..., action: _Optional[str] = ..., since: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListAuditLogResponse(_message.Message):
    __slots__ = ("entries", "next_cursor")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[AuditEntry]
    next_cursor: str
    def __init__(self, entries: _Optional[_Iterable[_Union[AuditEntry, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class ExportJob(_message.Message):
    __slots__ = ("id", "workspace_id", "requested_by", "include_files", "since", "until", "state", "size_bytes", "error", "created_at", "completed_at", "expires_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FILES_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    requested_by: str
    include_files: bool
    since: _timestamp_pb2.Timestamp
    until: _timestamp_pb2.Timestamp
    state: ExportState
    size_bytes: int
    error: str
    created_at: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., requested_by: _Optional[str] = ..., include_files: bool = ..., since: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[ExportState, str]] = ..., size_bytes: _Optional[int] = ..., error: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RequestExportRequest(_message.Message):
    __slots__ = ("workspace_id", "include_files", "since", "until")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FILES_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    include_files: bool
    since: _timestamp_pb2.Timestamp
    until: _timestamp_pb2.Timestamp
    def __init__(self, workspace_id: _Optional[str] = ..., include_files: bool = ..., since: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RequestExportResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: ExportJob
    def __init__(self, job: _Optional[_Union[ExportJob, _Mapping]] = ...) -> None: ...

class ListExportsRequest(_message.Message):
    __slots__ = ("workspace_id", "cursor", "limit")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    cursor: str
    limit: int
    def __init__(self, workspace_id: _Optional[str] = ..., cursor: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListExportsResponse(_message.Message):
    __slots__ = ("jobs", "next_cursor")
    JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[ExportJob]
    next_cursor: str
    def __init__(self, jobs: _Optional[_Iterable[_Union[ExportJob, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class GetExportDownloadUrlRequest(_message.Message):
    __slots__ = ("workspace_id", "export_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPORT_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    export_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., export_id: _Optional[str] = ...) -> None: ...

class GetExportDownloadUrlResponse(_message.Message):
    __slots__ = ("url", "expires_at")
    URL_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    url: str
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, url: _Optional[str] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetUsageRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class GetUsageResponse(_message.Message):
    __slots__ = ("members", "guests", "deactivated", "bots", "channels", "messages_30d", "files_count", "files_bytes", "agent_runs_30d", "cost_usd_30d", "computed_at")
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    GUESTS_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATED_FIELD_NUMBER: _ClassVar[int]
    BOTS_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_30D_FIELD_NUMBER: _ClassVar[int]
    FILES_COUNT_FIELD_NUMBER: _ClassVar[int]
    FILES_BYTES_FIELD_NUMBER: _ClassVar[int]
    AGENT_RUNS_30D_FIELD_NUMBER: _ClassVar[int]
    COST_USD_30D_FIELD_NUMBER: _ClassVar[int]
    COMPUTED_AT_FIELD_NUMBER: _ClassVar[int]
    members: int
    guests: int
    deactivated: int
    bots: int
    channels: int
    messages_30d: int
    files_count: int
    files_bytes: int
    agent_runs_30d: int
    cost_usd_30d: float
    computed_at: _timestamp_pb2.Timestamp
    def __init__(self, members: _Optional[int] = ..., guests: _Optional[int] = ..., deactivated: _Optional[int] = ..., bots: _Optional[int] = ..., channels: _Optional[int] = ..., messages_30d: _Optional[int] = ..., files_count: _Optional[int] = ..., files_bytes: _Optional[int] = ..., agent_runs_30d: _Optional[int] = ..., cost_usd_30d: _Optional[float] = ..., computed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ScimToken(_message.Message):
    __slots__ = ("id", "workspace_id", "name", "created_by", "created_at", "expires_at", "revoked_at", "last_used_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    REVOKED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    name: str
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    revoked_at: _timestamp_pb2.Timestamp
    last_used_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., name: _Optional[str] = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., revoked_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_used_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateScimTokenRequest(_message.Message):
    __slots__ = ("workspace_id", "name", "ttl_days")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TTL_DAYS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    name: str
    ttl_days: int
    def __init__(self, workspace_id: _Optional[str] = ..., name: _Optional[str] = ..., ttl_days: _Optional[int] = ...) -> None: ...

class CreateScimTokenResponse(_message.Message):
    __slots__ = ("token", "secret", "base_url")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    BASE_URL_FIELD_NUMBER: _ClassVar[int]
    token: ScimToken
    secret: str
    base_url: str
    def __init__(self, token: _Optional[_Union[ScimToken, _Mapping]] = ..., secret: _Optional[str] = ..., base_url: _Optional[str] = ...) -> None: ...

class ListScimTokensRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListScimTokensResponse(_message.Message):
    __slots__ = ("tokens",)
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedCompositeFieldContainer[ScimToken]
    def __init__(self, tokens: _Optional[_Iterable[_Union[ScimToken, _Mapping]]] = ...) -> None: ...

class RevokeScimTokenRequest(_message.Message):
    __slots__ = ("workspace_id", "token_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    token_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., token_id: _Optional[str] = ...) -> None: ...

class RevokeScimTokenResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IncomingWebhook(_message.Message):
    __slots__ = ("id", "workspace_id", "channel_id", "thread_root_id", "name", "created_by", "created_at", "last_post_at", "url")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_POST_AT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    channel_id: str
    thread_root_id: str
    name: str
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    last_post_at: _timestamp_pb2.Timestamp
    url: str
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., name: _Optional[str] = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_post_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., url: _Optional[str] = ...) -> None: ...

class CreateIncomingWebhookRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id", "thread_root_id", "name")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    thread_root_id: str
    name: str
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CreateIncomingWebhookResponse(_message.Message):
    __slots__ = ("webhook",)
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    webhook: IncomingWebhook
    def __init__(self, webhook: _Optional[_Union[IncomingWebhook, _Mapping]] = ...) -> None: ...

class ListIncomingWebhooksRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListIncomingWebhooksResponse(_message.Message):
    __slots__ = ("webhooks",)
    WEBHOOKS_FIELD_NUMBER: _ClassVar[int]
    webhooks: _containers.RepeatedCompositeFieldContainer[IncomingWebhook]
    def __init__(self, webhooks: _Optional[_Iterable[_Union[IncomingWebhook, _Mapping]]] = ...) -> None: ...

class RevokeIncomingWebhookRequest(_message.Message):
    __slots__ = ("workspace_id", "id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class RevokeIncomingWebhookResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
