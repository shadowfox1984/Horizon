from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID, uuid4

from ..shared.enums import ActiveStatus, StatusLevel
from ..shared.value_objects import AuditInfo


@dataclass
class BaseLookupEntity:
    code: str
    title: str
    id: UUID = field(default_factory=uuid4)
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class EducationLevel(BaseLookupEntity):
    pass


@dataclass
class Priority(BaseLookupEntity):
    ordering: int = 0
    color: str = "#000000"


@dataclass
class IssueType(BaseLookupEntity):
    icon_address: str = ""
    color: str = "#000000"


@dataclass
class Status(BaseLookupEntity):
    color: str = "#000000"
    status_effect: StatusLevel = StatusLevel.TO_DO


@dataclass
class Resolution(BaseLookupEntity):
    color: str = "#000000"
    is_resolved: bool = False


@dataclass
class MeetingType(BaseLookupEntity):
    pass


@dataclass
class DocumentType(BaseLookupEntity):
    pass


@dataclass
class FileExtension(BaseLookupEntity):
    pass


@dataclass
class StaffContractType(BaseLookupEntity):
    pass


@dataclass
class TestApproval(BaseLookupEntity):
    is_approved: bool = False
    color: str = "#000000"


@dataclass
class TestComplexityLevel(BaseLookupEntity):
    value_number: float = 0.0


@dataclass
class TimeUnit(BaseLookupEntity):
    value_based_on_millisecond: int = 0


@dataclass
class Currency(BaseLookupEntity):
    symbol: str = ""


@dataclass
class CustomerContractType(BaseLookupEntity):
    minimume_contract_amount: float = 0.0
    maximume_contract_amount: float = 0.0
    currency_id: Optional[UUID] = None