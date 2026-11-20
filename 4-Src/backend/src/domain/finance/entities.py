from dataclasses import dataclass, field
from datetime import date
from typing import Optional
from uuid import UUID, uuid4

from ..shared.enums import ActiveStatus, CalculationType
from ..shared.value_objects import AuditInfo


@dataclass
class StaffContract:
    profile_id: UUID
    staff_contract_type_id: UUID
    start_date: date
    end_date: date
    title: str
    id: UUID = field(default_factory=uuid4)
    description: Optional[str] = None
    auto_renewal: Optional[bool] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class ContractSalaryItem:
    staff_contract_id: UUID
    calculation_time_unit_id: UUID
    title: str
    amount: float
    currency_id: UUID
    id: UUID = field(default_factory=uuid4)
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class ContractDeductionItem:
    calculation_type: CalculationType
    staff_contract_id: UUID
    calculation_time_unit_id: UUID
    title: str
    id: UUID = field(default_factory=uuid4)
    deduction_percentage: Optional[float] = None
    fixed_amount: Optional[float] = None
    fixed_amount_currency_id: Optional[UUID] = None
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class Supplier:
    title: str
    code: str
    id: UUID = field(default_factory=uuid4)
    phone_number: Optional[str] = None
    mobile_number: Optional[str] = None
    fax_number: Optional[str] = None
    email: Optional[str] = None
    postal_code: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class CostInvoice:
    invoice_number: str
    supplier_id: UUID
    document_id: UUID
    invoice_date: date
    total_amount: float
    currency_id: UUID
    id: UUID = field(default_factory=uuid4)
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class CostInvoiceItem:
    cost_invoice_id: UUID
    item_title: str
    unit_amount: float
    currency_id: UUID
    quantity: float
    id: UUID = field(default_factory=uuid4)
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class ProjectDirectCostItem:
    project_id: UUID
    cost_invoice_item_id: UUID
    allocated_quantity: float
    id: UUID = field(default_factory=uuid4)
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class CostPaymentReceipt:
    receipt_number: str
    cost_invoice_id: UUID
    document_id: UUID
    payment_date: date
    amount: float
    currency_id: UUID
    id: UUID = field(default_factory=uuid4)
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class SalaryPaymentReceipt:
    receipt_number: str
    staff_contract_id: UUID
    document_id: UUID
    payment_date: date
    amount: float
    currency_id: UUID
    id: UUID = field(default_factory=uuid4)
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class StaffAdditionalPaymentReceipt:
    profile_id: UUID
    title: str
    document_id: UUID
    payment_date: date
    amount: float
    currency_id: UUID
    id: UUID = field(default_factory=uuid4)
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class Customer:
    title: str
    code: str
    id: UUID = field(default_factory=uuid4)
    phone_number: Optional[str] = None
    mobile_number: Optional[str] = None
    fax_number: Optional[str] = None
    email: Optional[str] = None
    postal_code: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class CustomerContract:
    customer_id: UUID
    project_id: UUID
    customer_contract_type_id: UUID
    contract_number: str
    total_amount: float
    currency_id: UUID
    document_id: UUID
    id: UUID = field(default_factory=uuid4)
    start_date: Optional[date] = None
    scheduled_end_date: Optional[date] = None
    real_end_date: Optional[date] = None
    is_development_contract: Optional[bool] = None
    is_support_contract: Optional[bool] = None
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class CustomerContractPaymentSchedule:
    customer_contract_id: UUID
    payment_title: str
    amount: float
    currency_id: UUID
    id: UUID = field(default_factory=uuid4)
    project_release_id: Optional[UUID] = None
    scheduled_payment_date: Optional[date] = None
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class CustomerContractPaymentReceipt:
    customer_contract_payment_schedule_id: UUID
    receipt_number: str
    amount: float
    currency_id: UUID
    id: UUID = field(default_factory=uuid4)
    receipt_document_id: Optional[UUID] = None
    payment_date: Optional[date] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None