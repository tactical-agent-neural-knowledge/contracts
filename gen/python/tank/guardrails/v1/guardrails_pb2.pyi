from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GuardrailKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GUARDRAIL_KIND_UNSPECIFIED: _ClassVar[GuardrailKind]
    GUARDRAIL_KIND_RULE: _ClassVar[GuardrailKind]
    GUARDRAIL_KIND_ORDER: _ClassVar[GuardrailKind]
    GUARDRAIL_KIND_DECIDE: _ClassVar[GuardrailKind]
    GUARDRAIL_KIND_VERIFY: _ClassVar[GuardrailKind]
    GUARDRAIL_KIND_SHAPE: _ClassVar[GuardrailKind]
    GUARDRAIL_KIND_SCOPE: _ClassVar[GuardrailKind]
    GUARDRAIL_KIND_TOOLS: _ClassVar[GuardrailKind]

class GuardrailScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GUARDRAIL_SCOPE_UNSPECIFIED: _ClassVar[GuardrailScope]
    GUARDRAIL_SCOPE_WORKSPACE: _ClassVar[GuardrailScope]
    GUARDRAIL_SCOPE_TREAD: _ClassVar[GuardrailScope]

class Strength(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STRENGTH_UNSPECIFIED: _ClassVar[Strength]
    STRENGTH_WEAK: _ClassVar[Strength]
    STRENGTH_OK: _ClassVar[Strength]
    STRENGTH_STRONG: _ClassVar[Strength]
    STRENGTH_VERY_STRONG: _ClassVar[Strength]

class VerdictState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VERDICT_STATE_UNSPECIFIED: _ClassVar[VerdictState]
    VERDICT_STATE_MET: _ClassVar[VerdictState]
    VERDICT_STATE_VIOLATED: _ClassVar[VerdictState]
    VERDICT_STATE_UNSURE: _ClassVar[VerdictState]
    VERDICT_STATE_NOT_APPLICABLE: _ClassVar[VerdictState]
GUARDRAIL_KIND_UNSPECIFIED: GuardrailKind
GUARDRAIL_KIND_RULE: GuardrailKind
GUARDRAIL_KIND_ORDER: GuardrailKind
GUARDRAIL_KIND_DECIDE: GuardrailKind
GUARDRAIL_KIND_VERIFY: GuardrailKind
GUARDRAIL_KIND_SHAPE: GuardrailKind
GUARDRAIL_KIND_SCOPE: GuardrailKind
GUARDRAIL_KIND_TOOLS: GuardrailKind
GUARDRAIL_SCOPE_UNSPECIFIED: GuardrailScope
GUARDRAIL_SCOPE_WORKSPACE: GuardrailScope
GUARDRAIL_SCOPE_TREAD: GuardrailScope
STRENGTH_UNSPECIFIED: Strength
STRENGTH_WEAK: Strength
STRENGTH_OK: Strength
STRENGTH_STRONG: Strength
STRENGTH_VERY_STRONG: Strength
VERDICT_STATE_UNSPECIFIED: VerdictState
VERDICT_STATE_MET: VerdictState
VERDICT_STATE_VIOLATED: VerdictState
VERDICT_STATE_UNSURE: VerdictState
VERDICT_STATE_NOT_APPLICABLE: VerdictState

class Guardrail(_message.Message):
    __slots__ = ("id", "workspace_id", "scope", "scope_id", "kind", "text", "params", "judged", "enabled", "created_by", "created_at", "updated_at", "strength", "strength_reasons", "risk", "stops", "platform")
    class StopsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    JUDGED_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    STRENGTH_FIELD_NUMBER: _ClassVar[int]
    STRENGTH_REASONS_FIELD_NUMBER: _ClassVar[int]
    RISK_FIELD_NUMBER: _ClassVar[int]
    STOPS_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    scope: GuardrailScope
    scope_id: str
    kind: GuardrailKind
    text: str
    params: _struct_pb2.Struct
    judged: bool
    enabled: bool
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    strength: Strength
    strength_reasons: _containers.RepeatedScalarFieldContainer[str]
    risk: str
    stops: _containers.ScalarMap[str, int]
    platform: bool
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., scope: _Optional[_Union[GuardrailScope, str]] = ..., scope_id: _Optional[str] = ..., kind: _Optional[_Union[GuardrailKind, str]] = ..., text: _Optional[str] = ..., params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., judged: bool = ..., enabled: bool = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., strength: _Optional[_Union[Strength, str]] = ..., strength_reasons: _Optional[_Iterable[str]] = ..., risk: _Optional[str] = ..., stops: _Optional[_Mapping[str, int]] = ..., platform: bool = ...) -> None: ...

class Verdict(_message.Message):
    __slots__ = ("id", "run_id", "guardrail_id", "guardrail_text", "checkpoint", "state", "detail", "quote", "at", "decided_by", "run_mode")
    ID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    GUARDRAIL_ID_FIELD_NUMBER: _ClassVar[int]
    GUARDRAIL_TEXT_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    QUOTE_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    DECIDED_BY_FIELD_NUMBER: _ClassVar[int]
    RUN_MODE_FIELD_NUMBER: _ClassVar[int]
    id: str
    run_id: str
    guardrail_id: str
    guardrail_text: str
    checkpoint: str
    state: VerdictState
    detail: str
    quote: str
    at: _timestamp_pb2.Timestamp
    decided_by: str
    run_mode: str
    def __init__(self, id: _Optional[str] = ..., run_id: _Optional[str] = ..., guardrail_id: _Optional[str] = ..., guardrail_text: _Optional[str] = ..., checkpoint: _Optional[str] = ..., state: _Optional[_Union[VerdictState, str]] = ..., detail: _Optional[str] = ..., quote: _Optional[str] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., decided_by: _Optional[str] = ..., run_mode: _Optional[str] = ...) -> None: ...

class Rating(_message.Message):
    __slots__ = ("strength", "reasons", "risk", "suggested_kind", "suggested_params")
    STRENGTH_FIELD_NUMBER: _ClassVar[int]
    REASONS_FIELD_NUMBER: _ClassVar[int]
    RISK_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_KIND_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_PARAMS_FIELD_NUMBER: _ClassVar[int]
    strength: Strength
    reasons: _containers.RepeatedScalarFieldContainer[str]
    risk: str
    suggested_kind: GuardrailKind
    suggested_params: _struct_pb2.Struct
    def __init__(self, strength: _Optional[_Union[Strength, str]] = ..., reasons: _Optional[_Iterable[str]] = ..., risk: _Optional[str] = ..., suggested_kind: _Optional[_Union[GuardrailKind, str]] = ..., suggested_params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ListGuardrailsRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...

class ListGuardrailsResponse(_message.Message):
    __slots__ = ("guardrails", "premium")
    GUARDRAILS_FIELD_NUMBER: _ClassVar[int]
    PREMIUM_FIELD_NUMBER: _ClassVar[int]
    guardrails: _containers.RepeatedCompositeFieldContainer[Guardrail]
    premium: bool
    def __init__(self, guardrails: _Optional[_Iterable[_Union[Guardrail, _Mapping]]] = ..., premium: bool = ...) -> None: ...

class PutGuardrailRequest(_message.Message):
    __slots__ = ("workspace_id", "guardrail")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    GUARDRAIL_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    guardrail: Guardrail
    def __init__(self, workspace_id: _Optional[str] = ..., guardrail: _Optional[_Union[Guardrail, _Mapping]] = ...) -> None: ...

class PutGuardrailResponse(_message.Message):
    __slots__ = ("guardrail",)
    GUARDRAIL_FIELD_NUMBER: _ClassVar[int]
    guardrail: Guardrail
    def __init__(self, guardrail: _Optional[_Union[Guardrail, _Mapping]] = ...) -> None: ...

class DeleteGuardrailRequest(_message.Message):
    __slots__ = ("workspace_id", "id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteGuardrailResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RateGuardrailRequest(_message.Message):
    __slots__ = ("workspace_id", "scope", "kind", "text", "params")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    scope: GuardrailScope
    kind: GuardrailKind
    text: str
    params: _struct_pb2.Struct
    def __init__(self, workspace_id: _Optional[str] = ..., scope: _Optional[_Union[GuardrailScope, str]] = ..., kind: _Optional[_Union[GuardrailKind, str]] = ..., text: _Optional[str] = ..., params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class RateGuardrailResponse(_message.Message):
    __slots__ = ("rating",)
    RATING_FIELD_NUMBER: _ClassVar[int]
    rating: Rating
    def __init__(self, rating: _Optional[_Union[Rating, _Mapping]] = ...) -> None: ...

class ListVerdictsRequest(_message.Message):
    __slots__ = ("workspace_id", "run_id", "guardrail_id", "limit")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    GUARDRAIL_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    run_id: str
    guardrail_id: str
    limit: int
    def __init__(self, workspace_id: _Optional[str] = ..., run_id: _Optional[str] = ..., guardrail_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListVerdictsResponse(_message.Message):
    __slots__ = ("verdicts",)
    VERDICTS_FIELD_NUMBER: _ClassVar[int]
    verdicts: _containers.RepeatedCompositeFieldContainer[Verdict]
    def __init__(self, verdicts: _Optional[_Iterable[_Union[Verdict, _Mapping]]] = ...) -> None: ...
