from src.domain.finance.entities import (
    StaffContract, ContractSalaryItem, ContractDeductionItem,
    Supplier, CostInvoice, CostInvoiceItem, ProjectDirectCostItem,
    CostPaymentReceipt, SalaryPaymentReceipt,
    StaffAdditionalPaymentReceipt, Customer, CustomerContract,
    CustomerContractPaymentSchedule, CustomerContractPaymentReceipt,
)
from src.domain.shared.enums import CalculationType
from src.infrastructure.persistence.models.finance import (
    StaffContractModel, ContractSalaryItemModel, ContractDeductionItemModel,
    SupplierModel, CostInvoiceModel, CostInvoiceItemModel,
    ProjectDirectCostItemModel, CostPaymentReceiptModel,
    SalaryPaymentReceiptModel, StaffAdditionalPaymentReceiptModel,
    CustomerModel, CustomerContractModel,
    CustomerContractPaymentScheduleModel, CustomerContractPaymentReceiptModel,
)
from ._helpers import audit_from_model, active_from_model


def _audit_kwargs(e):
    if e.audit:
        return dict(
            CreatorId=e.audit.creator_id, CreateDate=e.audit.create_date,
            ModifierId=e.audit.modifier_id, ModifyDate=e.audit.modify_date,
        )
    return {}


def _calc_type(raw):
    if raw is None:
        return None
    return CalculationType(raw.value if hasattr(raw, "value") else raw)


class StaffContractMapper:
    @staticmethod
    def to_domain(m: StaffContractModel) -> StaffContract:
        return StaffContract(
            id=m.Id, profile_id=m.ProfileId,
            staff_contract_type_id=m.StaffContractTypeId,
            start_date=m.StartDate, end_date=m.EndDate, title=m.Title,
            description=m.Description, auto_renewal=m.AutoRenewal,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: StaffContract) -> StaffContractModel:
        return StaffContractModel(
            Id=e.id, ProfileId=e.profile_id,
            StaffContractTypeId=e.staff_contract_type_id,
            StartDate=e.start_date, EndDate=e.end_date, Title=e.title,
            Description=e.description, AutoRenewal=e.auto_renewal,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class ContractSalaryItemMapper:
    @staticmethod
    def to_domain(m: ContractSalaryItemModel) -> ContractSalaryItem:
        return ContractSalaryItem(
            id=m.Id, staff_contract_id=m.StaffContractId,
            calculation_time_unit_id=m.CalculationTimeUnitId,
            title=m.Title, amount=float(m.Amount), currency_id=m.CurrencyId,
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: ContractSalaryItem) -> ContractSalaryItemModel:
        return ContractSalaryItemModel(
            Id=e.id, StaffContractId=e.staff_contract_id,
            CalculationTimeUnitId=e.calculation_time_unit_id,
            Title=e.title, Amount=e.amount, CurrencyId=e.currency_id,
            Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class ContractDeductionItemMapper:
    @staticmethod
    def to_domain(m: ContractDeductionItemModel) -> ContractDeductionItem:
        return ContractDeductionItem(
            id=m.Id, calculation_type=_calc_type(m.CalculationType),
            staff_contract_id=m.StaffContractId,
            calculation_time_unit_id=m.CalculationTimeUnitId,
            title=m.Title,
            deduction_percentage=float(m.DeductionPercentage) if m.DeductionPercentage is not None else None,
            fixed_amount=float(m.FixedAmount) if m.FixedAmount is not None else None,
            fixed_amount_currency_id=m.FixedAmountCurrencyId,
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: ContractDeductionItem) -> ContractDeductionItemModel:
        return ContractDeductionItemModel(
            Id=e.id, CalculationType=e.calculation_type,
            StaffContractId=e.staff_contract_id,
            CalculationTimeUnitId=e.calculation_time_unit_id,
            Title=e.title, DeductionPercentage=e.deduction_percentage,
            FixedAmount=e.fixed_amount,
            FixedAmountCurrencyId=e.fixed_amount_currency_id,
            Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class SupplierMapper:
    @staticmethod
    def to_domain(m: SupplierModel) -> Supplier:
        return Supplier(
            id=m.Id, title=m.Title, code=m.Code, phone_number=m.PhoneNumber,
            mobile_number=m.MobileNumber, fax_number=m.FaxNumber,
            email=m.Email, postal_code=m.PostalCode, city=m.City,
            address=m.Address, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: Supplier) -> SupplierModel:
        return SupplierModel(
            Id=e.id, Title=e.title, Code=e.code, PhoneNumber=e.phone_number,
            MobileNumber=e.mobile_number, FaxNumber=e.fax_number,
            Email=e.email, PostalCode=e.postal_code, City=e.city,
            Address=e.address, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class CostInvoiceMapper:
    @staticmethod
    def to_domain(m: CostInvoiceModel) -> CostInvoice:
        return CostInvoice(
            id=m.Id, invoice_number=m.InvoiceNumber, supplier_id=m.SupplierId,
            document_id=m.DocumentId, invoice_date=m.InvoiceDate,
            total_amount=float(m.TotalAmount), currency_id=m.CurrencyId,
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: CostInvoice) -> CostInvoiceModel:
        return CostInvoiceModel(
            Id=e.id, InvoiceNumber=e.invoice_number, SupplierId=e.supplier_id,
            DocumentId=e.document_id, InvoiceDate=e.invoice_date,
            TotalAmount=e.total_amount, CurrencyId=e.currency_id,
            Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class CostInvoiceItemMapper:
    @staticmethod
    def to_domain(m: CostInvoiceItemModel) -> CostInvoiceItem:
        return CostInvoiceItem(
            id=m.Id, cost_invoice_id=m.CostInvoiceId, item_title=m.ItemTitle,
            unit_amount=float(m.UnitAmount), currency_id=m.CurrencyId,
            quantity=m.Quantity, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: CostInvoiceItem) -> CostInvoiceItemModel:
        return CostInvoiceItemModel(
            Id=e.id, CostInvoiceId=e.cost_invoice_id, ItemTitle=e.item_title,
            UnitAmount=e.unit_amount, CurrencyId=e.currency_id,
            Quantity=e.quantity, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class ProjectDirectCostItemMapper:
    @staticmethod
    def to_domain(m: ProjectDirectCostItemModel) -> ProjectDirectCostItem:
        return ProjectDirectCostItem(
            id=m.Id, project_id=m.ProjectId,
            cost_invoice_item_id=m.CostInvoiceItemId,
            allocated_quantity=m.AllocatedQuantity,
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: ProjectDirectCostItem) -> ProjectDirectCostItemModel:
        return ProjectDirectCostItemModel(
            Id=e.id, ProjectId=e.project_id,
            CostInvoiceItemId=e.cost_invoice_item_id,
            AllocatedQuantity=e.allocated_quantity, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class CostPaymentReceiptMapper:
    @staticmethod
    def to_domain(m: CostPaymentReceiptModel) -> CostPaymentReceipt:
        return CostPaymentReceipt(
            id=m.Id, receipt_number=m.ReceiptNumber,
            cost_invoice_id=m.CostInvoiceId, document_id=m.DocumentId,
            payment_date=m.PaymentDate, amount=float(m.Amount),
            currency_id=m.CurrencyId, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: CostPaymentReceipt) -> CostPaymentReceiptModel:
        return CostPaymentReceiptModel(
            Id=e.id, ReceiptNumber=e.receipt_number,
            CostInvoiceId=e.cost_invoice_id, DocumentId=e.document_id,
            PaymentDate=e.payment_date, Amount=e.amount,
            CurrencyId=e.currency_id, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class SalaryPaymentReceiptMapper:
    @staticmethod
    def to_domain(m: SalaryPaymentReceiptModel) -> SalaryPaymentReceipt:
        return SalaryPaymentReceipt(
            id=m.Id, receipt_number=m.ReceiptNumber,
            staff_contract_id=m.StaffContractId, document_id=m.DocumentId,
            payment_date=m.PaymentDate, amount=float(m.Amount),
            currency_id=m.CurrencyId, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: SalaryPaymentReceipt) -> SalaryPaymentReceiptModel:
        return SalaryPaymentReceiptModel(
            Id=e.id, ReceiptNumber=e.receipt_number,
            StaffContractId=e.staff_contract_id, DocumentId=e.document_id,
            PaymentDate=e.payment_date, Amount=e.amount,
            CurrencyId=e.currency_id, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class StaffAdditionalPaymentReceiptMapper:
    @staticmethod
    def to_domain(m: StaffAdditionalPaymentReceiptModel) -> StaffAdditionalPaymentReceipt:
        return StaffAdditionalPaymentReceipt(
            id=m.Id, profile_id=m.ProfileId, title=m.Title,
            document_id=m.DocumentId, payment_date=m.PaymentDate,
            amount=float(m.Amount), currency_id=m.CurrencyId,
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: StaffAdditionalPaymentReceipt) -> StaffAdditionalPaymentReceiptModel:
        return StaffAdditionalPaymentReceiptModel(
            Id=e.id, ProfileId=e.profile_id, Title=e.title,
            DocumentId=e.document_id, PaymentDate=e.payment_date,
            Amount=e.amount, CurrencyId=e.currency_id,
            Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class CustomerMapper:
    @staticmethod
    def to_domain(m: CustomerModel) -> Customer:
        return Customer(
            id=m.Id, title=m.Title, code=m.Code, phone_number=m.PhoneNumber,
            mobile_number=m.MobileNumber, fax_number=m.FaxNumber,
            email=m.Email, postal_code=m.PostalCode, city=m.City,
            address=m.Address, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: Customer) -> CustomerModel:
        return CustomerModel(
            Id=e.id, Title=e.title, Code=e.code, PhoneNumber=e.phone_number,
            MobileNumber=e.mobile_number, FaxNumber=e.fax_number,
            Email=e.email, PostalCode=e.postal_code, City=e.city,
            Address=e.address, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class CustomerContractMapper:
    @staticmethod
    def to_domain(m: CustomerContractModel) -> CustomerContract:
        return CustomerContract(
            id=m.Id, customer_id=m.CustomerId, project_id=m.ProjectId,
            customer_contract_type_id=m.CustomerContractTypeId,
            contract_number=m.ContractNumber,
            total_amount=float(m.TotalAmount), currency_id=m.CurrencyId,
            document_id=m.DocumentId,
            start_date=m.StartDate, scheduled_end_date=m.ScheduledEndDate,
            real_end_date=m.RealEndDate,
            is_development_contract=m.IsDevelopmentContract,
            is_support_contract=m.IsSupportContract,
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: CustomerContract) -> CustomerContractModel:
        return CustomerContractModel(
            Id=e.id, CustomerId=e.customer_id, ProjectId=e.project_id,
            CustomerContractTypeId=e.customer_contract_type_id,
            ContractNumber=e.contract_number, TotalAmount=e.total_amount,
            CurrencyId=e.currency_id, DocumentId=e.document_id,
            StartDate=e.start_date, ScheduledEndDate=e.scheduled_end_date,
            RealEndDate=e.real_end_date,
            IsDevelopmentContract=e.is_development_contract,
            IsSupportContract=e.is_support_contract,
            Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class CustomerContractPaymentScheduleMapper:
    @staticmethod
    def to_domain(m: CustomerContractPaymentScheduleModel) -> CustomerContractPaymentSchedule:
        return CustomerContractPaymentSchedule(
            id=m.Id, customer_contract_id=m.CustomerContractId,
            payment_title=m.PaymentTitle, project_release_id=m.ProjectReleaseId,
            scheduled_payment_date=m.ScheduledPaymentDate,
            amount=float(m.Amount), currency_id=m.CurrencyId,
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: CustomerContractPaymentSchedule) -> CustomerContractPaymentScheduleModel:
        return CustomerContractPaymentScheduleModel(
            Id=e.id, CustomerContractId=e.customer_contract_id,
            PaymentTitle=e.payment_title, ProjectReleaseId=e.project_release_id,
            ScheduledPaymentDate=e.scheduled_payment_date,
            Amount=e.amount, CurrencyId=e.currency_id,
            Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class CustomerContractPaymentReceiptMapper:
    @staticmethod
    def to_domain(m: CustomerContractPaymentReceiptModel) -> CustomerContractPaymentReceipt:
        return CustomerContractPaymentReceipt(
            id=m.Id,
            customer_contract_payment_schedule_id=m.CustomerContractPaymentScheduleId,
            receipt_number=m.ReceiptNumber,
            receipt_document_id=m.ReceiptDocumentId,
            payment_date=m.PaymentDate, amount=float(m.Amount),
            currency_id=m.CurrencyId,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: CustomerContractPaymentReceipt) -> CustomerContractPaymentReceiptModel:
        return CustomerContractPaymentReceiptModel(
            Id=e.id,
            CustomerContractPaymentScheduleId=e.customer_contract_payment_schedule_id,
            ReceiptNumber=e.receipt_number,
            ReceiptDocumentId=e.receipt_document_id,
            PaymentDate=e.payment_date, Amount=e.amount,
            CurrencyId=e.currency_id,
            ActiveStatus=e.active_status, **_audit_kwargs(e))