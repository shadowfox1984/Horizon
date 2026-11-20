from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class LoginRequest(BaseModel):
    username: str
    password: str

class ChangePasswordRequest(BaseModel):
    currentPassword: str
    newPassword: str
    confirmPassword: str

class ChangePasswordByAdminRequest(BaseModel):
    profileId: UUID
    newPassword: str
    confirmPassword: str

class GroupCreateRequest(BaseModel):
    title: str
    code: str
    description: Optional[str] = None

class GroupUpdateRequest(BaseModel):
    title: str
    code: str
    description: Optional[str] = None

class GroupPermissionCreateRequest(BaseModel):
    formPermissionId: UUID
    groupId: UUID

class GroupPermissionUpdateRequest(BaseModel):
    formPermissionId: UUID
    groupId: UUID

class ProfileCreateRequest(BaseModel):
    firstName: str
    lastName: str
    gender: str
    staffNumber: str
    activeFrom: datetime
    activeTo: Optional[datetime] = None
    positionId: Optional[UUID] = None
    avatar: Optional[str] = None
    birthday: Optional[str] = None
    phoneNumber: Optional[str] = None
    mobileNumber: Optional[str] = None
    emailAddress: Optional[str] = None
    address: Optional[str] = None
    postalCode: Optional[str] = None
    username: str
    password: str

class ProfileUpdateRequest(BaseModel):
    firstName: str
    lastName: str
    gender: str
    staffNumber: str
    activeFrom: datetime
    activeTo: Optional[datetime] = None
    positionId: Optional[UUID] = None
    avatar: Optional[str] = None
    birthday: Optional[str] = None
    phoneNumber: Optional[str] = None
    mobileNumber: Optional[str] = None
    emailAddress: Optional[str] = None
    address: Optional[str] = None
    postalCode: Optional[str] = None
    username: str

class ProfilePermissionCreateRequest(BaseModel):
    formPermissionId: UUID
    profileId: UUID

class ProfilePermissionUpdateRequest(BaseModel):
    formPermissionId: UUID
    profileId: UUID

class ProfileGroupCreateRequest(BaseModel):
    profileId: UUID
    groupId: UUID

class ProfileGroupUpdateRequest(BaseModel):
    profileId: UUID
    groupId: UUID