from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID, uuid4

from ..shared.enums import ActiveStatus
from ..shared.value_objects import AuditInfo


@dataclass
class Document:
    table_id: UUID
    table_name: str
    file_address: str
    document_type_id: UUID
    file_extension_id: UUID
    id: UUID = field(default_factory=uuid4)
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None