from src.domain.basic.entities import (
    EducationLevel, Priority, IssueType, Status, Resolution,
    MeetingType, DocumentType, FileExtension, StaffContractType,
    TestApproval, TestComplexityLevel, TimeUnit, Currency,
    CustomerContractType,
)
from src.domain.shared.value_objects import AuditInfo
from src.infrastructure.persistence.models.basic import (
    EducationLevelModel, PriorityModel, IssueTypeModel, StatusModel,
    ResolutionModel, MeetingTypeModel, DocumentTypeModel,
    FileExtensionModel, StaffContractTypeModel, TestApprovalModel,
    TestComplexityLevelModel, TimeUnitModel, CurrencyModel,
    CustomerContractTypeModel,
)
from ._helpers import audit_from_model, active_from_model


def _audit_args(e):
    if e.audit:
        return dict(
            CreatorId=e.audit.creator_id,
            CreateDate=e.audit.create_date,
            ModifierId=e.audit.modifier_id,
            ModifyDate=e.audit.modify_date,
        )
    return {}


class EducationLevelMapper:
    @staticmethod
    def to_domain(m: EducationLevelModel) -> EducationLevel:
        return EducationLevel(
            id=m.Id, code=m.Code, title=m.Title, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: EducationLevel) -> EducationLevelModel:
        return EducationLevelModel(
            Id=e.id, Code=e.code, Title=e.title, Description=e.description,
            ActiveStatus=e.active_status, **_audit_args(e),
        )


class PriorityMapper:
    @staticmethod
    def to_domain(m: PriorityModel) -> Priority:
        return Priority(
            id=m.Id, code=m.Code, title=m.Title, ordering=m.Ordering,
            color=m.Color, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: Priority) -> PriorityModel:
        return PriorityModel(
            Id=e.id, Code=e.code, Title=e.title, Ordering=e.ordering,
            Color=e.color, Description=e.description,
            ActiveStatus=e.active_status, **_audit_args(e),
        )


class IssueTypeMapper:
    @staticmethod
    def to_domain(m: IssueTypeModel) -> IssueType:
        return IssueType(
            id=m.Id, code=m.Code, title=m.Title, icon_address=m.IconAddress,
            color=m.Color, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: IssueType) -> IssueTypeModel:
        return IssueTypeModel(
            Id=e.id, Code=e.code, Title=e.title, IconAddress=e.icon_address,
            Color=e.color, Description=e.description,
            ActiveStatus=e.active_status, **_audit_args(e),
        )


class StatusMapper:
    @staticmethod
    def to_domain(m: StatusModel) -> Status:
        return Status(
            id=m.Id, code=m.Code, title=m.Title, color=m.Color,
            status_effect=m.StatusEffect, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: Status) -> StatusModel:
        return StatusModel(
            Id=e.id, Code=e.code, Title=e.title, Color=e.color,
            StatusEffect=e.status_effect, Description=e.description,
            ActiveStatus=e.active_status, **_audit_args(e),
        )


class ResolutionMapper:
    @staticmethod
    def to_domain(m: ResolutionModel) -> Resolution:
        return Resolution(
            id=m.Id, code=m.Code, title=m.Title, color=m.Color,
            is_resolved=m.IsResolved, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: Resolution) -> ResolutionModel:
        return ResolutionModel(
            Id=e.id, Code=e.code, Title=e.title, Color=e.color,
            IsResolved=e.is_resolved, Description=e.description,
            ActiveStatus=e.active_status, **_audit_args(e),
        )


class MeetingTypeMapper:
    @staticmethod
    def to_domain(m: MeetingTypeModel) -> MeetingType:
        return MeetingType(
            id=m.Id, code=m.Code, title=m.Title, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: MeetingType) -> MeetingTypeModel:
        return MeetingTypeModel(
            Id=e.id, Code=e.code, Title=e.title, Description=e.description,
            ActiveStatus=e.active_status, **_audit_args(e),
        )


class DocumentTypeMapper:
    @staticmethod
    def to_domain(m: DocumentTypeModel) -> DocumentType:
        return DocumentType(
            id=m.Id, code=m.Code, title=m.Title, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: DocumentType) -> DocumentTypeModel:
        return DocumentTypeModel(
            Id=e.id, Code=e.code, Title=e.title, Description=e.description,
            ActiveStatus=e.active_status, **_audit_args(e),
        )


class FileExtensionMapper:
    @staticmethod
    def to_domain(m: FileExtensionModel) -> FileExtension:
        return FileExtension(
            id=m.Id, code=m.Code, title=m.Title, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: FileExtension) -> FileExtensionModel:
        return FileExtensionModel(
            Id=e.id, Code=e.code, Title=e.title, Description=e.description,
            ActiveStatus=e.active_status, **_audit_args(e),
        )


class StaffContractTypeMapper:
    @staticmethod
    def to_domain(m: StaffContractTypeModel) -> StaffContractType:
        return StaffContractType(
            id=m.Id, code=m.Code, title=m.Title, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: StaffContractType) -> StaffContractTypeModel:
        return StaffContractTypeModel(
            Id=e.id, Code=e.code, Title=e.title, Description=e.description,
            ActiveStatus=e.active_status, **_audit_args(e),
        )


class TestApprovalMapper:
    @staticmethod
    def to_domain(m: TestApprovalModel) -> TestApproval:
        return TestApproval(
            id=m.Id, code=m.Code, title=m.Title, is_approved=m.IsApproved,
            color=m.Color, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: TestApproval) -> TestApprovalModel:
        return TestApprovalModel(
            Id=e.id, Code=e.code, Title=e.title, IsApproved=e.is_approved,
            Color=e.color, Description=e.description,
            ActiveStatus=e.active_status, **_audit_args(e),
        )


class TestComplexityLevelMapper:
    @staticmethod
    def to_domain(m: TestComplexityLevelModel) -> TestComplexityLevel:
        return TestComplexityLevel(
            id=m.Id, code=m.Code, title=m.Title, value_number=m.ValueNumber,
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: TestComplexityLevel) -> TestComplexityLevelModel:
        return TestComplexityLevelModel(
            Id=e.id, Code=e.code, Title=e.title, ValueNumber=e.value_number,
            Description=e.description,
            ActiveStatus=e.active_status, **_audit_args(e),
        )


class TimeUnitMapper:
    @staticmethod
    def to_domain(m: TimeUnitModel) -> TimeUnit:
        return TimeUnit(
            id=m.Id, code=m.Code, title=m.Title,
            value_based_on_millisecond=m.ValueBasedOnMillisecond,
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: TimeUnit) -> TimeUnitModel:
        return TimeUnitModel(
            Id=e.id, Code=e.code, Title=e.title,
            ValueBasedOnMillisecond=e.value_based_on_millisecond,
            Description=e.description,
            ActiveStatus=e.active_status, **_audit_args(e),
        )


class CurrencyMapper:
    @staticmethod
    def to_domain(m: CurrencyModel) -> Currency:
        return Currency(
            id=m.Id, code=m.Code, title=m.Title, symbol=m.Symbol,
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: Currency) -> CurrencyModel:
        return CurrencyModel(
            Id=e.id, Code=e.code, Title=e.title, Symbol=e.symbol,
            Description=e.description,
            ActiveStatus=e.active_status, **_audit_args(e),
        )


class CustomerContractTypeMapper:
    @staticmethod
    def to_domain(m: CustomerContractTypeModel) -> CustomerContractType:
        return CustomerContractType(
            id=m.Id, code=m.Code, title=m.Title,
            minimume_contract_amount=float(m.MinimumeContractAmount),
            maximume_contract_amount=float(m.MaximumeContractAmount),
            currency_id=m.CurrencyId, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: CustomerContractType) -> CustomerContractTypeModel:
        return CustomerContractTypeModel(
            Id=e.id, Code=e.code, Title=e.title,
            MinimumeContractAmount=e.minimume_contract_amount,
            MaximumeContractAmount=e.maximume_contract_amount,
            CurrencyId=e.currency_id, Description=e.description,
            ActiveStatus=e.active_status, **_audit_args(e),
        )