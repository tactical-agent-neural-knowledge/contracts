from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PushPlatform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PUSH_PLATFORM_UNSPECIFIED: _ClassVar[PushPlatform]
    PUSH_PLATFORM_APNS: _ClassVar[PushPlatform]
    PUSH_PLATFORM_FCM: _ClassVar[PushPlatform]
    PUSH_PLATFORM_WEB: _ClassVar[PushPlatform]
PUSH_PLATFORM_UNSPECIFIED: PushPlatform
PUSH_PLATFORM_APNS: PushPlatform
PUSH_PLATFORM_FCM: PushPlatform
PUSH_PLATFORM_WEB: PushPlatform

class Notification(_message.Message):
    __slots__ = ("id", "workspace_id", "user_id", "kind", "message_id", "channel_id", "actor_id", "read_at", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    READ_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    user_id: str
    kind: str
    message_id: str
    channel_id: str
    actor_id: str
    read_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., user_id: _Optional[str] = ..., kind: _Optional[str] = ..., message_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., actor_id: _Optional[str] = ..., read_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListNotificationsRequest(_message.Message):
    __slots__ = ("workspace_id", "unread_only", "cursor", "limit")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    UNREAD_ONLY_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    unread_only: bool
    cursor: str
    limit: int
    def __init__(self, workspace_id: _Optional[str] = ..., unread_only: bool = ..., cursor: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListNotificationsResponse(_message.Message):
    __slots__ = ("notifications", "next_cursor", "unread_count")
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    UNREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    notifications: _containers.RepeatedCompositeFieldContainer[Notification]
    next_cursor: str
    unread_count: int
    def __init__(self, notifications: _Optional[_Iterable[_Union[Notification, _Mapping]]] = ..., next_cursor: _Optional[str] = ..., unread_count: _Optional[int] = ...) -> None: ...

class MarkNotificationsReadRequest(_message.Message):
    __slots__ = ("workspace_id", "notification_ids")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    notification_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, workspace_id: _Optional[str] = ..., notification_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class MarkNotificationsReadResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RegisterDeviceRequest(_message.Message):
    __slots__ = ("platform", "token", "p256dh", "auth", "bundle_id", "description")
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    P256DH_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    platform: PushPlatform
    token: str
    p256dh: str
    auth: str
    bundle_id: str
    description: str
    def __init__(self, platform: _Optional[_Union[PushPlatform, str]] = ..., token: _Optional[str] = ..., p256dh: _Optional[str] = ..., auth: _Optional[str] = ..., bundle_id: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class RegisterDeviceResponse(_message.Message):
    __slots__ = ("device_id",)
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    def __init__(self, device_id: _Optional[str] = ...) -> None: ...

class UnregisterDeviceRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class UnregisterDeviceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
