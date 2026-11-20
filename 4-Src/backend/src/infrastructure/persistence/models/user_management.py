from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.infrastructure.persistence.base_model import (
    Base, UUIDPrimaryKeyMixin, AuditColumnsMixin
)
from src.infrastructure.persistence.enums_pg import active_status, gender

SCHEMA = "UserManagement"


class GroupsModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Groups"
    __table_args__ = {"schema": SCHEMA}
    Code = Column(String(20), nullable=False, unique=True)
    Title = Column(String(200), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class PermissionModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Permission"
    __table_args__ = {"schema": SCHEMA}
    Code = Column(String(20), nullable=False, unique=True)
    Title = Column(String(200), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class FormModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Form"
    __table_args__ = {"schema": SCHEMA}
    Code = Column(String(20), nullable=False, unique=True)
    Title = Column(String(200), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class FormPermissionModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "FormPermission"
    __table_args__ = {"schema": SCHEMA}
    FormId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Form.Id"), nullable=False)
    PermissionId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Permission.Id"), nullable=False)
    ActiveStatus = active_status
    Form = relationship("FormModel", foreign_keys=[FormId])
    Permission = relationship("PermissionModel", foreign_keys=[PermissionId])


class GroupPermissionModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "GroupPermission"
    __table_args__ = {"schema": SCHEMA}
    FormPermissionId = Column(
        UUID(as_uuid=True), ForeignKey("UserManagement.FormPermission.Id"), nullable=False
    )
    GroupId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Groups.Id"), nullable=False)
    ActiveStatus = active_status
    FormPermission = relationship("FormPermissionModel", foreign_keys=[FormPermissionId])
    Group = relationship("GroupsModel", foreign_keys=[GroupId])


class ProfileModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Profile"
    __table_args__ = {"schema": SCHEMA}
    FirstName = Column(String(200), nullable=False)
    LastName = Column(String(200), nullable=False)
    Gender = gender
    StaffNumber = Column(String(20), nullable=False, unique=True)
    ActiveFrom = Column(DateTime, nullable=False)
    ActiveTo = Column(DateTime, nullable=True)
    PositionId = Column(UUID(as_uuid=True), ForeignKey("HumanResource.Position.Id"), nullable=True)
    Avatar = Column(String(1000))
    Birthday = Column(Date)
    PhoneNumber = Column(String(20))
    MobileNumber = Column(String(20))
    EmailAddress = Column(String(200))
    Address = Column(String(1000))
    PostalCode = Column(String(20))
    Username = Column(String(200), nullable=False, unique=True)
    Pass = Column(String(255), nullable=False)
    PassSalt = Column(String(5))
    LastLogInDate = Column(DateTime)
    LogInCount = Column(Integer, nullable=False, server_default="0")
    WrongLogInCount = Column(Integer, nullable=False, server_default="0")
    ActiveStatus = active_status
    Position = relationship("PositionModel", foreign_keys=[PositionId])


class ProfileClientSecretModel(Base, UUIDPrimaryKeyMixin):
    __tablename__ = "ProfileClientSecret"
    __table_args__ = {"schema": SCHEMA}
    ProfileId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Profile.Id"), nullable=False)
    ClientSecret = Column(String(255), nullable=False)
    ClientIp = Column(String(30), nullable=False)
    Profile = relationship("ProfileModel", foreign_keys=[ProfileId])


class UserTokenModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "UserToken"
    __table_args__ = {"schema": SCHEMA}
    ProfileClientSecretId = Column(
        UUID(as_uuid=True), ForeignKey("UserManagement.ProfileClientSecret.Id"), nullable=False
    )
    Token = Column(String(1000), nullable=False)
    ExpireDate = Column(DateTime, nullable=False)
    LastRefreshTime = Column(DateTime)
    RefreshCount = Column(Integer, nullable=False, server_default="0")
    ActiveStatus = active_status
    ProfileClientSecret = relationship(
        "ProfileClientSecretModel", foreign_keys=[ProfileClientSecretId]
    )


class ProfilePermissionModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "ProfilePermission"
    __table_args__ = {"schema": SCHEMA}
    FormPermissionId = Column(
        UUID(as_uuid=True), ForeignKey("UserManagement.FormPermission.Id"), nullable=False
    )
    ProfileId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Profile.Id"), nullable=False)
    ActiveStatus = active_status
    FormPermission = relationship("FormPermissionModel", foreign_keys=[FormPermissionId])
    Profile = relationship("ProfileModel", foreign_keys=[ProfileId])


class ProfileGroupModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "ProfileGroup"
    __table_args__ = {"schema": SCHEMA}
    ProfileId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Profile.Id"), nullable=False)
    GroupId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Groups.Id"), nullable=False)
    ActiveStatus = active_status
    Profile = relationship("ProfileModel", foreign_keys=[ProfileId])
    Group = relationship("GroupsModel", foreign_keys=[GroupId])