from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Command(_message.Message):
    __slots__ = ("name", "summary", "usage", "takes_text")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    TAKES_TEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    summary: str
    usage: str
    takes_text: bool
    def __init__(self, name: _Optional[str] = ..., summary: _Optional[str] = ..., usage: _Optional[str] = ..., takes_text: bool = ...) -> None: ...

class ListCommandsRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListCommandsResponse(_message.Message):
    __slots__ = ("commands",)
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    commands: _containers.RepeatedCompositeFieldContainer[Command]
    def __init__(self, commands: _Optional[_Iterable[_Union[Command, _Mapping]]] = ...) -> None: ...

class RunCommandRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id", "thread_root_id", "text", "draft", "local_time")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TIME_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    thread_root_id: str
    text: str
    draft: str
    local_time: str
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., text: _Optional[str] = ..., draft: _Optional[str] = ..., local_time: _Optional[str] = ...) -> None: ...

class RunCommandResponse(_message.Message):
    __slots__ = ("reply", "post", "replace_draft", "open_channel_id")
    REPLY_FIELD_NUMBER: _ClassVar[int]
    POST_FIELD_NUMBER: _ClassVar[int]
    REPLACE_DRAFT_FIELD_NUMBER: _ClassVar[int]
    OPEN_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    reply: str
    post: str
    replace_draft: str
    open_channel_id: str
    def __init__(self, reply: _Optional[str] = ..., post: _Optional[str] = ..., replace_draft: _Optional[str] = ..., open_channel_id: _Optional[str] = ...) -> None: ...
