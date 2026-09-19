from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tank.auth.v1 import auth_pb2 as _auth_pb2
from tank.channel.v1 import channel_pb2 as _channel_pb2
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
    __slots__ = ("workspace", "me", "channels", "read_states", "members", "custom_emoji_hash", "unread_notification_count")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    ME_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    READ_STATES_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_EMOJI_HASH_FIELD_NUMBER: _ClassVar[int]
    UNREAD_NOTIFICATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    workspace: Workspace
    me: Member
    channels: _containers.RepeatedCompositeFieldContainer[_channel_pb2.Channel]
    read_states: _containers.RepeatedCompositeFieldContainer[_channel_pb2.ChannelReadState]
    members: _containers.RepeatedCompositeFieldContainer[Member]
    custom_emoji_hash: str
    unread_notification_count: int
    def __init__(self, workspace: _Optional[_Union[Workspace, _Mapping]] = ..., me: _Optional[_Union[Member, _Mapping]] = ..., channels: _Optional[_Iterable[_Union[_channel_pb2.Channel, _Mapping]]] = ..., read_states: _Optional[_Iterable[_Union[_channel_pb2.ChannelReadState, _Mapping]]] = ..., members: _Optional[_Iterable[_Union[Member, _Mapping]]] = ..., custom_emoji_hash: _Optional[str] = ..., unread_notification_count: _Optional[int] = ...) -> None: ...

class ListMembersRequest(_message.Message):
    __slots__ = ("workspace_id", "cursor", "limit")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    cursor: str
    limit: int
    def __init__(self, workspace_id: _Optional[str] = ..., cursor: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

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
