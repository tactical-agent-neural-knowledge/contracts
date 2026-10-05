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
INVOICE_STATUS_UNSPECIFIED: InvoiceStatus
INVOICE_STATUS_DRAFT: InvoiceStatus
INVOICE_STATUS_SENT: InvoiceStatus
INVOICE_STATUS_OVERDUE: InvoiceStatus
INVOICE_STATUS_PAID: InvoiceStatus
INVOICE_STATUS_VOID: InvoiceStatus

class Settings(_message.Message):
    __slots__ = ("enabled", "currency", "business_name", "invoice_prefix", "next_invoice_number", "default_due_days", "chase_every_days", "competes_with", "payment_instructions")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    INVOICE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    NEXT_INVOICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DUE_DAYS_FIELD_NUMBER: _ClassVar[int]
    CHASE_EVERY_DAYS_FIELD_NUMBER: _ClassVar[int]
    COMPETES_WITH_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    currency: str
    business_name: str
    invoice_prefix: str
    next_invoice_number: int
    default_due_days: int
    chase_every_days: int
    competes_with: _containers.RepeatedScalarFieldContainer[str]
    payment_instructions: str
    def __init__(self, enabled: bool = ..., currency: _Optional[str] = ..., business_name: _Optional[str] = ..., invoice_prefix: _Optional[str] = ..., next_invoice_number: _Optional[int] = ..., default_due_days: _Optional[int] = ..., chase_every_days: _Optional[int] = ..., competes_with: _Optional[_Iterable[str]] = ..., payment_instructions: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("id", "customer_id", "customer_name", "number", "status", "lines", "subtotal_cents", "tax_cents", "total_cents", "paid_cents", "due_cents", "issued_at", "due_at", "sent_at", "paid_at", "notes", "thread_root_id", "predicted_paid_at", "predicted_confidence", "last_chased_at", "chase_count", "share_url")
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
    def __init__(self, id: _Optional[str] = ..., customer_id: _Optional[str] = ..., customer_name: _Optional[str] = ..., number: _Optional[str] = ..., status: _Optional[_Union[InvoiceStatus, str]] = ..., lines: _Optional[_Iterable[_Union[InvoiceLine, _Mapping]]] = ..., subtotal_cents: _Optional[int] = ..., tax_cents: _Optional[int] = ..., total_cents: _Optional[int] = ..., paid_cents: _Optional[int] = ..., due_cents: _Optional[int] = ..., issued_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., due_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sent_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., paid_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., notes: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., predicted_paid_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., predicted_confidence: _Optional[float] = ..., last_chased_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., chase_count: _Optional[int] = ..., share_url: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("id", "vendor", "category", "amount_cents", "at", "notes", "receipt_file_id", "booked_by", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    BOOKED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    vendor: str
    category: str
    amount_cents: int
    at: _timestamp_pb2.Timestamp
    notes: str
    receipt_file_id: str
    booked_by: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., vendor: _Optional[str] = ..., category: _Optional[str] = ..., amount_cents: _Optional[int] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., notes: _Optional[str] = ..., receipt_file_id: _Optional[str] = ..., booked_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("workspace_id", "id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class GetInvoiceResponse(_message.Message):
    __slots__ = ("invoice", "payments")
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    invoice: Invoice
    payments: _containers.RepeatedCompositeFieldContainer[Payment]
    def __init__(self, invoice: _Optional[_Union[Invoice, _Mapping]] = ..., payments: _Optional[_Iterable[_Union[Payment, _Mapping]]] = ...) -> None: ...

class CreateInvoiceRequest(_message.Message):
    __slots__ = ("workspace_id", "customer_id", "customer_name", "lines", "tax_cents", "due_days", "notes", "thread_root_id", "send")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    TAX_CENTS_FIELD_NUMBER: _ClassVar[int]
    DUE_DAYS_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    THREAD_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    SEND_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    customer_id: str
    customer_name: str
    lines: _containers.RepeatedCompositeFieldContainer[InvoiceLine]
    tax_cents: int
    due_days: int
    notes: str
    thread_root_id: str
    send: bool
    def __init__(self, workspace_id: _Optional[str] = ..., customer_id: _Optional[str] = ..., customer_name: _Optional[str] = ..., lines: _Optional[_Iterable[_Union[InvoiceLine, _Mapping]]] = ..., tax_cents: _Optional[int] = ..., due_days: _Optional[int] = ..., notes: _Optional[str] = ..., thread_root_id: _Optional[str] = ..., send: bool = ...) -> None: ...

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
    __slots__ = ("workspace_id", "invoice_id", "amount_cents", "method", "reference", "at")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    invoice_id: str
    amount_cents: int
    method: str
    reference: str
    at: _timestamp_pb2.Timestamp
    def __init__(self, workspace_id: _Optional[str] = ..., invoice_id: _Optional[str] = ..., amount_cents: _Optional[int] = ..., method: _Optional[str] = ..., reference: _Optional[str] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("workspace_id", "days")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    days: int
    def __init__(self, workspace_id: _Optional[str] = ..., days: _Optional[int] = ...) -> None: ...

class ListExpensesResponse(_message.Message):
    __slots__ = ("expenses",)
    EXPENSES_FIELD_NUMBER: _ClassVar[int]
    expenses: _containers.RepeatedCompositeFieldContainer[Expense]
    def __init__(self, expenses: _Optional[_Iterable[_Union[Expense, _Mapping]]] = ...) -> None: ...

class RecordExpenseRequest(_message.Message):
    __slots__ = ("workspace_id", "vendor", "category", "amount_cents", "at", "notes", "receipt_file_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_CENTS_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    vendor: str
    category: str
    amount_cents: int
    at: _timestamp_pb2.Timestamp
    notes: str
    receipt_file_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., vendor: _Optional[str] = ..., category: _Optional[str] = ..., amount_cents: _Optional[int] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., notes: _Optional[str] = ..., receipt_file_id: _Optional[str] = ...) -> None: ...

class RecordExpenseResponse(_message.Message):
    __slots__ = ("expense",)
    EXPENSE_FIELD_NUMBER: _ClassVar[int]
    expense: Expense
    def __init__(self, expense: _Optional[_Union[Expense, _Mapping]] = ...) -> None: ...

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

class GetReportRequest(_message.Message):
    __slots__ = ("workspace_id", "period")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    period: str
    def __init__(self, workspace_id: _Optional[str] = ..., period: _Optional[str] = ...) -> None: ...

class GetReportResponse(_message.Message):
    __slots__ = ("report",)
    REPORT_FIELD_NUMBER: _ClassVar[int]
    report: Report
    def __init__(self, report: _Optional[_Union[Report, _Mapping]] = ...) -> None: ...
