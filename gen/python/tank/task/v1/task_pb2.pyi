from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tank.channel.v1 import channel_pb2 as _channel_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_STAGE_UNSPECIFIED: _ClassVar[TaskStage]
    TASK_STAGE_QUEUED: _ClassVar[TaskStage]
    TASK_STAGE_IN_PROGRESS: _ClassVar[TaskStage]
    TASK_STAGE_READY_TO_CHECK: _ClassVar[TaskStage]
    TASK_STAGE_DONE: _ClassVar[TaskStage]
    TASK_STAGE_STUCK: _ClassVar[TaskStage]

class TaskRunEvent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_RUN_EVENT_UNSPECIFIED: _ClassVar[TaskRunEvent]
    TASK_RUN_EVENT_STARTED: _ClassVar[TaskRunEvent]
    TASK_RUN_EVENT_WAITING: _ClassVar[TaskRunEvent]
    TASK_RUN_EVENT_PROGRESS: _ClassVar[TaskRunEvent]
    TASK_RUN_EVENT_READY: _ClassVar[TaskRunEvent]
    TASK_RUN_EVENT_STUCK: _ClassVar[TaskRunEvent]
TASK_STAGE_UNSPECIFIED: TaskStage
TASK_STAGE_QUEUED: TaskStage
TASK_STAGE_IN_PROGRESS: TaskStage
TASK_STAGE_READY_TO_CHECK: TaskStage
TASK_STAGE_DONE: TaskStage
TASK_STAGE_STUCK: TaskStage
TASK_RUN_EVENT_UNSPECIFIED: TaskRunEvent
TASK_RUN_EVENT_STARTED: TaskRunEvent
TASK_RUN_EVENT_WAITING: TaskRunEvent
TASK_RUN_EVENT_PROGRESS: TaskRunEvent
TASK_RUN_EVENT_READY: TaskRunEvent
TASK_RUN_EVENT_STUCK: TaskRunEvent

class ProofCheck(_message.Message):
    __slots__ = ("text", "met")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    MET_FIELD_NUMBER: _ClassVar[int]
    text: str
    met: bool
    def __init__(self, text: _Optional[str] = ..., met: bool = ...) -> None: ...

class TaskProof(_message.Message):
    __slots__ = ("live_url", "screenshot_file_id", "checklist", "pull_request_url", "at", "video_file_id")
    LIVE_URL_FIELD_NUMBER: _ClassVar[int]
    SCREENSHOT_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    CHECKLIST_FIELD_NUMBER: _ClassVar[int]
    PULL_REQUEST_URL_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    live_url: str
    screenshot_file_id: str
    checklist: _containers.RepeatedCompositeFieldContainer[ProofCheck]
    pull_request_url: str
    at: _timestamp_pb2.Timestamp
    video_file_id: str
    def __init__(self, live_url: _Optional[str] = ..., screenshot_file_id: _Optional[str] = ..., checklist: _Optional[_Iterable[_Union[ProofCheck, _Mapping]]] = ..., pull_request_url: _Optional[str] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., video_file_id: _Optional[str] = ...) -> None: ...

class TaskNotify(_message.Message):
    __slots__ = ("stage", "user_id", "from_workspace")
    STAGE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    stage: TaskStage
    user_id: str
    from_workspace: bool
    def __init__(self, stage: _Optional[_Union[TaskStage, str]] = ..., user_id: _Optional[str] = ..., from_workspace: bool = ...) -> None: ...

class Task(_message.Message):
    __slots__ = ("id", "workspace_id", "channel_id", "thread_root_id", "title", "details", "stage", "created_by", "created_at", "updated_at", "stage_at", "run_id", "progress", "proof", "checked_by", "checked_at", "stuck_reason", "notify", "asker_muted", "channel_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    STAGE_AT_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    CHECKED_BY_FIELD_NUMBER: _ClassVar[int]
    CHECKED_AT_FIELD_NUMBER: _ClassVar[int]
    STUCK_REASON_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_FIELD_NUMBER: _ClassVar[int]
    ASKER_MUTED_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    channel_id: str
    thread_root_id: str
    title: str
    details: str
    stage: TaskStage
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    stage_at: _timestamp_pb2.Timestamp
    run_id: str
    progress: str
    proof: TaskProof
    checked_by: str
    checked_at: _timestamp_pb2.Timestamp
    stuck_reason: str
    notify: _containers.RepeatedCompositeFieldContainer[TaskNotify]
    asker_muted: bool
    channel_name: str
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., title: _Optional[str] = ..., details: _Optional[str] = ..., stage: _Optional[_Union[TaskStage, str]] = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., stage_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., run_id: _Optional[str] = ..., progress: _Optional[str] = ..., proof: _Optional[_Union[TaskProof, _Mapping]] = ..., checked_by: _Optional[str] = ..., checked_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., stuck_reason: _Optional[str] = ..., notify: _Optional[_Iterable[_Union[TaskNotify, _Mapping]]] = ..., asker_muted: bool = ..., channel_name: _Optional[str] = ...) -> None: ...

class ListTasksRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id", "stages", "asked_by", "limit")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    STAGES_FIELD_NUMBER: _ClassVar[int]
    ASKED_BY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    stages: _containers.RepeatedScalarFieldContainer[TaskStage]
    asked_by: str
    limit: int
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., stages: _Optional[_Iterable[_Union[TaskStage, str]]] = ..., asked_by: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListTasksResponse(_message.Message):
    __slots__ = ("tasks", "has_agent", "ready_to_check")
    TASKS_FIELD_NUMBER: _ClassVar[int]
    HAS_AGENT_FIELD_NUMBER: _ClassVar[int]
    READY_TO_CHECK_FIELD_NUMBER: _ClassVar[int]
    tasks: _containers.RepeatedCompositeFieldContainer[Task]
    has_agent: bool
    ready_to_check: int
    def __init__(self, tasks: _Optional[_Iterable[_Union[Task, _Mapping]]] = ..., has_agent: bool = ..., ready_to_check: _Optional[int] = ...) -> None: ...

class GetTaskRequest(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    def __init__(self, task_id: _Optional[str] = ...) -> None: ...

class GetTaskResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: Task
    def __init__(self, task: _Optional[_Union[Task, _Mapping]] = ...) -> None: ...

class CreateTaskRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id", "title", "details", "start_now", "notify")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    START_NOW_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    title: str
    details: str
    start_now: bool
    notify: _containers.RepeatedCompositeFieldContainer[TaskNotify]
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., title: _Optional[str] = ..., details: _Optional[str] = ..., start_now: bool = ..., notify: _Optional[_Iterable[_Union[TaskNotify, _Mapping]]] = ...) -> None: ...

class CreateTaskResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: Task
    def __init__(self, task: _Optional[_Union[Task, _Mapping]] = ...) -> None: ...

class CreateTaskWithChannelRequest(_message.Message):
    __slots__ = ("workspace_id", "title", "details", "start_now", "notify")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    START_NOW_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    title: str
    details: str
    start_now: bool
    notify: _containers.RepeatedCompositeFieldContainer[TaskNotify]
    def __init__(self, workspace_id: _Optional[str] = ..., title: _Optional[str] = ..., details: _Optional[str] = ..., start_now: bool = ..., notify: _Optional[_Iterable[_Union[TaskNotify, _Mapping]]] = ...) -> None: ...

class CreateTaskWithChannelResponse(_message.Message):
    __slots__ = ("task", "channel")
    TASK_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    task: Task
    channel: _channel_pb2.Channel
    def __init__(self, task: _Optional[_Union[Task, _Mapping]] = ..., channel: _Optional[_Union[_channel_pb2.Channel, _Mapping]] = ...) -> None: ...

class StartTaskRequest(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    def __init__(self, task_id: _Optional[str] = ...) -> None: ...

class StartTaskResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: Task
    def __init__(self, task: _Optional[_Union[Task, _Mapping]] = ...) -> None: ...

class ConfirmTaskRequest(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    def __init__(self, task_id: _Optional[str] = ...) -> None: ...

class ConfirmTaskResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: Task
    def __init__(self, task: _Optional[_Union[Task, _Mapping]] = ...) -> None: ...

class SendBackTaskRequest(_message.Message):
    __slots__ = ("task_id", "text")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    text: str
    def __init__(self, task_id: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class SendBackTaskResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: Task
    def __init__(self, task: _Optional[_Union[Task, _Mapping]] = ...) -> None: ...

class RetryTaskRequest(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    def __init__(self, task_id: _Optional[str] = ...) -> None: ...

class RetryTaskResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: Task
    def __init__(self, task: _Optional[_Union[Task, _Mapping]] = ...) -> None: ...

class SetTaskNotifyRequest(_message.Message):
    __slots__ = ("task_id", "notify", "asker_muted")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_FIELD_NUMBER: _ClassVar[int]
    ASKER_MUTED_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    notify: _containers.RepeatedCompositeFieldContainer[TaskNotify]
    asker_muted: bool
    def __init__(self, task_id: _Optional[str] = ..., notify: _Optional[_Iterable[_Union[TaskNotify, _Mapping]]] = ..., asker_muted: bool = ...) -> None: ...

class SetTaskNotifyResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: Task
    def __init__(self, task: _Optional[_Union[Task, _Mapping]] = ...) -> None: ...

class GetTaskSettingsRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class GetTaskSettingsResponse(_message.Message):
    __slots__ = ("notify", "can_manage")
    NOTIFY_FIELD_NUMBER: _ClassVar[int]
    CAN_MANAGE_FIELD_NUMBER: _ClassVar[int]
    notify: _containers.RepeatedCompositeFieldContainer[TaskNotify]
    can_manage: bool
    def __init__(self, notify: _Optional[_Iterable[_Union[TaskNotify, _Mapping]]] = ..., can_manage: bool = ...) -> None: ...

class SetTaskSettingsRequest(_message.Message):
    __slots__ = ("workspace_id", "notify")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    notify: _containers.RepeatedCompositeFieldContainer[TaskNotify]
    def __init__(self, workspace_id: _Optional[str] = ..., notify: _Optional[_Iterable[_Union[TaskNotify, _Mapping]]] = ...) -> None: ...

class SetTaskSettingsResponse(_message.Message):
    __slots__ = ("notify",)
    NOTIFY_FIELD_NUMBER: _ClassVar[int]
    notify: _containers.RepeatedCompositeFieldContainer[TaskNotify]
    def __init__(self, notify: _Optional[_Iterable[_Union[TaskNotify, _Mapping]]] = ...) -> None: ...

class RecordTaskRunRequest(_message.Message):
    __slots__ = ("run_id", "task_id", "event", "ask", "proof", "reason", "progress")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    ASK_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    task_id: str
    event: TaskRunEvent
    ask: str
    proof: TaskProof
    reason: str
    progress: str
    def __init__(self, run_id: _Optional[str] = ..., task_id: _Optional[str] = ..., event: _Optional[_Union[TaskRunEvent, str]] = ..., ask: _Optional[str] = ..., proof: _Optional[_Union[TaskProof, _Mapping]] = ..., reason: _Optional[str] = ..., progress: _Optional[str] = ...) -> None: ...

class RecordTaskRunResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: Task
    def __init__(self, task: _Optional[_Union[Task, _Mapping]] = ...) -> None: ...
