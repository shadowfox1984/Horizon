from typing import Optional
from src.domain.shared.enums import ActiveStatus
from src.domain.shared.value_objects import AuditInfo


def audit_from_model(m) -> Optional[AuditInfo]:
    if getattr(m, "CreatorId", None) is None:
        return None
    return AuditInfo(
        creator_id=m.CreatorId,
        create_date=m.CreateDate,
        modifier_id=getattr(m, "ModifierId", None),
        modify_date=getattr(m, "ModifyDate", None),
    )


def active_from_model(m) -> ActiveStatus:
    raw = m.ActiveStatus
    val = raw.value if hasattr(raw, "value") else raw
    return ActiveStatus(val)


def enum_value(raw):
    return raw.value if hasattr(raw, "value") else raw