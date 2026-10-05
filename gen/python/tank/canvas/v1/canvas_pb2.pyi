from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BlockKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BLOCK_KIND_UNSPECIFIED: _ClassVar[BlockKind]
    BLOCK_KIND_HEADING: _ClassVar[BlockKind]
    BLOCK_KIND_TEXT: _ClassVar[BlockKind]
    BLOCK_KIND_BULLET: _ClassVar[BlockKind]
    BLOCK_KIND_NUMBER: _ClassVar[BlockKind]
    BLOCK_KIND_QUOTE: _ClassVar[BlockKind]
    BLOCK_KIND_CODE: _ClassVar[BlockKind]
    BLOCK_KIND_DIVIDER: _ClassVar[BlockKind]
    BLOCK_KIND_TODO: _ClassVar[BlockKind]
    BLOCK_KIND_DECISION: _ClassVar[BlockKind]
    BLOCK_KIND_LIVE: _ClassVar[BlockKind]
    BLOCK_KIND_MESSAGE: _ClassVar[BlockKind]
    BLOCK_KIND_IMAGE: _ClassVar[BlockKind]
BLOCK_KIND_UNSPECIFIED: BlockKind
BLOCK_KIND_HEADING: BlockKind
BLOCK_KIND_TEXT: BlockKind
BLOCK_KIND_BULLET: BlockKind
BLOCK_KIND_NUMBER: BlockKind
BLOCK_KIND_QUOTE: BlockKind
BLOCK_KIND_CODE: BlockKind
BLOCK_KIND_DIVIDER: BlockKind
BLOCK_KIND_TODO: BlockKind
BLOCK_KIND_DECISION: BlockKind
BLOCK_KIND_LIVE: BlockKind
BLOCK_KIND_MESSAGE: BlockKind
BLOCK_KIND_IMAGE: BlockKind

class Decision(_message.Message):
    __slots__ = ("what", "decided_by", "decided_at", "because", "supersedes_block_id", "thread_root_id", "needs_revisiting", "revisit_note")
    WHAT_FIELD_NUMBER: _ClassVar[int]
    DECIDED_BY_FIELD_NUMBER: _ClassVar[int]
    DECIDED_AT_FIELD_NUMBER: _ClassVar[int]
    BECAUSE_FIELD_NUMBER: _ClassVar[int]
    SUPERSEDES_BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    NEEDS_REVISITING_FIELD_NUMBER: _ClassVar[int]
    REVISIT_NOTE_FIELD_NUMBER: _ClassVar[int]
    what: str
    decided_by: _containers.RepeatedScalarFieldContainer[str]
    decided_at: _timestamp_pb2.Timestamp
    because: str
    supersedes_block_id: str
    thread_root_id: str
    needs_revisiting: bool
    revisit_note: str
    def __init__(self, what: _Optional[str] = ..., decided_by: _Optional[_Iterable[str]] = ..., decided_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., because: _Optional[str] = ..., supersedes_block_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., needs_revisiting: bool = ..., revisit_note: _Optional[str] = ...) -> None: ...

class Live(_message.Message):
    __slots__ = ("kind", "ref", "label", "value", "detail", "as_of", "error")
    KIND_FIELD_NUMBER: _ClassVar[int]
    REF_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    AS_OF_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    kind: str
    ref: str
    label: str
    value: str
    detail: str
    as_of: _timestamp_pb2.Timestamp
    error: str
    def __init__(self, kind: _Optional[str] = ..., ref: _Optional[str] = ..., label: _Optional[str] = ..., value: _Optional[str] = ..., detail: _Optional[str] = ..., as_of: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[str] = ...) -> None: ...

class Block(_message.Message):
    __slots__ = ("id", "kind", "text", "depth", "checked", "lang", "decision", "live", "message_id", "file_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    CHECKED_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    DECISION_FIELD_NUMBER: _ClassVar[int]
    LIVE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    kind: BlockKind
    text: str
    depth: int
    checked: bool
    lang: str
    decision: Decision
    live: Live
    message_id: str
    file_id: str
    def __init__(self, id: _Optional[str] = ..., kind: _Optional[_Union[BlockKind, str]] = ..., text: _Optional[str] = ..., depth: _Optional[int] = ..., checked: bool = ..., lang: _Optional[str] = ..., decision: _Optional[_Union[Decision, _Mapping]] = ..., live: _Optional[_Union[Live, _Mapping]] = ..., message_id: _Optional[str] = ..., file_id: _Optional[str] = ...) -> None: ...

class Source(_message.Message):
    __slots__ = ("kind", "ref", "label", "seen_at", "changed", "changed_note")
    KIND_FIELD_NUMBER: _ClassVar[int]
    REF_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    CHANGED_FIELD_NUMBER: _ClassVar[int]
    CHANGED_NOTE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    ref: str
    label: str
    seen_at: _timestamp_pb2.Timestamp
    changed: bool
    changed_note: str
    def __init__(self, kind: _Optional[str] = ..., ref: _Optional[str] = ..., label: _Optional[str] = ..., seen_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., changed: bool = ..., changed_note: _Optional[str] = ...) -> None: ...

class Canvas(_message.Message):
    __slots__ = ("id", "workspace_id", "channel_id", "title", "icon", "blocks", "sources", "staleness", "staleness_note", "created_by", "created_at", "updated_by", "updated_at", "version", "written_by_agent", "summary")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    STALENESS_FIELD_NUMBER: _ClassVar[int]
    STALENESS_NOTE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    WRITTEN_BY_AGENT_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    channel_id: str
    title: str
    icon: str
    blocks: _containers.RepeatedCompositeFieldContainer[Block]
    sources: _containers.RepeatedCompositeFieldContainer[Source]
    staleness: int
    staleness_note: str
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    updated_by: str
    updated_at: _timestamp_pb2.Timestamp
    version: int
    written_by_agent: bool
    summary: str
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., title: _Optional[str] = ..., icon: _Optional[str] = ..., blocks: _Optional[_Iterable[_Union[Block, _Mapping]]] = ..., sources: _Optional[_Iterable[_Union[Source, _Mapping]]] = ..., staleness: _Optional[int] = ..., staleness_note: _Optional[str] = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_by: _Optional[str] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., version: _Optional[int] = ..., written_by_agent: bool = ..., summary: _Optional[str] = ...) -> None: ...

class CanvasSummary(_message.Message):
    __slots__ = ("id", "title", "icon", "channel_id", "summary", "staleness", "staleness_note", "updated_at", "updated_by", "written_by_agent", "decisions")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    STALENESS_FIELD_NUMBER: _ClassVar[int]
    STALENESS_NOTE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    WRITTEN_BY_AGENT_FIELD_NUMBER: _ClassVar[int]
    DECISIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    icon: str
    channel_id: str
    summary: str
    staleness: int
    staleness_note: str
    updated_at: _timestamp_pb2.Timestamp
    updated_by: str
    written_by_agent: bool
    decisions: int
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., icon: _Optional[str] = ..., channel_id: _Optional[str] = ..., summary: _Optional[str] = ..., staleness: _Optional[int] = ..., staleness_note: _Optional[str] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_by: _Optional[str] = ..., written_by_agent: bool = ..., decisions: _Optional[int] = ...) -> None: ...

class ListCanvasesRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id", "stale_only")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    STALE_ONLY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    stale_only: bool
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., stale_only: bool = ...) -> None: ...

class ListCanvasesResponse(_message.Message):
    __slots__ = ("canvases",)
    CANVASES_FIELD_NUMBER: _ClassVar[int]
    canvases: _containers.RepeatedCompositeFieldContainer[CanvasSummary]
    def __init__(self, canvases: _Optional[_Iterable[_Union[CanvasSummary, _Mapping]]] = ...) -> None: ...

class GetCanvasRequest(_message.Message):
    __slots__ = ("workspace_id", "id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class GetCanvasResponse(_message.Message):
    __slots__ = ("canvas",)
    CANVAS_FIELD_NUMBER: _ClassVar[int]
    canvas: Canvas
    def __init__(self, canvas: _Optional[_Union[Canvas, _Mapping]] = ...) -> None: ...

class CreateCanvasRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id", "title", "icon", "blocks", "sources")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    title: str
    icon: str
    blocks: _containers.RepeatedCompositeFieldContainer[Block]
    sources: _containers.RepeatedCompositeFieldContainer[Source]
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., title: _Optional[str] = ..., icon: _Optional[str] = ..., blocks: _Optional[_Iterable[_Union[Block, _Mapping]]] = ..., sources: _Optional[_Iterable[_Union[Source, _Mapping]]] = ...) -> None: ...

class CreateCanvasResponse(_message.Message):
    __slots__ = ("canvas",)
    CANVAS_FIELD_NUMBER: _ClassVar[int]
    canvas: Canvas
    def __init__(self, canvas: _Optional[_Union[Canvas, _Mapping]] = ...) -> None: ...

class UpdateCanvasRequest(_message.Message):
    __slots__ = ("workspace_id", "id", "title", "icon", "blocks", "set_blocks", "sources", "set_sources", "base_version")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    SET_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    SET_SOURCES_FIELD_NUMBER: _ClassVar[int]
    BASE_VERSION_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    title: str
    icon: str
    blocks: _containers.RepeatedCompositeFieldContainer[Block]
    set_blocks: bool
    sources: _containers.RepeatedCompositeFieldContainer[Source]
    set_sources: bool
    base_version: int
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ..., title: _Optional[str] = ..., icon: _Optional[str] = ..., blocks: _Optional[_Iterable[_Union[Block, _Mapping]]] = ..., set_blocks: bool = ..., sources: _Optional[_Iterable[_Union[Source, _Mapping]]] = ..., set_sources: bool = ..., base_version: _Optional[int] = ...) -> None: ...

class UpdateCanvasResponse(_message.Message):
    __slots__ = ("canvas",)
    CANVAS_FIELD_NUMBER: _ClassVar[int]
    canvas: Canvas
    def __init__(self, canvas: _Optional[_Union[Canvas, _Mapping]] = ...) -> None: ...

class DeleteCanvasRequest(_message.Message):
    __slots__ = ("workspace_id", "id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteCanvasResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WriteFromThreadRequest(_message.Message):
    __slots__ = ("workspace_id", "thread_root_id", "title")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    thread_root_id: str
    title: str
    def __init__(self, workspace_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class WriteFromThreadResponse(_message.Message):
    __slots__ = ("canvas",)
    CANVAS_FIELD_NUMBER: _ClassVar[int]
    canvas: Canvas
    def __init__(self, canvas: _Optional[_Union[Canvas, _Mapping]] = ...) -> None: ...

class AskRequest(_message.Message):
    __slots__ = ("workspace_id", "question", "limit")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    question: str
    limit: int
    def __init__(self, workspace_id: _Optional[str] = ..., question: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class Answer(_message.Message):
    __slots__ = ("canvas_id", "title", "icon", "passage", "block_id", "score")
    CANVAS_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    PASSAGE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    canvas_id: str
    title: str
    icon: str
    passage: str
    block_id: str
    score: float
    def __init__(self, canvas_id: _Optional[str] = ..., title: _Optional[str] = ..., icon: _Optional[str] = ..., passage: _Optional[str] = ..., block_id: _Optional[str] = ..., score: _Optional[float] = ...) -> None: ...

class AskResponse(_message.Message):
    __slots__ = ("answers", "summary")
    ANSWERS_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    answers: _containers.RepeatedCompositeFieldContainer[Answer]
    summary: str
    def __init__(self, answers: _Optional[_Iterable[_Union[Answer, _Mapping]]] = ..., summary: _Optional[str] = ...) -> None: ...
