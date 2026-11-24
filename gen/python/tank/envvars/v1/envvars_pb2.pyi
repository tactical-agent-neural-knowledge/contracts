from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnvVar(_message.Message):
    __slots__ = ("name", "value", "secret", "is_set", "updated_at", "updated_by", "preview_set", "preview_hosts", "preview_in_body")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    IS_SET_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_SET_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_HOSTS_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_IN_BODY_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    secret: bool
    is_set: bool
    updated_at: _timestamp_pb2.Timestamp
    updated_by: str
    preview_set: bool
    preview_hosts: _containers.RepeatedScalarFieldContainer[str]
    preview_in_body: bool
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., secret: bool = ..., is_set: bool = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_by: _Optional[str] = ..., preview_set: bool = ..., preview_hosts: _Optional[_Iterable[str]] = ..., preview_in_body: bool = ...) -> None: ...

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

class PutPreviewValueRequest(_message.Message):
    __slots__ = ("workspace_id", "name", "value", "hosts", "in_body")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    IN_BODY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    name: str
    value: str
    hosts: _containers.RepeatedScalarFieldContainer[str]
    in_body: bool
    def __init__(self, workspace_id: _Optional[str] = ..., name: _Optional[str] = ..., value: _Optional[str] = ..., hosts: _Optional[_Iterable[str]] = ..., in_body: bool = ...) -> None: ...

class PutPreviewValueResponse(_message.Message):
    __slots__ = ("var",)
    VAR_FIELD_NUMBER: _ClassVar[int]
    var: EnvVar
    def __init__(self, var: _Optional[_Union[EnvVar, _Mapping]] = ...) -> None: ...

class ClearPreviewValueRequest(_message.Message):
    __slots__ = ("workspace_id", "name")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    name: str
    def __init__(self, workspace_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ClearPreviewValueResponse(_message.Message):
    __slots__ = ("var",)
    VAR_FIELD_NUMBER: _ClassVar[int]
    var: EnvVar
    def __init__(self, var: _Optional[_Union[EnvVar, _Mapping]] = ...) -> None: ...
