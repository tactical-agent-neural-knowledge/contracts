from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Price(_message.Message):
    __slots__ = ("slug", "name", "description", "agent_minutes", "price_cents", "available")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AGENT_MINUTES_FIELD_NUMBER: _ClassVar[int]
    PRICE_CENTS_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    slug: str
    name: str
    description: str
    agent_minutes: int
    price_cents: int
    available: bool
    def __init__(self, slug: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., agent_minutes: _Optional[int] = ..., price_cents: _Optional[int] = ..., available: bool = ...) -> None: ...

class GetPriceRequest(_message.Message):
    __slots__ = ("slug",)
    SLUG_FIELD_NUMBER: _ClassVar[int]
    slug: str
    def __init__(self, slug: _Optional[str] = ...) -> None: ...

class GetPriceResponse(_message.Message):
    __slots__ = ("price",)
    PRICE_FIELD_NUMBER: _ClassVar[int]
    price: Price
    def __init__(self, price: _Optional[_Union[Price, _Mapping]] = ...) -> None: ...

class StartClaimCheckoutRequest(_message.Message):
    __slots__ = ("slug", "success_path", "cancel_path")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_PATH_FIELD_NUMBER: _ClassVar[int]
    CANCEL_PATH_FIELD_NUMBER: _ClassVar[int]
    slug: str
    success_path: str
    cancel_path: str
    def __init__(self, slug: _Optional[str] = ..., success_path: _Optional[str] = ..., cancel_path: _Optional[str] = ...) -> None: ...

class StartClaimCheckoutResponse(_message.Message):
    __slots__ = ("checkout_url", "held_until")
    CHECKOUT_URL_FIELD_NUMBER: _ClassVar[int]
    HELD_UNTIL_FIELD_NUMBER: _ClassVar[int]
    checkout_url: str
    held_until: _timestamp_pb2.Timestamp
    def __init__(self, checkout_url: _Optional[str] = ..., held_until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Subscription(_message.Message):
    __slots__ = ("workspace_id", "plan", "status", "monthly_cents", "agent_minute_cents", "agent_minutes_this_period", "agent_fees_cents_this_period", "period_end", "has_agents")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_CENTS_FIELD_NUMBER: _ClassVar[int]
    AGENT_MINUTE_CENTS_FIELD_NUMBER: _ClassVar[int]
    AGENT_MINUTES_THIS_PERIOD_FIELD_NUMBER: _ClassVar[int]
    AGENT_FEES_CENTS_THIS_PERIOD_FIELD_NUMBER: _ClassVar[int]
    PERIOD_END_FIELD_NUMBER: _ClassVar[int]
    HAS_AGENTS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    plan: str
    status: str
    monthly_cents: int
    agent_minute_cents: int
    agent_minutes_this_period: int
    agent_fees_cents_this_period: int
    period_end: _timestamp_pb2.Timestamp
    has_agents: bool
    def __init__(self, workspace_id: _Optional[str] = ..., plan: _Optional[str] = ..., status: _Optional[str] = ..., monthly_cents: _Optional[int] = ..., agent_minute_cents: _Optional[int] = ..., agent_minutes_this_period: _Optional[int] = ..., agent_fees_cents_this_period: _Optional[int] = ..., period_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., has_agents: bool = ...) -> None: ...

class GetSubscriptionRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class GetSubscriptionResponse(_message.Message):
    __slots__ = ("subscription",)
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: Subscription
    def __init__(self, subscription: _Optional[_Union[Subscription, _Mapping]] = ...) -> None: ...

class StartUpgradeCheckoutRequest(_message.Message):
    __slots__ = ("workspace_id", "success_path", "cancel_path")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_PATH_FIELD_NUMBER: _ClassVar[int]
    CANCEL_PATH_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    success_path: str
    cancel_path: str
    def __init__(self, workspace_id: _Optional[str] = ..., success_path: _Optional[str] = ..., cancel_path: _Optional[str] = ...) -> None: ...

class StartUpgradeCheckoutResponse(_message.Message):
    __slots__ = ("checkout_url",)
    CHECKOUT_URL_FIELD_NUMBER: _ClassVar[int]
    checkout_url: str
    def __init__(self, checkout_url: _Optional[str] = ...) -> None: ...

class OpenBillingPortalRequest(_message.Message):
    __slots__ = ("workspace_id", "return_path")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    RETURN_PATH_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    return_path: str
    def __init__(self, workspace_id: _Optional[str] = ..., return_path: _Optional[str] = ...) -> None: ...

class OpenBillingPortalResponse(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...
