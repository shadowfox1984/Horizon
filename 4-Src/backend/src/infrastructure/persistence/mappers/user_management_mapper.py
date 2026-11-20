from src.domain.user_management.entities import (
    Profile, Group, Permission, Form, FormPermission,
    GroupPermission, ProfilePermission, ProfileGroup,
    ProfileClientSecret, UserToken,
)
from src.domain.shared.enums import Gender
from src.infrastructure.persistence.models.user_management import (
    ProfileModel, GroupsModel, PermissionModel, FormModel,
    FormPermissionModel, GroupPermissionModel, ProfilePermissionModel,
    ProfileGroupModel, ProfileClientSecretModel, UserTokenModel,
)
from ._helpers import audit_from_model, active_from_model


def _audit_kwargs(e):
    if e.audit:
        return dict(
            CreatorId=e.audit.creator_id,
            CreateDate=e.audit.create_date,
            ModifierId=e.audit.modifier_id,
            ModifyDate=e.audit.modify_date,
        )
    return {}


class ProfileMapper:
    @staticmethod
    def to_domain(m: ProfileModel) -> Profile:
        return Profile(
            id=m.Id, first_name=m.FirstName, last_name=m.LastName,
            gender=Gender(m.Gender.value if hasattr(m.Gender, "value") else m.Gender),
            staff_number=m.StaffNumber, active_from=m.ActiveFrom,
            username=m.Username, password_hash=m.Pass,
            active_to=m.ActiveTo, position_id=m.PositionId, avatar=m.Avatar,
            birthday=m.Birthday, phone_number=m.PhoneNumber,
            mobile_number=m.MobileNumber, email_address=m.EmailAddress,
            address=m.Address, postal_code=m.PostalCode, pass_salt=m.PassSalt,
            last_login_date=m.LastLogInDate, login_count=m.LogInCount,
            wrong_login_count=m.WrongLogInCount,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )

    @staticmethod
    def to_model(e: Profile) -> ProfileModel:
        return ProfileModel(
            Id=e.id, FirstName=e.first_name, LastName=e.last_name,
            Gender=e.gender, StaffNumber=e.staff_number, ActiveFrom=e.active_from,
            ActiveTo=e.active_to, PositionId=e.position_id, Avatar=e.avatar,
            Birthday=e.birthday, PhoneNumber=e.phone_number,
            MobileNumber=e.mobile_number, EmailAddress=e.email_address,
            Address=e.address, PostalCode=e.postal_code, Username=e.username,
            Pass=e.password_hash, PassSalt=e.pass_salt,
            LastLogInDate=e.last_login_date, LogInCount=e.login_count,
            WrongLogInCount=e.wrong_login_count, ActiveStatus=e.active_status,
            **_audit_kwargs(e),
        )

    @staticmethod
    def update_model(m: ProfileModel, e: Profile) -> None:
        m.FirstName = e.first_name
        m.LastName = e.last_name
        m.Gender = e.gender
        m.StaffNumber = e.staff_number
        m.ActiveFrom = e.active_from
        m.ActiveTo = e.active_to
        m.PositionId = e.position_id
        m.Avatar = e.avatar
        m.Birthday = e.birthday
        m.PhoneNumber = e.phone_number
        m.MobileNumber = e.mobile_number
        m.EmailAddress = e.email_address
        m.Address = e.address
        m.PostalCode = e.postal_code
        m.Username = e.username
        m.Pass = e.password_hash
        m.PassSalt = e.pass_salt
        m.LastLogInDate = e.last_login_date
        m.LogInCount = e.login_count
        m.WrongLogInCount = e.wrong_login_count
        m.ActiveStatus = e.active_status
        if e.audit:
            m.ModifierId = e.audit.modifier_id
            m.ModifyDate = e.audit.modify_date


class GroupMapper:
    @staticmethod
    def to_domain(m: GroupsModel) -> Group:
        return Group(
            id=m.Id, code=m.Code, title=m.Title, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: Group) -> GroupsModel:
        return GroupsModel(
            Id=e.id, Code=e.code, Title=e.title, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e),
        )


class PermissionMapper:
    @staticmethod
    def to_domain(m: PermissionModel) -> Permission:
        return Permission(
            id=m.Id, code=m.Code, title=m.Title, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: Permission) -> PermissionModel:
        return PermissionModel(
            Id=e.id, Code=e.code, Title=e.title, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e),
        )


class FormMapper:
    @staticmethod
    def to_domain(m: FormModel) -> Form:
        return Form(
            id=m.Id, code=m.Code, title=m.Title, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: Form) -> FormModel:
        return FormModel(
            Id=e.id, Code=e.code, Title=e.title, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e),
        )


class FormPermissionMapper:
    @staticmethod
    def to_domain(m: FormPermissionModel) -> FormPermission:
        return FormPermission(
            id=m.Id, form_id=m.FormId, permission_id=m.PermissionId,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: FormPermission) -> FormPermissionModel:
        return FormPermissionModel(
            Id=e.id, FormId=e.form_id, PermissionId=e.permission_id,
            ActiveStatus=e.active_status, **_audit_kwargs(e),
        )


class GroupPermissionMapper:
    @staticmethod
    def to_domain(m: GroupPermissionModel) -> GroupPermission:
        return GroupPermission(
            id=m.Id, form_permission_id=m.FormPermissionId, group_id=m.GroupId,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: GroupPermission) -> GroupPermissionModel:
        return GroupPermissionModel(
            Id=e.id, FormPermissionId=e.form_permission_id, GroupId=e.group_id,
            ActiveStatus=e.active_status, **_audit_kwargs(e),
        )


class ProfilePermissionMapper:
    @staticmethod
    def to_domain(m: ProfilePermissionModel) -> ProfilePermission:
        return ProfilePermission(
            id=m.Id, form_permission_id=m.FormPermissionId, profile_id=m.ProfileId,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: ProfilePermission) -> ProfilePermissionModel:
        return ProfilePermissionModel(
            Id=e.id, FormPermissionId=e.form_permission_id, ProfileId=e.profile_id,
            ActiveStatus=e.active_status, **_audit_kwargs(e),
        )


class ProfileGroupMapper:
    @staticmethod
    def to_domain(m: ProfileGroupModel) -> ProfileGroup:
        return ProfileGroup(
            id=m.Id, profile_id=m.ProfileId, group_id=m.GroupId,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: ProfileGroup) -> ProfileGroupModel:
        return ProfileGroupModel(
            Id=e.id, ProfileId=e.profile_id, GroupId=e.group_id,
            ActiveStatus=e.active_status, **_audit_kwargs(e),
        )


class ProfileClientSecretMapper:
    @staticmethod
    def to_domain(m: ProfileClientSecretModel) -> ProfileClientSecret:
        return ProfileClientSecret(
            id=m.Id, profile_id=m.ProfileId,
            client_secret=m.ClientSecret, client_ip=m.ClientIp,
        )
    @staticmethod
    def to_model(e: ProfileClientSecret) -> ProfileClientSecretModel:
        return ProfileClientSecretModel(
            Id=e.id, ProfileId=e.profile_id,
            ClientSecret=e.client_secret, ClientIp=e.client_ip,
        )


class UserTokenMapper:
    @staticmethod
    def to_domain(m: UserTokenModel) -> UserToken:
        return UserToken(
            id=m.Id, profile_client_secret_id=m.ProfileClientSecretId,
            token=m.Token, expire_date=m.ExpireDate,
            last_refresh_time=m.LastRefreshTime, refresh_count=m.RefreshCount,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: UserToken) -> UserTokenModel:
        return UserTokenModel(
            Id=e.id, ProfileClientSecretId=e.profile_client_secret_id,
            Token=e.token, ExpireDate=e.expire_date,
            LastRefreshTime=e.last_refresh_time, RefreshCount=e.refresh_count,
            ActiveStatus=e.active_status, **_audit_kwargs(e),
        )