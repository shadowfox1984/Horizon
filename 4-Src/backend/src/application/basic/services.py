# src/application/basic/services.py
from uuid import UUID
import re
from src.domain.shared.exceptions import BusinessException, ErrorCodes
from src.domain.shared.unit_of_work import UnitOfWork
from src.domain.basic.repositories import (
    EducationLevelRepository, PriorityRepository, IssueTypeRepository,
    StatusRepository, ResolutionRepository, MeetingTypeRepository,
    DocumentTypeRepository, FileExtensionRepository, StaffContractTypeRepository,
    TestApprovalRepository, TestComplexityLevelRepository, TimeUnitRepository,
    CurrencyRepository
)
from src.domain.basic.entities import (
    EducationLevel, Priority, IssueType, Status, Resolution, MeetingType,
    DocumentType, FileExtension, StaffContractType, TestApproval,
    TestComplexityLevel, TimeUnit, Currency
)

class BaseLookupService:
    def __init__(self, repo, uow: UnitOfWork, entity_class):
        self.repo = repo
        self.uow = uow
        self.entity_class = entity_class

    def add(self, data: dict) -> UUID:
        if self.repo.get_by_code(data["code"]):
            raise BusinessException(*ErrorCodes.CODE_EXISTS)
        
        entity = self.entity_class(code=data["code"], title=data["title"], description=data.get("description"))
        self.repo.add(entity)
        self.uow.commit()
        return entity.id

    def update(self, id: UUID, data: dict) -> None:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
            
        existing = self.repo.get_by_code(data["code"])
        if existing and existing.id != id:
            raise BusinessException(*ErrorCodes.CODE_EXISTS)
            
        entity.code = data["code"]
        entity.title = data["title"]
        entity.description = data.get("description")
        self.repo.update(entity)
        self.uow.commit()

    def delete(self, id: UUID) -> None:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if self.repo.has_dependencies(id):
            raise BusinessException(*ErrorCodes.CASCADE_DELETE_ERROR)
        entity.active_status = "Deleted"
        self.repo.update(entity)
        self.uow.commit()

    def active(self, id: UUID) -> None:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if entity.active_status == "Active":
            raise BusinessException(*ErrorCodes.ALREADY_ACTIVE)
        entity.active_status = "Active"
        self.repo.update(entity)
        self.uow.commit()

    def inactive(self, id: UUID) -> None:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if entity.active_status == "Inactive":
            raise BusinessException(*ErrorCodes.ALREADY_INACTIVE)
        entity.active_status = "Inactive"
        self.repo.update(entity)
        self.uow.commit()

    def get_specific(self, id: UUID) -> dict:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        return {"id": entity.id, "code": entity.code, "title": entity.title, "description": entity.description, "createdAt": entity.audit.create_date, "createdBy": "System"}

    def get_all(self, title, code, description, offset, limit) -> dict:
        items, total = self.repo.search(title, code, description, offset, limit)
        if total == 0:
            raise BusinessException(*ErrorCodes.NO_DATA_FOUND)
        return {"offset": offset, "limit": limit, "totalRecord": total, "dataList": [{"id": i.id, "code": i.code, "title": i.title, "description": i.description, "createdAt": i.audit.create_date, "createdBy": "System"} for i in items]}

    def get_combo(self) -> list:
        items = self.repo.get_all_active()
        if not items:
            raise BusinessException(*ErrorCodes.NO_DATA_FOUND)
        return [{"id": i.id, "title": i.title, "code": i.code} for i in items]


class PriorityService:
    def __init__(self, repo: PriorityRepository, uow: UnitOfWork):
        self.repo = repo
        self.uow = uow

    def add(self, data: dict) -> UUID:
        if self.repo.get_by_code(data["code"]):
            raise BusinessException(*ErrorCodes.CODE_EXISTS)
        if not re.match(r'^#[0-9A-Fa-f]{6}$', data["color"]):
            raise BusinessException(*ErrorCodes.INVALID_COLOR_FORMAT)
        if self.repo.get_by_ordering(data["ordering"]):
            raise BusinessException(*ErrorCodes.ORDERING_DUPLICATED)
            
        entity = Priority(code=data["code"], title=data["title"], color=data["color"], ordering=data["ordering"], description=data.get("description"))
        self.repo.add(entity)
        self.uow.commit()
        return entity.id

    def update(self, id: UUID, data: dict) -> None:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
            
        existing = self.repo.get_by_code(data["code"])
        if existing and existing.id != id:
            raise BusinessException(*ErrorCodes.CODE_EXISTS)
        if not re.match(r'^#[0-9A-Fa-f]{6}$', data["color"]):
            raise BusinessException(*ErrorCodes.INVALID_COLOR_FORMAT)
            
        existing_ord = self.repo.get_by_ordering(data["ordering"])
        if existing_ord and existing_ord.id != id:
            raise BusinessException(*ErrorCodes.ORDERING_DUPLICATED)
            
        entity.code = data["code"]
        entity.title = data["title"]
        entity.color = data["color"]
        entity.ordering = data["ordering"]
        entity.description = data.get("description")
        self.repo.update(entity)
        self.uow.commit()

    def delete(self, id: UUID) -> None:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if self.repo.has_dependencies(id):
            raise BusinessException(*ErrorCodes.CASCADE_DELETE_ERROR)
        entity.active_status = "Deleted"
        self.repo.update(entity)
        self.uow.commit()

    def active(self, id: UUID) -> None:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if entity.active_status == "Active":
            raise BusinessException(*ErrorCodes.ALREADY_ACTIVE)
        entity.active_status = "Active"
        self.repo.update(entity)
        self.uow.commit()

    def inactive(self, id: UUID) -> None:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if entity.active_status == "Inactive":
            raise BusinessException(*ErrorCodes.ALREADY_INACTIVE)
        entity.active_status = "Inactive"
        self.repo.update(entity)
        self.uow.commit()

    def get_specific(self, id: UUID) -> dict:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        return {"id": entity.id, "code": entity.code, "title": entity.title, "color": entity.color, "ordering": entity.ordering, "description": entity.description, "createdAt": entity.audit.create_date, "createdBy": "System"}

    def get_all(self, title, code, description, offset, limit) -> dict:
        items, total = self.repo.search(title, code, description, offset, limit)
        if total == 0:
            raise BusinessException(*ErrorCodes.NO_DATA_FOUND)
        return {"offset": offset, "limit": limit, "totalRecord": total, "dataList": [{"id": i.id, "code": i.code, "title": i.title, "color": i.color, "ordering": i.ordering, "description": i.description, "createdAt": i.audit.create_date, "createdBy": "System"} for i in items]}

    def get_combo(self) -> list:
        items = self.repo.get_all_active()
        if not items:
            raise BusinessException(*ErrorCodes.NO_DATA_FOUND)
        return [{"id": i.id, "title": i.title, "code": i.code} for i in items]


class IssueTypeService:
    def __init__(self, repo: IssueTypeRepository, uow: UnitOfWork):
        self.repo = repo
        self.uow = uow

    def add(self, data: dict) -> UUID:
        if self.repo.get_by_code(data["code"]):
            raise BusinessException(*ErrorCodes.CODE_EXISTS)
        entity = IssueType(code=data["code"], title=data["title"], icon_address=data["iconAddress"], color=data["color"], description=data.get("description"))
        self.repo.add(entity)
        self.uow.commit()
        return entity.id

    def update(self, id: UUID, data: dict) -> None:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        existing = self.repo.get_by_code(data["code"])
        if existing and existing.id != id:
            raise BusinessException(*ErrorCodes.CODE_EXISTS)
        entity.code = data["code"]
        entity.title = data["title"]
        entity.icon_address = data["iconAddress"]
        entity.color = data["color"]
        entity.description = data.get("description")
        self.repo.update(entity)
        self.uow.commit()

    def delete(self, id: UUID) -> None:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if self.repo.has_dependencies(id):
            raise BusinessException(*ErrorCodes.CASCADE_DELETE_ERROR)
        entity.active_status = "Deleted"
        self.repo.update(entity)
        self.uow.commit()

    def active(self, id: UUID) -> None:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if entity.active_status == "Active":
            raise BusinessException(*ErrorCodes.ALREADY_ACTIVE)
        entity.active_status = "Active"
        self.repo.update(entity)
        self.uow.commit()

    def inactive(self, id: UUID) -> None:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if entity.active_status == "Inactive":
            raise BusinessException(*ErrorCodes.ALREADY_INACTIVE)
        entity.active_status = "Inactive"
        self.repo.update(entity)
        self.uow.commit()

    def get_specific(self, id: UUID) -> dict:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        return {"id": entity.id, "code": entity.code, "title": entity.title, "iconAddress": entity.icon_address, "color": entity.color, "description": entity.description, "createdAt": entity.audit.create_date, "createdBy": "System"}

    def get_all(self, title, code, description, offset, limit) -> dict:
        items, total = self.repo.search(title, code, description, offset, limit)
        if total == 0:
            raise BusinessException(*ErrorCodes.NO_DATA_FOUND)
        return {"offset": offset, "limit": limit, "totalRecord": total, "dataList": [{"id": i.id, "code": i.code, "title": i.title, "iconAddress": i.icon_address, "color": i.color, "description": i.description, "createdAt": i.audit.create_date, "createdBy": "System"} for i in items]}

    def get_combo(self) -> list:
        items = self.repo.get_all_active()
        if not items:
            raise BusinessException(*ErrorCodes.NO_DATA_FOUND)
        return [{"id": i.id, "title": i.title, "code": i.code} for i in items]


class StatusService:
    def __init__(self, repo: StatusRepository, uow: UnitOfWork):
        self.repo = repo
        self.uow = uow

    def add(self, data: dict) -> UUID:
        if self.repo.get_by_code(data["code"]):
            raise BusinessException(*ErrorCodes.CODE_EXISTS)
        valid_effects = ["To Do", "In Progress", "Done"]
        if data["statusEffect"] not in valid_effects:
            raise BusinessException(*ErrorCodes.STATUS_EFFECT_INCORRECT)
        entity = Status(code=data["code"], title=data["title"], color=data["color"], status_effect=data["statusEffect"], description=data.get("description"))
        self.repo.add(entity)
        self.uow.commit()
        return entity.id

    def update(self, id: UUID, data: dict) -> None:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        existing = self.repo.get_by_code(data["code"])
        if existing and existing.id != id:
            raise BusinessException(*ErrorCodes.CODE_EXISTS)
        valid_effects = ["To Do", "In Progress", "Done"]
        if data["statusEffect"] not in valid_effects:
            raise BusinessException(*ErrorCodes.STATUS_EFFECT_INCORRECT)
        entity.code = data["code"]
        entity.title = data["title"]
        entity.color = data["color"]
        entity.status_effect = data["statusEffect"]
        entity.description = data.get("description")
        self.repo.update(entity)
        self.uow.commit()

    def delete(self, id: UUID) -> None:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if self.repo.has_dependencies(id):
            raise BusinessException(*ErrorCodes.CASCADE_DELETE_ERROR)
        entity.active_status = "Deleted"
        self.repo.update(entity)
        self.uow.commit()

    def active(self, id: UUID) -> None:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if entity.active_status == "Active":
            raise BusinessException(*ErrorCodes.ALREADY_ACTIVE)
        entity.active_status = "Active"
        self.repo.update(entity)
        self.uow.commit()

    def inactive(self, id: UUID) -> None:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if entity.active_status == "Inactive":
            raise BusinessException(*ErrorCodes.ALREADY_INACTIVE)
        entity.active_status = "Inactive"
        self.repo.update(entity)
        self.uow.commit()

    def get_specific(self, id: UUID) -> dict:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        return {"id": entity.id, "code": entity.code, "title": entity.title, "color": entity.color, "statusEffect": entity.status_effect, "description": entity.description, "createdAt": entity.audit.create_date, "createdBy": "System"}

    def get_all(self, title, code, description, offset, limit) -> dict:
        items, total = self.repo.search(title, code, description, offset, limit)
        if total == 0:
            raise BusinessException(*ErrorCodes.NO_DATA_FOUND)
        return {"offset": offset, "limit": limit, "totalRecord": total, "dataList": [{"id": i.id, "code": i.code, "title": i.title, "color": i.color, "statusEffect": i.status_effect, "description": i.description, "createdAt": i.audit.create_date, "createdBy": "System"} for i in items]}

    def get_combo(self) -> list:
        items = self.repo.get_all_active()
        if not items:
            raise BusinessException(*ErrorCodes.NO_DATA_FOUND)
        return [{"id": i.id, "title": i.title, "code": i.code} for i in items]


class ResolutionService:
    def __init__(self, repo: ResolutionRepository, uow: UnitOfWork):
        self.repo = repo
        self.uow = uow

    def add(self, data: dict) -> UUID:
        if self.repo.get_by_code(data["code"]):
            raise BusinessException(*ErrorCodes.CODE_EXISTS)
        entity = Resolution(code=data["code"], title=data["title"], color=data["color"], is_resolved=data["isResolved"], description=data.get("description"))
        self.repo.add(entity)
        self.uow.commit()
        return entity.id

    def update(self, id: UUID, data: dict) -> None:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        existing = self.repo.get_by_code(data["code"])
        if existing and existing.id != id:
            raise BusinessException(*ErrorCodes.CODE_EXISTS)
        entity.code = data["code"]
        entity.title = data["title"]
        entity.color = data["color"]
        entity.is_resolved = data["isResolved"]
        entity.description = data.get("description")
        self.repo.update(entity)
        self.uow.commit()

    def delete(self, id: UUID) -> None:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if self.repo.has_dependencies(id):
            raise BusinessException(*ErrorCodes.CASCADE_DELETE_ERROR)
        entity.active_status = "Deleted"
        self.repo.update(entity)
        self.uow.commit()

    def active(self, id: UUID) -> None:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if entity.active_status == "Active":
            raise BusinessException(*ErrorCodes.ALREADY_ACTIVE)
        entity.active_status = "Active"
        self.repo.update(entity)
        self.uow.commit()

    def inactive(self, id: UUID) -> None:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if entity.active_status == "Inactive":
            raise BusinessException(*ErrorCodes.ALREADY_INACTIVE)
        entity.active_status = "Inactive"
        self.repo.update(entity)
        self.uow.commit()

    def get_specific(self, id: UUID) -> dict:
        entity = self.repo.get_by_id(id)
        if not entity:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        return {"id": entity.id, "code": entity.code, "title": entity.title, "color": entity.color, "isResolved": entity.is_resolved, "description": entity.description, "createdAt": entity.audit.create_date, "createdBy": "System"}

    def get_all(self, title, code, description, offset, limit) -> dict:
        items, total = self.repo.search(title, code, description, offset, limit)
        if total == 0:
            raise BusinessException(*ErrorCodes.NO_DATA_FOUND)
        return {"offset": offset, "limit": limit, "totalRecord": total, "dataList": [{"id": i.id, "code": i.code, "title": i.title, "color": i.color, "isResolved": i.is_resolved, "description": i.description, "createdAt": i.audit.create_date, "createdBy": "System"} for i in items]}

    def get_combo(self) -> list:
        items = self.repo.get_all_active()
        if not items:
            raise BusinessException(*ErrorCodes.NO_DATA_FOUND)
        return [{"id": i.id, "title": i.title, "code": i.code} for i in items]


class FileExtensionService(BaseLookupService):
    def __init__(self, repo: FileExtensionRepository, uow: UnitOfWork):
        super().__init__(repo, uow, FileExtension)
        
    def add(self, data: dict) -> UUID:
        if self.repo.get_by_code(data["code"]):
            raise BusinessException(*ErrorCodes.CODE_EXISTS)
        if self.repo.get_by_title(data["title"]):
            raise BusinessException(*ErrorCodes.FILE_EXTENSION_DUPLICATED)
        return super().add(data)


class TestComplexityLevelService(BaseLookupService):
    def __init__(self, repo: TestComplexityLevelRepository, uow: UnitOfWork):
        super().__init__(repo, uow, TestComplexityLevel)
        
    def add(self, data: dict) -> UUID:
        if self.repo.get_by_code(data["code"]):
            raise BusinessException(*ErrorCodes.CODE_EXISTS)
        if self.repo.get_by_value_number(data["valueNumber"]):
            raise BusinessException(*ErrorCodes.TEST_COMPLEXITY_DUPLICATED)
            
        entity = TestComplexityLevel(code=data["code"], title=data["title"], value_number=data["valueNumber"], description=data.get("description"))
        self.repo.add(entity)
        self.uow.commit()
        return entity.id


class CurrencyService(BaseLookupService):
    def __init__(self, repo: CurrencyRepository, uow: UnitOfWork):
        super().__init__(repo, uow, Currency)
        
    def add(self, data: dict) -> UUID:
        if self.repo.get_by_code(data["code"]):
            raise BusinessException(*ErrorCodes.CODE_EXISTS)
        if not re.match(r'^[A-Z]+$', data["symbol"]):
            raise BusinessException(*ErrorCodes.CURRENCY_SYMBOL_UPPERCASE)
        if self.repo.get_by_symbol(data["symbol"]):
            raise BusinessException(*ErrorCodes.CURRENCY_SYMBOL_DUPLICATED)
            
        entity = Currency(code=data["code"], title=data["title"], symbol=data["symbol"], description=data.get("description"))
        self.repo.add(entity)
        self.uow.commit()
        return entity.id