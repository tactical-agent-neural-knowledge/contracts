from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrincipalKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRINCIPAL_KIND_UNSPECIFIED: _ClassVar[PrincipalKind]
    PRINCIPAL_KIND_USER: _ClassVar[PrincipalKind]
    PRINCIPAL_KIND_BOT: _ClassVar[PrincipalKind]
    PRINCIPAL_KIND_AGENT: _ClassVar[PrincipalKind]
PRINCIPAL_KIND_UNSPECIFIED: PrincipalKind
PRINCIPAL_KIND_USER: PrincipalKind
PRINCIPAL_KIND_BOT: PrincipalKind
PRINCIPAL_KIND_AGENT: PrincipalKind

class Principal(_message.Message):
    __slots__ = ("id", "kind", "display_name", "avatar_url", "email", "avatar_file_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    kind: PrincipalKind
    display_name: str
    avatar_url: str
    email: str
    avatar_file_id: str
    def __init__(self, id: _Optional[str] = ..., kind: _Optional[_Union[PrincipalKind, str]] = ..., display_name: _Optional[str] = ..., avatar_url: _Optional[str] = ..., email: _Optional[str] = ..., avatar_file_id: _Optional[str] = ...) -> None: ...

class StartMagicLinkRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class StartMagicLinkResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CompleteMagicLinkRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class CompleteMagicLinkResponse(_message.Message):
    __slots__ = ("me", "access_token", "refresh_token", "access_expires_at")
    ME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    me: Principal
    access_token: str
    refresh_token: str
    access_expires_at: _timestamp_pb2.Timestamp
    def __init__(self, me: _Optional[_Union[Principal, _Mapping]] = ..., access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ..., access_expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ExchangeCodeRequest(_message.Message):
    __slots__ = ("provider", "code", "code_verifier", "redirect_uri")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CODE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    provider: str
    code: str
    code_verifier: str
    redirect_uri: str
    def __init__(self, provider: _Optional[str] = ..., code: _Optional[str] = ..., code_verifier: _Optional[str] = ..., redirect_uri: _Optional[str] = ...) -> None: ...

class ExchangeCodeResponse(_message.Message):
    __slots__ = ("me", "access_token", "refresh_token", "access_expires_at")
    ME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    me: Principal
    access_token: str
    refresh_token: str
    access_expires_at: _timestamp_pb2.Timestamp
    def __init__(self, me: _Optional[_Union[Principal, _Mapping]] = ..., access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ..., access_expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RefreshRequest(_message.Message):
    __slots__ = ("refresh_token",)
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    refresh_token: str
    def __init__(self, refresh_token: _Optional[str] = ...) -> None: ...

class RefreshResponse(_message.Message):
    __slots__ = ("access_token", "refresh_token", "access_expires_at")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str
    access_expires_at: _timestamp_pb2.Timestamp
    def __init__(self, access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ..., access_expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class LogoutRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LogoutResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MintGatewayTokenRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MintGatewayTokenResponse(_message.Message):
    __slots__ = ("token", "expires_at")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    token: str
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, token: _Optional[str] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetMeRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMeResponse(_message.Message):
    __slots__ = ("me",)
    ME_FIELD_NUMBER: _ClassVar[int]
    me: Principal
    def __init__(self, me: _Optional[_Union[Principal, _Mapping]] = ...) -> None: ...
