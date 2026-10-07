from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTROL_STATE_UNSPECIFIED: _ClassVar[ControlState]
    CONTROL_STATE_MET: _ClassVar[ControlState]
    CONTROL_STATE_PARTLY: _ClassVar[ControlState]
    CONTROL_STATE_NOT_YET: _ClassVar[ControlState]
    CONTROL_STATE_NOT_APPLICABLE: _ClassVar[ControlState]
    CONTROL_STATE_UNKNOWN: _ClassVar[ControlState]

class ControlCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTROL_CATEGORY_UNSPECIFIED: _ClassVar[ControlCategory]
    CONTROL_CATEGORY_IDENTITY: _ClassVar[ControlCategory]
    CONTROL_CATEGORY_DATA: _ClassVar[ControlCategory]
    CONTROL_CATEGORY_INFRASTRUCTURE: _ClassVar[ControlCategory]
    CONTROL_CATEGORY_OPERATIONS: _ClassVar[ControlCategory]
    CONTROL_CATEGORY_APPLICATION: _ClassVar[ControlCategory]
    CONTROL_CATEGORY_AGENT: _ClassVar[ControlCategory]

class CheckKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHECK_KIND_UNSPECIFIED: _ClassVar[CheckKind]
    CHECK_KIND_AUTOMATED: _ClassVar[CheckKind]
    CHECK_KIND_ATTESTATION: _ClassVar[CheckKind]
    CHECK_KIND_NONE: _ClassVar[CheckKind]
CONTROL_STATE_UNSPECIFIED: ControlState
CONTROL_STATE_MET: ControlState
CONTROL_STATE_PARTLY: ControlState
CONTROL_STATE_NOT_YET: ControlState
CONTROL_STATE_NOT_APPLICABLE: ControlState
CONTROL_STATE_UNKNOWN: ControlState
CONTROL_CATEGORY_UNSPECIFIED: ControlCategory
CONTROL_CATEGORY_IDENTITY: ControlCategory
CONTROL_CATEGORY_DATA: ControlCategory
CONTROL_CATEGORY_INFRASTRUCTURE: ControlCategory
CONTROL_CATEGORY_OPERATIONS: ControlCategory
CONTROL_CATEGORY_APPLICATION: ControlCategory
CONTROL_CATEGORY_AGENT: ControlCategory
CHECK_KIND_UNSPECIFIED: CheckKind
CHECK_KIND_AUTOMATED: CheckKind
CHECK_KIND_ATTESTATION: CheckKind
CHECK_KIND_NONE: CheckKind

class Evidence(_message.Message):
    __slots__ = ("summary", "source", "observed_at", "age_seconds", "stale", "detail")
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    AGE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    STALE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    summary: str
    source: str
    observed_at: _timestamp_pb2.Timestamp
    age_seconds: int
    stale: bool
    detail: str
    def __init__(self, summary: _Optional[str] = ..., source: _Optional[str] = ..., observed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., age_seconds: _Optional[int] = ..., stale: bool = ..., detail: _Optional[str] = ...) -> None: ...

class Attestation(_message.Message):
    __slots__ = ("author", "statement", "at", "expires_at", "expired")
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_FIELD_NUMBER: _ClassVar[int]
    author: str
    statement: str
    at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    expired: bool
    def __init__(self, author: _Optional[str] = ..., statement: _Optional[str] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expired: bool = ...) -> None: ...

class FrameworkClause(_message.Message):
    __slots__ = ("framework", "clause", "title")
    FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
    CLAUSE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    framework: str
    clause: str
    title: str
    def __init__(self, framework: _Optional[str] = ..., clause: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class Finding(_message.Message):
    __slots__ = ("id", "summary", "locus", "severity", "proposal")
    ID_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    LOCUS_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    id: str
    summary: str
    locus: str
    severity: str
    proposal: str
    def __init__(self, id: _Optional[str] = ..., summary: _Optional[str] = ..., locus: _Optional[str] = ..., severity: _Optional[str] = ..., proposal: _Optional[str] = ...) -> None: ...

class Control(_message.Message):
    __slots__ = ("id", "version", "statement", "owner", "category", "check_kind", "check", "evidence_query", "clauses", "state", "reason", "evidence", "attestation", "evaluated_at", "max_age_seconds", "stale", "findings", "tags")
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CHECK_KIND_FIELD_NUMBER: _ClassVar[int]
    CHECK_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_QUERY_FIELD_NUMBER: _ClassVar[int]
    CLAUSES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    ATTESTATION_FIELD_NUMBER: _ClassVar[int]
    EVALUATED_AT_FIELD_NUMBER: _ClassVar[int]
    MAX_AGE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    STALE_FIELD_NUMBER: _ClassVar[int]
    FINDINGS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    version: int
    statement: str
    owner: str
    category: ControlCategory
    check_kind: CheckKind
    check: str
    evidence_query: str
    clauses: _containers.RepeatedCompositeFieldContainer[FrameworkClause]
    state: ControlState
    reason: str
    evidence: Evidence
    attestation: Attestation
    evaluated_at: _timestamp_pb2.Timestamp
    max_age_seconds: int
    stale: bool
    findings: _containers.RepeatedCompositeFieldContainer[Finding]
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., version: _Optional[int] = ..., statement: _Optional[str] = ..., owner: _Optional[str] = ..., category: _Optional[_Union[ControlCategory, str]] = ..., check_kind: _Optional[_Union[CheckKind, str]] = ..., check: _Optional[str] = ..., evidence_query: _Optional[str] = ..., clauses: _Optional[_Iterable[_Union[FrameworkClause, _Mapping]]] = ..., state: _Optional[_Union[ControlState, str]] = ..., reason: _Optional[str] = ..., evidence: _Optional[_Union[Evidence, _Mapping]] = ..., attestation: _Optional[_Union[Attestation, _Mapping]] = ..., evaluated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., max_age_seconds: _Optional[int] = ..., stale: bool = ..., findings: _Optional[_Iterable[_Union[Finding, _Mapping]]] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class StateCount(_message.Message):
    __slots__ = ("state", "count")
    STATE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    state: ControlState
    count: int
    def __init__(self, state: _Optional[_Union[ControlState, str]] = ..., count: _Optional[int] = ...) -> None: ...

class Posture(_message.Message):
    __slots__ = ("registry_version", "generated_at", "total", "counts", "controls", "unknown")
    REGISTRY_VERSION_FIELD_NUMBER: _ClassVar[int]
    GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    COUNTS_FIELD_NUMBER: _ClassVar[int]
    CONTROLS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FIELD_NUMBER: _ClassVar[int]
    registry_version: str
    generated_at: _timestamp_pb2.Timestamp
    total: int
    counts: _containers.RepeatedCompositeFieldContainer[StateCount]
    controls: _containers.RepeatedCompositeFieldContainer[Control]
    unknown: int
    def __init__(self, registry_version: _Optional[str] = ..., generated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., total: _Optional[int] = ..., counts: _Optional[_Iterable[_Union[StateCount, _Mapping]]] = ..., controls: _Optional[_Iterable[_Union[Control, _Mapping]]] = ..., unknown: _Optional[int] = ...) -> None: ...

class ClauseCoverage(_message.Message):
    __slots__ = ("clause", "title", "control_ids", "state")
    CLAUSE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTROL_IDS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    clause: str
    title: str
    control_ids: _containers.RepeatedScalarFieldContainer[str]
    state: ControlState
    def __init__(self, clause: _Optional[str] = ..., title: _Optional[str] = ..., control_ids: _Optional[_Iterable[str]] = ..., state: _Optional[_Union[ControlState, str]] = ...) -> None: ...

class FrameworkCoverage(_message.Message):
    __slots__ = ("framework", "title", "scope_note", "clauses", "clause_coverage", "counts")
    FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_NOTE_FIELD_NUMBER: _ClassVar[int]
    CLAUSES_FIELD_NUMBER: _ClassVar[int]
    CLAUSE_COVERAGE_FIELD_NUMBER: _ClassVar[int]
    COUNTS_FIELD_NUMBER: _ClassVar[int]
    framework: str
    title: str
    scope_note: str
    clauses: int
    clause_coverage: _containers.RepeatedCompositeFieldContainer[ClauseCoverage]
    counts: _containers.RepeatedCompositeFieldContainer[StateCount]
    def __init__(self, framework: _Optional[str] = ..., title: _Optional[str] = ..., scope_note: _Optional[str] = ..., clauses: _Optional[int] = ..., clause_coverage: _Optional[_Iterable[_Union[ClauseCoverage, _Mapping]]] = ..., counts: _Optional[_Iterable[_Union[StateCount, _Mapping]]] = ...) -> None: ...

class GetPostureRequest(_message.Message):
    __slots__ = ("category", "state", "summary_only")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_ONLY_FIELD_NUMBER: _ClassVar[int]
    category: ControlCategory
    state: ControlState
    summary_only: bool
    def __init__(self, category: _Optional[_Union[ControlCategory, str]] = ..., state: _Optional[_Union[ControlState, str]] = ..., summary_only: bool = ...) -> None: ...

class GetPostureResponse(_message.Message):
    __slots__ = ("posture",)
    POSTURE_FIELD_NUMBER: _ClassVar[int]
    posture: Posture
    def __init__(self, posture: _Optional[_Union[Posture, _Mapping]] = ...) -> None: ...

class GetControlRequest(_message.Message):
    __slots__ = ("control_id",)
    CONTROL_ID_FIELD_NUMBER: _ClassVar[int]
    control_id: str
    def __init__(self, control_id: _Optional[str] = ...) -> None: ...

class GetControlResponse(_message.Message):
    __slots__ = ("control",)
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    control: Control
    def __init__(self, control: _Optional[_Union[Control, _Mapping]] = ...) -> None: ...

class ListFrameworksRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListFrameworksResponse(_message.Message):
    __slots__ = ("frameworks",)
    FRAMEWORKS_FIELD_NUMBER: _ClassVar[int]
    frameworks: _containers.RepeatedCompositeFieldContainer[FrameworkCoverage]
    def __init__(self, frameworks: _Optional[_Iterable[_Union[FrameworkCoverage, _Mapping]]] = ...) -> None: ...

class GetFrameworkCoverageRequest(_message.Message):
    __slots__ = ("framework",)
    FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
    framework: str
    def __init__(self, framework: _Optional[str] = ...) -> None: ...

class GetFrameworkCoverageResponse(_message.Message):
    __slots__ = ("coverage",)
    COVERAGE_FIELD_NUMBER: _ClassVar[int]
    coverage: FrameworkCoverage
    def __init__(self, coverage: _Optional[_Union[FrameworkCoverage, _Mapping]] = ...) -> None: ...

class EvaluateRequest(_message.Message):
    __slots__ = ("control_id",)
    CONTROL_ID_FIELD_NUMBER: _ClassVar[int]
    control_id: str
    def __init__(self, control_id: _Optional[str] = ...) -> None: ...

class EvaluateResponse(_message.Message):
    __slots__ = ("posture", "evaluated")
    POSTURE_FIELD_NUMBER: _ClassVar[int]
    EVALUATED_FIELD_NUMBER: _ClassVar[int]
    posture: Posture
    evaluated: int
    def __init__(self, posture: _Optional[_Union[Posture, _Mapping]] = ..., evaluated: _Optional[int] = ...) -> None: ...
