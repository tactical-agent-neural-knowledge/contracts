from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Disposition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DISPOSITION_UNSPECIFIED: _ClassVar[Disposition]
    DISPOSITION_PROPOSE: _ClassVar[Disposition]
    DISPOSITION_AUTO_APPLY: _ClassVar[Disposition]
    DISPOSITION_REFUSED: _ClassVar[Disposition]

class RemediationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REMEDIATION_STATE_UNSPECIFIED: _ClassVar[RemediationState]
    REMEDIATION_STATE_RECEIVED: _ClassVar[RemediationState]
    REMEDIATION_STATE_PLANNED: _ClassVar[RemediationState]
    REMEDIATION_STATE_RUNNING: _ClassVar[RemediationState]
    REMEDIATION_STATE_PROPOSED: _ClassVar[RemediationState]
    REMEDIATION_STATE_APPLIED: _ClassVar[RemediationState]
    REMEDIATION_STATE_FAILED: _ClassVar[RemediationState]
    REMEDIATION_STATE_REFUSED: _ClassVar[RemediationState]
    REMEDIATION_STATE_SUPERSEDED: _ClassVar[RemediationState]
DISPOSITION_UNSPECIFIED: Disposition
DISPOSITION_PROPOSE: Disposition
DISPOSITION_AUTO_APPLY: Disposition
DISPOSITION_REFUSED: Disposition
REMEDIATION_STATE_UNSPECIFIED: RemediationState
REMEDIATION_STATE_RECEIVED: RemediationState
REMEDIATION_STATE_PLANNED: RemediationState
REMEDIATION_STATE_RUNNING: RemediationState
REMEDIATION_STATE_PROPOSED: RemediationState
REMEDIATION_STATE_APPLIED: RemediationState
REMEDIATION_STATE_FAILED: RemediationState
REMEDIATION_STATE_REFUSED: RemediationState
REMEDIATION_STATE_SUPERSEDED: RemediationState

class Evidence(_message.Message):
    __slots__ = ("summary", "source", "observed_at", "detail")
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    summary: str
    source: str
    observed_at: _timestamp_pb2.Timestamp
    detail: str
    def __init__(self, summary: _Optional[str] = ..., source: _Optional[str] = ..., observed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., detail: _Optional[str] = ...) -> None: ...

class Finding(_message.Message):
    __slots__ = ("finding_id", "control_id", "control_version", "summary", "locus", "severity", "proposal", "evidence", "probe_id", "source", "control_state")
    FINDING_ID_FIELD_NUMBER: _ClassVar[int]
    CONTROL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTROL_VERSION_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    LOCUS_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    PROBE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CONTROL_STATE_FIELD_NUMBER: _ClassVar[int]
    finding_id: str
    control_id: str
    control_version: int
    summary: str
    locus: str
    severity: str
    proposal: str
    evidence: Evidence
    probe_id: str
    source: str
    control_state: str
    def __init__(self, finding_id: _Optional[str] = ..., control_id: _Optional[str] = ..., control_version: _Optional[int] = ..., summary: _Optional[str] = ..., locus: _Optional[str] = ..., severity: _Optional[str] = ..., proposal: _Optional[str] = ..., evidence: _Optional[_Union[Evidence, _Mapping]] = ..., probe_id: _Optional[str] = ..., source: _Optional[str] = ..., control_state: _Optional[str] = ...) -> None: ...

class Class(_message.Message):
    __slots__ = ("id", "title", "description", "max_disposition", "test_requirement", "reversible", "undo", "lockout_risk", "gate_kind")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MAX_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    TEST_REQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    REVERSIBLE_FIELD_NUMBER: _ClassVar[int]
    UNDO_FIELD_NUMBER: _ClassVar[int]
    LOCKOUT_RISK_FIELD_NUMBER: _ClassVar[int]
    GATE_KIND_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    description: str
    max_disposition: Disposition
    test_requirement: str
    reversible: bool
    undo: str
    lockout_risk: bool
    gate_kind: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., max_disposition: _Optional[_Union[Disposition, str]] = ..., test_requirement: _Optional[str] = ..., reversible: bool = ..., undo: _Optional[str] = ..., lockout_risk: bool = ..., gate_kind: _Optional[str] = ...) -> None: ...

class Target(_message.Message):
    __slots__ = ("repo", "workspace_id", "channel_id", "thread_root_id", "run_id", "branch", "pull_request_url", "state", "detail", "started_at", "ended_at", "why")
    REPO_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    PULL_REQUEST_URL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    WHY_FIELD_NUMBER: _ClassVar[int]
    repo: str
    workspace_id: str
    channel_id: str
    thread_root_id: str
    run_id: str
    branch: str
    pull_request_url: str
    state: RemediationState
    detail: str
    started_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    why: str
    def __init__(self, repo: _Optional[str] = ..., workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., run_id: _Optional[str] = ..., branch: _Optional[str] = ..., pull_request_url: _Optional[str] = ..., state: _Optional[_Union[RemediationState, str]] = ..., detail: _Optional[str] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., why: _Optional[str] = ...) -> None: ...

class Remediation(_message.Message):
    __slots__ = ("id", "finding", "class_id", "disposition", "state", "refusal_reason", "targets", "brief", "forbidden_paths", "judge_principal", "fix_principal", "received_at", "planned_at", "ended_at", "probe_id", "unwatched")
    ID_FIELD_NUMBER: _ClassVar[int]
    FINDING_FIELD_NUMBER: _ClassVar[int]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_REASON_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    BRIEF_FIELD_NUMBER: _ClassVar[int]
    FORBIDDEN_PATHS_FIELD_NUMBER: _ClassVar[int]
    JUDGE_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    FIX_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    PLANNED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    PROBE_ID_FIELD_NUMBER: _ClassVar[int]
    UNWATCHED_FIELD_NUMBER: _ClassVar[int]
    id: str
    finding: Finding
    class_id: str
    disposition: Disposition
    state: RemediationState
    refusal_reason: str
    targets: _containers.RepeatedCompositeFieldContainer[Target]
    brief: str
    forbidden_paths: _containers.RepeatedScalarFieldContainer[str]
    judge_principal: str
    fix_principal: str
    received_at: _timestamp_pb2.Timestamp
    planned_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    probe_id: str
    unwatched: bool
    def __init__(self, id: _Optional[str] = ..., finding: _Optional[_Union[Finding, _Mapping]] = ..., class_id: _Optional[str] = ..., disposition: _Optional[_Union[Disposition, str]] = ..., state: _Optional[_Union[RemediationState, str]] = ..., refusal_reason: _Optional[str] = ..., targets: _Optional[_Iterable[_Union[Target, _Mapping]]] = ..., brief: _Optional[str] = ..., forbidden_paths: _Optional[_Iterable[str]] = ..., judge_principal: _Optional[str] = ..., fix_principal: _Optional[str] = ..., received_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., planned_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., probe_id: _Optional[str] = ..., unwatched: bool = ...) -> None: ...

class SubmitFindingRequest(_message.Message):
    __slots__ = ("finding", "dry_run", "resubmit", "judge_principal")
    FINDING_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    RESUBMIT_FIELD_NUMBER: _ClassVar[int]
    JUDGE_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    finding: Finding
    dry_run: bool
    resubmit: bool
    judge_principal: str
    def __init__(self, finding: _Optional[_Union[Finding, _Mapping]] = ..., dry_run: bool = ..., resubmit: bool = ..., judge_principal: _Optional[str] = ...) -> None: ...

class SubmitFindingResponse(_message.Message):
    __slots__ = ("remediation", "declined")
    REMEDIATION_FIELD_NUMBER: _ClassVar[int]
    DECLINED_FIELD_NUMBER: _ClassVar[int]
    remediation: Remediation
    declined: _containers.RepeatedCompositeFieldContainer[Target]
    def __init__(self, remediation: _Optional[_Union[Remediation, _Mapping]] = ..., declined: _Optional[_Iterable[_Union[Target, _Mapping]]] = ...) -> None: ...

class GetRemediationRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetRemediationResponse(_message.Message):
    __slots__ = ("remediation",)
    REMEDIATION_FIELD_NUMBER: _ClassVar[int]
    remediation: Remediation
    def __init__(self, remediation: _Optional[_Union[Remediation, _Mapping]] = ...) -> None: ...

class ListRemediationsRequest(_message.Message):
    __slots__ = ("finding_id", "control_id", "state", "limit", "since")
    FINDING_ID_FIELD_NUMBER: _ClassVar[int]
    CONTROL_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    finding_id: str
    control_id: str
    state: RemediationState
    limit: int
    since: _timestamp_pb2.Timestamp
    def __init__(self, finding_id: _Optional[str] = ..., control_id: _Optional[str] = ..., state: _Optional[_Union[RemediationState, str]] = ..., limit: _Optional[int] = ..., since: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListRemediationsResponse(_message.Message):
    __slots__ = ("remediations",)
    REMEDIATIONS_FIELD_NUMBER: _ClassVar[int]
    remediations: _containers.RepeatedCompositeFieldContainer[Remediation]
    def __init__(self, remediations: _Optional[_Iterable[_Union[Remediation, _Mapping]]] = ...) -> None: ...

class ListClassesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListClassesResponse(_message.Message):
    __slots__ = ("classes",)
    CLASSES_FIELD_NUMBER: _ClassVar[int]
    classes: _containers.RepeatedCompositeFieldContainer[Class]
    def __init__(self, classes: _Optional[_Iterable[_Union[Class, _Mapping]]] = ...) -> None: ...

class CancelRemediationRequest(_message.Message):
    __slots__ = ("id", "reason", "user_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    reason: str
    user_id: str
    def __init__(self, id: _Optional[str] = ..., reason: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class CancelRemediationResponse(_message.Message):
    __slots__ = ("remediation",)
    REMEDIATION_FIELD_NUMBER: _ClassVar[int]
    remediation: Remediation
    def __init__(self, remediation: _Optional[_Union[Remediation, _Mapping]] = ...) -> None: ...
