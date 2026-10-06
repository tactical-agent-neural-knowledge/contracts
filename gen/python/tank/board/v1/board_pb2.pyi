from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObjectKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OBJECT_KIND_UNSPECIFIED: _ClassVar[ObjectKind]
    OBJECT_KIND_FRAME: _ClassVar[ObjectKind]
    OBJECT_KIND_RECT: _ClassVar[ObjectKind]
    OBJECT_KIND_ELLIPSE: _ClassVar[ObjectKind]
    OBJECT_KIND_LINE: _ClassVar[ObjectKind]
    OBJECT_KIND_ARROW: _ClassVar[ObjectKind]
    OBJECT_KIND_TEXT: _ClassVar[ObjectKind]
    OBJECT_KIND_STICKY: _ClassVar[ObjectKind]
    OBJECT_KIND_IMAGE: _ClassVar[ObjectKind]
    OBJECT_KIND_CONNECTOR: _ClassVar[ObjectKind]
    OBJECT_KIND_DRAW: _ClassVar[ObjectKind]
OBJECT_KIND_UNSPECIFIED: ObjectKind
OBJECT_KIND_FRAME: ObjectKind
OBJECT_KIND_RECT: ObjectKind
OBJECT_KIND_ELLIPSE: ObjectKind
OBJECT_KIND_LINE: ObjectKind
OBJECT_KIND_ARROW: ObjectKind
OBJECT_KIND_TEXT: ObjectKind
OBJECT_KIND_STICKY: ObjectKind
OBJECT_KIND_IMAGE: ObjectKind
OBJECT_KIND_CONNECTOR: ObjectKind
OBJECT_KIND_DRAW: ObjectKind

class Rect(_message.Message):
    __slots__ = ("x", "y", "w", "h")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    H_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    w: float
    h: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., w: _Optional[float] = ..., h: _Optional[float] = ...) -> None: ...

class Style(_message.Message):
    __slots__ = ("fill", "stroke", "stroke_width", "opacity", "corner_radius", "dash", "font_size", "font_weight", "align")
    FILL_FIELD_NUMBER: _ClassVar[int]
    STROKE_FIELD_NUMBER: _ClassVar[int]
    STROKE_WIDTH_FIELD_NUMBER: _ClassVar[int]
    OPACITY_FIELD_NUMBER: _ClassVar[int]
    CORNER_RADIUS_FIELD_NUMBER: _ClassVar[int]
    DASH_FIELD_NUMBER: _ClassVar[int]
    FONT_SIZE_FIELD_NUMBER: _ClassVar[int]
    FONT_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    ALIGN_FIELD_NUMBER: _ClassVar[int]
    fill: str
    stroke: str
    stroke_width: float
    opacity: float
    corner_radius: float
    dash: str
    font_size: int
    font_weight: str
    align: str
    def __init__(self, fill: _Optional[str] = ..., stroke: _Optional[str] = ..., stroke_width: _Optional[float] = ..., opacity: _Optional[float] = ..., corner_radius: _Optional[float] = ..., dash: _Optional[str] = ..., font_size: _Optional[int] = ..., font_weight: _Optional[str] = ..., align: _Optional[str] = ...) -> None: ...

class AppFrame(_message.Message):
    __slots__ = ("repo", "ref", "path", "platform", "viewport_width", "viewport_height", "preview_url", "status", "note")
    REPO_FIELD_NUMBER: _ClassVar[int]
    REF_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    VIEWPORT_WIDTH_FIELD_NUMBER: _ClassVar[int]
    VIEWPORT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_URL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    repo: str
    ref: str
    path: str
    platform: str
    viewport_width: int
    viewport_height: int
    preview_url: str
    status: str
    note: str
    def __init__(self, repo: _Optional[str] = ..., ref: _Optional[str] = ..., path: _Optional[str] = ..., platform: _Optional[str] = ..., viewport_width: _Optional[int] = ..., viewport_height: _Optional[int] = ..., preview_url: _Optional[str] = ..., status: _Optional[str] = ..., note: _Optional[str] = ...) -> None: ...

class BoardObject(_message.Message):
    __slots__ = ("id", "kind", "at", "style", "text", "rotation", "z", "parent_id", "from_id", "to_id", "points", "file_id", "file_url", "app", "locked", "created_by", "rev")
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    STYLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ROTATION_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_ID_FIELD_NUMBER: _ClassVar[int]
    TO_ID_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_URL_FIELD_NUMBER: _ClassVar[int]
    APP_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    REV_FIELD_NUMBER: _ClassVar[int]
    id: str
    kind: ObjectKind
    at: Rect
    style: Style
    text: str
    rotation: float
    z: int
    parent_id: str
    from_id: str
    to_id: str
    points: _containers.RepeatedScalarFieldContainer[float]
    file_id: str
    file_url: str
    app: AppFrame
    locked: bool
    created_by: str
    rev: int
    def __init__(self, id: _Optional[str] = ..., kind: _Optional[_Union[ObjectKind, str]] = ..., at: _Optional[_Union[Rect, _Mapping]] = ..., style: _Optional[_Union[Style, _Mapping]] = ..., text: _Optional[str] = ..., rotation: _Optional[float] = ..., z: _Optional[int] = ..., parent_id: _Optional[str] = ..., from_id: _Optional[str] = ..., to_id: _Optional[str] = ..., points: _Optional[_Iterable[float]] = ..., file_id: _Optional[str] = ..., file_url: _Optional[str] = ..., app: _Optional[_Union[AppFrame, _Mapping]] = ..., locked: bool = ..., created_by: _Optional[str] = ..., rev: _Optional[int] = ...) -> None: ...

class Board(_message.Message):
    __slots__ = ("id", "workspace_id", "channel_id", "title", "icon", "objects", "version", "created_by", "created_at", "updated_by", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    channel_id: str
    title: str
    icon: str
    objects: _containers.RepeatedCompositeFieldContainer[BoardObject]
    version: int
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    updated_by: str
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., title: _Optional[str] = ..., icon: _Optional[str] = ..., objects: _Optional[_Iterable[_Union[BoardObject, _Mapping]]] = ..., version: _Optional[int] = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_by: _Optional[str] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class BoardSummary(_message.Message):
    __slots__ = ("id", "title", "icon", "objects", "app_frames", "updated_at", "channel_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    APP_FRAMES_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    icon: str
    objects: int
    app_frames: int
    updated_at: _timestamp_pb2.Timestamp
    channel_id: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., icon: _Optional[str] = ..., objects: _Optional[int] = ..., app_frames: _Optional[int] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., channel_id: _Optional[str] = ...) -> None: ...

class ListBoardsRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id", "limit")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    limit: int
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListBoardsResponse(_message.Message):
    __slots__ = ("boards",)
    BOARDS_FIELD_NUMBER: _ClassVar[int]
    boards: _containers.RepeatedCompositeFieldContainer[BoardSummary]
    def __init__(self, boards: _Optional[_Iterable[_Union[BoardSummary, _Mapping]]] = ...) -> None: ...

class GetBoardRequest(_message.Message):
    __slots__ = ("workspace_id", "id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class GetBoardResponse(_message.Message):
    __slots__ = ("board",)
    BOARD_FIELD_NUMBER: _ClassVar[int]
    board: Board
    def __init__(self, board: _Optional[_Union[Board, _Mapping]] = ...) -> None: ...

class CreateBoardRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id", "title", "icon", "objects")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    title: str
    icon: str
    objects: _containers.RepeatedCompositeFieldContainer[BoardObject]
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., title: _Optional[str] = ..., icon: _Optional[str] = ..., objects: _Optional[_Iterable[_Union[BoardObject, _Mapping]]] = ...) -> None: ...

class CreateBoardResponse(_message.Message):
    __slots__ = ("board",)
    BOARD_FIELD_NUMBER: _ClassVar[int]
    board: Board
    def __init__(self, board: _Optional[_Union[Board, _Mapping]] = ...) -> None: ...

class UpdateBoardRequest(_message.Message):
    __slots__ = ("workspace_id", "id", "title", "icon")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    title: str
    icon: str
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ..., title: _Optional[str] = ..., icon: _Optional[str] = ...) -> None: ...

class UpdateBoardResponse(_message.Message):
    __slots__ = ("board",)
    BOARD_FIELD_NUMBER: _ClassVar[int]
    board: Board
    def __init__(self, board: _Optional[_Union[Board, _Mapping]] = ...) -> None: ...

class DeleteBoardRequest(_message.Message):
    __slots__ = ("workspace_id", "id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteBoardResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PutObjectsRequest(_message.Message):
    __slots__ = ("workspace_id", "board_id", "objects", "delete_ids", "base_revs")
    class BaseRevsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    BOARD_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    DELETE_IDS_FIELD_NUMBER: _ClassVar[int]
    BASE_REVS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    board_id: str
    objects: _containers.RepeatedCompositeFieldContainer[BoardObject]
    delete_ids: _containers.RepeatedScalarFieldContainer[str]
    base_revs: _containers.ScalarMap[str, int]
    def __init__(self, workspace_id: _Optional[str] = ..., board_id: _Optional[str] = ..., objects: _Optional[_Iterable[_Union[BoardObject, _Mapping]]] = ..., delete_ids: _Optional[_Iterable[str]] = ..., base_revs: _Optional[_Mapping[str, int]] = ...) -> None: ...

class PutObjectsResponse(_message.Message):
    __slots__ = ("board", "conflicts", "conflict_note")
    BOARD_FIELD_NUMBER: _ClassVar[int]
    CONFLICTS_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_NOTE_FIELD_NUMBER: _ClassVar[int]
    board: Board
    conflicts: _containers.RepeatedCompositeFieldContainer[BoardObject]
    conflict_note: str
    def __init__(self, board: _Optional[_Union[Board, _Mapping]] = ..., conflicts: _Optional[_Iterable[_Union[BoardObject, _Mapping]]] = ..., conflict_note: _Optional[str] = ...) -> None: ...

class Element(_message.Message):
    __slots__ = ("source", "tag", "text", "test_id", "at", "classes")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TEST_ID_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    CLASSES_FIELD_NUMBER: _ClassVar[int]
    source: str
    tag: str
    text: str
    test_id: str
    at: Rect
    classes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, source: _Optional[str] = ..., tag: _Optional[str] = ..., text: _Optional[str] = ..., test_id: _Optional[str] = ..., at: _Optional[_Union[Rect, _Mapping]] = ..., classes: _Optional[_Iterable[str]] = ...) -> None: ...

class RequestChangeRequest(_message.Message):
    __slots__ = ("workspace_id", "board_id", "object_id", "element", "ask")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    BOARD_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_FIELD_NUMBER: _ClassVar[int]
    ASK_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    board_id: str
    object_id: str
    element: Element
    ask: str
    def __init__(self, workspace_id: _Optional[str] = ..., board_id: _Optional[str] = ..., object_id: _Optional[str] = ..., element: _Optional[_Union[Element, _Mapping]] = ..., ask: _Optional[str] = ...) -> None: ...

class RequestChangeResponse(_message.Message):
    __slots__ = ("thread_root_id", "channel_id", "prompt")
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    thread_root_id: str
    channel_id: str
    prompt: str
    def __init__(self, thread_root_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., prompt: _Optional[str] = ...) -> None: ...
