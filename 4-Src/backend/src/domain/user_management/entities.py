from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional
from uuid import UUID, uuid4

from ..shared.enums import ActiveStatus, Gender
from ..shared.value_objects import AuditInfo


@dataclass
class Group:
    code: str
    title: str
    id: UUID = field(default_factory=uuid4)
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class Permission:
    code: str
    title: str
    id: UUID = field(default_factory=uuid4)
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class Form:
    code: str
    title: str
    id: UUID = field(default_factory=uuid4)
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class FormPermission:
    form_id: UUID
    permission_id: UUID
    id: UUID = field(default_factory=uuid4)
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class GroupPermission:
    form_permission_id: UUID
    group_id: UUID
    id: UUID = field(default_factory=uuid4)
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class Profile:
    first_name: str
    last_name: str
    gender: Gender
    staff_number: str
    active_from: datetime
    username: str
    password_hash: str
    id: UUID = field(default_factory=uuid4)
    active_to: Optional[datetime] = None
    position_id: Optional[UUID] = None
    avatar: Optional[str] = None
    birthday: Optional[date] = None
    phone_number: Optional[str] = None
    mobile_number: Optional[str] = None
    email_address: Optional[str] = None
    address: Optional[str] = None
    postal_code: Optional[str] = None
    pass_salt: Optional[str] = None
    last_login_date: Optional[datetime] = None
    login_count: int = 0
    wrong_login_count: int = 0
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class ProfileClientSecret:
    profile_id: UUID
    client_secret: str
    client_ip: str
    id: UUID = field(default_factory=uuid4)


@dataclass
class UserToken:
    profile_client_secret_id: UUID
    token: str
    expire_date: datetime
    id: UUID = field(default_factory=uuid4)
    last_refresh_time: Optional[datetime] = None
    refresh_count: int = 0
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class ProfilePermission:
    form_permission_id: UUID
    profile_id: UUID
    id: UUID = field(default_factory=uuid4)
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class ProfileGroup:
    profile_id: UUID
    group_id: UUID
    id: UUID = field(default_factory=uuid4)
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None