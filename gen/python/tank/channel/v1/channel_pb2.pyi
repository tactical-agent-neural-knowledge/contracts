from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHANNEL_TYPE_UNSPECIFIED: _ClassVar[ChannelType]
    CHANNEL_TYPE_PUBLIC: _ClassVar[ChannelType]
    CHANNEL_TYPE_PRIVATE: _ClassVar[ChannelType]
    CHANNEL_TYPE_DM: _ClassVar[ChannelType]
    CHANNEL_TYPE_MPDM: _ClassVar[ChannelType]
CHANNEL_TYPE_UNSPECIFIED: ChannelType
CHANNEL_TYPE_PUBLIC: ChannelType
CHANNEL_TYPE_PRIVATE: ChannelType
CHANNEL_TYPE_DM: ChannelType
CHANNEL_TYPE_MPDM: ChannelType

class TreadGoal(_message.Message):
    __slots__ = ("goal", "assignee_ids", "pipeline_status", "updated_at", "updated_by")
    GOAL_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_IDS_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_STATUS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    goal: str
    assignee_ids: _containers.RepeatedScalarFieldContainer[str]
    pipeline_status: str
    updated_at: _timestamp_pb2.Timestamp
    updated_by: str
    def __init__(self, goal: _Optional[str] = ..., assignee_ids: _Optional[_Iterable[str]] = ..., pipeline_status: _Optional[str] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_by: _Optional[str] = ...) -> None: ...

class Channel(_message.Message):
    __slots__ = ("id", "workspace_id", "type", "name", "topic", "purpose", "last_seq", "member_count", "last_message_at", "archived_at", "created_at", "goal", "member_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    LAST_SEQ_FIELD_NUMBER: _ClassVar[int]
    MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_AT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    GOAL_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    type: ChannelType
    name: str
    topic: str
    purpose: str
    last_seq: int
    member_count: int
    last_message_at: _timestamp_pb2.Timestamp
    archived_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    goal: TreadGoal
    member_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., type: _Optional[_Union[ChannelType, str]] = ..., name: _Optional[str] = ..., topic: _Optional[str] = ..., purpose: _Optional[str] = ..., last_seq: _Optional[int] = ..., member_count: _Optional[int] = ..., last_message_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., archived_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., goal: _Optional[_Union[TreadGoal, _Mapping]] = ..., member_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ChannelReadState(_message.Message):
    __slots__ = ("channel_id", "last_read_seq", "mention_count", "muted", "starred")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_READ_SEQ_FIELD_NUMBER: _ClassVar[int]
    MENTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    MUTED_FIELD_NUMBER: _ClassVar[int]
    STARRED_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    last_read_seq: int
    mention_count: int
    muted: bool
    starred: bool
    def __init__(self, channel_id: _Optional[str] = ..., last_read_seq: _Optional[int] = ..., mention_count: _Optional[int] = ..., muted: bool = ..., starred: bool = ...) -> None: ...

class CreateChannelRequest(_message.Message):
    __slots__ = ("workspace_id", "type", "name", "purpose", "member_ids")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    type: ChannelType
    name: str
    purpose: str
    member_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, workspace_id: _Optional[str] = ..., type: _Optional[_Union[ChannelType, str]] = ..., name: _Optional[str] = ..., purpose: _Optional[str] = ..., member_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateChannelResponse(_message.Message):
    __slots__ = ("channel",)
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: Channel
    def __init__(self, channel: _Optional[_Union[Channel, _Mapping]] = ...) -> None: ...

class ListChannelsRequest(_message.Message):
    __slots__ = ("workspace_id", "include_unjoined_public", "cursor", "limit")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_UNJOINED_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    include_unjoined_public: bool
    cursor: str
    limit: int
    def __init__(self, workspace_id: _Optional[str] = ..., include_unjoined_public: bool = ..., cursor: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListChannelsResponse(_message.Message):
    __slots__ = ("channels", "next_cursor")
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    channels: _containers.RepeatedCompositeFieldContainer[Channel]
    next_cursor: str
    def __init__(self, channels: _Optional[_Iterable[_Union[Channel, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class GetChannelRequest(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class GetChannelResponse(_message.Message):
    __slots__ = ("channel", "read_state")
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    READ_STATE_FIELD_NUMBER: _ClassVar[int]
    channel: Channel
    read_state: ChannelReadState
    def __init__(self, channel: _Optional[_Union[Channel, _Mapping]] = ..., read_state: _Optional[_Union[ChannelReadState, _Mapping]] = ...) -> None: ...

class JoinChannelRequest(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class JoinChannelResponse(_message.Message):
    __slots__ = ("channel",)
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: Channel
    def __init__(self, channel: _Optional[_Union[Channel, _Mapping]] = ...) -> None: ...

class LeaveChannelRequest(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class LeaveChannelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InviteToChannelRequest(_message.Message):
    __slots__ = ("channel_id", "member_ids")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    member_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, channel_id: _Optional[str] = ..., member_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class InviteToChannelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetGoalRequest(_message.Message):
    __slots__ = ("channel_id", "goal")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    GOAL_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    goal: TreadGoal
    def __init__(self, channel_id: _Optional[str] = ..., goal: _Optional[_Union[TreadGoal, _Mapping]] = ...) -> None: ...

class SetGoalResponse(_message.Message):
    __slots__ = ("channel",)
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: Channel
    def __init__(self, channel: _Optional[_Union[Channel, _Mapping]] = ...) -> None: ...

class ListChannelMembersRequest(_message.Message):
    __slots__ = ("channel_id", "cursor", "limit")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    cursor: str
    limit: int
    def __init__(self, channel_id: _Optional[str] = ..., cursor: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListChannelMembersResponse(_message.Message):
    __slots__ = ("member_ids", "next_cursor")
    MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    member_ids: _containers.RepeatedScalarFieldContainer[str]
    next_cursor: str
    def __init__(self, member_ids: _Optional[_Iterable[str]] = ..., next_cursor: _Optional[str] = ...) -> None: ...
