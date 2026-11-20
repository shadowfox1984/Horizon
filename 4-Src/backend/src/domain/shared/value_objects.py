from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from .enums import ActiveStatus


@dataclass(frozen=True)
class AuditInfo:
    creator_id: UUID
    create_date: datetime = field(default_factory=datetime.utcnow)
    modifier_id: Optional[UUID] = None
    modify_date: Optional[datetime] = None


@dataclass(frozen=True)
class ActiveStatusInfo:
    status: ActiveStatus = ActiveStatus.ACTIVE


@dataclass(frozen=True)
class Money:
    amount: float
    currency_id: UUID