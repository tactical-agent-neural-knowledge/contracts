from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tank.ai.v1 import ai_pb2 as _ai_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATE_UNSPECIFIED: _ClassVar[State]
    STATE_IDENTIFYING: _ClassVar[State]
    STATE_READING: _ClassVar[State]
    STATE_CLOSED: _ClassVar[State]
STATE_UNSPECIFIED: State
STATE_IDENTIFYING: State
STATE_READING: State
STATE_CLOSED: State

class Device(_message.Message):
    __slots__ = ("transport", "name", "manufacturer", "model", "firmware", "services", "company_id")
    TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    transport: str
    name: str
    manufacturer: str
    model: str
    firmware: str
    services: _containers.RepeatedCompositeFieldContainer[Service]
    company_id: int
    def __init__(self, transport: _Optional[str] = ..., name: _Optional[str] = ..., manufacturer: _Optional[str] = ..., model: _Optional[str] = ..., firmware: _Optional[str] = ..., services: _Optional[_Iterable[_Union[Service, _Mapping]]] = ..., company_id: _Optional[int] = ...) -> None: ...

class Service(_message.Message):
    __slots__ = ("uuid", "characteristics")
    UUID_FIELD_NUMBER: _ClassVar[int]
    CHARACTERISTICS_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    characteristics: _containers.RepeatedCompositeFieldContainer[Characteristic]
    def __init__(self, uuid: _Optional[str] = ..., characteristics: _Optional[_Iterable[_Union[Characteristic, _Mapping]]] = ...) -> None: ...

class Characteristic(_message.Message):
    __slots__ = ("uuid", "properties", "value", "name", "declared")
    UUID_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DECLARED_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    properties: _containers.RepeatedScalarFieldContainer[str]
    value: bytes
    name: str
    declared: _containers.RepeatedCompositeFieldContainer[DeclaredField]
    def __init__(self, uuid: _Optional[str] = ..., properties: _Optional[_Iterable[str]] = ..., value: _Optional[bytes] = ..., name: _Optional[str] = ..., declared: _Optional[_Iterable[_Union[DeclaredField, _Mapping]]] = ...) -> None: ...

class DeclaredField(_message.Message):
    __slots__ = ("name", "unit")
    NAME_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    name: str
    unit: str
    def __init__(self, name: _Optional[str] = ..., unit: _Optional[str] = ...) -> None: ...

class Frame(_message.Message):
    __slots__ = ("at_ms", "jpeg")
    AT_MS_FIELD_NUMBER: _ClassVar[int]
    JPEG_FIELD_NUMBER: _ClassVar[int]
    at_ms: int
    jpeg: bytes
    def __init__(self, at_ms: _Optional[int] = ..., jpeg: _Optional[bytes] = ...) -> None: ...

class Reading(_message.Message):
    __slots__ = ("characteristic_uuid", "at_ms", "value")
    CHARACTERISTIC_UUID_FIELD_NUMBER: _ClassVar[int]
    AT_MS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    characteristic_uuid: str
    at_ms: int
    value: bytes
    def __init__(self, characteristic_uuid: _Optional[str] = ..., at_ms: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...

class Point(_message.Message):
    __slots__ = ("field", "at_ms", "value")
    FIELD_FIELD_NUMBER: _ClassVar[int]
    AT_MS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    field: str
    at_ms: int
    value: float
    def __init__(self, field: _Optional[str] = ..., at_ms: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...

class Field(_message.Message):
    __slots__ = ("key", "label", "unit", "characteristic_uuid", "source")
    KEY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    CHARACTERISTIC_UUID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    key: str
    label: str
    unit: str
    characteristic_uuid: str
    source: str
    def __init__(self, key: _Optional[str] = ..., label: _Optional[str] = ..., unit: _Optional[str] = ..., characteristic_uuid: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...

class FieldStats(_message.Message):
    __slots__ = ("field", "last", "avg_30s", "avg_5m", "avg_session", "min", "max", "trend_per_min", "samples")
    FIELD_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    AVG_30S_FIELD_NUMBER: _ClassVar[int]
    AVG_5M_FIELD_NUMBER: _ClassVar[int]
    AVG_SESSION_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    TREND_PER_MIN_FIELD_NUMBER: _ClassVar[int]
    SAMPLES_FIELD_NUMBER: _ClassVar[int]
    field: str
    last: float
    avg_30s: float
    avg_5m: float
    avg_session: float
    min: float
    max: float
    trend_per_min: float
    samples: int
    def __init__(self, field: _Optional[str] = ..., last: _Optional[float] = ..., avg_30s: _Optional[float] = ..., avg_5m: _Optional[float] = ..., avg_session: _Optional[float] = ..., min: _Optional[float] = ..., max: _Optional[float] = ..., trend_per_min: _Optional[float] = ..., samples: _Optional[int] = ...) -> None: ...

class Session(_message.Message):
    __slots__ = ("id", "conversation_id", "device", "state", "identity", "fields", "subscribe", "opened_at", "closed_at", "feedback_rule", "view", "view_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    CLOSED_AT_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_RULE_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    VIEW_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    conversation_id: str
    device: Device
    state: State
    identity: str
    fields: _containers.RepeatedCompositeFieldContainer[Field]
    subscribe: _containers.RepeatedScalarFieldContainer[str]
    opened_at: _timestamp_pb2.Timestamp
    closed_at: _timestamp_pb2.Timestamp
    feedback_rule: str
    view: str
    view_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., conversation_id: _Optional[str] = ..., device: _Optional[_Union[Device, _Mapping]] = ..., state: _Optional[_Union[State, str]] = ..., identity: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[Field, _Mapping]]] = ..., subscribe: _Optional[_Iterable[str]] = ..., opened_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., closed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., feedback_rule: _Optional[str] = ..., view: _Optional[str] = ..., view_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListCatalogServicesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCatalogServicesResponse(_message.Message):
    __slots__ = ("uuids",)
    UUIDS_FIELD_NUMBER: _ClassVar[int]
    uuids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, uuids: _Optional[_Iterable[str]] = ...) -> None: ...

class OpenSessionRequest(_message.Message):
    __slots__ = ("conversation_id", "device")
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    device: Device
    def __init__(self, conversation_id: _Optional[str] = ..., device: _Optional[_Union[Device, _Mapping]] = ...) -> None: ...

class OpenSessionResponse(_message.Message):
    __slots__ = ("session",)
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: Session
    def __init__(self, session: _Optional[_Union[Session, _Mapping]] = ...) -> None: ...

class PushReadingsRequest(_message.Message):
    __slots__ = ("session_id", "readings", "frame")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    READINGS_FIELD_NUMBER: _ClassVar[int]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    readings: _containers.RepeatedCompositeFieldContainer[Reading]
    frame: Frame
    def __init__(self, session_id: _Optional[str] = ..., readings: _Optional[_Iterable[_Union[Reading, _Mapping]]] = ..., frame: _Optional[_Union[Frame, _Mapping]] = ...) -> None: ...

class PushReadingsResponse(_message.Message):
    __slots__ = ("points", "session", "stats", "messages")
    POINTS_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    points: _containers.RepeatedCompositeFieldContainer[Point]
    session: Session
    stats: _containers.RepeatedCompositeFieldContainer[FieldStats]
    messages: _containers.RepeatedCompositeFieldContainer[_ai_pb2.Message]
    def __init__(self, points: _Optional[_Iterable[_Union[Point, _Mapping]]] = ..., session: _Optional[_Union[Session, _Mapping]] = ..., stats: _Optional[_Iterable[_Union[FieldStats, _Mapping]]] = ..., messages: _Optional[_Iterable[_Union[_ai_pb2.Message, _Mapping]]] = ...) -> None: ...

class GetSessionRequest(_message.Message):
    __slots__ = ("session_id", "since_ms")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SINCE_MS_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    since_ms: int
    def __init__(self, session_id: _Optional[str] = ..., since_ms: _Optional[int] = ...) -> None: ...

class GetSessionResponse(_message.Message):
    __slots__ = ("session", "points", "stats")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    session: Session
    points: _containers.RepeatedCompositeFieldContainer[Point]
    stats: _containers.RepeatedCompositeFieldContainer[FieldStats]
    def __init__(self, session: _Optional[_Union[Session, _Mapping]] = ..., points: _Optional[_Iterable[_Union[Point, _Mapping]]] = ..., stats: _Optional[_Iterable[_Union[FieldStats, _Mapping]]] = ...) -> None: ...

class ListSessionsRequest(_message.Message):
    __slots__ = ("conversation_id",)
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    def __init__(self, conversation_id: _Optional[str] = ...) -> None: ...

class ListSessionsResponse(_message.Message):
    __slots__ = ("sessions",)
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[Session]
    def __init__(self, sessions: _Optional[_Iterable[_Union[Session, _Mapping]]] = ...) -> None: ...

class CloseSessionRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class CloseSessionResponse(_message.Message):
    __slots__ = ("session", "summary")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    session: Session
    summary: _ai_pb2.Message
    def __init__(self, session: _Optional[_Union[Session, _Mapping]] = ..., summary: _Optional[_Union[_ai_pb2.Message, _Mapping]] = ...) -> None: ...
