from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetExperienceRequest(_message.Message):
    __slots__ = ("prompt",)
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    prompt: str
    def __init__(self, prompt: _Optional[str] = ...) -> None: ...

class GetExperienceResponse(_message.Message):
    __slots__ = ("experience",)
    EXPERIENCE_FIELD_NUMBER: _ClassVar[int]
    experience: Experience
    def __init__(self, experience: _Optional[_Union[Experience, _Mapping]] = ...) -> None: ...

class Experience(_message.Message):
    __slots__ = ("headline", "lede", "sections", "closing", "closest", "written_for", "persona")
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    LEDE_FIELD_NUMBER: _ClassVar[int]
    SECTIONS_FIELD_NUMBER: _ClassVar[int]
    CLOSING_FIELD_NUMBER: _ClassVar[int]
    CLOSEST_FIELD_NUMBER: _ClassVar[int]
    WRITTEN_FOR_FIELD_NUMBER: _ClassVar[int]
    PERSONA_FIELD_NUMBER: _ClassVar[int]
    headline: str
    lede: str
    sections: _containers.RepeatedCompositeFieldContainer[ExperienceSection]
    closing: str
    closest: bool
    written_for: str
    persona: str
    def __init__(self, headline: _Optional[str] = ..., lede: _Optional[str] = ..., sections: _Optional[_Iterable[_Union[ExperienceSection, _Mapping]]] = ..., closing: _Optional[str] = ..., closest: bool = ..., written_for: _Optional[str] = ..., persona: _Optional[str] = ...) -> None: ...

class ExperienceSection(_message.Message):
    __slots__ = ("feature", "title", "body")
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    feature: str
    title: str
    body: str
    def __init__(self, feature: _Optional[str] = ..., title: _Optional[str] = ..., body: _Optional[str] = ...) -> None: ...
