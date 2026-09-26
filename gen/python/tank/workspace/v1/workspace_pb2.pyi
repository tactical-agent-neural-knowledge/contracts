from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tank.auth.v1 import auth_pb2 as _auth_pb2
from tank.channel.v1 import channel_pb2 as _channel_pb2
from tank.topo.v1 import topo_pb2 as _topo_pb2
from tank.richtext.v1 import richtext_pb2 as _richtext_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROLE_UNSPECIFIED: _ClassVar[Role]
    ROLE_OWNER: _ClassVar[Role]
    ROLE_ADMIN: _ClassVar[Role]
    ROLE_MEMBER: _ClassVar[Role]
    ROLE_GUEST: _ClassVar[Role]
    ROLE_BOT: _ClassVar[Role]
ROLE_UNSPECIFIED: Role
ROLE_OWNER: Role
ROLE_ADMIN: Role
ROLE_MEMBER: Role
ROLE_GUEST: Role
ROLE_BOT: Role

class Workspace(_message.Message):
    __slots__ = ("id", "slug", "name", "icon_url", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_URL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    slug: str
    name: str
    icon_url: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., slug: _Optional[str] = ..., name: _Optional[str] = ..., icon_url: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Member(_message.Message):
    __slots__ = ("principal", "role", "title", "timezone", "joined_at", "deactivated_at")
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    JOINED_AT_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATED_AT_FIELD_NUMBER: _ClassVar[int]
    principal: _auth_pb2.Principal
    role: Role
    title: str
    timezone: str
    joined_at: _timestamp_pb2.Timestamp
    deactivated_at: _timestamp_pb2.Timestamp
    def __init__(self, principal: _Optional[_Union[_auth_pb2.Principal, _Mapping]] = ..., role: _Optional[_Union[Role, str]] = ..., title: _Optional[str] = ..., timezone: _Optional[str] = ..., joined_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deactivated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateWorkspaceRequest(_message.Message):
    __slots__ = ("name", "slug")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ...) -> None: ...

class CreateWorkspaceResponse(_message.Message):
    __slots__ = ("workspace",)
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    workspace: Workspace
    def __init__(self, workspace: _Optional[_Union[Workspace, _Mapping]] = ...) -> None: ...

class ListWorkspacesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListWorkspacesResponse(_message.Message):
    __slots__ = ("workspaces",)
    WORKSPACES_FIELD_NUMBER: _ClassVar[int]
    workspaces: _containers.RepeatedCompositeFieldContainer[Workspace]
    def __init__(self, workspaces: _Optional[_Iterable[_Union[Workspace, _Mapping]]] = ...) -> None: ...

class GetBootstrapRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class GetBootstrapResponse(_message.Message):
    __slots__ = ("workspace", "me", "channels", "read_states", "members", "custom_emoji_hash", "unread_notification_count", "preferences", "user_groups", "entitlements")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    ME_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    READ_STATES_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_EMOJI_HASH_FIELD_NUMBER: _ClassVar[int]
    UNREAD_NOTIFICATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    USER_GROUPS_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENTS_FIELD_NUMBER: _ClassVar[int]
    workspace: Workspace
    me: Member
    channels: _containers.RepeatedCompositeFieldContainer[_channel_pb2.Channel]
    read_states: _containers.RepeatedCompositeFieldContainer[_channel_pb2.ChannelReadState]
    members: _containers.RepeatedCompositeFieldContainer[Member]
    custom_emoji_hash: str
    unread_notification_count: int
    preferences: Preferences
    user_groups: _containers.RepeatedCompositeFieldContainer[UserGroup]
    entitlements: Entitlements
    def __init__(self, workspace: _Optional[_Union[Workspace, _Mapping]] = ..., me: _Optional[_Union[Member, _Mapping]] = ..., channels: _Optional[_Iterable[_Union[_channel_pb2.Channel, _Mapping]]] = ..., read_states: _Optional[_Iterable[_Union[_channel_pb2.ChannelReadState, _Mapping]]] = ..., members: _Optional[_Iterable[_Union[Member, _Mapping]]] = ..., custom_emoji_hash: _Optional[str] = ..., unread_notification_count: _Optional[int] = ..., preferences: _Optional[_Union[Preferences, _Mapping]] = ..., user_groups: _Optional[_Iterable[_Union[UserGroup, _Mapping]]] = ..., entitlements: _Optional[_Union[Entitlements, _Mapping]] = ...) -> None: ...

class Entitlements(_message.Message):
    __slots__ = ("plan", "agent_runs", "neural_vault", "agent_runs_used", "agent_runs_limit", "vault_queries_used", "vault_queries_limit", "contact_email")
    PLAN_FIELD_NUMBER: _ClassVar[int]
    AGENT_RUNS_FIELD_NUMBER: _ClassVar[int]
    NEURAL_VAULT_FIELD_NUMBER: _ClassVar[int]
    AGENT_RUNS_USED_FIELD_NUMBER: _ClassVar[int]
    AGENT_RUNS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    VAULT_QUERIES_USED_FIELD_NUMBER: _ClassVar[int]
    VAULT_QUERIES_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CONTACT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    plan: str
    agent_runs: bool
    neural_vault: bool
    agent_runs_used: int
    agent_runs_limit: int
    vault_queries_used: int
    vault_queries_limit: int
    contact_email: str
    def __init__(self, plan: _Optional[str] = ..., agent_runs: bool = ..., neural_vault: bool = ..., agent_runs_used: _Optional[int] = ..., agent_runs_limit: _Optional[int] = ..., vault_queries_used: _Optional[int] = ..., vault_queries_limit: _Optional[int] = ..., contact_email: _Optional[str] = ...) -> None: ...

class ListMembersRequest(_message.Message):
    __slots__ = ("workspace_id", "cursor", "limit", "query")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    cursor: str
    limit: int
    query: str
    def __init__(self, workspace_id: _Optional[str] = ..., cursor: _Optional[str] = ..., limit: _Optional[int] = ..., query: _Optional[str] = ...) -> None: ...

class ListMembersResponse(_message.Message):
    __slots__ = ("members", "next_cursor")
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedCompositeFieldContainer[Member]
    next_cursor: str
    def __init__(self, members: _Optional[_Iterable[_Union[Member, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class InviteMemberRequest(_message.Message):
    __slots__ = ("workspace_id", "email", "role")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    email: str
    role: Role
    def __init__(self, workspace_id: _Optional[str] = ..., email: _Optional[str] = ..., role: _Optional[_Union[Role, str]] = ...) -> None: ...

class InviteMemberResponse(_message.Message):
    __slots__ = ("invite_id",)
    INVITE_ID_FIELD_NUMBER: _ClassVar[int]
    invite_id: str
    def __init__(self, invite_id: _Optional[str] = ...) -> None: ...

class Invite(_message.Message):
    __slots__ = ("invite_id", "email", "role", "expires_at")
    INVITE_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    invite_id: str
    email: str
    role: Role
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, invite_id: _Optional[str] = ..., email: _Optional[str] = ..., role: _Optional[_Union[Role, str]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListInvitesRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListInvitesResponse(_message.Message):
    __slots__ = ("invites",)
    INVITES_FIELD_NUMBER: _ClassVar[int]
    invites: _containers.RepeatedCompositeFieldContainer[Invite]
    def __init__(self, invites: _Optional[_Iterable[_Union[Invite, _Mapping]]] = ...) -> None: ...

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

class PendingInvite(_message.Message):
    __slots__ = ("workspace_id", "workspace_name", "workspace_slug", "role", "expires_at")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_SLUG_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    workspace_name: str
    workspace_slug: str
    role: Role
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, workspace_id: _Optional[str] = ..., workspace_name: _Optional[str] = ..., workspace_slug: _Optional[str] = ..., role: _Optional[_Union[Role, str]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListMyInvitesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListMyInvitesResponse(_message.Message):
    __slots__ = ("invites",)
    INVITES_FIELD_NUMBER: _ClassVar[int]
    invites: _containers.RepeatedCompositeFieldContainer[PendingInvite]
    def __init__(self, invites: _Optional[_Iterable[_Union[PendingInvite, _Mapping]]] = ...) -> None: ...

class AcceptInviteRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class AcceptInviteResponse(_message.Message):
    __slots__ = ("workspace", "me")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    ME_FIELD_NUMBER: _ClassVar[int]
    workspace: Workspace
    me: Member
    def __init__(self, workspace: _Optional[_Union[Workspace, _Mapping]] = ..., me: _Optional[_Union[Member, _Mapping]] = ...) -> None: ...

class JoinWorkspaceRequest(_message.Message):
    __slots__ = ("invite_token",)
    INVITE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    invite_token: str
    def __init__(self, invite_token: _Optional[str] = ...) -> None: ...

class JoinWorkspaceResponse(_message.Message):
    __slots__ = ("workspace", "me")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    ME_FIELD_NUMBER: _ClassVar[int]
    workspace: Workspace
    me: Member
    def __init__(self, workspace: _Optional[_Union[Workspace, _Mapping]] = ..., me: _Optional[_Union[Member, _Mapping]] = ...) -> None: ...

class UpdateProfileRequest(_message.Message):
    __slots__ = ("workspace_id", "display_name", "title", "timezone", "avatar_file_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    display_name: str
    title: str
    timezone: str
    avatar_file_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., display_name: _Optional[str] = ..., title: _Optional[str] = ..., timezone: _Optional[str] = ..., avatar_file_id: _Optional[str] = ...) -> None: ...

class UpdateProfileResponse(_message.Message):
    __slots__ = ("me",)
    ME_FIELD_NUMBER: _ClassVar[int]
    me: Member
    def __init__(self, me: _Optional[_Union[Member, _Mapping]] = ...) -> None: ...

class ArmorModeSchedule(_message.Message):
    __slots__ = ("enabled", "start", "end", "days", "timezone", "allow_critical")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CRITICAL_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    start: str
    end: str
    days: _containers.RepeatedScalarFieldContainer[int]
    timezone: str
    allow_critical: bool
    def __init__(self, enabled: bool = ..., start: _Optional[str] = ..., end: _Optional[str] = ..., days: _Optional[_Iterable[int]] = ..., timezone: _Optional[str] = ..., allow_critical: bool = ...) -> None: ...

class Preferences(_message.Message):
    __slots__ = ("notify_default", "dm_notify_default", "theme", "armor_mode_schedule", "email_digest", "desktop_sound", "push_on_mention_only", "topo")
    NOTIFY_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    DM_NOTIFY_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    THEME_FIELD_NUMBER: _ClassVar[int]
    ARMOR_MODE_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_DIGEST_FIELD_NUMBER: _ClassVar[int]
    DESKTOP_SOUND_FIELD_NUMBER: _ClassVar[int]
    PUSH_ON_MENTION_ONLY_FIELD_NUMBER: _ClassVar[int]
    TOPO_FIELD_NUMBER: _ClassVar[int]
    notify_default: _channel_pb2.NotifyPref
    dm_notify_default: _channel_pb2.NotifyPref
    theme: str
    armor_mode_schedule: ArmorModeSchedule
    email_digest: bool
    desktop_sound: bool
    push_on_mention_only: bool
    topo: TopoPreferences
    def __init__(self, notify_default: _Optional[_Union[_channel_pb2.NotifyPref, str]] = ..., dm_notify_default: _Optional[_Union[_channel_pb2.NotifyPref, str]] = ..., theme: _Optional[str] = ..., armor_mode_schedule: _Optional[_Union[ArmorModeSchedule, _Mapping]] = ..., email_digest: bool = ..., desktop_sound: bool = ..., push_on_mention_only: bool = ..., topo: _Optional[_Union[TopoPreferences, _Mapping]] = ...) -> None: ...

class TopoPreferences(_message.Message):
    __slots__ = ("configured", "visible", "time_axis")
    CONFIGURED_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    TIME_AXIS_FIELD_NUMBER: _ClassVar[int]
    configured: bool
    visible: _containers.RepeatedScalarFieldContainer[_topo_pb2.MarkType]
    time_axis: bool
    def __init__(self, configured: bool = ..., visible: _Optional[_Iterable[_Union[_topo_pb2.MarkType, str]]] = ..., time_axis: bool = ...) -> None: ...

class GetPreferencesRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class GetPreferencesResponse(_message.Message):
    __slots__ = ("preferences",)
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    preferences: Preferences
    def __init__(self, preferences: _Optional[_Union[Preferences, _Mapping]] = ...) -> None: ...

class UpdatePreferencesRequest(_message.Message):
    __slots__ = ("workspace_id", "preferences")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    preferences: Preferences
    def __init__(self, workspace_id: _Optional[str] = ..., preferences: _Optional[_Union[Preferences, _Mapping]] = ...) -> None: ...

class UpdatePreferencesResponse(_message.Message):
    __slots__ = ("preferences",)
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    preferences: Preferences
    def __init__(self, preferences: _Optional[_Union[Preferences, _Mapping]] = ...) -> None: ...

class CustomEmoji(_message.Message):
    __slots__ = ("id", "workspace_id", "name", "file_id", "created_by", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    name: str
    file_id: str
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., name: _Optional[str] = ..., file_id: _Optional[str] = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListEmojiRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListEmojiResponse(_message.Message):
    __slots__ = ("emoji", "hash")
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    emoji: _containers.RepeatedCompositeFieldContainer[CustomEmoji]
    hash: str
    def __init__(self, emoji: _Optional[_Iterable[_Union[CustomEmoji, _Mapping]]] = ..., hash: _Optional[str] = ...) -> None: ...

class CreateEmojiRequest(_message.Message):
    __slots__ = ("workspace_id", "name", "file_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    name: str
    file_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., name: _Optional[str] = ..., file_id: _Optional[str] = ...) -> None: ...

class CreateEmojiResponse(_message.Message):
    __slots__ = ("emoji",)
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    emoji: CustomEmoji
    def __init__(self, emoji: _Optional[_Union[CustomEmoji, _Mapping]] = ...) -> None: ...

class DeleteEmojiRequest(_message.Message):
    __slots__ = ("emoji_id",)
    EMOJI_ID_FIELD_NUMBER: _ClassVar[int]
    emoji_id: str
    def __init__(self, emoji_id: _Optional[str] = ...) -> None: ...

class DeleteEmojiResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UserGroup(_message.Message):
    __slots__ = ("id", "workspace_id", "handle", "name", "description", "member_ids", "created_by", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    handle: str
    name: str
    description: str
    member_ids: _containers.RepeatedScalarFieldContainer[str]
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., handle: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., member_ids: _Optional[_Iterable[str]] = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListUserGroupsRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListUserGroupsResponse(_message.Message):
    __slots__ = ("groups",)
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[UserGroup]
    def __init__(self, groups: _Optional[_Iterable[_Union[UserGroup, _Mapping]]] = ...) -> None: ...

class CreateUserGroupRequest(_message.Message):
    __slots__ = ("workspace_id", "handle", "name", "description", "member_ids")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    handle: str
    name: str
    description: str
    member_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, workspace_id: _Optional[str] = ..., handle: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., member_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateUserGroupResponse(_message.Message):
    __slots__ = ("group",)
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: UserGroup
    def __init__(self, group: _Optional[_Union[UserGroup, _Mapping]] = ...) -> None: ...

class UpdateUserGroupMembersRequest(_message.Message):
    __slots__ = ("group_id", "member_ids")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    member_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, group_id: _Optional[str] = ..., member_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateUserGroupMembersResponse(_message.Message):
    __slots__ = ("group",)
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: UserGroup
    def __init__(self, group: _Optional[_Union[UserGroup, _Mapping]] = ...) -> None: ...

class DeleteUserGroupRequest(_message.Message):
    __slots__ = ("group_id",)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    def __init__(self, group_id: _Optional[str] = ...) -> None: ...

class DeleteUserGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChannelBookmark(_message.Message):
    __slots__ = ("id", "channel_id", "title", "url", "emoji", "created_by", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    channel_id: str
    title: str
    url: str
    emoji: str
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., channel_id: _Optional[str] = ..., title: _Optional[str] = ..., url: _Optional[str] = ..., emoji: _Optional[str] = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListBookmarksRequest(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class ListBookmarksResponse(_message.Message):
    __slots__ = ("bookmarks",)
    BOOKMARKS_FIELD_NUMBER: _ClassVar[int]
    bookmarks: _containers.RepeatedCompositeFieldContainer[ChannelBookmark]
    def __init__(self, bookmarks: _Optional[_Iterable[_Union[ChannelBookmark, _Mapping]]] = ...) -> None: ...

class AddBookmarkRequest(_message.Message):
    __slots__ = ("channel_id", "title", "url", "emoji")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    title: str
    url: str
    emoji: str
    def __init__(self, channel_id: _Optional[str] = ..., title: _Optional[str] = ..., url: _Optional[str] = ..., emoji: _Optional[str] = ...) -> None: ...

class AddBookmarkResponse(_message.Message):
    __slots__ = ("bookmark",)
    BOOKMARK_FIELD_NUMBER: _ClassVar[int]
    bookmark: ChannelBookmark
    def __init__(self, bookmark: _Optional[_Union[ChannelBookmark, _Mapping]] = ...) -> None: ...

class RemoveBookmarkRequest(_message.Message):
    __slots__ = ("bookmark_id",)
    BOOKMARK_ID_FIELD_NUMBER: _ClassVar[int]
    bookmark_id: str
    def __init__(self, bookmark_id: _Optional[str] = ...) -> None: ...

class RemoveBookmarkResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Draft(_message.Message):
    __slots__ = ("channel_id", "thread_root_id", "rich_text", "text", "file_ids", "updated_at")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    thread_root_id: str
    rich_text: _richtext_pb2.RichText
    text: str
    file_ids: _containers.RepeatedScalarFieldContainer[str]
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., rich_text: _Optional[_Union[_richtext_pb2.RichText, _Mapping]] = ..., text: _Optional[str] = ..., file_ids: _Optional[_Iterable[str]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetDraftRequest(_message.Message):
    __slots__ = ("channel_id", "thread_root_id")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    thread_root_id: str
    def __init__(self, channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ...) -> None: ...

class GetDraftResponse(_message.Message):
    __slots__ = ("draft",)
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    draft: Draft
    def __init__(self, draft: _Optional[_Union[Draft, _Mapping]] = ...) -> None: ...

class PutDraftRequest(_message.Message):
    __slots__ = ("draft",)
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    draft: Draft
    def __init__(self, draft: _Optional[_Union[Draft, _Mapping]] = ...) -> None: ...

class PutDraftResponse(_message.Message):
    __slots__ = ("draft",)
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    draft: Draft
    def __init__(self, draft: _Optional[_Union[Draft, _Mapping]] = ...) -> None: ...

class DeleteDraftRequest(_message.Message):
    __slots__ = ("channel_id", "thread_root_id")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    thread_root_id: str
    def __init__(self, channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ...) -> None: ...

class DeleteDraftResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListDraftsRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListDraftsResponse(_message.Message):
    __slots__ = ("drafts",)
    DRAFTS_FIELD_NUMBER: _ClassVar[int]
    drafts: _containers.RepeatedCompositeFieldContainer[Draft]
    def __init__(self, drafts: _Optional[_Iterable[_Union[Draft, _Mapping]]] = ...) -> None: ...

class ScheduledMessage(_message.Message):
    __slots__ = ("id", "workspace_id", "channel_id", "thread_root_id", "text", "rich_text", "file_ids", "send_at", "created_at", "sent_at", "sent_message_id", "error")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
    FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    SEND_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    SENT_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    channel_id: str
    thread_root_id: str
    text: str
    rich_text: _richtext_pb2.RichText
    file_ids: _containers.RepeatedScalarFieldContainer[str]
    send_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    sent_at: _timestamp_pb2.Timestamp
    sent_message_id: str
    error: str
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., text: _Optional[str] = ..., rich_text: _Optional[_Union[_richtext_pb2.RichText, _Mapping]] = ..., file_ids: _Optional[_Iterable[str]] = ..., send_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sent_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sent_message_id: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class ScheduleMessageRequest(_message.Message):
    __slots__ = ("channel_id", "thread_root_id", "text", "rich_text", "file_ids", "send_at")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
    FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    SEND_AT_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    thread_root_id: str
    text: str
    rich_text: _richtext_pb2.RichText
    file_ids: _containers.RepeatedScalarFieldContainer[str]
    send_at: _timestamp_pb2.Timestamp
    def __init__(self, channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., text: _Optional[str] = ..., rich_text: _Optional[_Union[_richtext_pb2.RichText, _Mapping]] = ..., file_ids: _Optional[_Iterable[str]] = ..., send_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ScheduleMessageResponse(_message.Message):
    __slots__ = ("scheduled",)
    SCHEDULED_FIELD_NUMBER: _ClassVar[int]
    scheduled: ScheduledMessage
    def __init__(self, scheduled: _Optional[_Union[ScheduledMessage, _Mapping]] = ...) -> None: ...

class ListScheduledRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListScheduledResponse(_message.Message):
    __slots__ = ("scheduled",)
    SCHEDULED_FIELD_NUMBER: _ClassVar[int]
    scheduled: _containers.RepeatedCompositeFieldContainer[ScheduledMessage]
    def __init__(self, scheduled: _Optional[_Iterable[_Union[ScheduledMessage, _Mapping]]] = ...) -> None: ...

class CancelScheduledRequest(_message.Message):
    __slots__ = ("scheduled_id",)
    SCHEDULED_ID_FIELD_NUMBER: _ClassVar[int]
    scheduled_id: str
    def __init__(self, scheduled_id: _Optional[str] = ...) -> None: ...

class CancelScheduledResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
