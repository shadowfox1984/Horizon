from src.domain.document_management.entities import Document
from src.infrastructure.persistence.models.document_management import DocumentModel
from ._helpers import audit_from_model, active_from_model


def _audit_kwargs(e):
    if e.audit:
        return dict(
            CreatorId=e.audit.creator_id, CreateDate=e.audit.create_date,
            ModifierId=e.audit.modifier_id, ModifyDate=e.audit.modify_date,
        )
    return {}


class DocumentMapper:
    @staticmethod
    def to_domain(m: DocumentModel) -> Document:
        return Document(
            id=m.Id, table_id=m.TableId, table_name=m.TableName,
            file_address=m.FileAddress, document_type_id=m.DocumentTypeId,
            file_extension_id=m.FileExtensionId,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: Document) -> DocumentModel:
        return DocumentModel(
            Id=e.id, TableId=e.table_id, TableName=e.table_name,
            FileAddress=e.file_address, DocumentTypeId=e.document_type_id,
            FileExtensionId=e.file_extension_id,
            ActiveStatus=e.active_status, **_audit_kwargs(e),
        )