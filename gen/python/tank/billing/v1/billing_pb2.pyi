from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

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
    __slots__ = ("workspace_id", "plan", "status", "monthly_cents", "agent_minute_cents", "agent_minutes_this_period", "agent_fees_cents_this_period", "period_end", "has_agents", "addons", "agent_usage_cents_this_month", "agent_cap_cents", "provider", "seats", "waivers", "no_charge", "payment_state", "payment_failed_at")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_CENTS_FIELD_NUMBER: _ClassVar[int]
    AGENT_MINUTE_CENTS_FIELD_NUMBER: _ClassVar[int]
    AGENT_MINUTES_THIS_PERIOD_FIELD_NUMBER: _ClassVar[int]
    AGENT_FEES_CENTS_THIS_PERIOD_FIELD_NUMBER: _ClassVar[int]
    PERIOD_END_FIELD_NUMBER: _ClassVar[int]
    HAS_AGENTS_FIELD_NUMBER: _ClassVar[int]
    ADDONS_FIELD_NUMBER: _ClassVar[int]
    AGENT_USAGE_CENTS_THIS_MONTH_FIELD_NUMBER: _ClassVar[int]
    AGENT_CAP_CENTS_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    SEATS_FIELD_NUMBER: _ClassVar[int]
    WAIVERS_FIELD_NUMBER: _ClassVar[int]
    NO_CHARGE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FAILED_AT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    plan: str
    status: str
    monthly_cents: int
    agent_minute_cents: int
    agent_minutes_this_period: int
    agent_fees_cents_this_period: int
    period_end: _timestamp_pb2.Timestamp
    has_agents: bool
    addons: _containers.RepeatedScalarFieldContainer[str]
    agent_usage_cents_this_month: int
    agent_cap_cents: int
    provider: str
    seats: int
    waivers: _containers.RepeatedCompositeFieldContainer[Waiver]
    no_charge: bool
    payment_state: str
    payment_failed_at: _timestamp_pb2.Timestamp
    def __init__(self, workspace_id: _Optional[str] = ..., plan: _Optional[str] = ..., status: _Optional[str] = ..., monthly_cents: _Optional[int] = ..., agent_minute_cents: _Optional[int] = ..., agent_minutes_this_period: _Optional[int] = ..., agent_fees_cents_this_period: _Optional[int] = ..., period_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., has_agents: bool = ..., addons: _Optional[_Iterable[str]] = ..., agent_usage_cents_this_month: _Optional[int] = ..., agent_cap_cents: _Optional[int] = ..., provider: _Optional[str] = ..., seats: _Optional[int] = ..., waivers: _Optional[_Iterable[_Union[Waiver, _Mapping]]] = ..., no_charge: bool = ..., payment_state: _Optional[str] = ..., payment_failed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Waiver(_message.Message):
    __slots__ = ("product", "by_name", "at")
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    BY_NAME_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    product: str
    by_name: str
    at: _timestamp_pb2.Timestamp
    def __init__(self, product: _Optional[str] = ..., by_name: _Optional[str] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("workspace_id", "success_path", "cancel_path", "product")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_PATH_FIELD_NUMBER: _ClassVar[int]
    CANCEL_PATH_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    success_path: str
    cancel_path: str
    product: str
    def __init__(self, workspace_id: _Optional[str] = ..., success_path: _Optional[str] = ..., cancel_path: _Optional[str] = ..., product: _Optional[str] = ...) -> None: ...

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

class VerifyAppleTransactionRequest(_message.Message):
    __slots__ = ("workspace_id", "signed_transaction")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNED_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    signed_transaction: str
    def __init__(self, workspace_id: _Optional[str] = ..., signed_transaction: _Optional[str] = ...) -> None: ...

class VerifyAppleTransactionResponse(_message.Message):
    __slots__ = ("product", "status")
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    product: str
    status: str
    def __init__(self, product: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class SetAgentCapRequest(_message.Message):
    __slots__ = ("workspace_id", "agent_cap_cents")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_CAP_CENTS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    agent_cap_cents: int
    def __init__(self, workspace_id: _Optional[str] = ..., agent_cap_cents: _Optional[int] = ...) -> None: ...

class SetAgentCapResponse(_message.Message):
    __slots__ = ("agent_cap_cents",)
    AGENT_CAP_CENTS_FIELD_NUMBER: _ClassVar[int]
    agent_cap_cents: int
    def __init__(self, agent_cap_cents: _Optional[int] = ...) -> None: ...

class BillingRecord(_message.Message):
    __slots__ = ("id", "at", "description", "amount_cents", "status", "url", "kind", "number")
    ID_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    id: str
    at: _timestamp_pb2.Timestamp
    description: str
    amount_cents: int
    status: str
    url: str
    kind: str
    number: str
    def __init__(self, id: _Optional[str] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., description: _Optional[str] = ..., amount_cents: _Optional[int] = ..., status: _Optional[str] = ..., url: _Optional[str] = ..., kind: _Optional[str] = ..., number: _Optional[str] = ...) -> None: ...

class ListBillingHistoryRequest(_message.Message):
    __slots__ = ("workspace_id", "limit")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    limit: int
    def __init__(self, workspace_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListBillingHistoryResponse(_message.Message):
    __slots__ = ("records",)
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    records: _containers.RepeatedCompositeFieldContainer[BillingRecord]
    def __init__(self, records: _Optional[_Iterable[_Union[BillingRecord, _Mapping]]] = ...) -> None: ...

class AgentTime(_message.Message):
    __slots__ = ("balance_cents", "included_cents", "included_left_cents", "used_this_month_cents", "blocked", "auto_refill", "auto_refilled_this_month_cents", "has_payment_method", "history", "pack_cents", "min_custom_cents", "can_manage", "prepaid", "no_charge")
    BALANCE_CENTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_CENTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_LEFT_CENTS_FIELD_NUMBER: _ClassVar[int]
    USED_THIS_MONTH_CENTS_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_FIELD_NUMBER: _ClassVar[int]
    AUTO_REFILL_FIELD_NUMBER: _ClassVar[int]
    AUTO_REFILLED_THIS_MONTH_CENTS_FIELD_NUMBER: _ClassVar[int]
    HAS_PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    PACK_CENTS_FIELD_NUMBER: _ClassVar[int]
    MIN_CUSTOM_CENTS_FIELD_NUMBER: _ClassVar[int]
    CAN_MANAGE_FIELD_NUMBER: _ClassVar[int]
    PREPAID_FIELD_NUMBER: _ClassVar[int]
    NO_CHARGE_FIELD_NUMBER: _ClassVar[int]
    balance_cents: int
    included_cents: int
    included_left_cents: int
    used_this_month_cents: int
    blocked: bool
    auto_refill: AutoRefill
    auto_refilled_this_month_cents: int
    has_payment_method: bool
    history: _containers.RepeatedCompositeFieldContainer[AgentTimeEntry]
    pack_cents: _containers.RepeatedScalarFieldContainer[int]
    min_custom_cents: int
    can_manage: bool
    prepaid: bool
    no_charge: bool
    def __init__(self, balance_cents: _Optional[int] = ..., included_cents: _Optional[int] = ..., included_left_cents: _Optional[int] = ..., used_this_month_cents: _Optional[int] = ..., blocked: bool = ..., auto_refill: _Optional[_Union[AutoRefill, _Mapping]] = ..., auto_refilled_this_month_cents: _Optional[int] = ..., has_payment_method: bool = ..., history: _Optional[_Iterable[_Union[AgentTimeEntry, _Mapping]]] = ..., pack_cents: _Optional[_Iterable[int]] = ..., min_custom_cents: _Optional[int] = ..., can_manage: bool = ..., prepaid: bool = ..., no_charge: bool = ...) -> None: ...

class AutoRefill(_message.Message):
    __slots__ = ("enabled", "below_cents", "amount_cents", "monthly_cap_cents", "last_error")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    BELOW_CENTS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_CAP_CENTS_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    below_cents: int
    amount_cents: int
    monthly_cap_cents: int
    last_error: str
    def __init__(self, enabled: bool = ..., below_cents: _Optional[int] = ..., amount_cents: _Optional[int] = ..., monthly_cap_cents: _Optional[int] = ..., last_error: _Optional[str] = ...) -> None: ...

class AgentTimeEntry(_message.Message):
    __slots__ = ("kind", "cents", "at", "note")
    KIND_FIELD_NUMBER: _ClassVar[int]
    CENTS_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    cents: int
    at: _timestamp_pb2.Timestamp
    note: str
    def __init__(self, kind: _Optional[str] = ..., cents: _Optional[int] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., note: _Optional[str] = ...) -> None: ...

class GetAgentTimeRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class GetAgentTimeResponse(_message.Message):
    __slots__ = ("agent_time",)
    AGENT_TIME_FIELD_NUMBER: _ClassVar[int]
    agent_time: AgentTime
    def __init__(self, agent_time: _Optional[_Union[AgentTime, _Mapping]] = ...) -> None: ...

class StartAgentTimeCheckoutRequest(_message.Message):
    __slots__ = ("workspace_id", "cents", "return_path")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CENTS_FIELD_NUMBER: _ClassVar[int]
    RETURN_PATH_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    cents: int
    return_path: str
    def __init__(self, workspace_id: _Optional[str] = ..., cents: _Optional[int] = ..., return_path: _Optional[str] = ...) -> None: ...

class StartAgentTimeCheckoutResponse(_message.Message):
    __slots__ = ("checkout_url",)
    CHECKOUT_URL_FIELD_NUMBER: _ClassVar[int]
    checkout_url: str
    def __init__(self, checkout_url: _Optional[str] = ...) -> None: ...

class SetAutoRefillRequest(_message.Message):
    __slots__ = ("workspace_id", "auto_refill")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    AUTO_REFILL_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    auto_refill: AutoRefill
    def __init__(self, workspace_id: _Optional[str] = ..., auto_refill: _Optional[_Union[AutoRefill, _Mapping]] = ...) -> None: ...

class SetAutoRefillResponse(_message.Message):
    __slots__ = ("agent_time",)
    AGENT_TIME_FIELD_NUMBER: _ClassVar[int]
    agent_time: AgentTime
    def __init__(self, agent_time: _Optional[_Union[AgentTime, _Mapping]] = ...) -> None: ...

class ServiceSubscription(_message.Message):
    __slots__ = ("product_workspace_id", "product_slug", "product_name", "status", "current_period_end", "price_cents", "has_api_key", "api_key_hint")
    PRODUCT_WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SLUG_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PERIOD_END_FIELD_NUMBER: _ClassVar[int]
    PRICE_CENTS_FIELD_NUMBER: _ClassVar[int]
    HAS_API_KEY_FIELD_NUMBER: _ClassVar[int]
    API_KEY_HINT_FIELD_NUMBER: _ClassVar[int]
    product_workspace_id: str
    product_slug: str
    product_name: str
    status: str
    current_period_end: _timestamp_pb2.Timestamp
    price_cents: int
    has_api_key: bool
    api_key_hint: str
    def __init__(self, product_workspace_id: _Optional[str] = ..., product_slug: _Optional[str] = ..., product_name: _Optional[str] = ..., status: _Optional[str] = ..., current_period_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., price_cents: _Optional[int] = ..., has_api_key: bool = ..., api_key_hint: _Optional[str] = ...) -> None: ...

class StartServiceCheckoutRequest(_message.Message):
    __slots__ = ("product_slug", "return_path")
    PRODUCT_SLUG_FIELD_NUMBER: _ClassVar[int]
    RETURN_PATH_FIELD_NUMBER: _ClassVar[int]
    product_slug: str
    return_path: str
    def __init__(self, product_slug: _Optional[str] = ..., return_path: _Optional[str] = ...) -> None: ...

class StartServiceCheckoutResponse(_message.Message):
    __slots__ = ("checkout_url",)
    CHECKOUT_URL_FIELD_NUMBER: _ClassVar[int]
    checkout_url: str
    def __init__(self, checkout_url: _Optional[str] = ...) -> None: ...

class ListServiceSubscriptionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListServiceSubscriptionsResponse(_message.Message):
    __slots__ = ("subscriptions", "price_cents")
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    PRICE_CENTS_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedCompositeFieldContainer[ServiceSubscription]
    price_cents: int
    def __init__(self, subscriptions: _Optional[_Iterable[_Union[ServiceSubscription, _Mapping]]] = ..., price_cents: _Optional[int] = ...) -> None: ...

class OpenServicePortalRequest(_message.Message):
    __slots__ = ("return_path",)
    RETURN_PATH_FIELD_NUMBER: _ClassVar[int]
    return_path: str
    def __init__(self, return_path: _Optional[str] = ...) -> None: ...

class OpenServicePortalResponse(_message.Message):
    __slots__ = ("portal_url",)
    PORTAL_URL_FIELD_NUMBER: _ClassVar[int]
    portal_url: str
    def __init__(self, portal_url: _Optional[str] = ...) -> None: ...

class CreateServiceApiKeyRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateServiceApiKeyResponse(_message.Message):
    __slots__ = ("key", "hint")
    KEY_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    key: str
    hint: str
    def __init__(self, key: _Optional[str] = ..., hint: _Optional[str] = ...) -> None: ...
