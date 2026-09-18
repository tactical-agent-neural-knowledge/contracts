from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Broadcast(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BROADCAST_UNSPECIFIED: _ClassVar[Broadcast]
    BROADCAST_HERE: _ClassVar[Broadcast]
    BROADCAST_CHANNEL: _ClassVar[Broadcast]
    BROADCAST_EVERYONE: _ClassVar[Broadcast]
BROADCAST_UNSPECIFIED: Broadcast
BROADCAST_HERE: Broadcast
BROADCAST_CHANNEL: Broadcast
BROADCAST_EVERYONE: Broadcast

class RichText(_message.Message):
    __slots__ = ("blocks",)
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    blocks: _containers.RepeatedCompositeFieldContainer[RichTextBlock]
    def __init__(self, blocks: _Optional[_Iterable[_Union[RichTextBlock, _Mapping]]] = ...) -> None: ...

class RichTextBlock(_message.Message):
    __slots__ = ("section", "code", "quote", "list")
    SECTION_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    QUOTE_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    section: RichTextSection
    code: RichTextCode
    quote: RichTextQuote
    list: RichTextList
    def __init__(self, section: _Optional[_Union[RichTextSection, _Mapping]] = ..., code: _Optional[_Union[RichTextCode, _Mapping]] = ..., quote: _Optional[_Union[RichTextQuote, _Mapping]] = ..., list: _Optional[_Union[RichTextList, _Mapping]] = ...) -> None: ...

class Style(_message.Message):
    __slots__ = ("bold", "italic", "strike", "code")
    BOLD_FIELD_NUMBER: _ClassVar[int]
    ITALIC_FIELD_NUMBER: _ClassVar[int]
    STRIKE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    bold: bool
    italic: bool
    strike: bool
    code: bool
    def __init__(self, bold: bool = ..., italic: bool = ..., strike: bool = ..., code: bool = ...) -> None: ...

class RichTextElement(_message.Message):
    __slots__ = ("text", "emoji", "user", "channel", "broadcast", "link")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    text: TextElement
    emoji: EmojiElement
    user: UserMention
    channel: ChannelMention
    broadcast: BroadcastMention
    link: LinkElement
    def __init__(self, text: _Optional[_Union[TextElement, _Mapping]] = ..., emoji: _Optional[_Union[EmojiElement, _Mapping]] = ..., user: _Optional[_Union[UserMention, _Mapping]] = ..., channel: _Optional[_Union[ChannelMention, _Mapping]] = ..., broadcast: _Optional[_Union[BroadcastMention, _Mapping]] = ..., link: _Optional[_Union[LinkElement, _Mapping]] = ...) -> None: ...

class TextElement(_message.Message):
    __slots__ = ("text", "style")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    STYLE_FIELD_NUMBER: _ClassVar[int]
    text: str
    style: Style
    def __init__(self, text: _Optional[str] = ..., style: _Optional[_Union[Style, _Mapping]] = ...) -> None: ...

class EmojiElement(_message.Message):
    __slots__ = ("name", "unicode")
    NAME_FIELD_NUMBER: _ClassVar[int]
    UNICODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    unicode: str
    def __init__(self, name: _Optional[str] = ..., unicode: _Optional[str] = ...) -> None: ...

class UserMention(_message.Message):
    __slots__ = ("user_id", "style")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    STYLE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    style: Style
    def __init__(self, user_id: _Optional[str] = ..., style: _Optional[_Union[Style, _Mapping]] = ...) -> None: ...

class ChannelMention(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class BroadcastMention(_message.Message):
    __slots__ = ("range",)
    RANGE_FIELD_NUMBER: _ClassVar[int]
    range: Broadcast
    def __init__(self, range: _Optional[_Union[Broadcast, str]] = ...) -> None: ...

class LinkElement(_message.Message):
    __slots__ = ("url", "text", "style")
    URL_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    STYLE_FIELD_NUMBER: _ClassVar[int]
    url: str
    text: str
    style: Style
    def __init__(self, url: _Optional[str] = ..., text: _Optional[str] = ..., style: _Optional[_Union[Style, _Mapping]] = ...) -> None: ...

class RichTextSection(_message.Message):
    __slots__ = ("elements",)
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    elements: _containers.RepeatedCompositeFieldContainer[RichTextElement]
    def __init__(self, elements: _Optional[_Iterable[_Union[RichTextElement, _Mapping]]] = ...) -> None: ...

class RichTextCode(_message.Message):
    __slots__ = ("language", "text")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    language: str
    text: str
    def __init__(self, language: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class RichTextQuote(_message.Message):
    __slots__ = ("elements",)
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    elements: _containers.RepeatedCompositeFieldContainer[RichTextElement]
    def __init__(self, elements: _Optional[_Iterable[_Union[RichTextElement, _Mapping]]] = ...) -> None: ...

class RichTextList(_message.Message):
    __slots__ = ("ordered", "indent", "items")
    ORDERED_FIELD_NUMBER: _ClassVar[int]
    INDENT_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    ordered: bool
    indent: int
    items: _containers.RepeatedCompositeFieldContainer[RichTextSection]
    def __init__(self, ordered: bool = ..., indent: _Optional[int] = ..., items: _Optional[_Iterable[_Union[RichTextSection, _Mapping]]] = ...) -> None: ...
