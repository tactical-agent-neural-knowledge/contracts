from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnvVar(_message.Message):
    __slots__ = ("name", "value", "secret", "is_set", "updated_at", "updated_by")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    IS_SET_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    secret: bool
    is_set: bool
    updated_at: _timestamp_pb2.Timestamp
    updated_by: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., secret: bool = ..., is_set: bool = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_by: _Optional[str] = ...) -> None: ...

class ListEnvVarsRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListEnvVarsResponse(_message.Message):
    __slots__ = ("vars",)
    VARS_FIELD_NUMBER: _ClassVar[int]
    vars: _containers.RepeatedCompositeFieldContainer[EnvVar]
    def __init__(self, vars: _Optional[_Iterable[_Union[EnvVar, _Mapping]]] = ...) -> None: ...

class PutEnvVarRequest(_message.Message):
    __slots__ = ("workspace_id", "name", "value", "secret", "create_only")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    CREATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    name: str
    value: str
    secret: bool
    create_only: bool
    def __init__(self, workspace_id: _Optional[str] = ..., name: _Optional[str] = ..., value: _Optional[str] = ..., secret: bool = ..., create_only: bool = ...) -> None: ...

class PutEnvVarResponse(_message.Message):
    __slots__ = ("var", "created")
    VAR_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    var: EnvVar
    created: bool
    def __init__(self, var: _Optional[_Union[EnvVar, _Mapping]] = ..., created: bool = ...) -> None: ...

class DeleteEnvVarRequest(_message.Message):
    __slots__ = ("workspace_id", "name")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    name: str
    def __init__(self, workspace_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class DeleteEnvVarResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
