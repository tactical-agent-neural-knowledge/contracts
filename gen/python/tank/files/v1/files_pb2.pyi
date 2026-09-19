from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScanStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCAN_STATUS_UNSPECIFIED: _ClassVar[ScanStatus]
    SCAN_STATUS_PENDING: _ClassVar[ScanStatus]
    SCAN_STATUS_CLEAN: _ClassVar[ScanStatus]
    SCAN_STATUS_INFECTED: _ClassVar[ScanStatus]
    SCAN_STATUS_FAILED: _ClassVar[ScanStatus]
SCAN_STATUS_UNSPECIFIED: ScanStatus
SCAN_STATUS_PENDING: ScanStatus
SCAN_STATUS_CLEAN: ScanStatus
SCAN_STATUS_INFECTED: ScanStatus
SCAN_STATUS_FAILED: ScanStatus

class File(_message.Message):
    __slots__ = ("id", "workspace_id", "uploader_id", "name", "mime", "size", "scan_status", "width", "height", "duration_ms", "thumbnails", "created_at", "shared_in_channel_ids", "uploader_display_name")
    class ThumbnailsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    UPLOADER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MIME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SCAN_STATUS_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    THUMBNAILS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    SHARED_IN_CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    UPLOADER_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    uploader_id: str
    name: str
    mime: str
    size: int
    scan_status: ScanStatus
    width: int
    height: int
    duration_ms: int
    thumbnails: _containers.ScalarMap[str, str]
    created_at: _timestamp_pb2.Timestamp
    shared_in_channel_ids: _containers.RepeatedScalarFieldContainer[str]
    uploader_display_name: str
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., uploader_id: _Optional[str] = ..., name: _Optional[str] = ..., mime: _Optional[str] = ..., size: _Optional[int] = ..., scan_status: _Optional[_Union[ScanStatus, str]] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., duration_ms: _Optional[int] = ..., thumbnails: _Optional[_Mapping[str, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., shared_in_channel_ids: _Optional[_Iterable[str]] = ..., uploader_display_name: _Optional[str] = ...) -> None: ...

class CreateUploadRequest(_message.Message):
    __slots__ = ("workspace_id", "name", "mime", "size", "channel_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MIME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    name: str
    mime: str
    size: int
    channel_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., name: _Optional[str] = ..., mime: _Optional[str] = ..., size: _Optional[int] = ..., channel_id: _Optional[str] = ...) -> None: ...

class CreateUploadResponse(_message.Message):
    __slots__ = ("file", "upload_url", "upload_id", "part_urls", "part_size")
    FILE_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    PART_URLS_FIELD_NUMBER: _ClassVar[int]
    PART_SIZE_FIELD_NUMBER: _ClassVar[int]
    file: File
    upload_url: str
    upload_id: str
    part_urls: _containers.RepeatedScalarFieldContainer[str]
    part_size: int
    def __init__(self, file: _Optional[_Union[File, _Mapping]] = ..., upload_url: _Optional[str] = ..., upload_id: _Optional[str] = ..., part_urls: _Optional[_Iterable[str]] = ..., part_size: _Optional[int] = ...) -> None: ...

class CompleteUploadRequest(_message.Message):
    __slots__ = ("file_id", "upload_id", "etags")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    ETAGS_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    upload_id: str
    etags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, file_id: _Optional[str] = ..., upload_id: _Optional[str] = ..., etags: _Optional[_Iterable[str]] = ...) -> None: ...

class CompleteUploadResponse(_message.Message):
    __slots__ = ("file",)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: File
    def __init__(self, file: _Optional[_Union[File, _Mapping]] = ...) -> None: ...

class GetDownloadUrlRequest(_message.Message):
    __slots__ = ("file_id",)
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    def __init__(self, file_id: _Optional[str] = ...) -> None: ...

class GetDownloadUrlResponse(_message.Message):
    __slots__ = ("url", "expires_at")
    URL_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    url: str
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, url: _Optional[str] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetFileRequest(_message.Message):
    __slots__ = ("file_id",)
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    def __init__(self, file_id: _Optional[str] = ...) -> None: ...

class GetFileResponse(_message.Message):
    __slots__ = ("file",)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: File
    def __init__(self, file: _Optional[_Union[File, _Mapping]] = ...) -> None: ...

class ListFilesRequest(_message.Message):
    __slots__ = ("workspace_id", "channel_id", "cursor", "limit")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    channel_id: str
    cursor: str
    limit: int
    def __init__(self, workspace_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., cursor: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListFilesResponse(_message.Message):
    __slots__ = ("files", "next_cursor")
    FILES_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[File]
    next_cursor: str
    def __init__(self, files: _Optional[_Iterable[_Union[File, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...
