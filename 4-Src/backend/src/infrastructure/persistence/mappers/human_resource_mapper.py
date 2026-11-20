from src.domain.human_resource.entities import (
    Department, Position, ProfileEducation, ProfileJobExperience,
    ProfileCertificate, WorkingTimeTable, Holiday, Attendance,
    Leave, WorkMission,
)
from src.domain.shared.enums import Weekday, HolidayType, EnteranceType, LeaveType
from src.infrastructure.persistence.models.human_resource import (
    DepartmentModel, PositionModel, ProfileEducationModel,
    ProfileJobExperienceModel, ProfileCertificateModel,
    WorkingTimeTableModel, HolidayModel, AttendanceModel,
    LeaveModel, WorkMissionModel,
)
from ._helpers import audit_from_model, active_from_model


def _audit_kwargs(e):
    if e.audit:
        return dict(
            CreatorId=e.audit.creator_id, CreateDate=e.audit.create_date,
            ModifierId=e.audit.modifier_id, ModifyDate=e.audit.modify_date,
        )
    return {}


class DepartmentMapper:
    @staticmethod
    def to_domain(m: DepartmentModel) -> Department:
        return Department(
            id=m.Id, code=m.Code, title=m.Title, description=m.Description,
            parent_id=m.ParentId,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: Department) -> DepartmentModel:
        return DepartmentModel(
            Id=e.id, Code=e.code, Title=e.title, Description=e.description,
            ParentId=e.parent_id, ActiveStatus=e.active_status, **_audit_kwargs(e),
        )


class PositionMapper:
    @staticmethod
    def to_domain(m: PositionModel) -> Position:
        return Position(
            id=m.Id, code=m.Code, title=m.Title, description=m.Description,
            parent_id=m.ParentId, department_id=m.DepartmentId,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: Position) -> PositionModel:
        return PositionModel(
            Id=e.id, Code=e.code, Title=e.title, Description=e.description,
            ParentId=e.parent_id, DepartmentId=e.department_id,
            ActiveStatus=e.active_status, **_audit_kwargs(e),
        )


class ProfileEducationMapper:
    @staticmethod
    def to_domain(m: ProfileEducationModel) -> ProfileEducation:
        return ProfileEducation(
            id=m.Id, profile_id=m.ProfileId, education_level_id=m.EducationLevelId,
            document_id=m.DocumentId, title=m.Title, collage_name=m.CollageName,
            start_date=m.StartDate, end_date=m.EndDate, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: ProfileEducation) -> ProfileEducationModel:
        return ProfileEducationModel(
            Id=e.id, ProfileId=e.profile_id, EducationLevelId=e.education_level_id,
            DocumentId=e.document_id, Title=e.title, CollageName=e.collage_name,
            StartDate=e.start_date, EndDate=e.end_date, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e),
        )


class ProfileJobExperienceMapper:
    @staticmethod
    def to_domain(m: ProfileJobExperienceModel) -> ProfileJobExperience:
        return ProfileJobExperience(
            id=m.Id, profile_id=m.ProfileId, job_title=m.JobTitle,
            company_name=m.CompanyName, start_date=m.StartDate,
            end_date=m.EndDate, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: ProfileJobExperience) -> ProfileJobExperienceModel:
        return ProfileJobExperienceModel(
            Id=e.id, ProfileId=e.profile_id, JobTitle=e.job_title,
            CompanyName=e.company_name, StartDate=e.start_date,
            EndDate=e.end_date, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e),
        )


class ProfileCertificateMapper:
    @staticmethod
    def to_domain(m: ProfileCertificateModel) -> ProfileCertificate:
        return ProfileCertificate(
            id=m.Id, profile_id=m.ProfileId, title=m.Title,
            institute_name=m.InstituteName, has_certificate=m.HasCertificate,
            document_id=m.DocumentId, start_date=m.StartDate, end_date=m.EndDate,
            description=m.Description, certificate_file_address=m.CertificateFileAddress,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: ProfileCertificate) -> ProfileCertificateModel:
        return ProfileCertificateModel(
            Id=e.id, ProfileId=e.profile_id, Title=e.title,
            InstituteName=e.institute_name, HasCertificate=e.has_certificate,
            DocumentId=e.document_id, StartDate=e.start_date, EndDate=e.end_date,
            Description=e.description, CertificateFileAddress=e.certificate_file_address,
            ActiveStatus=e.active_status, **_audit_kwargs(e),
        )


class WorkingTimeTableMapper:
    @staticmethod
    def to_domain(m: WorkingTimeTableModel) -> WorkingTimeTable:
        return WorkingTimeTable(
            id=m.Id, staff_contract_type_id=m.StaffContractTypeId,
            working_day=Weekday(m.WorkingDay.value if hasattr(m.WorkingDay, "value") else m.WorkingDay),
            start_time=m.StartTime, end_time=m.EndTime,
            floating_start_time=m.FloatingStartTime, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: WorkingTimeTable) -> WorkingTimeTableModel:
        return WorkingTimeTableModel(
            Id=e.id, StaffContractTypeId=e.staff_contract_type_id,
            WorkingDay=e.working_day, StartTime=e.start_time, EndTime=e.end_time,
            FloatingStartTime=e.floating_start_time, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e),
        )


class HolidayMapper:
    @staticmethod
    def to_domain(m: HolidayModel) -> Holiday:
        return Holiday(
            id=m.Id, title=m.Title,
            holiday_type=HolidayType(m.HolidayType.value if hasattr(m.HolidayType, "value") else m.HolidayType),
            holiday_date=m.HolidayDate, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: Holiday) -> HolidayModel:
        return HolidayModel(
            Id=e.id, Title=e.title, HolidayType=e.holiday_type,
            HolidayDate=e.holiday_date, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e),
        )


class AttendanceMapper:
    @staticmethod
    def to_domain(m: AttendanceModel) -> Attendance:
        return Attendance(
            id=m.Id, profile_id=m.ProfileId, working_date=m.WorkingDate,
            enterance_type=EnteranceType(m.EnteranceType.value if hasattr(m.EnteranceType, "value") else m.EnteranceType),
            entrance_time=m.EnternaceTime,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: Attendance) -> AttendanceModel:
        return AttendanceModel(
            Id=e.id, ProfileId=e.profile_id, WorkingDate=e.working_date,
            EnteranceType=e.enterance_type, EnternaceTime=e.entrance_time,
            ActiveStatus=e.active_status, **_audit_kwargs(e),
        )


class LeaveMapper:
    @staticmethod
    def to_domain(m: LeaveModel) -> Leave:
        return Leave(
            id=m.Id, profile_id=m.ProfileId,
            leave_type=LeaveType(m.LeaveType.value if hasattr(m.LeaveType, "value") else m.LeaveType),
            leaving_start_date=m.LeavingStartDate, leaving_end_date=m.LeavingEndDate,
            leaving_start_time=m.LeavingStartTime, leaving_end_time=m.LeavingEndTime,
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: Leave) -> LeaveModel:
        return LeaveModel(
            Id=e.id, ProfileId=e.profile_id, LeaveType=e.leave_type,
            LeavingStartDate=e.leaving_start_date, LeavingEndDate=e.leaving_end_date,
            LeavingStartTime=e.leaving_start_time, LeavingEndTime=e.leaving_end_time,
            Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e),
        )


class WorkMissionMapper:
    @staticmethod
    def to_domain(m: WorkMissionModel) -> WorkMission:
        return WorkMission(
            id=m.Id, profile_id=m.ProfileId, mission_start_date=m.MissionStartDate,
            mission_end_date=m.MissionEndDate, mission_start_time=m.MissionStartTime,
            mission_end_time=m.MissionEndTime, mission_location=m.MissionLocation,
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m),
        )
    @staticmethod
    def to_model(e: WorkMission) -> WorkMissionModel:
        return WorkMissionModel(
            Id=e.id, ProfileId=e.profile_id,
            MissionStartDate=e.mission_start_date, MissionEndDate=e.mission_end_date,
            MissionStartTime=e.mission_start_time, MissionEndTime=e.mission_end_time,
            MissionLocation=e.mission_location, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e),
        )