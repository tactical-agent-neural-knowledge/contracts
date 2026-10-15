from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PLATFORM_UNSPECIFIED: _ClassVar[Platform]
    PLATFORM_X: _ClassVar[Platform]
    PLATFORM_INSTAGRAM: _ClassVar[Platform]

class PostStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POST_STATUS_UNSPECIFIED: _ClassVar[PostStatus]
    POST_STATUS_DRAFT: _ClassVar[PostStatus]
    POST_STATUS_POSTED: _ClassVar[PostStatus]
    POST_STATUS_FAILED: _ClassVar[PostStatus]
PLATFORM_UNSPECIFIED: Platform
PLATFORM_X: Platform
PLATFORM_INSTAGRAM: Platform
POST_STATUS_UNSPECIFIED: PostStatus
POST_STATUS_DRAFT: PostStatus
POST_STATUS_POSTED: PostStatus
POST_STATUS_FAILED: PostStatus

class Provider(_message.Message):
    __slots__ = ("platform", "configured", "signup_url")
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_FIELD_NUMBER: _ClassVar[int]
    SIGNUP_URL_FIELD_NUMBER: _ClassVar[int]
    platform: Platform
    configured: bool
    signup_url: str
    def __init__(self, platform: _Optional[_Union[Platform, str]] = ..., configured: bool = ..., signup_url: _Optional[str] = ...) -> None: ...

class Account(_message.Message):
    __slots__ = ("id", "platform", "handle", "display_name", "profile_url", "connected_by", "connected_at", "needs_reconnect")
    ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_URL_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_BY_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_AT_FIELD_NUMBER: _ClassVar[int]
    NEEDS_RECONNECT_FIELD_NUMBER: _ClassVar[int]
    id: str
    platform: Platform
    handle: str
    display_name: str
    profile_url: str
    connected_by: str
    connected_at: _timestamp_pb2.Timestamp
    needs_reconnect: bool
    def __init__(self, id: _Optional[str] = ..., platform: _Optional[_Union[Platform, str]] = ..., handle: _Optional[str] = ..., display_name: _Optional[str] = ..., profile_url: _Optional[str] = ..., connected_by: _Optional[str] = ..., connected_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., needs_reconnect: bool = ...) -> None: ...

class Settings(_message.Message):
    __slots__ = ("enabled", "review_required", "cadence", "hour_utc", "channel_id", "platforms", "voice")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    REVIEW_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    CADENCE_FIELD_NUMBER: _ClassVar[int]
    HOUR_UTC_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORMS_FIELD_NUMBER: _ClassVar[int]
    VOICE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    review_required: bool
    cadence: str
    hour_utc: int
    channel_id: str
    platforms: _containers.RepeatedScalarFieldContainer[Platform]
    voice: str
    def __init__(self, enabled: bool = ..., review_required: bool = ..., cadence: _Optional[str] = ..., hour_utc: _Optional[int] = ..., channel_id: _Optional[str] = ..., platforms: _Optional[_Iterable[_Union[Platform, str]]] = ..., voice: _Optional[str] = ...) -> None: ...

class Post(_message.Message):
    __slots__ = ("id", "account_id", "platform", "text", "file_ids", "status", "url", "requested_by", "thread_root_id", "created_at", "posted_at", "error")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    POSTED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    id: str
    account_id: str
    platform: Platform
    text: str
    file_ids: _containers.RepeatedScalarFieldContainer[str]
    status: PostStatus
    url: str
    requested_by: str
    thread_root_id: str
    created_at: _timestamp_pb2.Timestamp
    posted_at: _timestamp_pb2.Timestamp
    error: str
    def __init__(self, id: _Optional[str] = ..., account_id: _Optional[str] = ..., platform: _Optional[_Union[Platform, str]] = ..., text: _Optional[str] = ..., file_ids: _Optional[_Iterable[str]] = ..., status: _Optional[_Union[PostStatus, str]] = ..., url: _Optional[str] = ..., requested_by: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., posted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[str] = ...) -> None: ...

class ListAccountsRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListAccountsResponse(_message.Message):
    __slots__ = ("accounts", "providers", "settings", "can_manage")
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CAN_MANAGE_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[Account]
    providers: _containers.RepeatedCompositeFieldContainer[Provider]
    settings: Settings
    can_manage: bool
    def __init__(self, accounts: _Optional[_Iterable[_Union[Account, _Mapping]]] = ..., providers: _Optional[_Iterable[_Union[Provider, _Mapping]]] = ..., settings: _Optional[_Union[Settings, _Mapping]] = ..., can_manage: bool = ...) -> None: ...

class StartConnectRequest(_message.Message):
    __slots__ = ("workspace_id", "platform", "return_url")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    RETURN_URL_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    platform: Platform
    return_url: str
    def __init__(self, workspace_id: _Optional[str] = ..., platform: _Optional[_Union[Platform, str]] = ..., return_url: _Optional[str] = ...) -> None: ...

class StartConnectResponse(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class DisconnectRequest(_message.Message):
    __slots__ = ("workspace_id", "account_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    account_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class DisconnectResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSettingsRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class GetSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: Settings
    def __init__(self, settings: _Optional[_Union[Settings, _Mapping]] = ...) -> None: ...

class UpdateSettingsRequest(_message.Message):
    __slots__ = ("workspace_id", "settings")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    settings: Settings
    def __init__(self, workspace_id: _Optional[str] = ..., settings: _Optional[_Union[Settings, _Mapping]] = ...) -> None: ...

class UpdateSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: Settings
    def __init__(self, settings: _Optional[_Union[Settings, _Mapping]] = ...) -> None: ...

class ListPostsRequest(_message.Message):
    __slots__ = ("workspace_id", "limit")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    limit: int
    def __init__(self, workspace_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListPostsResponse(_message.Message):
    __slots__ = ("posts",)
    POSTS_FIELD_NUMBER: _ClassVar[int]
    posts: _containers.RepeatedCompositeFieldContainer[Post]
    def __init__(self, posts: _Optional[_Iterable[_Union[Post, _Mapping]]] = ...) -> None: ...

class CreatePostRequest(_message.Message):
    __slots__ = ("workspace_id", "platform", "text", "file_ids", "publish")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    platform: Platform
    text: str
    file_ids: _containers.RepeatedScalarFieldContainer[str]
    publish: bool
    def __init__(self, workspace_id: _Optional[str] = ..., platform: _Optional[_Union[Platform, str]] = ..., text: _Optional[str] = ..., file_ids: _Optional[_Iterable[str]] = ..., publish: bool = ...) -> None: ...

class CreatePostResponse(_message.Message):
    __slots__ = ("post",)
    POST_FIELD_NUMBER: _ClassVar[int]
    post: Post
    def __init__(self, post: _Optional[_Union[Post, _Mapping]] = ...) -> None: ...

class PublishPostRequest(_message.Message):
    __slots__ = ("workspace_id", "post_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    post_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., post_id: _Optional[str] = ...) -> None: ...

class PublishPostResponse(_message.Message):
    __slots__ = ("post",)
    POST_FIELD_NUMBER: _ClassVar[int]
    post: Post
    def __init__(self, post: _Optional[_Union[Post, _Mapping]] = ...) -> None: ...

class DeletePostRequest(_message.Message):
    __slots__ = ("workspace_id", "post_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    post_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., post_id: _Optional[str] = ...) -> None: ...

class DeletePostResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
