from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tank.apps.v1 import apps_pb2 as _apps_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Page(_message.Message):
    __slots__ = ("id", "conversation_id", "url", "title", "owner_id", "owner_name", "opened_at", "state", "reason", "driver_id", "driver_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_NAME_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    DRIVER_ID_FIELD_NUMBER: _ClassVar[int]
    DRIVER_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    conversation_id: str
    url: str
    title: str
    owner_id: str
    owner_name: str
    opened_at: _timestamp_pb2.Timestamp
    state: str
    reason: str
    driver_id: str
    driver_name: str
    def __init__(self, id: _Optional[str] = ..., conversation_id: _Optional[str] = ..., url: _Optional[str] = ..., title: _Optional[str] = ..., owner_id: _Optional[str] = ..., owner_name: _Optional[str] = ..., opened_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[str] = ..., reason: _Optional[str] = ..., driver_id: _Optional[str] = ..., driver_name: _Optional[str] = ...) -> None: ...

class SetDriverRequest(_message.Message):
    __slots__ = ("page_id", "user_id")
    PAGE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    page_id: str
    user_id: str
    def __init__(self, page_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class SetDriverResponse(_message.Message):
    __slots__ = ("page",)
    PAGE_FIELD_NUMBER: _ClassVar[int]
    page: Page
    def __init__(self, page: _Optional[_Union[Page, _Mapping]] = ...) -> None: ...

class OpenPageRequest(_message.Message):
    __slots__ = ("conversation_id", "url", "viewport_width", "viewport_height")
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VIEWPORT_WIDTH_FIELD_NUMBER: _ClassVar[int]
    VIEWPORT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    url: str
    viewport_width: int
    viewport_height: int
    def __init__(self, conversation_id: _Optional[str] = ..., url: _Optional[str] = ..., viewport_width: _Optional[int] = ..., viewport_height: _Optional[int] = ...) -> None: ...

class OpenPageResponse(_message.Message):
    __slots__ = ("page",)
    PAGE_FIELD_NUMBER: _ClassVar[int]
    page: Page
    def __init__(self, page: _Optional[_Union[Page, _Mapping]] = ...) -> None: ...

class ClosePageRequest(_message.Message):
    __slots__ = ("page_id",)
    PAGE_ID_FIELD_NUMBER: _ClassVar[int]
    page_id: str
    def __init__(self, page_id: _Optional[str] = ...) -> None: ...

class ClosePageResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPagesRequest(_message.Message):
    __slots__ = ("conversation_id",)
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    def __init__(self, conversation_id: _Optional[str] = ...) -> None: ...

class ListPagesResponse(_message.Message):
    __slots__ = ("pages",)
    PAGES_FIELD_NUMBER: _ClassVar[int]
    pages: _containers.RepeatedCompositeFieldContainer[Page]
    def __init__(self, pages: _Optional[_Iterable[_Union[Page, _Mapping]]] = ...) -> None: ...

class ActRequest(_message.Message):
    __slots__ = ("page_id", "tap", "type", "key", "scroll", "back", "forward", "navigate", "reload")
    PAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TAP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    SCROLL_FIELD_NUMBER: _ClassVar[int]
    BACK_FIELD_NUMBER: _ClassVar[int]
    FORWARD_FIELD_NUMBER: _ClassVar[int]
    NAVIGATE_FIELD_NUMBER: _ClassVar[int]
    RELOAD_FIELD_NUMBER: _ClassVar[int]
    page_id: str
    tap: Point
    type: str
    key: str
    scroll: int
    back: bool
    forward: bool
    navigate: str
    reload: bool
    def __init__(self, page_id: _Optional[str] = ..., tap: _Optional[_Union[Point, _Mapping]] = ..., type: _Optional[str] = ..., key: _Optional[str] = ..., scroll: _Optional[int] = ..., back: bool = ..., forward: bool = ..., navigate: _Optional[str] = ..., reload: bool = ...) -> None: ...

class Point(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class ActResponse(_message.Message):
    __slots__ = ("page",)
    PAGE_FIELD_NUMBER: _ClassVar[int]
    page: Page
    def __init__(self, page: _Optional[_Union[Page, _Mapping]] = ...) -> None: ...

class WatchPageRequest(_message.Message):
    __slots__ = ("page_id",)
    PAGE_ID_FIELD_NUMBER: _ClassVar[int]
    page_id: str
    def __init__(self, page_id: _Optional[str] = ...) -> None: ...

class WatchPageResponse(_message.Message):
    __slots__ = ("frame", "page")
    FRAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    frame: Frame
    page: Page
    def __init__(self, frame: _Optional[_Union[Frame, _Mapping]] = ..., page: _Optional[_Union[Page, _Mapping]] = ...) -> None: ...

class Frame(_message.Message):
    __slots__ = ("jpeg", "width", "height", "url", "title", "at", "marks", "waiting_for_tap")
    JPEG_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    MARKS_FIELD_NUMBER: _ClassVar[int]
    WAITING_FOR_TAP_FIELD_NUMBER: _ClassVar[int]
    jpeg: bytes
    width: int
    height: int
    url: str
    title: str
    at: _timestamp_pb2.Timestamp
    marks: _containers.RepeatedCompositeFieldContainer[_apps_pb2.Mark]
    waiting_for_tap: str
    def __init__(self, jpeg: _Optional[bytes] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., url: _Optional[str] = ..., title: _Optional[str] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., marks: _Optional[_Iterable[_Union[_apps_pb2.Mark, _Mapping]]] = ..., waiting_for_tap: _Optional[str] = ...) -> None: ...
