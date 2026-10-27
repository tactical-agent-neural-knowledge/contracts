from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROLE_UNSPECIFIED: _ClassVar[Role]
    ROLE_VIEW: _ClassVar[Role]
    ROLE_EDIT: _ClassVar[Role]
    ROLE_MANAGE: _ClassVar[Role]

class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SOURCE_UNSPECIFIED: _ClassVar[Source]
    SOURCE_OWNER: _ClassVar[Source]
    SOURCE_ADMIN: _ClassVar[Source]
    SOURCE_TREAD: _ClassVar[Source]
    SOURCE_INVITED: _ClassVar[Source]
ROLE_UNSPECIFIED: Role
ROLE_VIEW: Role
ROLE_EDIT: Role
ROLE_MANAGE: Role
SOURCE_UNSPECIFIED: Source
SOURCE_OWNER: Source
SOURCE_ADMIN: Source
SOURCE_TREAD: Source
SOURCE_INVITED: Source

class Grant(_message.Message):
    __slots__ = ("user_id", "role", "source", "removable", "role_editable", "granted_by")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    REMOVABLE_FIELD_NUMBER: _ClassVar[int]
    ROLE_EDITABLE_FIELD_NUMBER: _ClassVar[int]
    GRANTED_BY_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    role: Role
    source: Source
    removable: bool
    role_editable: bool
    granted_by: str
    def __init__(self, user_id: _Optional[str] = ..., role: _Optional[_Union[Role, str]] = ..., source: _Optional[_Union[Source, str]] = ..., removable: bool = ..., role_editable: bool = ..., granted_by: _Optional[str] = ...) -> None: ...

class Invite(_message.Message):
    __slots__ = ("user_id", "role")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    role: Role
    def __init__(self, user_id: _Optional[str] = ..., role: _Optional[_Union[Role, str]] = ...) -> None: ...
