from dataclasses import dataclass, field
from datetime import date, time
from typing import Optional
from uuid import UUID, uuid4

from ..shared.enums import (
    ActiveStatus, Weekday, HolidayType, EnteranceType, LeaveType
)
from ..shared.value_objects import AuditInfo


@dataclass
class Department:
    code: str
    title: str
    id: UUID = field(default_factory=uuid4)
    description: Optional[str] = None
    parent_id: Optional[UUID] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class Position:
    code: str
    title: str
    department_id: UUID
    id: UUID = field(default_factory=uuid4)
    description: Optional[str] = None
    parent_id: Optional[UUID] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class ProfileEducation:
    profile_id: UUID
    education_level_id: UUID
    title: str
    id: UUID = field(default_factory=uuid4)
    document_id: Optional[UUID] = None
    collage_name: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class ProfileJobExperience:
    profile_id: UUID
    job_title: str
    company_name: str
    id: UUID = field(default_factory=uuid4)
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class ProfileCertificate:
    profile_id: UUID
    title: str
    institute_name: str
    has_certificate: bool
    id: UUID = field(default_factory=uuid4)
    document_id: Optional[UUID] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    description: Optional[str] = None
    certificate_file_address: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class WorkingTimeTable:
    staff_contract_type_id: UUID
    working_day: Weekday
    start_time: time
    end_time: time
    id: UUID = field(default_factory=uuid4)
    floating_start_time: Optional[time] = None
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class Holiday:
    title: str
    holiday_type: HolidayType
    holiday_date: date
    id: UUID = field(default_factory=uuid4)
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class Attendance:
    profile_id: UUID
    working_date: date
    enterance_type: EnteranceType
    entrance_time: time
    id: UUID = field(default_factory=uuid4)
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class Leave:
    profile_id: UUID
    leave_type: LeaveType
    leaving_start_date: date
    leaving_start_time: time
    leaving_end_time: time
    id: UUID = field(default_factory=uuid4)
    leaving_end_date: Optional[date] = None
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class WorkMission:
    profile_id: UUID
    mission_start_date: date
    mission_start_time: time
    mission_end_time: time
    id: UUID = field(default_factory=uuid4)
    mission_end_date: Optional[date] = None
    mission_location: Optional[str] = None
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None