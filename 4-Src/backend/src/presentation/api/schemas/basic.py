from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

# --- Shared ---
class BaseLookupCreateRequest(BaseModel):
    code: str
    title: str
    description: Optional[str] = None

class BaseLookupUpdateRequest(BaseModel):
    code: str
    title: str
    description: Optional[str] = None

# --- Education Level ---
class EducationLevelCreateRequest(BaseLookupCreateRequest):
    pass

class EducationLevelUpdateRequest(BaseLookupUpdateRequest):
    pass

# --- Priority ---
class PriorityCreateRequest(BaseModel):
    code: str
    title: str
    color: str
    ordering: int
    description: Optional[str] = None

class PriorityUpdateRequest(BaseModel):
    code: str
    title: str
    color: str
    ordering: int
    description: Optional[str] = None

# --- Issue Type ---
class IssueTypeCreateRequest(BaseModel):
    code: str
    title: str
    iconAddress: str
    color: str
    description: Optional[str] = None

class IssueTypeUpdateRequest(BaseModel):
    code: str
    title: str
    iconAddress: str
    color: str
    description: Optional[str] = None

# --- Status ---
class StatusCreateRequest(BaseModel):
    code: str
    title: str
    color: str
    statusEffect: str
    description: Optional[str] = None

class StatusUpdateRequest(BaseModel):
    code: str
    title: str
    color: str
    statusEffect: str
    description: Optional[str] = None

# --- Resolution ---
class ResolutionCreateRequest(BaseModel):
    code: str
    title: str
    color: str
    isResolved: bool
    description: Optional[str] = None

class ResolutionUpdateRequest(BaseModel):
    code: str
    title: str
    color: str
    isResolved: bool
    description: Optional[str] = None

# --- Meeting Type ---
class MeetingTypeCreateRequest(BaseLookupCreateRequest):
    pass

class MeetingTypeUpdateRequest(BaseLookupUpdateRequest):
    pass

# --- Document Type ---
class DocumentTypeCreateRequest(BaseLookupCreateRequest):
    pass

class DocumentTypeUpdateRequest(BaseLookupUpdateRequest):
    pass

# --- File Extension ---
class FileExtensionCreateRequest(BaseLookupCreateRequest):
    pass

class FileExtensionUpdateRequest(BaseLookupUpdateRequest):
    pass

# --- Contract Type (StaffContractType) ---
class ContractTypeCreateRequest(BaseLookupCreateRequest):
    pass

class ContractTypeUpdateRequest(BaseLookupUpdateRequest):
    pass

# --- Test Approval ---
class TestApprovalCreateRequest(BaseModel):
    code: str
    title: str
    isApproved: bool
    color: str
    description: Optional[str] = None

class TestApprovalUpdateRequest(BaseModel):
    code: str
    title: str
    isApproved: bool
    color: str
    description: Optional[str] = None

# --- Test Complexity Level ---
class TestComplexityLevelCreateRequest(BaseModel):
    code: str
    title: str
    valueNumber: float
    description: Optional[str] = None

class TestComplexityLevelUpdateRequest(BaseModel):
    code: str
    title: str
    valueNumber: float
    description: Optional[str] = None

# --- Time Unit ---
class TimeUnitCreateRequest(BaseModel):
    code: str
    title: str
    valueBasedOnMillisecond: int
    description: Optional[str] = None

class TimeUnitUpdateRequest(BaseModel):
    code: str
    title: str
    valueBasedOnMillisecond: int
    description: Optional[str] = None

# --- Currency ---
class CurrencyCreateRequest(BaseModel):
    code: str
    title: str
    symbol: str
    description: Optional[str] = None

class CurrencyUpdateRequest(BaseModel):
    code: str
    title: str
    symbol: str
    description: Optional[str] = None