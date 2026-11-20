# src/application/user_management/services.py
from uuid import UUID
from src.domain.shared.exceptions import BusinessException, ErrorCodes
from src.domain.user_management.repositories import (
    ProfileRepository, GroupRepository, UserTokenRepository, 
    GroupPermissionRepository, ProfilePermissionRepository, ProfileGroupRepository, FormRepository
)
from src.domain.user_management.entities import (
    Profile, Group, GroupPermission, ProfilePermission, ProfileGroup
)
from src.domain.shared.unit_of_work import UnitOfWork
from src.infrastructure.security.password_hasher import PasswordHasher
from src.infrastructure.security.jwt_handler import JWTHandler

class AuthService:
    def __init__(self, profile_repo: ProfileRepository, token_repo: UserTokenRepository, uow: UnitOfWork):
        self.profile_repo = profile_repo
        self.token_repo = token_repo
        self.uow = uow

    def login(self, username: str, password: str) -> str:
        profile = self.profile_repo.get_by_username(username)
        if not profile:
            raise BusinessException(*ErrorCodes.INVALID_CREDENTIALS)
        if profile.wrong_login_count >= 5:
            raise BusinessException(*ErrorCodes.USER_LOCKED)
        if not PasswordHasher.verify(password, profile.pass_salt, profile.password_hash):
            profile.wrong_login_count += 1
            self.profile_repo.update(profile)
            self.uow.commit()
            raise BusinessException(*ErrorCodes.INVALID_CREDENTIALS)
        profile.wrong_login_count = 0
        self.profile_repo.update(profile)
        self.token_repo.invalidate_all_for_profile(profile.id)
        self.uow.commit()
        return JWTHandler.create_access_token(str(profile.id))

    def refresh_token(self, token: str) -> str:
        payload = JWTHandler.decode_token(token)
        if not payload:
            raise BusinessException(*ErrorCodes.TOKEN_EXPIRED)
        user_token = self.token_repo.get_by_token(token)
        if not user_token:
            raise BusinessException(*ErrorCodes.TOKEN_INCORRECT)
        if user_token.is_signed_out:
            raise BusinessException(*ErrorCodes.SESSION_TERMINATED)
        if user_token.refresh_window_expired():
            raise BusinessException(*ErrorCodes.SESSION_EXPIRED)
        new_token = JWTHandler.create_access_token(payload["sub"])
        user_token.refresh_count += 1
        user_token.token = new_token
        self.token_repo.update(user_token)
        self.uow.commit()
        return new_token

    def sign_out(self, token: str) -> None:
        user_token = self.token_repo.get_by_token(token)
        if not user_token:
            raise BusinessException(*ErrorCodes.TOKEN_INCORRECT)
        user_token.is_signed_out = True
        self.token_repo.update(user_token)
        self.uow.commit()

    def change_password(self, profile_id: UUID, current: str, new: str, confirm: str) -> None:
        profile = self.profile_repo.get_by_id(profile_id)
        if not profile:
            raise BusinessException(*ErrorCodes.PROFILE_NOT_EXIST)
        if not PasswordHasher.verify(current, profile.pass_salt, profile.password_hash):
            raise BusinessException(*ErrorCodes.OLD_PASSWORD_INCORRECT)
        if new != confirm:
            raise BusinessException(*ErrorCodes.PASSWORD_MISMATCH)
        if not self._validate_password_format(new):
            raise BusinessException(*ErrorCodes.PASSWORD_FORMAT_INVALID)
        salt = PasswordHasher.generate_salt()
        profile.password_hash = PasswordHasher.hash_password(new, salt)
        profile.pass_salt = salt
        self.profile_repo.update(profile)
        self.uow.commit()

    def change_password_by_admin(self, admin_id: UUID, profile_id: UUID, new: str, confirm: str) -> None:
        admin = self.profile_repo.get_by_id(admin_id)
        if not admin or not self._is_admin(admin):
            raise BusinessException(*ErrorCodes.ACCESS_DENIED)
        profile = self.profile_repo.get_by_id(profile_id)
        if not profile:
            raise BusinessException(*ErrorCodes.PROFILE_NOT_EXIST)
        if new != confirm:
            raise BusinessException(*ErrorCodes.PASSWORD_MISMATCH)
        if not self._validate_password_format(new):
            raise BusinessException(*ErrorCodes.PASSWORD_FORMAT_INVALID)
        salt = PasswordHasher.generate_salt()
        profile.password_hash = PasswordHasher.hash_password(new, salt)
        profile.pass_salt = salt
        self.profile_repo.update(profile)
        self.uow.commit()

    def get_captcha(self) -> str:
        return "base64_image_string"

    def _validate_password_format(self, password: str) -> bool:
        return len(password) >= 8

    def _is_admin(self, profile: Profile) -> bool:
        return True

class GroupService:
    def __init__(self, group_repo: GroupRepository, uow: UnitOfWork):
        self.group_repo = group_repo
        self.uow = uow

    def add(self, title: str, code: str, description: str) -> UUID:
        if self.group_repo.get_by_code(code):
            raise BusinessException(*ErrorCodes.CODE_EXISTS)
        group = Group(title=title, code=code, description=description)
        self.group_repo.add(group)
        self.uow.commit()
        return group.id

    def update(self, group_id: UUID, title: str, code: str, description: str) -> None:
        group = self.group_repo.get_by_id(group_id)
        if not group:
            raise BusinessException(*ErrorCodes.GROUP_NOT_EXIST)
        existing = self.group_repo.get_by_code(code)
        if existing and existing.id != group_id:
            raise BusinessException(*ErrorCodes.CODE_EXISTS)
        group.title = title
        group.code = code
        group.description = description
        self.group_repo.update(group)
        self.uow.commit()

    def delete(self, group_id: UUID) -> None:
        group = self.group_repo.get_by_id(group_id)
        if not group:
            raise BusinessException(*ErrorCodes.GROUP_NOT_EXIST)
        if self.group_repo.has_dependencies(group_id):
            raise BusinessException(*ErrorCodes.CASCADE_DELETE_ERROR)
        group.active_status = "Deleted"
        self.group_repo.update(group)
        self.uow.commit()

    def active(self, group_id: UUID) -> None:
        group = self.group_repo.get_by_id(group_id)
        if not group:
            raise BusinessException(*ErrorCodes.GROUP_NOT_EXIST)
        if group.active_status == "Active":
            raise BusinessException(*ErrorCodes.ALREADY_ACTIVE)
        group.active_status = "Active"
        self.group_repo.update(group)
        self.uow.commit()

    def inactive(self, group_id: UUID) -> None:
        group = self.group_repo.get_by_id(group_id)
        if not group:
            raise BusinessException(*ErrorCodes.GROUP_NOT_EXIST)
        if group.active_status == "Inactive":
            raise BusinessException(*ErrorCodes.ALREADY_INACTIVE)
        group.active_status = "Inactive"
        self.group_repo.update(group)
        self.uow.commit()

    def get_specific(self, group_id: UUID) -> dict:
        group = self.group_repo.get_by_id(group_id)
        if not group:
            raise BusinessException(*ErrorCodes.GROUP_NOT_EXIST)
        return {"id": group.id, "title": group.title, "code": group.code, "description": group.description, "createdAt": group.audit.create_date, "createdBy": "System"}

    def get_all(self, title: str, code: str, description: str, offset: int, limit: int) -> dict:
        groups, total = self.group_repo.search(title, code, description, offset, limit)
        return {"offset": offset, "limit": limit, "totalRecord": total, "dataList": [{"id": g.id, "title": g.title, "code": g.code, "description": g.description, "createdAt": g.audit.create_date, "createdBy": "System"} for g in groups]}

    def get_combo(self) -> list:
        groups = self.group_repo.get_all_active()
        return [{"id": g.id, "title": g.title} for g in groups]

class GroupPermissionService:
    def __init__(self, repo: GroupPermissionRepository, group_repo: GroupRepository, perm_repo: FormRepository, uow: UnitOfWork):
        self.repo = repo
        self.group_repo = group_repo
        self.perm_repo = perm_repo
        self.uow = uow

    def add(self, form_permission_id: UUID, group_id: UUID) -> UUID:
        group = self.group_repo.get_by_id(group_id)
        if not group:
            raise BusinessException(*ErrorCodes.GROUP_NOT_EXIST)
        if self.repo.exists(form_permission_id, group_id):
            raise BusinessException(*ErrorCodes.GROUP_PERMISSION_EXISTS)
        gp = GroupPermission(form_permission_id=form_permission_id, group_id=group_id)
        self.repo.add(gp)
        self.uow.commit()
        return gp.id

    def update(self, id: UUID, form_permission_id: UUID, group_id: UUID) -> None:
        gp = self.repo.get_by_id(id)
        if not gp:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if self.repo.exists(form_permission_id, group_id, exclude_id=id):
            raise BusinessException(*ErrorCodes.GROUP_PERMISSION_EXISTS)
        gp.form_permission_id = form_permission_id
        gp.group_id = group_id
        self.repo.update(gp)
        self.uow.commit()

    def delete(self, id: UUID) -> None:
        gp = self.repo.get_by_id(id)
        if not gp:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        gp.active_status = "Deleted"
        self.repo.update(gp)
        self.uow.commit()

    def active(self, id: UUID) -> None:
        gp = self.repo.get_by_id(id)
        if not gp:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if gp.active_status == "Active":
            raise BusinessException(*ErrorCodes.ALREADY_ACTIVE)
        gp.active_status = "Active"
        self.repo.update(gp)
        self.uow.commit()

    def inactive(self, id: UUID) -> None:
        gp = self.repo.get_by_id(id)
        if not gp:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if gp.active_status == "Inactive":
            raise BusinessException(*ErrorCodes.ALREADY_INACTIVE)
        gp.active_status = "Inactive"
        self.repo.update(gp)
        self.uow.commit()

    def get_specific(self, id: UUID) -> dict:
        gp = self.repo.get_by_id(id)
        if not gp:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        return {"id": gp.id, "formPermissionId": gp.form_permission_id, "groupId": gp.group_id}

    def get_all(self, group_id: UUID, offset: int, limit: int) -> dict:
        items, total = self.repo.search(group_id, offset, limit)
        return {"offset": offset, "limit": limit, "totalRecord": total, "dataList": [{"id": i.id, "formPermissionId": i.form_permission_id, "groupId": i.group_id} for i in items]}

    def get_combo(self) -> list:
        items = self.repo.get_all_active()
        return [{"id": i.id, "title": f"{i.form_id}-{i.permission_id}"} for i in items]

class ProfileService:
    def __init__(self, profile_repo: ProfileRepository, group_repo: GroupRepository, uow: UnitOfWork):
        self.profile_repo = profile_repo
        self.group_repo = group_repo
        self.uow = uow

    def add(self, data: dict) -> UUID:
        if self.profile_repo.get_by_username(data["username"]):
            raise BusinessException(*ErrorCodes.USERNAME_EXISTS)
        salt = PasswordHasher.generate_salt()
        password_hash = PasswordHasher.hash_password(data["password"], salt)
        profile = Profile(
            first_name=data["firstName"], last_name=data["lastName"], gender=data["gender"],
            staff_number=data["staffNumber"], active_from=data["activeFrom"], active_to=data.get("activeTo"),
            position_id=data.get("positionId"), avatar=data.get("avatar"), birthday=data.get("birthday"),
            phone_number=data.get("phoneNumber"), mobile_number=data.get("mobileNumber"),
            email_address=data.get("emailAddress"), address=data.get("address"), postal_code=data.get("postalCode"),
            username=data["username"], password_hash=password_hash, pass_salt=salt
        )
        self.profile_repo.add(profile)
        self.uow.commit()
        return profile.id

    def update(self, profile_id: UUID, data: dict) -> None:
        profile = self.profile_repo.get_by_id(profile_id)
        if not profile:
            raise BusinessException(*ErrorCodes.PROFILE_NOT_EXIST)
        existing = self.profile_repo.get_by_username(data["username"])
        if existing and existing.id != profile_id:
            raise BusinessException(*ErrorCodes.USERNAME_EXISTS)
        profile.first_name = data["firstName"]
        profile.last_name = data["lastName"]
        profile.gender = data["gender"]
        profile.staff_number = data["staffNumber"]
        profile.active_from = data["activeFrom"]
        profile.active_to = data.get("activeTo")
        profile.position_id = data.get("positionId")
        profile.avatar = data.get("avatar")
        profile.birthday = data.get("birthday")
        profile.phone_number = data.get("phoneNumber")
        profile.mobile_number = data.get("mobileNumber")
        profile.email_address = data.get("emailAddress")
        profile.address = data.get("address")
        profile.postal_code = data.get("postalCode")
        profile.username = data["username"]
        self.profile_repo.update(profile)
        self.uow.commit()

    def delete(self, profile_id: UUID) -> None:
        profile = self.profile_repo.get_by_id(profile_id)
        if not profile:
            raise BusinessException(*ErrorCodes.PROFILE_NOT_EXIST)
        if self.profile_repo.has_dependencies(profile_id):
            raise BusinessException(*ErrorCodes.CASCADE_DELETE_ERROR)
        profile.active_status = "Deleted"
        self.profile_repo.update(profile)
        self.uow.commit()

    def active(self, profile_id: UUID) -> None:
        profile = self.profile_repo.get_by_id(profile_id)
        if not profile:
            raise BusinessException(*ErrorCodes.PROFILE_NOT_EXIST)
        if profile.active_status == "Active":
            raise BusinessException(*ErrorCodes.ALREADY_ACTIVE)
        profile.active_status = "Active"
        self.profile_repo.update(profile)
        self.uow.commit()

    def inactive(self, profile_id: UUID) -> None:
        profile = self.profile_repo.get_by_id(profile_id)
        if not profile:
            raise BusinessException(*ErrorCodes.PROFILE_NOT_EXIST)
        if profile.active_status == "Inactive":
            raise BusinessException(*ErrorCodes.ALREADY_INACTIVE)
        profile.active_status = "Inactive"
        self.profile_repo.update(profile)
        self.uow.commit()

    def get_specific(self, profile_id: UUID) -> dict:
        profile = self.profile_repo.get_by_id(profile_id)
        if not profile:
            raise BusinessException(*ErrorCodes.PROFILE_NOT_EXIST)
        return {"id": profile.id, "firstName": profile.first_name, "lastName": profile.last_name}

    def get_all(self, first_name: str, last_name: str, username: str, offset: int, limit: int) -> dict:
        items, total = self.profile_repo.search(first_name, last_name, username, offset, limit)
        return {"offset": offset, "limit": limit, "totalRecord": total, "dataList": [{"id": i.id, "firstName": i.first_name, "lastName": i.last_name, "username": i.username} for i in items]}

    def get_combo(self) -> list:
        profiles = self.profile_repo.get_all_active()
        return [{"id": p.id, "title": f"{p.first_name} {p.last_name}"} for p in profiles]

class ProfilePermissionService:
    def __init__(self, repo: ProfilePermissionRepository, profile_repo: ProfileRepository, uow: UnitOfWork):
        self.repo = repo
        self.profile_repo = profile_repo
        self.uow = uow

    def add(self, form_permission_id: UUID, profile_id: UUID) -> UUID:
        profile = self.profile_repo.get_by_id(profile_id)
        if not profile:
            raise BusinessException(*ErrorCodes.PROFILE_NOT_EXIST)
        if self.repo.exists(form_permission_id, profile_id):
            raise BusinessException(*ErrorCodes.PROFILE_PERMISSION_EXISTS)
        pp = ProfilePermission(form_permission_id=form_permission_id, profile_id=profile_id)
        self.repo.add(pp)
        self.uow.commit()
        return pp.id

    def update(self, id: UUID, form_permission_id: UUID, profile_id: UUID) -> None:
        pp = self.repo.get_by_id(id)
        if not pp:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if self.repo.exists(form_permission_id, profile_id, exclude_id=id):
            raise BusinessException(*ErrorCodes.PROFILE_PERMISSION_EXISTS)
        pp.form_permission_id = form_permission_id
        pp.profile_id = profile_id
        self.repo.update(pp)
        self.uow.commit()

    def delete(self, id: UUID) -> None:
        pp = self.repo.get_by_id(id)
        if not pp:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        pp.active_status = "Deleted"
        self.repo.update(pp)
        self.uow.commit()

    def active(self, id: UUID) -> None:
        pp = self.repo.get_by_id(id)
        if not pp:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if pp.active_status == "Active":
            raise BusinessException(*ErrorCodes.ALREADY_ACTIVE)
        pp.active_status = "Active"
        self.repo.update(pp)
        self.uow.commit()

    def inactive(self, id: UUID) -> None:
        pp = self.repo.get_by_id(id)
        if not pp:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if pp.active_status == "Inactive":
            raise BusinessException(*ErrorCodes.ALREADY_INACTIVE)
        pp.active_status = "Inactive"
        self.repo.update(pp)
        self.uow.commit()

    def get_specific(self, id: UUID) -> dict:
        pp = self.repo.get_by_id(id)
        if not pp:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        return {"id": pp.id, "formPermissionId": pp.form_permission_id, "profileId": pp.profile_id}

    def get_all(self, profile_id: UUID, offset: int, limit: int) -> dict:
        items, total = self.repo.search(profile_id, offset, limit)
        return {"offset": offset, "limit": limit, "totalRecord": total, "dataList": [{"id": i.id, "formPermissionId": i.form_permission_id, "profileId": i.profile_id} for i in items]}

    def get_combo(self) -> list:
        items = self.repo.get_all_active()
        return [{"id": i.id, "title": f"{i.form_id}-{i.permission_id}"} for i in items]

class ProfileGroupService:
    def __init__(self, repo: ProfileGroupRepository, profile_repo: ProfileRepository, group_repo: GroupRepository, uow: UnitOfWork):
        self.repo = repo
        self.profile_repo = profile_repo
        self.group_repo = group_repo
        self.uow = uow

    def add(self, profile_id: UUID, group_id: UUID) -> UUID:
        profile = self.profile_repo.get_by_id(profile_id)
        if not profile:
            raise BusinessException(*ErrorCodes.PROFILE_NOT_EXIST)
        group = self.group_repo.get_by_id(group_id)
        if not group:
            raise BusinessException(*ErrorCodes.GROUP_NOT_EXIST)
        if self.repo.exists(profile_id, group_id):
            raise BusinessException(*ErrorCodes.PROFILE_GROUP_EXISTS)
        pg = ProfileGroup(profile_id=profile_id, group_id=group_id)
        self.repo.add(pg)
        self.uow.commit()
        return pg.id

    def update(self, id: UUID, profile_id: UUID, group_id: UUID) -> None:
        pg = self.repo.get_by_id(id)
        if not pg:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if self.repo.exists(profile_id, group_id, exclude_id=id):
            raise BusinessException(*ErrorCodes.PROFILE_GROUP_EXISTS)
        pg.profile_id = profile_id
        pg.group_id = group_id
        self.repo.update(pg)
        self.uow.commit()

    def delete(self, id: UUID) -> None:
        pg = self.repo.get_by_id(id)
        if not pg:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        pg.active_status = "Deleted"
        self.repo.update(pg)
        self.uow.commit()

    def active(self, id: UUID) -> None:
        pg = self.repo.get_by_id(id)
        if not pg:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if pg.active_status == "Active":
            raise BusinessException(*ErrorCodes.ALREADY_ACTIVE)
        pg.active_status = "Active"
        self.repo.update(pg)
        self.uow.commit()

    def inactive(self, id: UUID) -> None:
        pg = self.repo.get_by_id(id)
        if not pg:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        if pg.active_status == "Inactive":
            raise BusinessException(*ErrorCodes.ALREADY_INACTIVE)
        pg.active_status = "Inactive"
        self.repo.update(pg)
        self.uow.commit()

    def get_specific(self, id: UUID) -> dict:
        pg = self.repo.get_by_id(id)
        if not pg:
            raise BusinessException(*ErrorCodes.RECORD_NOT_FOUND)
        return {"id": pg.id, "profileId": pg.profile_id, "groupId": pg.group_id}

    def get_all(self, profile_id: UUID, group_id: UUID, offset: int, limit: int) -> dict:
        items, total = self.repo.search(profile_id, group_id, offset, limit)
        return {"offset": offset, "limit": limit, "totalRecord": total, "dataList": [{"id": i.id, "profileId": i.profile_id, "groupId": i.group_id} for i in items]}

    def get_combo(self) -> list:
        items = self.repo.get_all_active()
        return [{"id": i.id, "title": f"{i.profile_id}-{i.group_id}"} for i in items]