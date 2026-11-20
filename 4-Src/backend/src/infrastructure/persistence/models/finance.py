from sqlalchemy import Column, String, Date, Boolean, ForeignKey, Float, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.infrastructure.persistence.base_model import (
    Base, UUIDPrimaryKeyMixin, AuditColumnsMixin
)
from src.infrastructure.persistence.enums_pg import active_status, calculation_type

SCHEMA = "Finance"


class StaffContractModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "StaffContract"
    __table_args__ = {"schema": SCHEMA}
    ProfileId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Profile.Id"), nullable=False)
    StaffContractTypeId = Column(UUID(as_uuid=True), ForeignKey("Basic.StaffContractType.Id"), nullable=False)
    StartDate = Column(Date, nullable=False)
    EndDate = Column(Date, nullable=False)
    Title = Column(String(255), nullable=False)
    Description = Column(String(4000))
    AutoRenewal = Column(Boolean)
    ActiveStatus = active_status


class ContractSalaryItemModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "ContractSalaryItem"
    __table_args__ = {"schema": SCHEMA}
    StaffContractId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.StaffContract.Id"), nullable=False)
    CalculationTimeUnitId = Column(UUID(as_uuid=True), ForeignKey("Basic.TimeUnit.Id"), nullable=False)
    Title = Column(String(255), nullable=False)
    Amount = Column(Numeric(22, 2), nullable=False)
    CurrencyId = Column(UUID(as_uuid=True), ForeignKey("Basic.Currency.Id"), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class ContractDeductionItemModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "ContractDeductionItem"
    __table_args__ = {"schema": SCHEMA}
    CalculationType = calculation_type
    StaffContractId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.StaffContract.Id"), nullable=False)
    CalculationTimeUnitId = Column(UUID(as_uuid=True), ForeignKey("Basic.TimeUnit.Id"), nullable=False)
    Title = Column(String(255), nullable=False)
    DeductionPercentage = Column(Numeric(3, 2))
    FixedAmount = Column(Numeric(22, 2))
    FixedAmountCurrencyId = Column(UUID(as_uuid=True), ForeignKey("Basic.Currency.Id"), nullable=True)
    Description = Column(String(4000))
    ActiveStatus = active_status


class SupplierModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Supplier"
    __table_args__ = {"schema": SCHEMA}
    Title = Column(String(255), nullable=False)
    Code = Column(String(20), nullable=False, unique=True)
    PhoneNumber = Column(String(20))
    MobileNumber = Column(String(20))
    FaxNumber = Column(String(20))
    Email = Column(String(100))
    PostalCode = Column(String(20))
    City = Column(String(255))
    Address = Column(String(4000))
    Description = Column(String(4000))
    ActiveStatus = active_status


class CostInvoiceModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "CostInvoice"
    __table_args__ = {"schema": SCHEMA}
    InvoiceNumber = Column(String(20), nullable=False)
    SupplierId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Supplier.Id"), nullable=False)
    DocumentId = Column(UUID(as_uuid=True), ForeignKey("DocumentManagement.Document.Id"), nullable=False)
    InvoiceDate = Column(Date, nullable=False)
    TotalAmount = Column(Numeric(22, 2), nullable=False)
    CurrencyId = Column(UUID(as_uuid=True), ForeignKey("Basic.Currency.Id"), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class CostInvoiceItemModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "CostInvoiceItem"
    __table_args__ = {"schema": SCHEMA}
    CostInvoiceId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.CostInvoice.Id"), nullable=False)
    ItemTitle = Column(String(255), nullable=False)
    UnitAmount = Column(Numeric(22, 2), nullable=False)
    CurrencyId = Column(UUID(as_uuid=True), ForeignKey("Basic.Currency.Id"), nullable=False)
    Quantity = Column(Float, nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class ProjectDirectCostItemModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "ProjectDirectCostItem"
    __table_args__ = {"schema": SCHEMA}
    ProjectId = Column(UUID(as_uuid=True), ForeignKey("ProjectManagement.Project.Id"), nullable=False)
    CostInvoiceItemId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.CostInvoiceItem.Id"), nullable=False)
    AllocatedQuantity = Column(Float, nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class CostPaymentReceiptModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "CostPaymentReceipt"
    __table_args__ = {"schema": SCHEMA}
    ReceiptNumber = Column(String(20), nullable=False)
    CostInvoiceId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.CostInvoice.Id"), nullable=False)
    DocumentId = Column(UUID(as_uuid=True), ForeignKey("DocumentManagement.Document.Id"), nullable=False)
    PaymentDate = Column(Date, nullable=False)
    Amount = Column(Numeric(22, 2), nullable=False)
    CurrencyId = Column(UUID(as_uuid=True), ForeignKey("Basic.Currency.Id"), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class SalaryPaymentReceiptModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "SalaryPaymentReceipt"
    __table_args__ = {"schema": SCHEMA}
    ReceiptNumber = Column(String(20), nullable=False)
    StaffContractId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.StaffContract.Id"), nullable=False)
    DocumentId = Column(UUID(as_uuid=True), ForeignKey("DocumentManagement.Document.Id"), nullable=False)
    PaymentDate = Column(Date, nullable=False)
    Amount = Column(Numeric(22, 2), nullable=False)
    CurrencyId = Column(UUID(as_uuid=True), ForeignKey("Basic.Currency.Id"), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class StaffAdditionalPaymentReceiptModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "StaffAdditionalPaymentReceipt"
    __table_args__ = {"schema": SCHEMA}
    ProfileId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Profile.Id"), nullable=False)
    Title = Column(String(255), nullable=False)
    DocumentId = Column(UUID(as_uuid=True), ForeignKey("DocumentManagement.Document.Id"), nullable=False)
    PaymentDate = Column(Date, nullable=False)
    Amount = Column(Numeric(22, 2), nullable=False)
    CurrencyId = Column(UUID(as_uuid=True), ForeignKey("Basic.Currency.Id"), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class CustomerModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Customer"
    __table_args__ = {"schema": SCHEMA}
    Title = Column(String(255), nullable=False)
    Code = Column(String(20), nullable=False, unique=True)
    PhoneNumber = Column(String(20))
    MobileNumber = Column(String(20))
    FaxNumber = Column(String(20))
    Email = Column(String(100))
    PostalCode = Column(String(20))
    City = Column(String(200))
    Address = Column(String(4000))
    Description = Column(String(4000))
    ActiveStatus = active_status


class CustomerContractModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "CustomerContract"
    __table_args__ = {"schema": SCHEMA}
    CustomerId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Customer.Id"), nullable=False)
    ProjectId = Column(UUID(as_uuid=True), ForeignKey("ProjectManagement.Project.Id"), nullable=False)
    CustomerContractTypeId = Column(UUID(as_uuid=True), ForeignKey("Basic.CustomerContractType.Id"), nullable=False)
    ContractNumber = Column(String(20), nullable=False)
    StartDate = Column(Date)
    ScheduledEndDate = Column(Date)
    RealEndDate = Column(Date)
    IsDevelopmentContract = Column(Boolean)
    IsSupportContract = Column(Boolean)
    TotalAmount = Column(Numeric(22, 2), nullable=False)
    CurrencyId = Column(UUID(as_uuid=True), ForeignKey("Basic.Currency.Id"), nullable=False)
    DocumentId = Column(UUID(as_uuid=True), ForeignKey("DocumentManagement.Document.Id"), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class CustomerContractPaymentScheduleModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "CustomerContractPaymentSchedule"
    __table_args__ = {"schema": SCHEMA}
    CustomerContractId = Column(
        UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.CustomerContract.Id"), nullable=False
    )
    PaymentTitle = Column(String(255), nullable=False)
    ProjectReleaseId = Column(UUID(as_uuid=True), ForeignKey("ProjectManagement.ProjectRelease.Id"), nullable=True)
    ScheduledPaymentDate = Column(Date)
    Amount = Column(Numeric(22, 2), nullable=False)
    CurrencyId = Column(UUID(as_uuid=True), ForeignKey("Basic.Currency.Id"), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class CustomerContractPaymentReceiptModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "CustomerContractPaymentReceipt"
    __table_args__ = {"schema": SCHEMA}
    CustomerContractPaymentScheduleId = Column(
        UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.CustomerContractPaymentSchedule.Id"), nullable=False
    )
    ReceiptNumber = Column(String(20), nullable=False)
    ReceiptDocumentId = Column(UUID(as_uuid=True), ForeignKey("DocumentManagement.Document.Id"), nullable=True)
    PaymentDate = Column(Date)
    Amount = Column(Numeric(22, 2), nullable=False)
    CurrencyId = Column(UUID(as_uuid=True), ForeignKey("Basic.Currency.Id"), nullable=False)
    ActiveStatus = active_status