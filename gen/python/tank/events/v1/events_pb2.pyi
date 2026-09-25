from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tank.admin.v1 import admin_pb2 as _admin_pb2
from tank.agent.v1 import agent_pb2 as _agent_pb2
from tank.blocks.v1 import blocks_pb2 as _blocks_pb2
from tank.channel.v1 import channel_pb2 as _channel_pb2
from tank.files.v1 import files_pb2 as _files_pb2
from tank.huddle.v1 import huddle_pb2 as _huddle_pb2
from tank.message.v1 import message_pb2 as _message_pb2
from tank.presence.v1 import presence_pb2 as _presence_pb2
from tank.topo.v1 import topo_pb2 as _topo_pb2
from tank.workspace.v1 import workspace_pb2 as _workspace_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Envelope(_message.Message):
    __slots__ = ("id", "workspace_id", "type", "subject", "occurred_at", "trace_parent", "payload")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    TRACE_PARENT_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    type: str
    subject: str
    occurred_at: _timestamp_pb2.Timestamp
    trace_parent: str
    payload: _any_pb2.Any
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., type: _Optional[str] = ..., subject: _Optional[str] = ..., occurred_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., trace_parent: _Optional[str] = ..., payload: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class MessageCreated(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _message_pb2.Message
    def __init__(self, message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class MessageUpdated(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _message_pb2.Message
    def __init__(self, message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class MessageDeleted(_message.Message):
    __slots__ = ("message_id", "channel_id", "thread_root_id")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    channel_id: str
    thread_root_id: str
    def __init__(self, message_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ...) -> None: ...

class ReactionAdded(_message.Message):
    __slots__ = ("message_id", "user_id", "emoji")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    user_id: str
    emoji: str
    def __init__(self, message_id: _Optional[str] = ..., user_id: _Optional[str] = ..., emoji: _Optional[str] = ...) -> None: ...

class ReactionRemoved(_message.Message):
    __slots__ = ("message_id", "user_id", "emoji")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    user_id: str
    emoji: str
    def __init__(self, message_id: _Optional[str] = ..., user_id: _Optional[str] = ..., emoji: _Optional[str] = ...) -> None: ...

class ReadStateUpdated(_message.Message):
    __slots__ = ("user_id", "channel_id", "last_read_seq", "thread_root_id", "last_read_thread_seq")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_READ_SEQ_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_READ_THREAD_SEQ_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    channel_id: str
    last_read_seq: int
    thread_root_id: str
    last_read_thread_seq: int
    def __init__(self, user_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., last_read_seq: _Optional[int] = ..., thread_root_id: _Optional[str] = ..., last_read_thread_seq: _Optional[int] = ...) -> None: ...

class ChannelUpdated(_message.Message):
    __slots__ = ("channel_id", "channel")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    channel: _channel_pb2.Channel
    def __init__(self, channel_id: _Optional[str] = ..., channel: _Optional[_Union[_channel_pb2.Channel, _Mapping]] = ...) -> None: ...

class ChannelMembershipChanged(_message.Message):
    __slots__ = ("channel_id", "user_id", "joined", "actor_id")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    JOINED_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    user_id: str
    joined: bool
    actor_id: str
    def __init__(self, channel_id: _Optional[str] = ..., user_id: _Optional[str] = ..., joined: bool = ..., actor_id: _Optional[str] = ...) -> None: ...

class CardAction(_message.Message):
    __slots__ = ("action",)
    ACTION_FIELD_NUMBER: _ClassVar[int]
    action: _blocks_pb2.BlockAction
    def __init__(self, action: _Optional[_Union[_blocks_pb2.BlockAction, _Mapping]] = ...) -> None: ...

class AppCommand(_message.Message):
    __slots__ = ("command", "text", "user_id", "channel_id", "thread_root_id")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    command: str
    text: str
    user_id: str
    channel_id: str
    thread_root_id: str
    def __init__(self, command: _Optional[str] = ..., text: _Optional[str] = ..., user_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ...) -> None: ...

class PresenceChanged(_message.Message):
    __slots__ = ("presence",)
    PRESENCE_FIELD_NUMBER: _ClassVar[int]
    presence: _presence_pb2.Presence
    def __init__(self, presence: _Optional[_Union[_presence_pb2.Presence, _Mapping]] = ...) -> None: ...

class Typing(_message.Message):
    __slots__ = ("channel_id", "user_id", "thread_root_id")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    user_id: str
    thread_root_id: str
    def __init__(self, channel_id: _Optional[str] = ..., user_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ...) -> None: ...

class AgentStatus(_message.Message):
    __slots__ = ("channel_id", "thread_root_id", "run_id", "status")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    thread_root_id: str
    run_id: str
    status: str
    def __init__(self, channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., run_id: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class FileReady(_message.Message):
    __slots__ = ("file",)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: _files_pb2.File
    def __init__(self, file: _Optional[_Union[_files_pb2.File, _Mapping]] = ...) -> None: ...

class MessageEphemeral(_message.Message):
    __slots__ = ("message", "user_id")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    message: _message_pb2.Message
    user_id: str
    def __init__(self, message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class NotificationsRead(_message.Message):
    __slots__ = ("notification_ids",)
    NOTIFICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    notification_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, notification_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class AgentRunUpdated(_message.Message):
    __slots__ = ("run",)
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: _agent_pb2.Run
    def __init__(self, run: _Optional[_Union[_agent_pb2.Run, _Mapping]] = ...) -> None: ...

class NotificationCreated(_message.Message):
    __slots__ = ("notification_id", "kind", "message_id", "channel_id", "actor_id")
    NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    notification_id: str
    kind: str
    message_id: str
    channel_id: str
    actor_id: str
    def __init__(self, notification_id: _Optional[str] = ..., kind: _Optional[str] = ..., message_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., actor_id: _Optional[str] = ...) -> None: ...

class PinChanged(_message.Message):
    __slots__ = ("message_id", "channel_id", "user_id", "pinned")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PINNED_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    channel_id: str
    user_id: str
    pinned: bool
    def __init__(self, message_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., user_id: _Optional[str] = ..., pinned: bool = ...) -> None: ...

class EmojiChanged(_message.Message):
    __slots__ = ("emoji", "deleted", "hash")
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    emoji: _workspace_pb2.CustomEmoji
    deleted: bool
    hash: str
    def __init__(self, emoji: _Optional[_Union[_workspace_pb2.CustomEmoji, _Mapping]] = ..., deleted: bool = ..., hash: _Optional[str] = ...) -> None: ...

class PreferencesUpdated(_message.Message):
    __slots__ = ("user_id", "preferences")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    preferences: _workspace_pb2.Preferences
    def __init__(self, user_id: _Optional[str] = ..., preferences: _Optional[_Union[_workspace_pb2.Preferences, _Mapping]] = ...) -> None: ...

class ChannelPreferenceUpdated(_message.Message):
    __slots__ = ("user_id", "read_state")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    READ_STATE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    read_state: _channel_pb2.ChannelReadState
    def __init__(self, user_id: _Optional[str] = ..., read_state: _Optional[_Union[_channel_pb2.ChannelReadState, _Mapping]] = ...) -> None: ...

class DraftUpdated(_message.Message):
    __slots__ = ("user_id", "draft", "deleted")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    draft: _workspace_pb2.Draft
    deleted: bool
    def __init__(self, user_id: _Optional[str] = ..., draft: _Optional[_Union[_workspace_pb2.Draft, _Mapping]] = ..., deleted: bool = ...) -> None: ...

class ScheduledMessageSent(_message.Message):
    __slots__ = ("scheduled",)
    SCHEDULED_FIELD_NUMBER: _ClassVar[int]
    scheduled: _workspace_pb2.ScheduledMessage
    def __init__(self, scheduled: _Optional[_Union[_workspace_pb2.ScheduledMessage, _Mapping]] = ...) -> None: ...

class UserGroupUpdated(_message.Message):
    __slots__ = ("group", "deleted")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    group: _workspace_pb2.UserGroup
    deleted: bool
    def __init__(self, group: _Optional[_Union[_workspace_pb2.UserGroup, _Mapping]] = ..., deleted: bool = ...) -> None: ...

class BookmarkChanged(_message.Message):
    __slots__ = ("bookmark", "removed")
    BOOKMARK_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    bookmark: _workspace_pb2.ChannelBookmark
    removed: bool
    def __init__(self, bookmark: _Optional[_Union[_workspace_pb2.ChannelBookmark, _Mapping]] = ..., removed: bool = ...) -> None: ...

class MemberUpdated(_message.Message):
    __slots__ = ("member",)
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: _workspace_pb2.Member
    def __init__(self, member: _Optional[_Union[_workspace_pb2.Member, _Mapping]] = ...) -> None: ...

class HuddleStarted(_message.Message):
    __slots__ = ("huddle",)
    HUDDLE_FIELD_NUMBER: _ClassVar[int]
    huddle: _huddle_pb2.Huddle
    def __init__(self, huddle: _Optional[_Union[_huddle_pb2.Huddle, _Mapping]] = ...) -> None: ...

class HuddleEnded(_message.Message):
    __slots__ = ("huddle",)
    HUDDLE_FIELD_NUMBER: _ClassVar[int]
    huddle: _huddle_pb2.Huddle
    def __init__(self, huddle: _Optional[_Union[_huddle_pb2.Huddle, _Mapping]] = ...) -> None: ...

class HuddleParticipantsChanged(_message.Message):
    __slots__ = ("huddle",)
    HUDDLE_FIELD_NUMBER: _ClassVar[int]
    huddle: _huddle_pb2.Huddle
    def __init__(self, huddle: _Optional[_Union[_huddle_pb2.Huddle, _Mapping]] = ...) -> None: ...

class MemberRoleChanged(_message.Message):
    __slots__ = ("member", "previous_role", "actor_id")
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_ROLE_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    member: _workspace_pb2.Member
    previous_role: _workspace_pb2.Role
    actor_id: str
    def __init__(self, member: _Optional[_Union[_workspace_pb2.Member, _Mapping]] = ..., previous_role: _Optional[_Union[_workspace_pb2.Role, str]] = ..., actor_id: _Optional[str] = ...) -> None: ...

class MemberDeactivated(_message.Message):
    __slots__ = ("member", "reactivated", "removed", "actor_id")
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    REACTIVATED_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    member: _workspace_pb2.Member
    reactivated: bool
    removed: bool
    actor_id: str
    def __init__(self, member: _Optional[_Union[_workspace_pb2.Member, _Mapping]] = ..., reactivated: bool = ..., removed: bool = ..., actor_id: _Optional[str] = ...) -> None: ...

class WorkspaceSettingsUpdated(_message.Message):
    __slots__ = ("settings", "actor_id")
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    settings: _admin_pb2.WorkspaceSettings
    actor_id: str
    def __init__(self, settings: _Optional[_Union[_admin_pb2.WorkspaceSettings, _Mapping]] = ..., actor_id: _Optional[str] = ...) -> None: ...

class AuditLogged(_message.Message):
    __slots__ = ("entry",)
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    entry: _admin_pb2.AuditEntry
    def __init__(self, entry: _Optional[_Union[_admin_pb2.AuditEntry, _Mapping]] = ...) -> None: ...

class ExportReady(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: _admin_pb2.ExportJob
    def __init__(self, job: _Optional[_Union[_admin_pb2.ExportJob, _Mapping]] = ...) -> None: ...

class TopoMarkUpdated(_message.Message):
    __slots__ = ("mark",)
    MARK_FIELD_NUMBER: _ClassVar[int]
    mark: _topo_pb2.Mark
    def __init__(self, mark: _Optional[_Union[_topo_pb2.Mark, _Mapping]] = ...) -> None: ...
