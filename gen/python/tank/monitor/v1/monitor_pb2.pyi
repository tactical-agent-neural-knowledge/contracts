from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WIDGET_KIND_UNSPECIFIED: _ClassVar[WidgetKind]
    WIDGET_KIND_NUMBER: _ClassVar[WidgetKind]
    WIDGET_KIND_LINE: _ClassVar[WidgetKind]
    WIDGET_KIND_BAR: _ClassVar[WidgetKind]
    WIDGET_KIND_STATUS: _ClassVar[WidgetKind]
    WIDGET_KIND_TEXT: _ClassVar[WidgetKind]
    WIDGET_KIND_TABLE: _ClassVar[WidgetKind]

class SourceKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SOURCE_KIND_UNSPECIFIED: _ClassVar[SourceKind]
    SOURCE_KIND_WEBHOOK: _ClassVar[SourceKind]
    SOURCE_KIND_PROBE: _ClassVar[SourceKind]
    SOURCE_KIND_INTERNAL: _ClassVar[SourceKind]

class Health(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HEALTH_UNSPECIFIED: _ClassVar[Health]
    HEALTH_OK: _ClassVar[Health]
    HEALTH_WARN: _ClassVar[Health]
    HEALTH_CRIT: _ClassVar[Health]
    HEALTH_UNKNOWN: _ClassVar[Health]
WIDGET_KIND_UNSPECIFIED: WidgetKind
WIDGET_KIND_NUMBER: WidgetKind
WIDGET_KIND_LINE: WidgetKind
WIDGET_KIND_BAR: WidgetKind
WIDGET_KIND_STATUS: WidgetKind
WIDGET_KIND_TEXT: WidgetKind
WIDGET_KIND_TABLE: WidgetKind
SOURCE_KIND_UNSPECIFIED: SourceKind
SOURCE_KIND_WEBHOOK: SourceKind
SOURCE_KIND_PROBE: SourceKind
SOURCE_KIND_INTERNAL: SourceKind
HEALTH_UNSPECIFIED: Health
HEALTH_OK: Health
HEALTH_WARN: Health
HEALTH_CRIT: Health
HEALTH_UNKNOWN: Health

class Point(_message.Message):
    __slots__ = ("at", "value", "text", "labels_json", "url")
    AT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    LABELS_JSON_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    at: _timestamp_pb2.Timestamp
    value: float
    text: str
    labels_json: str
    url: str
    def __init__(self, at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., value: _Optional[float] = ..., text: _Optional[str] = ..., labels_json: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class Position(_message.Message):
    __slots__ = ("x", "y", "w", "h")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    H_FIELD_NUMBER: _ClassVar[int]
    x: int
    y: int
    w: int
    h: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., w: _Optional[int] = ..., h: _Optional[int] = ...) -> None: ...

class Thresholds(_message.Message):
    __slots__ = ("warn_at", "crit_at", "higher_is_bad")
    WARN_AT_FIELD_NUMBER: _ClassVar[int]
    CRIT_AT_FIELD_NUMBER: _ClassVar[int]
    HIGHER_IS_BAD_FIELD_NUMBER: _ClassVar[int]
    warn_at: float
    crit_at: float
    higher_is_bad: bool
    def __init__(self, warn_at: _Optional[float] = ..., crit_at: _Optional[float] = ..., higher_is_bad: bool = ...) -> None: ...

class Widget(_message.Message):
    __slots__ = ("id", "channel_id", "kind", "title", "unit", "source_id", "mapping", "thresholds", "position", "latest", "health", "message_id", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    MAPPING_FIELD_NUMBER: _ClassVar[int]
    THRESHOLDS_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    LATEST_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    channel_id: str
    kind: WidgetKind
    title: str
    unit: str
    source_id: str
    mapping: str
    thresholds: Thresholds
    position: Position
    latest: Point
    health: Health
    message_id: str
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., channel_id: _Optional[str] = ..., kind: _Optional[_Union[WidgetKind, str]] = ..., title: _Optional[str] = ..., unit: _Optional[str] = ..., source_id: _Optional[str] = ..., mapping: _Optional[str] = ..., thresholds: _Optional[_Union[Thresholds, _Mapping]] = ..., position: _Optional[_Union[Position, _Mapping]] = ..., latest: _Optional[_Union[Point, _Mapping]] = ..., health: _Optional[_Union[Health, str]] = ..., message_id: _Optional[str] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Schedule(_message.Message):
    __slots__ = ("interval_seconds", "cron")
    INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    CRON_FIELD_NUMBER: _ClassVar[int]
    interval_seconds: int
    cron: str
    def __init__(self, interval_seconds: _Optional[int] = ..., cron: _Optional[str] = ...) -> None: ...

class Source(_message.Message):
    __slots__ = ("id", "channel_id", "kind", "name", "schedule", "config_json", "ingest_path", "enabled", "last_run_at", "last_error", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    INGEST_PATH_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    channel_id: str
    kind: SourceKind
    name: str
    schedule: Schedule
    config_json: str
    ingest_path: str
    enabled: bool
    last_run_at: _timestamp_pb2.Timestamp
    last_error: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., channel_id: _Optional[str] = ..., kind: _Optional[_Union[SourceKind, str]] = ..., name: _Optional[str] = ..., schedule: _Optional[_Union[Schedule, _Mapping]] = ..., config_json: _Optional[str] = ..., ingest_path: _Optional[str] = ..., enabled: bool = ..., last_run_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_error: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListWidgetsRequest(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class ListWidgetsResponse(_message.Message):
    __slots__ = ("widgets", "sources")
    WIDGETS_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    widgets: _containers.RepeatedCompositeFieldContainer[Widget]
    sources: _containers.RepeatedCompositeFieldContainer[Source]
    def __init__(self, widgets: _Optional[_Iterable[_Union[Widget, _Mapping]]] = ..., sources: _Optional[_Iterable[_Union[Source, _Mapping]]] = ...) -> None: ...

class UpsertWidgetRequest(_message.Message):
    __slots__ = ("id", "channel_id", "kind", "title", "unit", "source_id", "mapping", "thresholds", "position")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    MAPPING_FIELD_NUMBER: _ClassVar[int]
    THRESHOLDS_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    id: str
    channel_id: str
    kind: WidgetKind
    title: str
    unit: str
    source_id: str
    mapping: str
    thresholds: Thresholds
    position: Position
    def __init__(self, id: _Optional[str] = ..., channel_id: _Optional[str] = ..., kind: _Optional[_Union[WidgetKind, str]] = ..., title: _Optional[str] = ..., unit: _Optional[str] = ..., source_id: _Optional[str] = ..., mapping: _Optional[str] = ..., thresholds: _Optional[_Union[Thresholds, _Mapping]] = ..., position: _Optional[_Union[Position, _Mapping]] = ...) -> None: ...

class UpsertWidgetResponse(_message.Message):
    __slots__ = ("widget",)
    WIDGET_FIELD_NUMBER: _ClassVar[int]
    widget: Widget
    def __init__(self, widget: _Optional[_Union[Widget, _Mapping]] = ...) -> None: ...

class DeleteWidgetRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteWidgetResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSeriesRequest(_message.Message):
    __slots__ = ("widget_id", "since", "until", "step_seconds")
    WIDGET_ID_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    STEP_SECONDS_FIELD_NUMBER: _ClassVar[int]
    widget_id: str
    since: _timestamp_pb2.Timestamp
    until: _timestamp_pb2.Timestamp
    step_seconds: int
    def __init__(self, widget_id: _Optional[str] = ..., since: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., step_seconds: _Optional[int] = ...) -> None: ...

class GetSeriesResponse(_message.Message):
    __slots__ = ("points",)
    POINTS_FIELD_NUMBER: _ClassVar[int]
    points: _containers.RepeatedCompositeFieldContainer[Point]
    def __init__(self, points: _Optional[_Iterable[_Union[Point, _Mapping]]] = ...) -> None: ...

class CreateSourceRequest(_message.Message):
    __slots__ = ("channel_id", "kind", "name", "schedule", "config_json")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    kind: SourceKind
    name: str
    schedule: Schedule
    config_json: str
    def __init__(self, channel_id: _Optional[str] = ..., kind: _Optional[_Union[SourceKind, str]] = ..., name: _Optional[str] = ..., schedule: _Optional[_Union[Schedule, _Mapping]] = ..., config_json: _Optional[str] = ...) -> None: ...

class CreateSourceResponse(_message.Message):
    __slots__ = ("source", "ingest_url")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    INGEST_URL_FIELD_NUMBER: _ClassVar[int]
    source: Source
    ingest_url: str
    def __init__(self, source: _Optional[_Union[Source, _Mapping]] = ..., ingest_url: _Optional[str] = ...) -> None: ...

class UpdateSourceRequest(_message.Message):
    __slots__ = ("id", "name", "schedule", "config_json", "enabled")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    schedule: Schedule
    config_json: str
    enabled: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., schedule: _Optional[_Union[Schedule, _Mapping]] = ..., config_json: _Optional[str] = ..., enabled: bool = ...) -> None: ...

class UpdateSourceResponse(_message.Message):
    __slots__ = ("source",)
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    source: Source
    def __init__(self, source: _Optional[_Union[Source, _Mapping]] = ...) -> None: ...

class DeleteSourceRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteSourceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RotateSourceTokenRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class RotateSourceTokenResponse(_message.Message):
    __slots__ = ("ingest_url",)
    INGEST_URL_FIELD_NUMBER: _ClassVar[int]
    ingest_url: str
    def __init__(self, ingest_url: _Optional[str] = ...) -> None: ...

class PushPointsRequest(_message.Message):
    __slots__ = ("channel_id", "points")
    class WidgetPoint(_message.Message):
        __slots__ = ("widget_id", "point")
        WIDGET_ID_FIELD_NUMBER: _ClassVar[int]
        POINT_FIELD_NUMBER: _ClassVar[int]
        widget_id: str
        point: Point
        def __init__(self, widget_id: _Optional[str] = ..., point: _Optional[_Union[Point, _Mapping]] = ...) -> None: ...
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    points: _containers.RepeatedCompositeFieldContainer[PushPointsRequest.WidgetPoint]
    def __init__(self, channel_id: _Optional[str] = ..., points: _Optional[_Iterable[_Union[PushPointsRequest.WidgetPoint, _Mapping]]] = ...) -> None: ...

class PushPointsResponse(_message.Message):
    __slots__ = ("widgets",)
    WIDGETS_FIELD_NUMBER: _ClassVar[int]
    widgets: _containers.RepeatedCompositeFieldContainer[Widget]
    def __init__(self, widgets: _Optional[_Iterable[_Union[Widget, _Mapping]]] = ...) -> None: ...
