from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RunState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RUN_STATE_UNSPECIFIED: _ClassVar[RunState]
    RUN_STATE_REQUESTED: _ClassVar[RunState]
    RUN_STATE_ADMITTED: _ClassVar[RunState]
    RUN_STATE_PROVISIONING: _ClassVar[RunState]
    RUN_STATE_PLANNING: _ClassVar[RunState]
    RUN_STATE_AWAITING_PLAN_APPROVAL: _ClassVar[RunState]
    RUN_STATE_IMPLEMENTING: _ClassVar[RunState]
    RUN_STATE_PUSHED: _ClassVar[RunState]
    RUN_STATE_CI_WATCHING: _ClassVar[RunState]
    RUN_STATE_PR_OPEN: _ClassVar[RunState]
    RUN_STATE_AWAITING_MERGE_APPROVAL: _ClassVar[RunState]
    RUN_STATE_MERGED: _ClassVar[RunState]
    RUN_STATE_VERIFYING_DEPLOY: _ClassVar[RunState]
    RUN_STATE_DONE: _ClassVar[RunState]
    RUN_STATE_CANCELLED: _ClassVar[RunState]
    RUN_STATE_FAILED: _ClassVar[RunState]
    RUN_STATE_BUDGET_EXHAUSTED: _ClassVar[RunState]
    RUN_STATE_TIMED_OUT: _ClassVar[RunState]
    RUN_STATE_APPROVAL_EXPIRED: _ClassVar[RunState]
RUN_STATE_UNSPECIFIED: RunState
RUN_STATE_REQUESTED: RunState
RUN_STATE_ADMITTED: RunState
RUN_STATE_PROVISIONING: RunState
RUN_STATE_PLANNING: RunState
RUN_STATE_AWAITING_PLAN_APPROVAL: RunState
RUN_STATE_IMPLEMENTING: RunState
RUN_STATE_PUSHED: RunState
RUN_STATE_CI_WATCHING: RunState
RUN_STATE_PR_OPEN: RunState
RUN_STATE_AWAITING_MERGE_APPROVAL: RunState
RUN_STATE_MERGED: RunState
RUN_STATE_VERIFYING_DEPLOY: RunState
RUN_STATE_DONE: RunState
RUN_STATE_CANCELLED: RunState
RUN_STATE_FAILED: RunState
RUN_STATE_BUDGET_EXHAUSTED: RunState
RUN_STATE_TIMED_OUT: RunState
RUN_STATE_APPROVAL_EXPIRED: RunState

class Agent(_message.Message):
    __slots__ = ("id", "workspace_id", "principal_id", "name", "scopes")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    principal_id: str
    name: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., principal_id: _Optional[str] = ..., name: _Optional[str] = ..., scopes: _Optional[_Iterable[str]] = ...) -> None: ...

class Run(_message.Message):
    __slots__ = ("id", "workspace_id", "channel_id", "thread_root_id", "agent_id", "requested_by", "state", "branch", "pr_url", "cost_usd", "status_message_id", "started_at", "ended_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    PR_URL_FIELD_NUMBER: _ClassVar[int]
    COST_USD_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    channel_id: str
    thread_root_id: str
    agent_id: str
    requested_by: str
    state: RunState
    branch: str
    pr_url: str
    cost_usd: float
    status_message_id: str
    started_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., requested_by: _Optional[str] = ..., state: _Optional[_Union[RunState, str]] = ..., branch: _Optional[str] = ..., pr_url: _Optional[str] = ..., cost_usd: _Optional[float] = ..., status_message_id: _Optional[str] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StartRunRequest(_message.Message):
    __slots__ = ("thread_root_id", "agent_id", "instructions")
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    thread_root_id: str
    agent_id: str
    instructions: str
    def __init__(self, thread_root_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., instructions: _Optional[str] = ...) -> None: ...

class StartRunResponse(_message.Message):
    __slots__ = ("run", "agent_session_token", "token_expires_at")
    RUN_FIELD_NUMBER: _ClassVar[int]
    AGENT_SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    run: Run
    agent_session_token: str
    token_expires_at: _timestamp_pb2.Timestamp
    def __init__(self, run: _Optional[_Union[Run, _Mapping]] = ..., agent_session_token: _Optional[str] = ..., token_expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StopRunRequest(_message.Message):
    __slots__ = ("run_id", "reason")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    reason: str
    def __init__(self, run_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class StopRunResponse(_message.Message):
    __slots__ = ("run",)
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: Run
    def __init__(self, run: _Optional[_Union[Run, _Mapping]] = ...) -> None: ...

class HeartbeatRequest(_message.Message):
    __slots__ = ("run_id",)
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class HeartbeatResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetStatusRequest(_message.Message):
    __slots__ = ("run_id", "state", "status", "branch", "pr_url", "cost_usd")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    PR_URL_FIELD_NUMBER: _ClassVar[int]
    COST_USD_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    state: RunState
    status: str
    branch: str
    pr_url: str
    cost_usd: float
    def __init__(self, run_id: _Optional[str] = ..., state: _Optional[_Union[RunState, str]] = ..., status: _Optional[str] = ..., branch: _Optional[str] = ..., pr_url: _Optional[str] = ..., cost_usd: _Optional[float] = ...) -> None: ...

class SetStatusResponse(_message.Message):
    __slots__ = ("run",)
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: Run
    def __init__(self, run: _Optional[_Union[Run, _Mapping]] = ...) -> None: ...

class GetRunRequest(_message.Message):
    __slots__ = ("run_id",)
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class GetRunResponse(_message.Message):
    __slots__ = ("run",)
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: Run
    def __init__(self, run: _Optional[_Union[Run, _Mapping]] = ...) -> None: ...

class ListRunsRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id", "thread_root_id", "cursor", "limit")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    thread_root_id: str
    cursor: str
    limit: int
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., cursor: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListRunsResponse(_message.Message):
    __slots__ = ("runs", "next_cursor")
    RUNS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    runs: _containers.RepeatedCompositeFieldContainer[Run]
    next_cursor: str
    def __init__(self, runs: _Optional[_Iterable[_Union[Run, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...
