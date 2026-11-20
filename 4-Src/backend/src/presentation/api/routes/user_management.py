from fastapi import APIRouter, Depends, Query, Body
from typing import Optional
from uuid import UUID
from src.presentation.api.schemas.base import StandardResponse
from src.presentation.api.schemas.user_management import *
from src.application.user_management.services import (
    AuthService, GroupService, GroupPermissionService,
    ProfileService, ProfilePermissionService, ProfileGroupService
)
from src.infrastructure.persistence.container import get_uow_dep
from src.infrastructure.persistence.unit_of_work import SqlAlchemyUnitOfWork

router = APIRouter(prefix="/api/user", tags=["User Management"])

@router.post("/auth/login", response_model=StandardResponse[dict])
def login(request: LoginRequest, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = AuthService(uow.profiles, uow.user_tokens, uow)
    token = service.login(request.username, request.password)
    return StandardResponse(statusCode=200, status="success", message="The token is generated successfully.", data={"token": token})

@router.put("/auth/refreshToken", response_model=StandardResponse[None])
def refresh_token(authorization: str = Body(..., embed=True), uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = AuthService(uow.profiles, uow.user_tokens, uow)
    service.refresh_token(authorization)
    return StandardResponse(statusCode=200, status="success", message="The token is refreshed successfully.")

@router.put("/auth/signOut", response_model=StandardResponse[None])
def sign_out(authorization: str = Body(..., embed=True), uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = AuthService(uow.profiles, uow.user_tokens, uow)
    service.sign_out(authorization)
    return StandardResponse(statusCode=200, status="success", message="The user is signed out successfully.")

@router.put("/auth/changePassword", response_model=StandardResponse[None])
def change_password(request: ChangePasswordRequest, profile_id: UUID = Query(...), uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = AuthService(uow.profiles, uow.user_tokens, uow)
    service.change_password(profile_id, request.currentPassword, request.newPassword, request.confirmPassword)
    return StandardResponse(statusCode=200, status="success", message="The password is changed successfully.")

@router.put("/auth/changePasswordByAdmin", response_model=StandardResponse[None])
def change_password_by_admin(request: ChangePasswordByAdminRequest, admin_id: UUID = Query(...), uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = AuthService(uow.profiles, uow.user_tokens, uow)
    service.change_password_by_admin(admin_id, request.profileId, request.newPassword, request.confirmPassword)
    return StandardResponse(statusCode=200, status="success", message="The password is changed successfully.")

@router.get("/auth/getCaptcha", response_model=StandardResponse[dict])
def get_captcha(uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = AuthService(uow.profiles, uow.user_tokens, uow)
    captcha = service.get_captcha()
    return StandardResponse(statusCode=200, status="success", message="The CAPTCHA image is generated successfully.", data={"captcha": captcha})

@router.post("/group", response_model=StandardResponse[dict])
def add_group(request: GroupCreateRequest, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = GroupService(uow.groups, uow)
    new_id = service.add(request.title, request.code, request.description)
    return StandardResponse(statusCode=200, status="success", message="The record is added successfully.", data={"id": new_id})

@router.put("/group/{id}", response_model=StandardResponse[None])
def update_group(id: UUID, request: GroupUpdateRequest, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = GroupService(uow.groups, uow)
    service.update(id, request.title, request.code, request.description)
    return StandardResponse(statusCode=200, status="success", message="The record is updated successfully.")

@router.delete("/group/{id}", response_model=StandardResponse[None])
def delete_group(id: UUID, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = GroupService(uow.groups, uow)
    service.delete(id)
    return StandardResponse(statusCode=200, status="success", message="The record is deleted successfully.")

@router.put("/group/active/{id}", response_model=StandardResponse[None])
def active_group(id: UUID, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = GroupService(uow.groups, uow)
    service.active(id)
    return StandardResponse(statusCode=200, status="success", message="The record is activated successfully.")

@router.put("/group/inactive/{id}", response_model=StandardResponse[None])
def inactive_group(id: UUID, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = GroupService(uow.groups, uow)
    service.inactive(id)
    return StandardResponse(statusCode=200, status="success", message="The record is inactivated successfully.")

@router.get("/group/{id}", response_model=StandardResponse[dict])
def get_group(id: UUID, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = GroupService(uow.groups, uow)
    data = service.get_specific(id)
    return StandardResponse(statusCode=200, status="success", message="The data is returned successfully.", data=data)

@router.get("/group/getAll", response_model=StandardResponse[dict])
def get_all_groups(
    title: Optional[str] = Query(None),
    code: Optional[str] = Query(None),
    description: Optional[str] = Query(None),
    offset: int = Query(0),
    limit: int = Query(15),
    uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)
):
    service = GroupService(uow.groups, uow)
    data = service.get_all(title, code, description, offset, limit)
    return StandardResponse(statusCode=200, status="success", message="The data is returned successfully.", data=data)

@router.get("/group/getCombo", response_model=StandardResponse[list])
def get_combo_groups(uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = GroupService(uow.groups, uow)
    data = service.get_combo()
    return StandardResponse(statusCode=200, status="success", message="The data is returned successfully.", data=data)

@router.post("/groupPermission", response_model=StandardResponse[dict])
def add_group_permission(request: GroupPermissionCreateRequest, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = GroupPermissionService(uow.group_permissions, uow.groups, uow.forms, uow)
    new_id = service.add(request.formPermissionId, request.groupId)
    return StandardResponse(statusCode=200, status="success", message="The record is added successfully.", data={"id": new_id})

@router.put("/groupPermission/{id}", response_model=StandardResponse[None])
def update_group_permission(id: UUID, request: GroupPermissionUpdateRequest, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = GroupPermissionService(uow.group_permissions, uow.groups, uow.forms, uow)
    service.update(id, request.formPermissionId, request.groupId)
    return StandardResponse(statusCode=200, status="success", message="The record is updated successfully.")

@router.delete("/groupPermission/{id}", response_model=StandardResponse[None])
def delete_group_permission(id: UUID, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = GroupPermissionService(uow.group_permissions, uow.groups, uow.forms, uow)
    service.delete(id)
    return StandardResponse(statusCode=200, status="success", message="The record is deleted successfully.")

@router.put("/groupPermission/active/{id}", response_model=StandardResponse[None])
def active_group_permission(id: UUID, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = GroupPermissionService(uow.group_permissions, uow.groups, uow.forms, uow)
    service.active(id)
    return StandardResponse(statusCode=200, status="success", message="The record is activated successfully.")

@router.put("/groupPermission/inactive/{id}", response_model=StandardResponse[None])
def inactive_group_permission(id: UUID, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = GroupPermissionService(uow.group_permissions, uow.groups, uow.forms, uow)
    service.inactive(id)
    return StandardResponse(statusCode=200, status="success", message="The record is inactivated successfully.")

@router.get("/groupPermission/{id}", response_model=StandardResponse[dict])
def get_specific_group_permission(id: UUID, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = GroupPermissionService(uow.group_permissions, uow.groups, uow.forms, uow)
    data = service.get_specific(id)
    return StandardResponse(statusCode=200, status="success", message="The data is returned successfully.", data=data)

@router.get("/groupPermission/getAll", response_model=StandardResponse[dict])
def get_all_group_permissions(
    groupId: Optional[UUID] = Query(None),
    offset: int = Query(0),
    limit: int = Query(15),
    uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)
):
    service = GroupPermissionService(uow.group_permissions, uow.groups, uow.forms, uow)
    data = service.get_all(groupId, offset, limit)
    return StandardResponse(statusCode=200, status="success", message="The data is returned successfully.", data=data)

@router.get("/groupPermission/getCombo", response_model=StandardResponse[list])
def get_combo_group_permissions(uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = GroupPermissionService(uow.group_permissions, uow.groups, uow.forms, uow)
    data = service.get_combo()
    return StandardResponse(statusCode=200, status="success", message="The data is returned successfully.", data=data)

@router.post("/profile", response_model=StandardResponse[dict])
def add_profile(request: ProfileCreateRequest, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfileService(uow.profiles, uow.groups, uow)
    new_id = service.add(request.model_dump())
    return StandardResponse(statusCode=200, status="success", message="The record is added successfully.", data={"id": new_id})

@router.put("/profile/{id}", response_model=StandardResponse[None])
def update_profile(id: UUID, request: ProfileUpdateRequest, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfileService(uow.profiles, uow.groups, uow)
    service.update(id, request.model_dump())
    return StandardResponse(statusCode=200, status="success", message="The record is updated successfully.")

@router.delete("/profile/{id}", response_model=StandardResponse[None])
def delete_profile(id: UUID, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfileService(uow.profiles, uow.groups, uow)
    service.delete(id)
    return StandardResponse(statusCode=200, status="success", message="The record is deleted successfully.")

@router.put("/profile/active/{id}", response_model=StandardResponse[None])
def active_profile(id: UUID, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfileService(uow.profiles, uow.groups, uow)
    service.active(id)
    return StandardResponse(statusCode=200, status="success", message="The record is activated successfully.")

@router.put("/profile/inactive/{id}", response_model=StandardResponse[None])
def inactive_profile(id: UUID, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfileService(uow.profiles, uow.groups, uow)
    service.inactive(id)
    return StandardResponse(statusCode=200, status="success", message="The record is inactivated successfully.")

@router.get("/profile/{id}", response_model=StandardResponse[dict])
def get_profile(id: UUID, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfileService(uow.profiles, uow.groups, uow)
    data = service.get_specific(id)
    return StandardResponse(statusCode=200, status="success", message="The data is returned successfully.", data=data)

@router.get("/profile/getAll", response_model=StandardResponse[dict])
def get_all_profiles(
    firstName: Optional[str] = Query(None),
    lastName: Optional[str] = Query(None),
    username: Optional[str] = Query(None),
    offset: int = Query(0),
    limit: int = Query(15),
    uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)
):
    service = ProfileService(uow.profiles, uow.groups, uow)
    data = service.get_all(firstName, lastName, username, offset, limit)
    return StandardResponse(statusCode=200, status="success", message="The data is returned successfully.", data=data)

@router.get("/profile/getCombo", response_model=StandardResponse[list])
def get_combo_profiles(uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfileService(uow.profiles, uow.groups, uow)
    data = service.get_combo()
    return StandardResponse(statusCode=200, status="success", message="The data is returned successfully.", data=data)

@router.post("/profilePermission", response_model=StandardResponse[dict])
def add_profile_permission(request: ProfilePermissionCreateRequest, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfilePermissionService(uow.profile_permissions, uow.profiles, uow)
    new_id = service.add(request.formPermissionId, request.profileId)
    return StandardResponse(statusCode=200, status="success", message="The record is added successfully.", data={"id": new_id})

@router.put("/profilePermission/{id}", response_model=StandardResponse[None])
def update_profile_permission(id: UUID, request: ProfilePermissionUpdateRequest, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfilePermissionService(uow.profile_permissions, uow.profiles, uow)
    service.update(id, request.formPermissionId, request.profileId)
    return StandardResponse(statusCode=200, status="success", message="The record is updated successfully.")

@router.delete("/profilePermission/{id}", response_model=StandardResponse[None])
def delete_profile_permission(id: UUID, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfilePermissionService(uow.profile_permissions, uow.profiles, uow)
    service.delete(id)
    return StandardResponse(statusCode=200, status="success", message="The record is deleted successfully.")

@router.put("/profilePermission/active/{id}", response_model=StandardResponse[None])
def active_profile_permission(id: UUID, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfilePermissionService(uow.profile_permissions, uow.profiles, uow)
    service.active(id)
    return StandardResponse(statusCode=200, status="success", message="The record is activated successfully.")

@router.put("/profilePermission/inactive/{id}", response_model=StandardResponse[None])
def inactive_profile_permission(id: UUID, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfilePermissionService(uow.profile_permissions, uow.profiles, uow)
    service.inactive(id)
    return StandardResponse(statusCode=200, status="success", message="The record is inactivated successfully.")

@router.get("/profilePermission/{id}", response_model=StandardResponse[dict])
def get_specific_profile_permission(id: UUID, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfilePermissionService(uow.profile_permissions, uow.profiles, uow)
    data = service.get_specific(id)
    return StandardResponse(statusCode=200, status="success", message="The data is returned successfully.", data=data)

@router.get("/profilePermission/getAll", response_model=StandardResponse[dict])
def get_all_profile_permissions(
    profileId: Optional[UUID] = Query(None),
    offset: int = Query(0),
    limit: int = Query(15),
    uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)
):
    service = ProfilePermissionService(uow.profile_permissions, uow.profiles, uow)
    data = service.get_all(profileId, offset, limit)
    return StandardResponse(statusCode=200, status="success", message="The data is returned successfully.", data=data)

@router.get("/profilePermission/getCombo", response_model=StandardResponse[list])
def get_combo_profile_permissions(uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfilePermissionService(uow.profile_permissions, uow.profiles, uow)
    data = service.get_combo()
    return StandardResponse(statusCode=200, status="success", message="The data is returned successfully.", data=data)

@router.post("/profileGroup", response_model=StandardResponse[dict])
def add_profile_group(request: ProfileGroupCreateRequest, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfileGroupService(uow.profile_groups, uow.profiles, uow.groups, uow)
    new_id = service.add(request.profileId, request.groupId)
    return StandardResponse(statusCode=200, status="success", message="The record is added successfully.", data={"id": new_id})

@router.put("/profileGroup/{id}", response_model=StandardResponse[None])
def update_profile_group(id: UUID, request: ProfileGroupUpdateRequest, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfileGroupService(uow.profile_groups, uow.profiles, uow.groups, uow)
    service.update(id, request.profileId, request.groupId)
    return StandardResponse(statusCode=200, status="success", message="The record is updated successfully.")

@router.delete("/profileGroup/{id}", response_model=StandardResponse[None])
def delete_profile_group(id: UUID, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfileGroupService(uow.profile_groups, uow.profiles, uow.groups, uow)
    service.delete(id)
    return StandardResponse(statusCode=200, status="success", message="The record is deleted successfully.")

@router.put("/profileGroup/active/{id}", response_model=StandardResponse[None])
def active_profile_group(id: UUID, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfileGroupService(uow.profile_groups, uow.profiles, uow.groups, uow)
    service.active(id)
    return StandardResponse(statusCode=200, status="success", message="The record is activated successfully.")

@router.put("/profileGroup/inactive/{id}", response_model=StandardResponse[None])
def inactive_profile_group(id: UUID, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfileGroupService(uow.profile_groups, uow.profiles, uow.groups, uow)
    service.inactive(id)
    return StandardResponse(statusCode=200, status="success", message="The record is inactivated successfully.")

@router.get("/profileGroup/{id}", response_model=StandardResponse[dict])
def get_specific_profile_group(id: UUID, uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfileGroupService(uow.profile_groups, uow.profiles, uow.groups, uow)
    data = service.get_specific(id)
    return StandardResponse(statusCode=200, status="success", message="The data is returned successfully.", data=data)

@router.get("/profileGroup/getAll", response_model=StandardResponse[dict])
def get_all_profile_groups(
    profileId: Optional[UUID] = Query(None),
    groupId: Optional[UUID] = Query(None),
    offset: int = Query(0),
    limit: int = Query(15),
    uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)
):
    service = ProfileGroupService(uow.profile_groups, uow.profiles, uow.groups, uow)
    data = service.get_all(profileId, groupId, offset, limit)
    return StandardResponse(statusCode=200, status="success", message="The data is returned successfully.", data=data)

@router.get("/profileGroup/getCombo", response_model=StandardResponse[list])
def get_combo_profile_groups(uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    service = ProfileGroupService(uow.profile_groups, uow.profiles, uow.groups, uow)
    data = service.get_combo()
    return StandardResponse(statusCode=200, status="success", message="The data is returned successfully.", data=data)

@router.get("/formPermission/getFormCombo", response_model=StandardResponse[list])
def get_form_combo(uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    forms = uow.forms.get_all_active()
    data = [{"id": f.id, "title": f.title} for f in forms]
    return StandardResponse(statusCode=200, status="success", message="The data is returned successfully.", data=data)

@router.get("/formPermission/getPermissionCombo", response_model=StandardResponse[list])
def get_permission_combo(uow: SqlAlchemyUnitOfWork = Depends(get_uow_dep)):
    permissions = uow.permissions.get_all_active()
    data = [{"id": p.id, "title": p.title} for p in permissions]
    return StandardResponse(statusCode=200, status="success", message="The data is returned successfully.", data=data)