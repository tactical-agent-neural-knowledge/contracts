from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class App(_message.Message):
    __slots__ = ("id", "name", "description", "logo_url", "url", "maker")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    MAKER_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    logo_url: str
    url: str
    maker: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., logo_url: _Optional[str] = ..., url: _Optional[str] = ..., maker: _Optional[str] = ...) -> None: ...

class Tool(_message.Message):
    __slots__ = ("name", "description", "input_schema_json", "offer")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    input_schema_json: str
    offer: Offer
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., input_schema_json: _Optional[str] = ..., offer: _Optional[_Union[Offer, _Mapping]] = ...) -> None: ...

class Offer(_message.Message):
    __slots__ = ("text", "needs", "title")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    NEEDS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    text: str
    needs: _containers.RepeatedScalarFieldContainer[str]
    title: str
    def __init__(self, text: _Optional[str] = ..., needs: _Optional[_Iterable[str]] = ..., title: _Optional[str] = ...) -> None: ...

class Mark(_message.Message):
    __slots__ = ("kind", "bearing", "label", "detail", "elevation", "x", "y", "w", "h")
    KIND_FIELD_NUMBER: _ClassVar[int]
    BEARING_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    ELEVATION_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    H_FIELD_NUMBER: _ClassVar[int]
    kind: str
    bearing: float
    label: str
    detail: str
    elevation: float
    x: float
    y: float
    w: float
    h: float
    def __init__(self, kind: _Optional[str] = ..., bearing: _Optional[float] = ..., label: _Optional[str] = ..., detail: _Optional[str] = ..., elevation: _Optional[float] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., w: _Optional[float] = ..., h: _Optional[float] = ...) -> None: ...

class Source(_message.Message):
    __slots__ = ("title", "url")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    title: str
    url: str
    def __init__(self, title: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class ListAppsRequest(_message.Message):
    __slots__ = ("query",)
    QUERY_FIELD_NUMBER: _ClassVar[int]
    query: str
    def __init__(self, query: _Optional[str] = ...) -> None: ...

class ListAppsResponse(_message.Message):
    __slots__ = ("apps",)
    APPS_FIELD_NUMBER: _ClassVar[int]
    apps: _containers.RepeatedCompositeFieldContainer[App]
    def __init__(self, apps: _Optional[_Iterable[_Union[App, _Mapping]]] = ...) -> None: ...

class GetToolsRequest(_message.Message):
    __slots__ = ("app_id",)
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    def __init__(self, app_id: _Optional[str] = ...) -> None: ...

class GetToolsResponse(_message.Message):
    __slots__ = ("app", "tools")
    APP_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    app: App
    tools: _containers.RepeatedCompositeFieldContainer[Tool]
    def __init__(self, app: _Optional[_Union[App, _Mapping]] = ..., tools: _Optional[_Iterable[_Union[Tool, _Mapping]]] = ...) -> None: ...

class CallToolRequest(_message.Message):
    __slots__ = ("app_id", "tool", "arguments_json")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_JSON_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    tool: str
    arguments_json: str
    def __init__(self, app_id: _Optional[str] = ..., tool: _Optional[str] = ..., arguments_json: _Optional[str] = ...) -> None: ...

class CallToolResponse(_message.Message):
    __slots__ = ("text", "sources", "is_error", "marks")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    IS_ERROR_FIELD_NUMBER: _ClassVar[int]
    MARKS_FIELD_NUMBER: _ClassVar[int]
    text: str
    sources: _containers.RepeatedCompositeFieldContainer[Source]
    is_error: bool
    marks: _containers.RepeatedCompositeFieldContainer[Mark]
    def __init__(self, text: _Optional[str] = ..., sources: _Optional[_Iterable[_Union[Source, _Mapping]]] = ..., is_error: bool = ..., marks: _Optional[_Iterable[_Union[Mark, _Mapping]]] = ...) -> None: ...
