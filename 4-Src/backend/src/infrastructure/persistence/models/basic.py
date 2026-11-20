from sqlalchemy import Column, String, Integer, Float, BigInteger, Numeric, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.infrastructure.persistence.base_model import (
    Base, UUIDPrimaryKeyMixin, AuditColumnsMixin
)
from src.infrastructure.persistence.enums_pg import active_status, status_level

SCHEMA = "Basic"


class EducationLevelModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "EducationLevel"
    __table_args__ = {"schema": SCHEMA}
    Code = Column(String(20), nullable=False, unique=True)
    Title = Column(String(200), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class PriorityModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Priority"
    __table_args__ = {"schema": SCHEMA}
    Code = Column(String(20), nullable=False, unique=True)
    Title = Column(String(200), nullable=False)
    Ordering = Column(Integer, nullable=False)
    Color = Column(String(7), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class IssueTypeModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "IssueType"
    __table_args__ = {"schema": SCHEMA}
    Code = Column(String(20), nullable=False, unique=True)
    Title = Column(String(200), nullable=False)
    IconAddress = Column(String(1000), nullable=False)
    Color = Column(String(7), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class StatusModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Status"
    __table_args__ = {"schema": SCHEMA}
    Code = Column(String(20), nullable=False, unique=True)
    Title = Column(String(200), nullable=False)
    Color = Column(String(7), nullable=False)
    StatusEffect = status_level
    Description = Column(String(4000))
    ActiveStatus = active_status


class ResolutionModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Resolution"
    __table_args__ = {"schema": SCHEMA}
    Code = Column(String(20), nullable=False, unique=True)
    Title = Column(String(200), nullable=False)
    Color = Column(String(7), nullable=False)
    IsResolved = Column(Boolean, nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class MeetingTypeModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "MeetingType"
    __table_args__ = {"schema": SCHEMA}
    Code = Column(String(20), nullable=False, unique=True)
    Title = Column(String(200), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class DocumentTypeModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "DocumentType"
    __table_args__ = {"schema": SCHEMA}
    Code = Column(String(20), nullable=False, unique=True)
    Title = Column(String(200), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class FileExtensionModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "FileExtension"
    __table_args__ = {"schema": SCHEMA}
    Code = Column(String(20), nullable=False, unique=True)
    Title = Column(String(200), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class StaffContractTypeModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "StaffContractType"
    __table_args__ = {"schema": SCHEMA}
    Code = Column(String(20), nullable=False, unique=True)
    Title = Column(String(200), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class TestApprovalModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "TestApproval"
    __table_args__ = {"schema": SCHEMA}
    Code = Column(String(20), nullable=False, unique=True)
    Title = Column(String(200), nullable=False)
    IsApproved = Column(Boolean, nullable=False)
    Color = Column(String(10), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class TestComplexityLevelModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "TestComplexityLevel"
    __table_args__ = {"schema": SCHEMA}
    Code = Column(String(20), nullable=False, unique=True)
    Title = Column(String(200), nullable=False)
    ValueNumber = Column(Float, nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class TimeUnitModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "TimeUnit"
    __table_args__ = {"schema": SCHEMA}
    Code = Column(String(20), nullable=False, unique=True)
    Title = Column(String(200), nullable=False)
    ValueBasedOnMillisecond = Column(BigInteger, nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class CurrencyModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Currency"
    __table_args__ = {"schema": SCHEMA}
    Code = Column(String(20), nullable=False, unique=True)
    Symbol = Column(String(20), nullable=False, unique=True)
    Title = Column(String(200), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class CustomerContractTypeModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "CustomerContractType"
    __table_args__ = {"schema": SCHEMA}
    Code = Column(String(20), nullable=False, unique=True)
    Title = Column(String(200), nullable=False)
    MinimumeContractAmount = Column(Numeric(28, 2), nullable=False)
    MaximumeContractAmount = Column(Numeric(28, 2), nullable=False)
    CurrencyId = Column(UUID(as_uuid=True), ForeignKey("Basic.Currency.Id"), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status
    Currency = relationship("CurrencyModel", foreign_keys=[CurrencyId])