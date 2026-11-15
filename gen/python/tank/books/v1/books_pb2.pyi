from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InvoiceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVOICE_STATUS_UNSPECIFIED: _ClassVar[InvoiceStatus]
    INVOICE_STATUS_DRAFT: _ClassVar[InvoiceStatus]
    INVOICE_STATUS_SENT: _ClassVar[InvoiceStatus]
    INVOICE_STATUS_OVERDUE: _ClassVar[InvoiceStatus]
    INVOICE_STATUS_PAID: _ClassVar[InvoiceStatus]
    INVOICE_STATUS_VOID: _ClassVar[InvoiceStatus]

class CategoryKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CATEGORY_KIND_UNSPECIFIED: _ClassVar[CategoryKind]
    CATEGORY_KIND_INCOME: _ClassVar[CategoryKind]
    CATEGORY_KIND_EXPENSE: _ClassVar[CategoryKind]

class StatementGrain(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATEMENT_GRAIN_UNSPECIFIED: _ClassVar[StatementGrain]
    STATEMENT_GRAIN_MONTH: _ClassVar[StatementGrain]
    STATEMENT_GRAIN_QUARTER: _ClassVar[StatementGrain]
    STATEMENT_GRAIN_YEAR: _ClassVar[StatementGrain]

class StatementBasis(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATEMENT_BASIS_UNSPECIFIED: _ClassVar[StatementBasis]
    STATEMENT_BASIS_EARNED: _ClassVar[StatementBasis]
    STATEMENT_BASIS_CASH: _ClassVar[StatementBasis]

class PeriodKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PERIOD_KIND_UNSPECIFIED: _ClassVar[PeriodKind]
    PERIOD_KIND_PAST: _ClassVar[PeriodKind]
    PERIOD_KIND_CURRENT: _ClassVar[PeriodKind]
    PERIOD_KIND_FUTURE: _ClassVar[PeriodKind]

class CellState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CELL_STATE_UNSPECIFIED: _ClassVar[CellState]
    CELL_STATE_ACTUAL: _ClassVar[CellState]
    CELL_STATE_EXPECTED: _ClassVar[CellState]
    CELL_STATE_MIXED: _ClassVar[CellState]

class StatementRowKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATEMENT_ROW_KIND_UNSPECIFIED: _ClassVar[StatementRowKind]
    STATEMENT_ROW_KIND_CATEGORY: _ClassVar[StatementRowKind]
    STATEMENT_ROW_KIND_SUBTOTAL: _ClassVar[StatementRowKind]
    STATEMENT_ROW_KIND_TOTAL: _ClassVar[StatementRowKind]

class Cadence(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CADENCE_UNSPECIFIED: _ClassVar[Cadence]
    CADENCE_WEEKLY: _ClassVar[Cadence]
    CADENCE_MONTHLY: _ClassVar[Cadence]
    CADENCE_QUARTERLY: _ClassVar[Cadence]
    CADENCE_YEARLY: _ClassVar[Cadence]

class RecurringSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RECURRING_SOURCE_UNSPECIFIED: _ClassVar[RecurringSource]
    RECURRING_SOURCE_PERSON: _ClassVar[RecurringSource]
    RECURRING_SOURCE_DETECTED: _ClassVar[RecurringSource]
    RECURRING_SOURCE_TANK: _ClassVar[RecurringSource]
    RECURRING_SOURCE_AGENT: _ClassVar[RecurringSource]

class RecurringStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RECURRING_STATUS_UNSPECIFIED: _ClassVar[RecurringStatus]
    RECURRING_STATUS_ACTIVE: _ClassVar[RecurringStatus]
    RECURRING_STATUS_PROPOSED: _ClassVar[RecurringStatus]
    RECURRING_STATUS_PAUSED: _ClassVar[RecurringStatus]
    RECURRING_STATUS_DISMISSED: _ClassVar[RecurringStatus]
INVOICE_STATUS_UNSPECIFIED: InvoiceStatus
INVOICE_STATUS_DRAFT: InvoiceStatus
INVOICE_STATUS_SENT: InvoiceStatus
INVOICE_STATUS_OVERDUE: InvoiceStatus
INVOICE_STATUS_PAID: InvoiceStatus
INVOICE_STATUS_VOID: InvoiceStatus
CATEGORY_KIND_UNSPECIFIED: CategoryKind
CATEGORY_KIND_INCOME: CategoryKind
CATEGORY_KIND_EXPENSE: CategoryKind
STATEMENT_GRAIN_UNSPECIFIED: StatementGrain
STATEMENT_GRAIN_MONTH: StatementGrain
STATEMENT_GRAIN_QUARTER: StatementGrain
STATEMENT_GRAIN_YEAR: StatementGrain
STATEMENT_BASIS_UNSPECIFIED: StatementBasis
STATEMENT_BASIS_EARNED: StatementBasis
STATEMENT_BASIS_CASH: StatementBasis
PERIOD_KIND_UNSPECIFIED: PeriodKind
PERIOD_KIND_PAST: PeriodKind
PERIOD_KIND_CURRENT: PeriodKind
PERIOD_KIND_FUTURE: PeriodKind
CELL_STATE_UNSPECIFIED: CellState
CELL_STATE_ACTUAL: CellState
CELL_STATE_EXPECTED: CellState
CELL_STATE_MIXED: CellState
STATEMENT_ROW_KIND_UNSPECIFIED: StatementRowKind
STATEMENT_ROW_KIND_CATEGORY: StatementRowKind
STATEMENT_ROW_KIND_SUBTOTAL: StatementRowKind
STATEMENT_ROW_KIND_TOTAL: StatementRowKind
CADENCE_UNSPECIFIED: Cadence
CADENCE_WEEKLY: Cadence
CADENCE_MONTHLY: Cadence
CADENCE_QUARTERLY: Cadence
CADENCE_YEARLY: Cadence
RECURRING_SOURCE_UNSPECIFIED: RecurringSource
RECURRING_SOURCE_PERSON: RecurringSource
RECURRING_SOURCE_DETECTED: RecurringSource
RECURRING_SOURCE_TANK: RecurringSource
RECURRING_SOURCE_AGENT: RecurringSource
RECURRING_STATUS_UNSPECIFIED: RecurringStatus
RECURRING_STATUS_ACTIVE: RecurringStatus
RECURRING_STATUS_PROPOSED: RecurringStatus
RECURRING_STATUS_PAUSED: RecurringStatus
RECURRING_STATUS_DISMISSED: RecurringStatus

class Settings(_message.Message):
    __slots__ = ("enabled", "currency", "business_name", "invoice_prefix", "next_invoice_number", "default_due_days", "chase_every_days", "competes_with", "payment_instructions", "stripe_secret_key", "stripe_key_hint", "payments_ready", "fiscal_year_start_month", "timezone", "finance_channel_id")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    INVOICE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    NEXT_INVOICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DUE_DAYS_FIELD_NUMBER: _ClassVar[int]
    CHASE_EVERY_DAYS_FIELD_NUMBER: _ClassVar[int]
    COMPETES_WITH_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    STRIPE_SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    STRIPE_KEY_HINT_FIELD_NUMBER: _ClassVar[int]
    PAYMENTS_READY_FIELD_NUMBER: _ClassVar[int]
    FISCAL_YEAR_START_MONTH_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    FINANCE_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    currency: str
    business_name: str
    invoice_prefix: str
    next_invoice_number: int
    default_due_days: int
    chase_every_days: int
    competes_with: _containers.RepeatedScalarFieldContainer[str]
    payment_instructions: str
    stripe_secret_key: str
    stripe_key_hint: str
    payments_ready: bool
    fiscal_year_start_month: int
    timezone: str
    finance_channel_id: str
    def __init__(self, enabled: bool = ..., currency: _Optional[str] = ..., business_name: _Optional[str] = ..., invoice_prefix: _Optional[str] = ..., next_invoice_number: _Optional[int] = ..., default_due_days: _Optional[int] = ..., chase_every_days: _Optional[int] = ..., competes_with: _Optional[_Iterable[str]] = ..., payment_instructions: _Optional[str] = ..., stripe_secret_key: _Optional[str] = ..., stripe_key_hint: _Optional[str] = ..., payments_ready: bool = ..., fiscal_year_start_month: _Optional[int] = ..., timezone: _Optional[str] = ..., finance_channel_id: _Optional[str] = ...) -> None: ...

class Customer(_message.Message):
    __slots__ = ("id", "name", "email", "notes", "created_at", "owed_cents")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    OWED_CENTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    email: str
    notes: str
    created_at: _timestamp_pb2.Timestamp
    owed_cents: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., notes: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., owed_cents: _Optional[int] = ...) -> None: ...

class InvoiceLine(_message.Message):
    __slots__ = ("description", "quantity", "unit_cents", "total_cents")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    UNIT_CENTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CENTS_FIELD_NUMBER: _ClassVar[int]
    description: str
    quantity: float
    unit_cents: int
    total_cents: int
    def __init__(self, description: _Optional[str] = ..., quantity: _Optional[float] = ..., unit_cents: _Optional[int] = ..., total_cents: _Optional[int] = ...) -> None: ...

class Invoice(_message.Message):
    __slots__ = ("id", "customer_id", "customer_name", "number", "status", "lines", "subtotal_cents", "tax_cents", "total_cents", "paid_cents", "due_cents", "issued_at", "due_at", "sent_at", "paid_at", "notes", "thread_root_id", "predicted_paid_at", "predicted_confidence", "last_chased_at", "chase_count", "share_url", "pay_url", "category_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    SUBTOTAL_CENTS_FIELD_NUMBER: _ClassVar[int]
    TAX_CENTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CENTS_FIELD_NUMBER: _ClassVar[int]
    PAID_CENTS_FIELD_NUMBER: _ClassVar[int]
    DUE_CENTS_FIELD_NUMBER: _ClassVar[int]
    ISSUED_AT_FIELD_NUMBER: _ClassVar[int]
    DUE_AT_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    PAID_AT_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    PREDICTED_PAID_AT_FIELD_NUMBER: _ClassVar[int]
    PREDICTED_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    LAST_CHASED_AT_FIELD_NUMBER: _ClassVar[int]
    CHASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SHARE_URL_FIELD_NUMBER: _ClassVar[int]
    PAY_URL_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    customer_id: str
    customer_name: str
    number: str
    status: InvoiceStatus
    lines: _containers.RepeatedCompositeFieldContainer[InvoiceLine]
    subtotal_cents: int
    tax_cents: int
    total_cents: int
    paid_cents: int
    due_cents: int
    issued_at: _timestamp_pb2.Timestamp
    due_at: _timestamp_pb2.Timestamp
    sent_at: _timestamp_pb2.Timestamp
    paid_at: _timestamp_pb2.Timestamp
    notes: str
    thread_root_id: str
    predicted_paid_at: _timestamp_pb2.Timestamp
    predicted_confidence: float
    last_chased_at: _timestamp_pb2.Timestamp
    chase_count: int
    share_url: str
    pay_url: str
    category_id: str
    def __init__(self, id: _Optional[str] = ..., customer_id: _Optional[str] = ..., customer_name: _Optional[str] = ..., number: _Optional[str] = ..., status: _Optional[_Union[InvoiceStatus, str]] = ..., lines: _Optional[_Iterable[_Union[InvoiceLine, _Mapping]]] = ..., subtotal_cents: _Optional[int] = ..., tax_cents: _Optional[int] = ..., total_cents: _Optional[int] = ..., paid_cents: _Optional[int] = ..., due_cents: _Optional[int] = ..., issued_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., due_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sent_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., paid_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., notes: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., predicted_paid_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., predicted_confidence: _Optional[float] = ..., last_chased_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., chase_count: _Optional[int] = ..., share_url: _Optional[str] = ..., pay_url: _Optional[str] = ..., category_id: _Optional[str] = ...) -> None: ...

class Payment(_message.Message):
    __slots__ = ("id", "invoice_id", "amount_cents", "at", "method", "reference")
    ID_FIELD_NUMBER: _ClassVar[int]
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    id: str
    invoice_id: str
    amount_cents: int
    at: _timestamp_pb2.Timestamp
    method: str
    reference: str
    def __init__(self, id: _Optional[str] = ..., invoice_id: _Optional[str] = ..., amount_cents: _Optional[int] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., method: _Optional[str] = ..., reference: _Optional[str] = ...) -> None: ...

class Expense(_message.Message):
    __slots__ = ("id", "vendor", "category", "amount_cents", "at", "notes", "receipt_file_id", "booked_by", "created_at", "period_start", "period_end", "source", "category_id", "paid_at", "category_needs_review")
    ID_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    BOOKED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    PERIOD_START_FIELD_NUMBER: _ClassVar[int]
    PERIOD_END_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    PAID_AT_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_NEEDS_REVIEW_FIELD_NUMBER: _ClassVar[int]
    id: str
    vendor: str
    category: str
    amount_cents: int
    at: _timestamp_pb2.Timestamp
    notes: str
    receipt_file_id: str
    booked_by: str
    created_at: _timestamp_pb2.Timestamp
    period_start: _timestamp_pb2.Timestamp
    period_end: _timestamp_pb2.Timestamp
    source: str
    category_id: str
    paid_at: _timestamp_pb2.Timestamp
    category_needs_review: bool
    def __init__(self, id: _Optional[str] = ..., vendor: _Optional[str] = ..., category: _Optional[str] = ..., amount_cents: _Optional[int] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., notes: _Optional[str] = ..., receipt_file_id: _Optional[str] = ..., booked_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., period_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., period_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., source: _Optional[str] = ..., category_id: _Optional[str] = ..., paid_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., category_needs_review: bool = ...) -> None: ...

class Category(_message.Message):
    __slots__ = ("id", "key", "name", "kind", "group", "sort", "archived", "standard")
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    STANDARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    key: str
    name: str
    kind: CategoryKind
    group: str
    sort: int
    archived: bool
    standard: bool
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., name: _Optional[str] = ..., kind: _Optional[_Union[CategoryKind, str]] = ..., group: _Optional[str] = ..., sort: _Optional[int] = ..., archived: bool = ..., standard: bool = ...) -> None: ...

class CashBalance(_message.Message):
    __slots__ = ("id", "as_of", "amount_cents", "note", "set_by", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    AS_OF_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    SET_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    as_of: _timestamp_pb2.Timestamp
    amount_cents: int
    note: str
    set_by: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., as_of: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., amount_cents: _Optional[int] = ..., note: _Optional[str] = ..., set_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CashSummary(_message.Message):
    __slots__ = ("as_of", "currency", "owed_cents", "overdue_cents", "open_invoices", "overdue_invoices", "received_30d_cents", "spent_30d_cents", "expected_30d_cents", "expected_6w_cents")
    AS_OF_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    OWED_CENTS_FIELD_NUMBER: _ClassVar[int]
    OVERDUE_CENTS_FIELD_NUMBER: _ClassVar[int]
    OPEN_INVOICES_FIELD_NUMBER: _ClassVar[int]
    OVERDUE_INVOICES_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_30D_CENTS_FIELD_NUMBER: _ClassVar[int]
    SPENT_30D_CENTS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_30D_CENTS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_6W_CENTS_FIELD_NUMBER: _ClassVar[int]
    as_of: _timestamp_pb2.Timestamp
    currency: str
    owed_cents: int
    overdue_cents: int
    open_invoices: int
    overdue_invoices: int
    received_30d_cents: int
    spent_30d_cents: int
    expected_30d_cents: int
    expected_6w_cents: int
    def __init__(self, as_of: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., currency: _Optional[str] = ..., owed_cents: _Optional[int] = ..., overdue_cents: _Optional[int] = ..., open_invoices: _Optional[int] = ..., overdue_invoices: _Optional[int] = ..., received_30d_cents: _Optional[int] = ..., spent_30d_cents: _Optional[int] = ..., expected_30d_cents: _Optional[int] = ..., expected_6w_cents: _Optional[int] = ...) -> None: ...

class GetSettingsRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class GetSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: Settings
    def __init__(self, settings: _Optional[_Union[Settings, _Mapping]] = ...) -> None: ...

class UpdateSettingsRequest(_message.Message):
    __slots__ = ("workspace_id", "settings")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    settings: Settings
    def __init__(self, workspace_id: _Optional[str] = ..., settings: _Optional[_Union[Settings, _Mapping]] = ...) -> None: ...

class UpdateSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: Settings
    def __init__(self, settings: _Optional[_Union[Settings, _Mapping]] = ...) -> None: ...

class ListCustomersRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListCustomersResponse(_message.Message):
    __slots__ = ("customers",)
    CUSTOMERS_FIELD_NUMBER: _ClassVar[int]
    customers: _containers.RepeatedCompositeFieldContainer[Customer]
    def __init__(self, customers: _Optional[_Iterable[_Union[Customer, _Mapping]]] = ...) -> None: ...

class UpsertCustomerRequest(_message.Message):
    __slots__ = ("workspace_id", "id", "name", "email", "notes")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    name: str
    email: str
    notes: str
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., notes: _Optional[str] = ...) -> None: ...

class UpsertCustomerResponse(_message.Message):
    __slots__ = ("customer",)
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    customer: Customer
    def __init__(self, customer: _Optional[_Union[Customer, _Mapping]] = ...) -> None: ...

class ListInvoicesRequest(_message.Message):
    __slots__ = ("workspace_id", "status", "customer_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    status: InvoiceStatus
    customer_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., status: _Optional[_Union[InvoiceStatus, str]] = ..., customer_id: _Optional[str] = ...) -> None: ...

class ListInvoicesResponse(_message.Message):
    __slots__ = ("invoices",)
    INVOICES_FIELD_NUMBER: _ClassVar[int]
    invoices: _containers.RepeatedCompositeFieldContainer[Invoice]
    def __init__(self, invoices: _Optional[_Iterable[_Union[Invoice, _Mapping]]] = ...) -> None: ...

class GetInvoiceRequest(_message.Message):
    __slots__ = ("workspace_id", "id", "rotate")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ROTATE_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    rotate: bool
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ..., rotate: bool = ...) -> None: ...

class GetInvoiceResponse(_message.Message):
    __slots__ = ("invoice", "payments")
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    invoice: Invoice
    payments: _containers.RepeatedCompositeFieldContainer[Payment]
    def __init__(self, invoice: _Optional[_Union[Invoice, _Mapping]] = ..., payments: _Optional[_Iterable[_Union[Payment, _Mapping]]] = ...) -> None: ...

class CreateInvoiceRequest(_message.Message):
    __slots__ = ("workspace_id", "customer_id", "customer_name", "lines", "tax_cents", "due_days", "notes", "thread_root_id", "send", "category_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    TAX_CENTS_FIELD_NUMBER: _ClassVar[int]
    DUE_DAYS_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    SEND_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    customer_id: str
    customer_name: str
    lines: _containers.RepeatedCompositeFieldContainer[InvoiceLine]
    tax_cents: int
    due_days: int
    notes: str
    thread_root_id: str
    send: bool
    category_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., customer_id: _Optional[str] = ..., customer_name: _Optional[str] = ..., lines: _Optional[_Iterable[_Union[InvoiceLine, _Mapping]]] = ..., tax_cents: _Optional[int] = ..., due_days: _Optional[int] = ..., notes: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., send: bool = ..., category_id: _Optional[str] = ...) -> None: ...

class CreateInvoiceResponse(_message.Message):
    __slots__ = ("invoice",)
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: Invoice
    def __init__(self, invoice: _Optional[_Union[Invoice, _Mapping]] = ...) -> None: ...

class SendInvoiceRequest(_message.Message):
    __slots__ = ("workspace_id", "id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class SendInvoiceResponse(_message.Message):
    __slots__ = ("invoice",)
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: Invoice
    def __init__(self, invoice: _Optional[_Union[Invoice, _Mapping]] = ...) -> None: ...

class RecordPaymentRequest(_message.Message):
    __slots__ = ("workspace_id", "invoice_id", "amount_cents", "method", "reference", "at", "evidence_message_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    invoice_id: str
    amount_cents: int
    method: str
    reference: str
    at: _timestamp_pb2.Timestamp
    evidence_message_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., invoice_id: _Optional[str] = ..., amount_cents: _Optional[int] = ..., method: _Optional[str] = ..., reference: _Optional[str] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., evidence_message_id: _Optional[str] = ...) -> None: ...

class RecordPaymentResponse(_message.Message):
    __slots__ = ("invoice", "payment")
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    invoice: Invoice
    payment: Payment
    def __init__(self, invoice: _Optional[_Union[Invoice, _Mapping]] = ..., payment: _Optional[_Union[Payment, _Mapping]] = ...) -> None: ...

class VoidInvoiceRequest(_message.Message):
    __slots__ = ("workspace_id", "id", "reason")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    reason: str
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class VoidInvoiceResponse(_message.Message):
    __slots__ = ("invoice",)
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: Invoice
    def __init__(self, invoice: _Optional[_Union[Invoice, _Mapping]] = ...) -> None: ...

class ListExpensesRequest(_message.Message):
    __slots__ = ("workspace_id", "days", "needs_review")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    NEEDS_REVIEW_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    days: int
    needs_review: bool
    def __init__(self, workspace_id: _Optional[str] = ..., days: _Optional[int] = ..., needs_review: bool = ...) -> None: ...

class ListExpensesResponse(_message.Message):
    __slots__ = ("expenses",)
    EXPENSES_FIELD_NUMBER: _ClassVar[int]
    expenses: _containers.RepeatedCompositeFieldContainer[Expense]
    def __init__(self, expenses: _Optional[_Iterable[_Union[Expense, _Mapping]]] = ...) -> None: ...

class RecordExpenseRequest(_message.Message):
    __slots__ = ("workspace_id", "vendor", "category", "amount_cents", "at", "notes", "receipt_file_id", "period_start", "period_end", "source", "category_id", "paid", "paid_at")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    PERIOD_START_FIELD_NUMBER: _ClassVar[int]
    PERIOD_END_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    PAID_FIELD_NUMBER: _ClassVar[int]
    PAID_AT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    vendor: str
    category: str
    amount_cents: int
    at: _timestamp_pb2.Timestamp
    notes: str
    receipt_file_id: str
    period_start: _timestamp_pb2.Timestamp
    period_end: _timestamp_pb2.Timestamp
    source: str
    category_id: str
    paid: bool
    paid_at: _timestamp_pb2.Timestamp
    def __init__(self, workspace_id: _Optional[str] = ..., vendor: _Optional[str] = ..., category: _Optional[str] = ..., amount_cents: _Optional[int] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., notes: _Optional[str] = ..., receipt_file_id: _Optional[str] = ..., period_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., period_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., source: _Optional[str] = ..., category_id: _Optional[str] = ..., paid: bool = ..., paid_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RecordExpenseResponse(_message.Message):
    __slots__ = ("expense", "outcome")
    EXPENSE_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    expense: Expense
    outcome: str
    def __init__(self, expense: _Optional[_Union[Expense, _Mapping]] = ..., outcome: _Optional[str] = ...) -> None: ...

class GetCashSummaryRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class GetCashSummaryResponse(_message.Message):
    __slots__ = ("summary",)
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    summary: CashSummary
    def __init__(self, summary: _Optional[_Union[CashSummary, _Mapping]] = ...) -> None: ...

class BankTransaction(_message.Message):
    __slots__ = ("id", "at", "description", "amount_cents", "reference", "matched_kind", "matched_id", "matched_label", "explanation", "suggested_kind", "suggested_id", "suggested_label", "suggested_confidence")
    ID_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    MATCHED_KIND_FIELD_NUMBER: _ClassVar[int]
    MATCHED_ID_FIELD_NUMBER: _ClassVar[int]
    MATCHED_LABEL_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_KIND_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_ID_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_LABEL_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    id: str
    at: _timestamp_pb2.Timestamp
    description: str
    amount_cents: int
    reference: str
    matched_kind: str
    matched_id: str
    matched_label: str
    explanation: str
    suggested_kind: str
    suggested_id: str
    suggested_label: str
    suggested_confidence: float
    def __init__(self, id: _Optional[str] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., description: _Optional[str] = ..., amount_cents: _Optional[int] = ..., reference: _Optional[str] = ..., matched_kind: _Optional[str] = ..., matched_id: _Optional[str] = ..., matched_label: _Optional[str] = ..., explanation: _Optional[str] = ..., suggested_kind: _Optional[str] = ..., suggested_id: _Optional[str] = ..., suggested_label: _Optional[str] = ..., suggested_confidence: _Optional[float] = ...) -> None: ...

class ImportBankTransactionsRequest(_message.Message):
    __slots__ = ("workspace_id", "csv", "account_name")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CSV_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    csv: str
    account_name: str
    def __init__(self, workspace_id: _Optional[str] = ..., csv: _Optional[str] = ..., account_name: _Optional[str] = ...) -> None: ...

class ImportBankTransactionsResponse(_message.Message):
    __slots__ = ("imported", "skipped", "auto_matched", "transactions")
    IMPORTED_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_FIELD_NUMBER: _ClassVar[int]
    AUTO_MATCHED_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    imported: int
    skipped: int
    auto_matched: int
    transactions: _containers.RepeatedCompositeFieldContainer[BankTransaction]
    def __init__(self, imported: _Optional[int] = ..., skipped: _Optional[int] = ..., auto_matched: _Optional[int] = ..., transactions: _Optional[_Iterable[_Union[BankTransaction, _Mapping]]] = ...) -> None: ...

class ListBankTransactionsRequest(_message.Message):
    __slots__ = ("workspace_id", "unmatched_only")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    UNMATCHED_ONLY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    unmatched_only: bool
    def __init__(self, workspace_id: _Optional[str] = ..., unmatched_only: bool = ...) -> None: ...

class ListBankTransactionsResponse(_message.Message):
    __slots__ = ("transactions",)
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[BankTransaction]
    def __init__(self, transactions: _Optional[_Iterable[_Union[BankTransaction, _Mapping]]] = ...) -> None: ...

class MatchBankTransactionRequest(_message.Message):
    __slots__ = ("workspace_id", "transaction_id", "invoice_id", "expense_id", "new_expense_vendor", "new_expense_category")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPENSE_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_EXPENSE_VENDOR_FIELD_NUMBER: _ClassVar[int]
    NEW_EXPENSE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    transaction_id: str
    invoice_id: str
    expense_id: str
    new_expense_vendor: str
    new_expense_category: str
    def __init__(self, workspace_id: _Optional[str] = ..., transaction_id: _Optional[str] = ..., invoice_id: _Optional[str] = ..., expense_id: _Optional[str] = ..., new_expense_vendor: _Optional[str] = ..., new_expense_category: _Optional[str] = ...) -> None: ...

class MatchBankTransactionResponse(_message.Message):
    __slots__ = ("transaction",)
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: BankTransaction
    def __init__(self, transaction: _Optional[_Union[BankTransaction, _Mapping]] = ...) -> None: ...

class ReportLine(_message.Message):
    __slots__ = ("label", "cents")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    CENTS_FIELD_NUMBER: _ClassVar[int]
    label: str
    cents: int
    def __init__(self, label: _Optional[str] = ..., cents: _Optional[int] = ...) -> None: ...

class Report(_message.Message):
    __slots__ = ("to", "currency", "revenue_cents", "expenses_cents", "profit_cents", "received_cents", "cash_cents", "receivable_cents", "expenses_by_category", "revenue_by_customer", "sentence")
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    REVENUE_CENTS_FIELD_NUMBER: _ClassVar[int]
    EXPENSES_CENTS_FIELD_NUMBER: _ClassVar[int]
    PROFIT_CENTS_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_CENTS_FIELD_NUMBER: _ClassVar[int]
    CASH_CENTS_FIELD_NUMBER: _ClassVar[int]
    RECEIVABLE_CENTS_FIELD_NUMBER: _ClassVar[int]
    EXPENSES_BY_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    REVENUE_BY_CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    SENTENCE_FIELD_NUMBER: _ClassVar[int]
    to: _timestamp_pb2.Timestamp
    currency: str
    revenue_cents: int
    expenses_cents: int
    profit_cents: int
    received_cents: int
    cash_cents: int
    receivable_cents: int
    expenses_by_category: _containers.RepeatedCompositeFieldContainer[ReportLine]
    revenue_by_customer: _containers.RepeatedCompositeFieldContainer[ReportLine]
    sentence: str
    def __init__(self, to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., currency: _Optional[str] = ..., revenue_cents: _Optional[int] = ..., expenses_cents: _Optional[int] = ..., profit_cents: _Optional[int] = ..., received_cents: _Optional[int] = ..., cash_cents: _Optional[int] = ..., receivable_cents: _Optional[int] = ..., expenses_by_category: _Optional[_Iterable[_Union[ReportLine, _Mapping]]] = ..., revenue_by_customer: _Optional[_Iterable[_Union[ReportLine, _Mapping]]] = ..., sentence: _Optional[str] = ..., **kwargs) -> None: ...

class ReadReceiptRequest(_message.Message):
    __slots__ = ("workspace_id", "file_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    file_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., file_id: _Optional[str] = ...) -> None: ...

class ReadReceiptResponse(_message.Message):
    __slots__ = ("vendor", "category", "amount_cents", "at", "confidence", "note", "currency")
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    vendor: str
    category: str
    amount_cents: int
    at: _timestamp_pb2.Timestamp
    confidence: float
    note: str
    currency: str
    def __init__(self, vendor: _Optional[str] = ..., category: _Optional[str] = ..., amount_cents: _Optional[int] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., confidence: _Optional[float] = ..., note: _Optional[str] = ..., currency: _Optional[str] = ...) -> None: ...

class ExportRequest(_message.Message):
    __slots__ = ("workspace_id", "period", "kind", "statement", "to")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    period: str
    kind: str
    statement: GetStatementRequest
    to: _timestamp_pb2.Timestamp
    def __init__(self, workspace_id: _Optional[str] = ..., period: _Optional[str] = ..., kind: _Optional[str] = ..., statement: _Optional[_Union[GetStatementRequest, _Mapping]] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...

class ExportResponse(_message.Message):
    __slots__ = ("filename", "csv", "rows")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    CSV_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    filename: str
    csv: str
    rows: int
    def __init__(self, filename: _Optional[str] = ..., csv: _Optional[str] = ..., rows: _Optional[int] = ...) -> None: ...

class GetReportRequest(_message.Message):
    __slots__ = ("workspace_id", "period", "to")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    period: str
    to: _timestamp_pb2.Timestamp
    def __init__(self, workspace_id: _Optional[str] = ..., period: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...

class GetReportResponse(_message.Message):
    __slots__ = ("report",)
    REPORT_FIELD_NUMBER: _ClassVar[int]
    report: Report
    def __init__(self, report: _Optional[_Union[Report, _Mapping]] = ...) -> None: ...

class ListCategoriesRequest(_message.Message):
    __slots__ = ("workspace_id", "include_archived")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    include_archived: bool
    def __init__(self, workspace_id: _Optional[str] = ..., include_archived: bool = ...) -> None: ...

class ListCategoriesResponse(_message.Message):
    __slots__ = ("categories",)
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    categories: _containers.RepeatedCompositeFieldContainer[Category]
    def __init__(self, categories: _Optional[_Iterable[_Union[Category, _Mapping]]] = ...) -> None: ...

class UpsertCategoryRequest(_message.Message):
    __slots__ = ("workspace_id", "id", "name", "group", "archived", "sort")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    name: str
    group: str
    archived: bool
    sort: int
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., group: _Optional[str] = ..., archived: bool = ..., sort: _Optional[int] = ...) -> None: ...

class UpsertCategoryResponse(_message.Message):
    __slots__ = ("category",)
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    category: Category
    def __init__(self, category: _Optional[_Union[Category, _Mapping]] = ...) -> None: ...

class SetCashBalanceRequest(_message.Message):
    __slots__ = ("workspace_id", "as_of", "amount_cents", "note")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    AS_OF_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    as_of: _timestamp_pb2.Timestamp
    amount_cents: int
    note: str
    def __init__(self, workspace_id: _Optional[str] = ..., as_of: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., amount_cents: _Optional[int] = ..., note: _Optional[str] = ...) -> None: ...

class SetCashBalanceResponse(_message.Message):
    __slots__ = ("balance",)
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    balance: CashBalance
    def __init__(self, balance: _Optional[_Union[CashBalance, _Mapping]] = ...) -> None: ...

class PayExpenseRequest(_message.Message):
    __slots__ = ("workspace_id", "id", "paid_at")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PAID_AT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    paid_at: _timestamp_pb2.Timestamp
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ..., paid_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PayExpenseResponse(_message.Message):
    __slots__ = ("expense",)
    EXPENSE_FIELD_NUMBER: _ClassVar[int]
    expense: Expense
    def __init__(self, expense: _Optional[_Union[Expense, _Mapping]] = ...) -> None: ...

class StatementPeriod(_message.Message):
    __slots__ = ("key", "label", "start", "end", "kind")
    KEY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    key: str
    label: str
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    kind: PeriodKind
    def __init__(self, key: _Optional[str] = ..., label: _Optional[str] = ..., start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., kind: _Optional[_Union[PeriodKind, str]] = ...) -> None: ...

class StatementCell(_message.Message):
    __slots__ = ("actual_cents", "expected_cents", "budget_cents", "state", "missed_cents", "missed_count")
    ACTUAL_CENTS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_CENTS_FIELD_NUMBER: _ClassVar[int]
    BUDGET_CENTS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    MISSED_CENTS_FIELD_NUMBER: _ClassVar[int]
    MISSED_COUNT_FIELD_NUMBER: _ClassVar[int]
    actual_cents: int
    expected_cents: int
    budget_cents: int
    state: CellState
    missed_cents: int
    missed_count: int
    def __init__(self, actual_cents: _Optional[int] = ..., expected_cents: _Optional[int] = ..., budget_cents: _Optional[int] = ..., state: _Optional[_Union[CellState, str]] = ..., missed_cents: _Optional[int] = ..., missed_count: _Optional[int] = ...) -> None: ...

class StatementRow(_message.Message):
    __slots__ = ("kind", "category_id", "group", "label", "key", "cells", "total")
    KIND_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    CELLS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    kind: StatementRowKind
    category_id: str
    group: str
    label: str
    key: str
    cells: _containers.RepeatedCompositeFieldContainer[StatementCell]
    total: StatementCell
    def __init__(self, kind: _Optional[_Union[StatementRowKind, str]] = ..., category_id: _Optional[str] = ..., group: _Optional[str] = ..., label: _Optional[str] = ..., key: _Optional[str] = ..., cells: _Optional[_Iterable[_Union[StatementCell, _Mapping]]] = ..., total: _Optional[_Union[StatementCell, _Mapping]] = ...) -> None: ...

class GetStatementRequest(_message.Message):
    __slots__ = ("workspace_id", "grain", "basis", "from_period", "to_period", "to", "scenario_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    GRAIN_FIELD_NUMBER: _ClassVar[int]
    BASIS_FIELD_NUMBER: _ClassVar[int]
    FROM_PERIOD_FIELD_NUMBER: _ClassVar[int]
    TO_PERIOD_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    grain: StatementGrain
    basis: StatementBasis
    from_period: str
    to_period: str
    to: _timestamp_pb2.Timestamp
    scenario_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., grain: _Optional[_Union[StatementGrain, str]] = ..., basis: _Optional[_Union[StatementBasis, str]] = ..., from_period: _Optional[str] = ..., to_period: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., scenario_id: _Optional[str] = ..., **kwargs) -> None: ...

class GetStatementResponse(_message.Message):
    __slots__ = ("currency", "grain", "basis", "fiscal_year_start_month", "timezone", "periods", "rows", "net", "cash_in", "cash_out", "ending_cash", "has_opening_balance", "opening_balance", "runway")
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    GRAIN_FIELD_NUMBER: _ClassVar[int]
    BASIS_FIELD_NUMBER: _ClassVar[int]
    FISCAL_YEAR_START_MONTH_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    PERIODS_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    NET_FIELD_NUMBER: _ClassVar[int]
    CASH_IN_FIELD_NUMBER: _ClassVar[int]
    CASH_OUT_FIELD_NUMBER: _ClassVar[int]
    ENDING_CASH_FIELD_NUMBER: _ClassVar[int]
    HAS_OPENING_BALANCE_FIELD_NUMBER: _ClassVar[int]
    OPENING_BALANCE_FIELD_NUMBER: _ClassVar[int]
    RUNWAY_FIELD_NUMBER: _ClassVar[int]
    currency: str
    grain: StatementGrain
    basis: StatementBasis
    fiscal_year_start_month: int
    timezone: str
    periods: _containers.RepeatedCompositeFieldContainer[StatementPeriod]
    rows: _containers.RepeatedCompositeFieldContainer[StatementRow]
    net: StatementRow
    cash_in: StatementRow
    cash_out: StatementRow
    ending_cash: StatementRow
    has_opening_balance: bool
    opening_balance: CashBalance
    runway: Runway
    def __init__(self, currency: _Optional[str] = ..., grain: _Optional[_Union[StatementGrain, str]] = ..., basis: _Optional[_Union[StatementBasis, str]] = ..., fiscal_year_start_month: _Optional[int] = ..., timezone: _Optional[str] = ..., periods: _Optional[_Iterable[_Union[StatementPeriod, _Mapping]]] = ..., rows: _Optional[_Iterable[_Union[StatementRow, _Mapping]]] = ..., net: _Optional[_Union[StatementRow, _Mapping]] = ..., cash_in: _Optional[_Union[StatementRow, _Mapping]] = ..., cash_out: _Optional[_Union[StatementRow, _Mapping]] = ..., ending_cash: _Optional[_Union[StatementRow, _Mapping]] = ..., has_opening_balance: bool = ..., opening_balance: _Optional[_Union[CashBalance, _Mapping]] = ..., runway: _Optional[_Union[Runway, _Mapping]] = ...) -> None: ...

class Recurring(_message.Message):
    __slots__ = ("id", "kind", "category_id", "customer_id", "customer_name", "vendor", "name", "amount_cents", "cadence", "anchor_day", "starts_on", "ends_on", "basis_offset_days", "source", "status", "created_by", "created_at", "read_only", "seen_count", "seen_since", "next_on", "daily_average_cents", "capped", "cap_cents")
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    CADENCE_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_DAY_FIELD_NUMBER: _ClassVar[int]
    STARTS_ON_FIELD_NUMBER: _ClassVar[int]
    ENDS_ON_FIELD_NUMBER: _ClassVar[int]
    BASIS_OFFSET_DAYS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    SEEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    SEEN_SINCE_FIELD_NUMBER: _ClassVar[int]
    NEXT_ON_FIELD_NUMBER: _ClassVar[int]
    DAILY_AVERAGE_CENTS_FIELD_NUMBER: _ClassVar[int]
    CAPPED_FIELD_NUMBER: _ClassVar[int]
    CAP_CENTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    kind: CategoryKind
    category_id: str
    customer_id: str
    customer_name: str
    vendor: str
    name: str
    amount_cents: int
    cadence: Cadence
    anchor_day: int
    starts_on: _timestamp_pb2.Timestamp
    ends_on: _timestamp_pb2.Timestamp
    basis_offset_days: int
    source: RecurringSource
    status: RecurringStatus
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    read_only: bool
    seen_count: int
    seen_since: _timestamp_pb2.Timestamp
    next_on: _timestamp_pb2.Timestamp
    daily_average_cents: int
    capped: bool
    cap_cents: int
    def __init__(self, id: _Optional[str] = ..., kind: _Optional[_Union[CategoryKind, str]] = ..., category_id: _Optional[str] = ..., customer_id: _Optional[str] = ..., customer_name: _Optional[str] = ..., vendor: _Optional[str] = ..., name: _Optional[str] = ..., amount_cents: _Optional[int] = ..., cadence: _Optional[_Union[Cadence, str]] = ..., anchor_day: _Optional[int] = ..., starts_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ends_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., basis_offset_days: _Optional[int] = ..., source: _Optional[_Union[RecurringSource, str]] = ..., status: _Optional[_Union[RecurringStatus, str]] = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., read_only: bool = ..., seen_count: _Optional[int] = ..., seen_since: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., next_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., daily_average_cents: _Optional[int] = ..., capped: bool = ..., cap_cents: _Optional[int] = ...) -> None: ...

class Occurrence(_message.Message):
    __slots__ = ("recurring_id", "on", "amount_cents", "kind", "category_id", "name")
    RECURRING_ID_FIELD_NUMBER: _ClassVar[int]
    ON_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    recurring_id: str
    on: _timestamp_pb2.Timestamp
    amount_cents: int
    kind: CategoryKind
    category_id: str
    name: str
    def __init__(self, recurring_id: _Optional[str] = ..., on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., amount_cents: _Optional[int] = ..., kind: _Optional[_Union[CategoryKind, str]] = ..., category_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class Runway(_message.Message):
    __slots__ = ("runs_out_month", "runs_out_at", "horizon_month", "lowest_cents", "lowest_month")
    RUNS_OUT_MONTH_FIELD_NUMBER: _ClassVar[int]
    RUNS_OUT_AT_FIELD_NUMBER: _ClassVar[int]
    HORIZON_MONTH_FIELD_NUMBER: _ClassVar[int]
    LOWEST_CENTS_FIELD_NUMBER: _ClassVar[int]
    LOWEST_MONTH_FIELD_NUMBER: _ClassVar[int]
    runs_out_month: str
    runs_out_at: _timestamp_pb2.Timestamp
    horizon_month: str
    lowest_cents: int
    lowest_month: str
    def __init__(self, runs_out_month: _Optional[str] = ..., runs_out_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., horizon_month: _Optional[str] = ..., lowest_cents: _Optional[int] = ..., lowest_month: _Optional[str] = ...) -> None: ...

class ListRecurringRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListRecurringResponse(_message.Message):
    __slots__ = ("rules", "proposals", "tank", "not_seen", "runway", "can_edit", "currency")
    RULES_FIELD_NUMBER: _ClassVar[int]
    PROPOSALS_FIELD_NUMBER: _ClassVar[int]
    TANK_FIELD_NUMBER: _ClassVar[int]
    NOT_SEEN_FIELD_NUMBER: _ClassVar[int]
    RUNWAY_FIELD_NUMBER: _ClassVar[int]
    CAN_EDIT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[Recurring]
    proposals: _containers.RepeatedCompositeFieldContainer[Recurring]
    tank: _containers.RepeatedCompositeFieldContainer[Recurring]
    not_seen: _containers.RepeatedCompositeFieldContainer[Occurrence]
    runway: Runway
    can_edit: bool
    currency: str
    def __init__(self, rules: _Optional[_Iterable[_Union[Recurring, _Mapping]]] = ..., proposals: _Optional[_Iterable[_Union[Recurring, _Mapping]]] = ..., tank: _Optional[_Iterable[_Union[Recurring, _Mapping]]] = ..., not_seen: _Optional[_Iterable[_Union[Occurrence, _Mapping]]] = ..., runway: _Optional[_Union[Runway, _Mapping]] = ..., can_edit: bool = ..., currency: _Optional[str] = ...) -> None: ...

class UpsertRecurringRequest(_message.Message):
    __slots__ = ("workspace_id", "rule")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    rule: Recurring
    def __init__(self, workspace_id: _Optional[str] = ..., rule: _Optional[_Union[Recurring, _Mapping]] = ...) -> None: ...

class UpsertRecurringResponse(_message.Message):
    __slots__ = ("rule",)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: Recurring
    def __init__(self, rule: _Optional[_Union[Recurring, _Mapping]] = ...) -> None: ...

class SetRecurringStatusRequest(_message.Message):
    __slots__ = ("workspace_id", "id", "status")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    status: RecurringStatus
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ..., status: _Optional[_Union[RecurringStatus, str]] = ...) -> None: ...

class SetRecurringStatusResponse(_message.Message):
    __slots__ = ("rule",)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: Recurring
    def __init__(self, rule: _Optional[_Union[Recurring, _Mapping]] = ...) -> None: ...

class ListTransactionsRequest(_message.Message):
    __slots__ = ("workspace_id", "category_id", "start", "end", "basis")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    BASIS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    category_id: str
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    basis: StatementBasis
    def __init__(self, workspace_id: _Optional[str] = ..., category_id: _Optional[str] = ..., start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., basis: _Optional[_Union[StatementBasis, str]] = ...) -> None: ...

class StatementTransaction(_message.Message):
    __slots__ = ("kind", "id", "at", "label", "amount_cents", "memo", "invoice_id", "category_id")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    kind: str
    id: str
    at: _timestamp_pb2.Timestamp
    label: str
    amount_cents: int
    memo: str
    invoice_id: str
    category_id: str
    def __init__(self, kind: _Optional[str] = ..., id: _Optional[str] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., label: _Optional[str] = ..., amount_cents: _Optional[int] = ..., memo: _Optional[str] = ..., invoice_id: _Optional[str] = ..., category_id: _Optional[str] = ...) -> None: ...

class ListTransactionsResponse(_message.Message):
    __slots__ = ("transactions", "total_cents")
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CENTS_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[StatementTransaction]
    total_cents: int
    def __init__(self, transactions: _Optional[_Iterable[_Union[StatementTransaction, _Mapping]]] = ..., total_cents: _Optional[int] = ...) -> None: ...
