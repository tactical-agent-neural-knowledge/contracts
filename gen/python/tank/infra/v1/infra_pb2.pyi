from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Provider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROVIDER_UNSPECIFIED: _ClassVar[Provider]
    PROVIDER_AWS: _ClassVar[Provider]
    PROVIDER_GCP: _ClassVar[Provider]
    PROVIDER_AZURE: _ClassVar[Provider]
    PROVIDER_KUBERNETES: _ClassVar[Provider]
    PROVIDER_API: _ClassVar[Provider]
    PROVIDER_DATABASE: _ClassVar[Provider]

class DatabaseEngine(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATABASE_ENGINE_UNSPECIFIED: _ClassVar[DatabaseEngine]
    DATABASE_ENGINE_POSTGRES: _ClassVar[DatabaseEngine]

class ConnectionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONNECTION_STATE_UNSPECIFIED: _ClassVar[ConnectionState]
    CONNECTION_STATE_UNVERIFIED: _ClassVar[ConnectionState]
    CONNECTION_STATE_OK: _ClassVar[ConnectionState]
    CONNECTION_STATE_FAILING: _ClassVar[ConnectionState]

class KubeAuth(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KUBE_AUTH_UNSPECIFIED: _ClassVar[KubeAuth]
    KUBE_AUTH_OIDC: _ClassVar[KubeAuth]
    KUBE_AUTH_TOKEN: _ClassVar[KubeAuth]
PROVIDER_UNSPECIFIED: Provider
PROVIDER_AWS: Provider
PROVIDER_GCP: Provider
PROVIDER_AZURE: Provider
PROVIDER_KUBERNETES: Provider
PROVIDER_API: Provider
PROVIDER_DATABASE: Provider
DATABASE_ENGINE_UNSPECIFIED: DatabaseEngine
DATABASE_ENGINE_POSTGRES: DatabaseEngine
CONNECTION_STATE_UNSPECIFIED: ConnectionState
CONNECTION_STATE_UNVERIFIED: ConnectionState
CONNECTION_STATE_OK: ConnectionState
CONNECTION_STATE_FAILING: ConnectionState
KUBE_AUTH_UNSPECIFIED: KubeAuth
KUBE_AUTH_OIDC: KubeAuth
KUBE_AUTH_TOKEN: KubeAuth

class AwsConfig(_message.Message):
    __slots__ = ("role_arn", "external_id", "regions", "eks_clusters")
    ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    REGIONS_FIELD_NUMBER: _ClassVar[int]
    EKS_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    role_arn: str
    external_id: str
    regions: _containers.RepeatedScalarFieldContainer[str]
    eks_clusters: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, role_arn: _Optional[str] = ..., external_id: _Optional[str] = ..., regions: _Optional[_Iterable[str]] = ..., eks_clusters: _Optional[_Iterable[str]] = ...) -> None: ...

class GcpConfig(_message.Message):
    __slots__ = ("project_id", "project_number", "pool_id", "provider_id", "service_account", "gke_clusters")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    GKE_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    project_number: str
    pool_id: str
    provider_id: str
    service_account: str
    gke_clusters: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, project_id: _Optional[str] = ..., project_number: _Optional[str] = ..., pool_id: _Optional[str] = ..., provider_id: _Optional[str] = ..., service_account: _Optional[str] = ..., gke_clusters: _Optional[_Iterable[str]] = ...) -> None: ...

class AzureConfig(_message.Message):
    __slots__ = ("tenant_id", "client_id", "subscription_id", "aks_clusters")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    AKS_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    client_id: str
    subscription_id: str
    aks_clusters: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tenant_id: _Optional[str] = ..., client_id: _Optional[str] = ..., subscription_id: _Optional[str] = ..., aks_clusters: _Optional[_Iterable[str]] = ...) -> None: ...

class KubernetesConfig(_message.Message):
    __slots__ = ("server", "ca_data", "auth", "audience")
    SERVER_FIELD_NUMBER: _ClassVar[int]
    CA_DATA_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    server: str
    ca_data: str
    auth: KubeAuth
    audience: str
    def __init__(self, server: _Optional[str] = ..., ca_data: _Optional[str] = ..., auth: _Optional[_Union[KubeAuth, str]] = ..., audience: _Optional[str] = ...) -> None: ...

class ApiConfig(_message.Message):
    __slots__ = ("base_url", "allowed_hosts", "header_name", "header_prefix")
    BASE_URL_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_HOSTS_FIELD_NUMBER: _ClassVar[int]
    HEADER_NAME_FIELD_NUMBER: _ClassVar[int]
    HEADER_PREFIX_FIELD_NUMBER: _ClassVar[int]
    base_url: str
    allowed_hosts: _containers.RepeatedScalarFieldContainer[str]
    header_name: str
    header_prefix: str
    def __init__(self, base_url: _Optional[str] = ..., allowed_hosts: _Optional[_Iterable[str]] = ..., header_name: _Optional[str] = ..., header_prefix: _Optional[str] = ...) -> None: ...

class DatabaseConfig(_message.Message):
    __slots__ = ("engine", "host", "port", "database", "user", "ssl_mode")
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    SSL_MODE_FIELD_NUMBER: _ClassVar[int]
    engine: DatabaseEngine
    host: str
    port: int
    database: str
    user: str
    ssl_mode: str
    def __init__(self, engine: _Optional[_Union[DatabaseEngine, str]] = ..., host: _Optional[str] = ..., port: _Optional[int] = ..., database: _Optional[str] = ..., user: _Optional[str] = ..., ssl_mode: _Optional[str] = ...) -> None: ...

class Connection(_message.Message):
    __slots__ = ("id", "workspace_id", "name", "provider", "description", "aws", "gcp", "azure", "kubernetes", "api", "channel_ids", "via_relay", "relay_id", "state", "last_error", "last_checked_at", "created_by", "created_at", "updated_at", "subject", "has_secret", "database")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AWS_FIELD_NUMBER: _ClassVar[int]
    GCP_FIELD_NUMBER: _ClassVar[int]
    AZURE_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_FIELD_NUMBER: _ClassVar[int]
    API_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    VIA_RELAY_FIELD_NUMBER: _ClassVar[int]
    RELAY_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    LAST_CHECKED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    HAS_SECRET_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    name: str
    provider: Provider
    description: str
    aws: AwsConfig
    gcp: GcpConfig
    azure: AzureConfig
    kubernetes: KubernetesConfig
    api: ApiConfig
    channel_ids: _containers.RepeatedScalarFieldContainer[str]
    via_relay: bool
    relay_id: str
    state: ConnectionState
    last_error: str
    last_checked_at: _timestamp_pb2.Timestamp
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    subject: str
    has_secret: bool
    database: DatabaseConfig
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., name: _Optional[str] = ..., provider: _Optional[_Union[Provider, str]] = ..., description: _Optional[str] = ..., aws: _Optional[_Union[AwsConfig, _Mapping]] = ..., gcp: _Optional[_Union[GcpConfig, _Mapping]] = ..., azure: _Optional[_Union[AzureConfig, _Mapping]] = ..., kubernetes: _Optional[_Union[KubernetesConfig, _Mapping]] = ..., api: _Optional[_Union[ApiConfig, _Mapping]] = ..., channel_ids: _Optional[_Iterable[str]] = ..., via_relay: bool = ..., relay_id: _Optional[str] = ..., state: _Optional[_Union[ConnectionState, str]] = ..., last_error: _Optional[str] = ..., last_checked_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., subject: _Optional[str] = ..., has_secret: bool = ..., database: _Optional[_Union[DatabaseConfig, _Mapping]] = ...) -> None: ...

class SetupStep(_message.Message):
    __slots__ = ("title", "text", "code", "code_language", "download_name")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CODE_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_NAME_FIELD_NUMBER: _ClassVar[int]
    title: str
    text: str
    code: str
    code_language: str
    download_name: str
    def __init__(self, title: _Optional[str] = ..., text: _Optional[str] = ..., code: _Optional[str] = ..., code_language: _Optional[str] = ..., download_name: _Optional[str] = ...) -> None: ...

class Use(_message.Message):
    __slots__ = ("id", "connection_id", "connection_name", "run_id", "channel_id", "user_id", "kind", "command", "exit_code", "refused", "duration_ms", "output_bytes", "at")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    REFUSED_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_BYTES_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    connection_id: str
    connection_name: str
    run_id: str
    channel_id: str
    user_id: str
    kind: str
    command: str
    exit_code: int
    refused: str
    duration_ms: int
    output_bytes: int
    at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., connection_id: _Optional[str] = ..., connection_name: _Optional[str] = ..., run_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., user_id: _Optional[str] = ..., kind: _Optional[str] = ..., command: _Optional[str] = ..., exit_code: _Optional[int] = ..., refused: _Optional[str] = ..., duration_ms: _Optional[int] = ..., output_bytes: _Optional[int] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RunbookInput(_message.Message):
    __slots__ = ("name", "description", "required", "default_value", "options")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    required: bool
    default_value: str
    options: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., required: bool = ..., default_value: _Optional[str] = ..., options: _Optional[_Iterable[str]] = ...) -> None: ...

class Runbook(_message.Message):
    __slots__ = ("id", "workspace_id", "repo", "workflow", "ref", "name", "description", "inputs", "created_by", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    REPO_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_FIELD_NUMBER: _ClassVar[int]
    REF_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    repo: str
    workflow: str
    ref: str
    name: str
    description: str
    inputs: _containers.RepeatedCompositeFieldContainer[RunbookInput]
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., repo: _Optional[str] = ..., workflow: _Optional[str] = ..., ref: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., inputs: _Optional[_Iterable[_Union[RunbookInput, _Mapping]]] = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class WorkflowCandidate(_message.Message):
    __slots__ = ("repo", "workflow", "name", "inputs")
    REPO_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    repo: str
    workflow: str
    name: str
    inputs: _containers.RepeatedCompositeFieldContainer[RunbookInput]
    def __init__(self, repo: _Optional[str] = ..., workflow: _Optional[str] = ..., name: _Optional[str] = ..., inputs: _Optional[_Iterable[_Union[RunbookInput, _Mapping]]] = ...) -> None: ...

class Relay(_message.Message):
    __slots__ = ("id", "workspace_id", "name", "last_seen_at", "version", "created_at", "created_by")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    name: str
    last_seen_at: _timestamp_pb2.Timestamp
    version: str
    created_at: _timestamp_pb2.Timestamp
    created_by: str
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., name: _Optional[str] = ..., last_seen_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., version: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ...) -> None: ...

class ListConnectionsRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class ListConnectionsResponse(_message.Message):
    __slots__ = ("connections", "premium", "aws_principal", "oidc_issuer")
    CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    PREMIUM_FIELD_NUMBER: _ClassVar[int]
    AWS_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    OIDC_ISSUER_FIELD_NUMBER: _ClassVar[int]
    connections: _containers.RepeatedCompositeFieldContainer[Connection]
    premium: bool
    aws_principal: str
    oidc_issuer: str
    def __init__(self, connections: _Optional[_Iterable[_Union[Connection, _Mapping]]] = ..., premium: bool = ..., aws_principal: _Optional[str] = ..., oidc_issuer: _Optional[str] = ...) -> None: ...

class GetConnectionRequest(_message.Message):
    __slots__ = ("workspace_id", "id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class GetConnectionResponse(_message.Message):
    __slots__ = ("connection",)
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    connection: Connection
    def __init__(self, connection: _Optional[_Union[Connection, _Mapping]] = ...) -> None: ...

class CreateConnectionRequest(_message.Message):
    __slots__ = ("workspace_id", "connection", "secret", "requested_by")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    connection: Connection
    secret: str
    requested_by: str
    def __init__(self, workspace_id: _Optional[str] = ..., connection: _Optional[_Union[Connection, _Mapping]] = ..., secret: _Optional[str] = ..., requested_by: _Optional[str] = ...) -> None: ...

class CreateConnectionResponse(_message.Message):
    __slots__ = ("connection",)
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    connection: Connection
    def __init__(self, connection: _Optional[_Union[Connection, _Mapping]] = ...) -> None: ...

class UpdateConnectionRequest(_message.Message):
    __slots__ = ("workspace_id", "connection", "secret", "requested_by")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    connection: Connection
    secret: str
    requested_by: str
    def __init__(self, workspace_id: _Optional[str] = ..., connection: _Optional[_Union[Connection, _Mapping]] = ..., secret: _Optional[str] = ..., requested_by: _Optional[str] = ...) -> None: ...

class UpdateConnectionResponse(_message.Message):
    __slots__ = ("connection",)
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    connection: Connection
    def __init__(self, connection: _Optional[_Union[Connection, _Mapping]] = ...) -> None: ...

class DeleteConnectionRequest(_message.Message):
    __slots__ = ("workspace_id", "id", "requested_by")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    requested_by: str
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ..., requested_by: _Optional[str] = ...) -> None: ...

class DeleteConnectionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TestConnectionRequest(_message.Message):
    __slots__ = ("workspace_id", "id", "requested_by")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    requested_by: str
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ..., requested_by: _Optional[str] = ...) -> None: ...

class TestConnectionResponse(_message.Message):
    __slots__ = ("state", "detail", "output", "warning")
    STATE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    state: ConnectionState
    detail: str
    output: _containers.RepeatedScalarFieldContainer[str]
    warning: str
    def __init__(self, state: _Optional[_Union[ConnectionState, str]] = ..., detail: _Optional[str] = ..., output: _Optional[_Iterable[str]] = ..., warning: _Optional[str] = ...) -> None: ...

class GetSetupGuideRequest(_message.Message):
    __slots__ = ("workspace_id", "id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class GetSetupGuideResponse(_message.Message):
    __slots__ = ("steps",)
    STEPS_FIELD_NUMBER: _ClassVar[int]
    steps: _containers.RepeatedCompositeFieldContainer[SetupStep]
    def __init__(self, steps: _Optional[_Iterable[_Union[SetupStep, _Mapping]]] = ...) -> None: ...

class ListUsesRequest(_message.Message):
    __slots__ = ("workspace_id", "connection_id", "limit")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    connection_id: str
    limit: int
    def __init__(self, workspace_id: _Optional[str] = ..., connection_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListUsesResponse(_message.Message):
    __slots__ = ("uses",)
    USES_FIELD_NUMBER: _ClassVar[int]
    uses: _containers.RepeatedCompositeFieldContainer[Use]
    def __init__(self, uses: _Optional[_Iterable[_Union[Use, _Mapping]]] = ...) -> None: ...

class ListRunbooksRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListRunbooksResponse(_message.Message):
    __slots__ = ("runbooks",)
    RUNBOOKS_FIELD_NUMBER: _ClassVar[int]
    runbooks: _containers.RepeatedCompositeFieldContainer[Runbook]
    def __init__(self, runbooks: _Optional[_Iterable[_Union[Runbook, _Mapping]]] = ...) -> None: ...

class PutRunbookRequest(_message.Message):
    __slots__ = ("workspace_id", "runbook", "requested_by")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    RUNBOOK_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    runbook: Runbook
    requested_by: str
    def __init__(self, workspace_id: _Optional[str] = ..., runbook: _Optional[_Union[Runbook, _Mapping]] = ..., requested_by: _Optional[str] = ...) -> None: ...

class PutRunbookResponse(_message.Message):
    __slots__ = ("runbook",)
    RUNBOOK_FIELD_NUMBER: _ClassVar[int]
    runbook: Runbook
    def __init__(self, runbook: _Optional[_Union[Runbook, _Mapping]] = ...) -> None: ...

class DeleteRunbookRequest(_message.Message):
    __slots__ = ("workspace_id", "id", "requested_by")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    requested_by: str
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ..., requested_by: _Optional[str] = ...) -> None: ...

class DeleteRunbookResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListWorkflowCandidatesRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListWorkflowCandidatesResponse(_message.Message):
    __slots__ = ("candidates", "note")
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    candidates: _containers.RepeatedCompositeFieldContainer[WorkflowCandidate]
    note: str
    def __init__(self, candidates: _Optional[_Iterable[_Union[WorkflowCandidate, _Mapping]]] = ..., note: _Optional[str] = ...) -> None: ...

class ListRelaysRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListRelaysResponse(_message.Message):
    __slots__ = ("relays",)
    RELAYS_FIELD_NUMBER: _ClassVar[int]
    relays: _containers.RepeatedCompositeFieldContainer[Relay]
    def __init__(self, relays: _Optional[_Iterable[_Union[Relay, _Mapping]]] = ...) -> None: ...

class CreateRelayRequest(_message.Message):
    __slots__ = ("workspace_id", "name", "requested_by")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    name: str
    requested_by: str
    def __init__(self, workspace_id: _Optional[str] = ..., name: _Optional[str] = ..., requested_by: _Optional[str] = ...) -> None: ...

class CreateRelayResponse(_message.Message):
    __slots__ = ("relay", "token", "steps")
    RELAY_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    relay: Relay
    token: str
    steps: _containers.RepeatedCompositeFieldContainer[SetupStep]
    def __init__(self, relay: _Optional[_Union[Relay, _Mapping]] = ..., token: _Optional[str] = ..., steps: _Optional[_Iterable[_Union[SetupStep, _Mapping]]] = ...) -> None: ...

class RevokeRelayRequest(_message.Message):
    __slots__ = ("workspace_id", "id", "requested_by")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    requested_by: str
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ..., requested_by: _Optional[str] = ...) -> None: ...

class RevokeRelayResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
