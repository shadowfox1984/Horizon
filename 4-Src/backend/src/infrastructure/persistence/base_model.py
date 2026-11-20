import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class UUIDPrimaryKeyMixin:
    Id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False
    )


class AuditColumnsMixin:
    CreateDate = Column(DateTime, nullable=False, server_default=func.now())
    CreatorId = Column(UUID(as_uuid=True), nullable=True)
    ModifyDate = Column(DateTime, nullable=True)
    ModifierId = Column(UUID(as_uuid=True), nullable=True)