from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgentureRow(_message.Message):
    __slots__ = ("workspace_id", "slug", "name", "description", "enabled", "weight", "next_due_at", "last_run_at", "runs", "last_error", "agent_minutes", "live_run_id", "live_state", "spend_usd", "price_cents", "claimed", "auto_approve")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    NEXT_DUE_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_AT_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    AGENT_MINUTES_FIELD_NUMBER: _ClassVar[int]
    LIVE_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    LIVE_STATE_FIELD_NUMBER: _ClassVar[int]
    SPEND_USD_FIELD_NUMBER: _ClassVar[int]
    PRICE_CENTS_FIELD_NUMBER: _ClassVar[int]
    CLAIMED_FIELD_NUMBER: _ClassVar[int]
    AUTO_APPROVE_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    slug: str
    name: str
    description: str
    enabled: bool
    weight: int
    next_due_at: _timestamp_pb2.Timestamp
    last_run_at: _timestamp_pb2.Timestamp
    runs: int
    last_error: str
    agent_minutes: int
    live_run_id: str
    live_state: str
    spend_usd: float
    price_cents: int
    claimed: bool
    auto_approve: bool
    def __init__(self, workspace_id: _Optional[str] = ..., slug: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., enabled: bool = ..., weight: _Optional[int] = ..., next_due_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_run_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., runs: _Optional[int] = ..., last_error: _Optional[str] = ..., agent_minutes: _Optional[int] = ..., live_run_id: _Optional[str] = ..., live_state: _Optional[str] = ..., spend_usd: _Optional[float] = ..., price_cents: _Optional[int] = ..., claimed: bool = ..., auto_approve: bool = ...) -> None: ...

class ListAgenturesRequest(_message.Message):
    __slots__ = ("query", "limit", "offset")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    query: str
    limit: int
    offset: int
    def __init__(self, query: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListAgenturesResponse(_message.Message):
    __slots__ = ("agentures", "total", "summary")
    AGENTURES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    agentures: _containers.RepeatedCompositeFieldContainer[AgentureRow]
    total: int
    summary: BoardSummary
    def __init__(self, agentures: _Optional[_Iterable[_Union[AgentureRow, _Mapping]]] = ..., total: _Optional[int] = ..., summary: _Optional[_Union[BoardSummary, _Mapping]] = ...) -> None: ...

class BoardSummary(_message.Message):
    __slots__ = ("in_flight", "max_concurrent", "enabled", "unclaimed", "agent_minutes_24h", "spend_usd_24h", "spend_usd_total")
    IN_FLIGHT_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    UNCLAIMED_FIELD_NUMBER: _ClassVar[int]
    AGENT_MINUTES_24H_FIELD_NUMBER: _ClassVar[int]
    SPEND_USD_24H_FIELD_NUMBER: _ClassVar[int]
    SPEND_USD_TOTAL_FIELD_NUMBER: _ClassVar[int]
    in_flight: int
    max_concurrent: int
    enabled: bool
    unclaimed: int
    agent_minutes_24h: int
    spend_usd_24h: float
    spend_usd_total: float
    def __init__(self, in_flight: _Optional[int] = ..., max_concurrent: _Optional[int] = ..., enabled: bool = ..., unclaimed: _Optional[int] = ..., agent_minutes_24h: _Optional[int] = ..., spend_usd_24h: _Optional[float] = ..., spend_usd_total: _Optional[float] = ...) -> None: ...

class SetAllocationRequest(_message.Message):
    __slots__ = ("workspace_id", "enabled", "weight", "run_now", "auto_approve")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    RUN_NOW_FIELD_NUMBER: _ClassVar[int]
    AUTO_APPROVE_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    enabled: bool
    weight: int
    run_now: bool
    auto_approve: bool
    def __init__(self, workspace_id: _Optional[str] = ..., enabled: bool = ..., weight: _Optional[int] = ..., run_now: bool = ..., auto_approve: bool = ...) -> None: ...

class SetAllocationResponse(_message.Message):
    __slots__ = ("agenture",)
    AGENTURE_FIELD_NUMBER: _ClassVar[int]
    agenture: AgentureRow
    def __init__(self, agenture: _Optional[_Union[AgentureRow, _Mapping]] = ...) -> None: ...

class SetBoardSettingsRequest(_message.Message):
    __slots__ = ("max_concurrent",)
    MAX_CONCURRENT_FIELD_NUMBER: _ClassVar[int]
    max_concurrent: int
    def __init__(self, max_concurrent: _Optional[int] = ...) -> None: ...

class SetBoardSettingsResponse(_message.Message):
    __slots__ = ("summary",)
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    summary: BoardSummary
    def __init__(self, summary: _Optional[_Union[BoardSummary, _Mapping]] = ...) -> None: ...

class StopRunRequest(_message.Message):
    __slots__ = ("run_id", "reason")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    reason: str
    def __init__(self, run_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class StopRunResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
