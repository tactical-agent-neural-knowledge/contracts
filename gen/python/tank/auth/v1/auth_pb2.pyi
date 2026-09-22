from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrincipalKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRINCIPAL_KIND_UNSPECIFIED: _ClassVar[PrincipalKind]
    PRINCIPAL_KIND_USER: _ClassVar[PrincipalKind]
    PRINCIPAL_KIND_BOT: _ClassVar[PrincipalKind]
    PRINCIPAL_KIND_AGENT: _ClassVar[PrincipalKind]

class SsoProvider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SSO_PROVIDER_UNSPECIFIED: _ClassVar[SsoProvider]
    SSO_PROVIDER_OIDC: _ClassVar[SsoProvider]
    SSO_PROVIDER_SAML: _ClassVar[SsoProvider]
PRINCIPAL_KIND_UNSPECIFIED: PrincipalKind
PRINCIPAL_KIND_USER: PrincipalKind
PRINCIPAL_KIND_BOT: PrincipalKind
PRINCIPAL_KIND_AGENT: PrincipalKind
SSO_PROVIDER_UNSPECIFIED: SsoProvider
SSO_PROVIDER_OIDC: SsoProvider
SSO_PROVIDER_SAML: SsoProvider

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

class Identity(_message.Message):
    __slots__ = ("principal", "is_default", "added_at")
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    ADDED_AT_FIELD_NUMBER: _ClassVar[int]
    principal: Principal
    is_default: bool
    added_at: _timestamp_pb2.Timestamp
    def __init__(self, principal: _Optional[_Union[Principal, _Mapping]] = ..., is_default: bool = ..., added_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListIdentitiesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListIdentitiesResponse(_message.Message):
    __slots__ = ("identities",)
    IDENTITIES_FIELD_NUMBER: _ClassVar[int]
    identities: _containers.RepeatedCompositeFieldContainer[Identity]
    def __init__(self, identities: _Optional[_Iterable[_Union[Identity, _Mapping]]] = ...) -> None: ...

class SignOutIdentityRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class SignOutIdentityResponse(_message.Message):
    __slots__ = ("session_remains",)
    SESSION_REMAINS_FIELD_NUMBER: _ClassVar[int]
    session_remains: bool
    def __init__(self, session_remains: bool = ...) -> None: ...

class Session(_message.Message):
    __slots__ = ("id", "kind", "created_at", "expires_at", "user_agent", "ip", "current")
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    kind: str
    created_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    user_agent: str
    ip: str
    current: bool
    def __init__(self, id: _Optional[str] = ..., kind: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., user_agent: _Optional[str] = ..., ip: _Optional[str] = ..., current: bool = ...) -> None: ...

class ListSessionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSessionsResponse(_message.Message):
    __slots__ = ("sessions",)
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[Session]
    def __init__(self, sessions: _Optional[_Iterable[_Union[Session, _Mapping]]] = ...) -> None: ...

class RevokeSessionRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class RevokeSessionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AdminRevokeUserSessionsRequest(_message.Message):
    __slots__ = ("workspace_id", "user_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    user_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class AdminRevokeUserSessionsResponse(_message.Message):
    __slots__ = ("revoked",)
    REVOKED_FIELD_NUMBER: _ClassVar[int]
    revoked: int
    def __init__(self, revoked: _Optional[int] = ...) -> None: ...

class SsoConfig(_message.Message):
    __slots__ = ("workspace_id", "provider", "enabled", "issuer", "metadata_xml", "client_id", "client_secret_ref", "has_client_secret", "domain_claim", "enforce", "redirect_uri", "sp_entity_id", "sp_metadata_url", "acs_url", "updated_at")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    METADATA_XML_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_REF_FIELD_NUMBER: _ClassVar[int]
    HAS_CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_CLAIM_FIELD_NUMBER: _ClassVar[int]
    ENFORCE_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    SP_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    SP_METADATA_URL_FIELD_NUMBER: _ClassVar[int]
    ACS_URL_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    provider: SsoProvider
    enabled: bool
    issuer: str
    metadata_xml: str
    client_id: str
    client_secret_ref: str
    has_client_secret: bool
    domain_claim: str
    enforce: bool
    redirect_uri: str
    sp_entity_id: str
    sp_metadata_url: str
    acs_url: str
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, workspace_id: _Optional[str] = ..., provider: _Optional[_Union[SsoProvider, str]] = ..., enabled: bool = ..., issuer: _Optional[str] = ..., metadata_xml: _Optional[str] = ..., client_id: _Optional[str] = ..., client_secret_ref: _Optional[str] = ..., has_client_secret: bool = ..., domain_claim: _Optional[str] = ..., enforce: bool = ..., redirect_uri: _Optional[str] = ..., sp_entity_id: _Optional[str] = ..., sp_metadata_url: _Optional[str] = ..., acs_url: _Optional[str] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetSsoConfigRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class GetSsoConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: SsoConfig
    def __init__(self, config: _Optional[_Union[SsoConfig, _Mapping]] = ...) -> None: ...

class SetSsoConfigRequest(_message.Message):
    __slots__ = ("workspace_id", "provider", "enabled", "issuer", "metadata_xml", "client_id", "client_secret", "client_secret_ref", "domain_claim", "enforce")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    METADATA_XML_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_REF_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_CLAIM_FIELD_NUMBER: _ClassVar[int]
    ENFORCE_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    provider: SsoProvider
    enabled: bool
    issuer: str
    metadata_xml: str
    client_id: str
    client_secret: str
    client_secret_ref: str
    domain_claim: str
    enforce: bool
    def __init__(self, workspace_id: _Optional[str] = ..., provider: _Optional[_Union[SsoProvider, str]] = ..., enabled: bool = ..., issuer: _Optional[str] = ..., metadata_xml: _Optional[str] = ..., client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., client_secret_ref: _Optional[str] = ..., domain_claim: _Optional[str] = ..., enforce: bool = ...) -> None: ...

class SetSsoConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: SsoConfig
    def __init__(self, config: _Optional[_Union[SsoConfig, _Mapping]] = ...) -> None: ...

class StartSsoRequest(_message.Message):
    __slots__ = ("workspace_slug", "redirect_uri")
    WORKSPACE_SLUG_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    workspace_slug: str
    redirect_uri: str
    def __init__(self, workspace_slug: _Optional[str] = ..., redirect_uri: _Optional[str] = ...) -> None: ...

class StartSsoResponse(_message.Message):
    __slots__ = ("redirect_url", "state", "expires_at")
    REDIRECT_URL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    redirect_url: str
    state: str
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, redirect_url: _Optional[str] = ..., state: _Optional[str] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CompleteSsoRequest(_message.Message):
    __slots__ = ("state", "code", "saml_response")
    STATE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    SAML_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    state: str
    code: str
    saml_response: str
    def __init__(self, state: _Optional[str] = ..., code: _Optional[str] = ..., saml_response: _Optional[str] = ...) -> None: ...

class CompleteSsoResponse(_message.Message):
    __slots__ = ("me", "access_token", "refresh_token", "access_expires_at", "workspace_id")
    ME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    me: Principal
    access_token: str
    refresh_token: str
    access_expires_at: _timestamp_pb2.Timestamp
    workspace_id: str
    def __init__(self, me: _Optional[_Union[Principal, _Mapping]] = ..., access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ..., access_expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., workspace_id: _Optional[str] = ...) -> None: ...
