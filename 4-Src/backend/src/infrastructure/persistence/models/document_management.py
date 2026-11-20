from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.infrastructure.persistence.base_model import (
    Base, UUIDPrimaryKeyMixin, AuditColumnsMixin
)
from src.infrastructure.persistence.enums_pg import active_status

SCHEMA = "DocumentManagement"


class DocumentModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Document"
    __table_args__ = {"schema": SCHEMA}
    TableId = Column(UUID(as_uuid=True), nullable=False)
    TableName = Column(String(255), nullable=False)
    FileAddress = Column(String(4000), nullable=False)
    DocumentTypeId = Column(UUID(as_uuid=True), ForeignKey("Basic.DocumentType.Id"), nullable=False)
    FileExtensionId = Column(UUID(as_uuid=True), ForeignKey("Basic.FileExtension.Id"), nullable=False)
    ActiveStatus = active_status
    DocumentType = relationship("DocumentTypeModel", foreign_keys=[DocumentTypeId])
    FileExtension = relationship("FileExtensionModel", foreign_keys=[FileExtensionId])