from sqlalchemy import Column, String, Date, Time, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.infrastructure.persistence.base_model import (
    Base, UUIDPrimaryKeyMixin, AuditColumnsMixin
)
from src.infrastructure.persistence.enums_pg import (
    active_status, weekday, holiday_type, enterance_type, leave_type
)

SCHEMA = "HumanResource"


class DepartmentModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Department"
    __table_args__ = {"schema": SCHEMA}
    Code = Column(String(20), nullable=False, unique=True)
    Title = Column(String(255), nullable=False)
    Description = Column(String(4000))
    ParentId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Department.Id"), nullable=True)
    ActiveStatus = active_status
    Parent = relationship(
        "DepartmentModel", remote_side="DepartmentModel.Id", foreign_keys=[ParentId]
    )


class PositionModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Position"
    __table_args__ = {"schema": SCHEMA}
    Code = Column(String(10), nullable=False, unique=True)
    Title = Column(String(255), nullable=False)
    Description = Column(String(4000))
    ParentId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Position.Id"), nullable=True)
    DepartmentId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Department.Id"), nullable=False)
    ActiveStatus = active_status
    Parent = relationship(
        "PositionModel", remote_side="PositionModel.Id", foreign_keys=[ParentId]
    )
    Department = relationship("DepartmentModel", foreign_keys=[DepartmentId])


class ProfileEducationModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "ProfileEducation"
    __table_args__ = {"schema": SCHEMA}
    ProfileId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Profile.Id"), nullable=False)
    EducationLevelId = Column(UUID(as_uuid=True), ForeignKey("Basic.EducationLevel.Id"), nullable=False)
    DocumentId = Column(UUID(as_uuid=True), ForeignKey("DocumentManagement.Document.Id"), nullable=True)
    Title = Column(String(255), nullable=False)
    CollageName = Column(String(255))
    StartDate = Column(Date)
    EndDate = Column(Date)
    Description = Column(String(4000))
    ActiveStatus = active_status


class ProfileJobExperienceModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "ProfileJobExperience"
    __table_args__ = {"schema": SCHEMA}
    ProfileId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Profile.Id"), nullable=False)
    JobTitle = Column(String(255), nullable=False)
    CompanyName = Column(String(255), nullable=False)
    StartDate = Column(Date)
    EndDate = Column(Date)
    Description = Column(String(4000))
    ActiveStatus = active_status


class ProfileCertificateModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "ProfileCertificate"
    __table_args__ = {"schema": SCHEMA}
    ProfileId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Profile.Id"), nullable=False)
    Title = Column(String(255), nullable=False)
    InstituteName = Column(String(255), nullable=False)
    HasCertificate = Column(Boolean, nullable=False)
    DocumentId = Column(UUID(as_uuid=True), ForeignKey("DocumentManagement.Document.Id"), nullable=True)
    StartDate = Column(Date)
    EndDate = Column(Date)
    Description = Column(String(4000))
    CertificateFileAddress = Column(String(4000))
    ActiveStatus = active_status


class WorkingTimeTableModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "WorkingTimeTable"
    __table_args__ = {"schema": SCHEMA}
    StaffContractTypeId = Column(UUID(as_uuid=True), ForeignKey("Basic.StaffContractType.Id"), nullable=False)
    WorkingDay = weekday
    StartTime = Column(Time, nullable=False)
    EndTime = Column(Time, nullable=False)
    FloatingStartTime = Column(Time)
    Description = Column(String(4000))
    ActiveStatus = active_status


class HolidayModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Holiday"
    __table_args__ = {"schema": SCHEMA}
    Title = Column(String(255), nullable=False)
    HolidayType = holiday_type
    HolidayDate = Column(Date, nullable=False, unique=True)
    Description = Column(String(4000))
    ActiveStatus = active_status


class AttendanceModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Attendance"
    __table_args__ = {"schema": SCHEMA}
    ProfileId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Profile.Id"), nullable=False)
    WorkingDate = Column(Date, nullable=False)
    EnteranceType = enterance_type
    EnternaceTime = Column(Time, nullable=False)
    ActiveStatus = active_status


class LeaveModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Leave"
    __table_args__ = {"schema": SCHEMA}
    ProfileId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Profile.Id"), nullable=False)
    LeaveType = leave_type
    LeavingStartDate = Column(Date, nullable=False)
    LeavingEndDate = Column(Date)
    LeavingStartTime = Column(Time, nullable=False)
    LeavingEndTime = Column(Time, nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class WorkMissionModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "WorkMission"
    __table_args__ = {"schema": SCHEMA}
    ProfileId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Profile.Id"), nullable=False)
    MissionStartDate = Column(Date, nullable=False)
    MissionEndDate = Column(Date)
    MissionStartTime = Column(Time, nullable=False)
    MissionEndTime = Column(Time, nullable=False)
    MissionLocation = Column(String(255))
    Description = Column(String(4000))
    ActiveStatus = active_status