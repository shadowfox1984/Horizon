from src.domain.project_management.entities import (
    Role, Project, ProjectRoleMember, ProjectGroupMember,
    ProjectDepartmentMember, ProjectWorkflow, ProjectWorkflowStatus,
    ProjectWorkflowResolution, ProjectWorkflowProgress, Issue,
    IssueWorkflowHistory, IssueComment, IssueAttachment,
    ProjectRelease, ProjectReleaseIssue, WorkLog,
    WorkflowAllowedFileExtension, WorkflowAllowedDocumentType,
    ProjectMeeting, MeetingInvitee, MeetingMinute,
)
from src.domain.shared.enums import (
    IssueSize, LinkedIssueType, IssueChangeType, ActiveStatus
)
from src.infrastructure.persistence.models.project_management import (
    RoleModel, ProjectModel, ProjectRoleMemberModel,
    ProjectGroupMemberModel, ProjectDepartmentMemberModel,
    ProjectWorkflowModel, ProjectWorkflowStatusModel,
    ProjectWorkflowResolutionModel, ProjectWorkflowProgressModel,
    IssueModel, IssueWorkflowHistoryModel, IssueCommentModel,
    IssueAttachmentModel, ProjectReleaseModel, ProjectReleaseIssueModel,
    WorkLogModel, WorkflowAllowedFileExtensionModel,
    WorkflowAllowedDocumentTypeModel, ProjectMeetingModel,
    MeetingInviteesModel, MeetingMinutesModel,
)
from ._helpers import audit_from_model, active_from_model


def _audit_kwargs(e):
    if e.audit:
        return dict(
            CreatorId=e.audit.creator_id, CreateDate=e.audit.create_date,
            ModifierId=e.audit.modifier_id, ModifyDate=e.audit.modify_date,
        )
    return {}


def _enum_or_none(enum_cls, raw):
    if raw is None:
        return None
    return enum_cls(raw.value if hasattr(raw, "value") else raw)


class RoleMapper:
    @staticmethod
    def to_domain(m: RoleModel) -> Role:
        return Role(id=m.Id, code=m.Code, title=m.Title, description=m.Description,
                    active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: Role) -> RoleModel:
        return RoleModel(Id=e.id, Code=e.code, Title=e.title,
                         Description=e.description, ActiveStatus=e.active_status,
                         **_audit_kwargs(e))


class ProjectMapper:
    @staticmethod
    def to_domain(m: ProjectModel) -> Project:
        return Project(id=m.Id, title=m.Title, code=m.Code,
                       start_date=m.StartDate, end_date=m.EndDate,
                       description=m.Description,
                       active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: Project) -> ProjectModel:
        return ProjectModel(Id=e.id, Title=e.title, Code=e.code,
                            StartDate=e.start_date, EndDate=e.end_date,
                            Description=e.description,
                            ActiveStatus=e.active_status, **_audit_kwargs(e))


class ProjectRoleMemberMapper:
    @staticmethod
    def to_domain(m: ProjectRoleMemberModel) -> ProjectRoleMember:
        return ProjectRoleMember(
            id=m.Id, profile_id=m.ProfileId, project_id=m.ProjectId,
            role_id=m.RoleId, is_project_admin=m.IsProjectAdmin,
            is_active=m.IsActive, is_deleted=m.IsDeleted,
            create_date=m.CreateDate, creator_id=m.CreatorId,
            modify_date=m.ModifyDate, modifier_id=m.ModifierId,
        )
    @staticmethod
    def to_model(e: ProjectRoleMember) -> ProjectRoleMemberModel:
        return ProjectRoleMemberModel(
            Id=e.id, ProfileId=e.profile_id, ProjectId=e.project_id,
            RoleId=e.role_id, IsProjectAdmin=e.is_project_admin,
            IsActive=e.is_active, IsDeleted=e.is_deleted,
            CreateDate=e.create_date, CreatorId=e.creator_id,
            ModifyDate=e.modify_date, ModifierId=e.modifier_id,
        )


class ProjectGroupMemberMapper:
    @staticmethod
    def to_domain(m: ProjectGroupMemberModel) -> ProjectGroupMember:
        return ProjectGroupMember(
            id=m.Id, project_id=m.ProjectId, group_id=m.GroupId,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: ProjectGroupMember) -> ProjectGroupMemberModel:
        return ProjectGroupMemberModel(
            Id=e.id, ProjectId=e.project_id, GroupId=e.group_id,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class ProjectDepartmentMemberMapper:
    @staticmethod
    def to_domain(m: ProjectDepartmentMemberModel) -> ProjectDepartmentMember:
        return ProjectDepartmentMember(
            id=m.Id, project_id=m.ProjectId, department_id=m.DepartmentId,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: ProjectDepartmentMember) -> ProjectDepartmentMemberModel:
        return ProjectDepartmentMemberModel(
            Id=e.id, ProjectId=e.project_id, DepartmentId=e.department_id,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class ProjectWorkflowMapper:
    @staticmethod
    def to_domain(m: ProjectWorkflowModel) -> ProjectWorkflow:
        return ProjectWorkflow(
            id=m.Id, project_id=m.ProjectId, title=m.Title, code=m.Code,
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: ProjectWorkflow) -> ProjectWorkflowModel:
        return ProjectWorkflowModel(
            Id=e.id, ProjectId=e.project_id, Title=e.title, Code=e.code,
            Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class ProjectWorkflowStatusMapper:
    @staticmethod
    def to_domain(m: ProjectWorkflowStatusModel) -> ProjectWorkflowStatus:
        return ProjectWorkflowStatus(
            id=m.Id, project_workflow_id=m.ProjectWorkflowId, status_id=m.StatusId,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: ProjectWorkflowStatus) -> ProjectWorkflowStatusModel:
        return ProjectWorkflowStatusModel(
            Id=e.id, ProjectWorkflowId=e.project_workflow_id,
            StatusId=e.status_id, ActiveStatus=e.active_status,
            **_audit_kwargs(e))


class ProjectWorkflowResolutionMapper:
    @staticmethod
    def to_domain(m: ProjectWorkflowResolutionModel) -> ProjectWorkflowResolution:
        return ProjectWorkflowResolution(
            id=m.Id, project_workflow_id=m.ProjectWorkflowId,
            resolution_id=m.ResolutionId,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: ProjectWorkflowResolution) -> ProjectWorkflowResolutionModel:
        return ProjectWorkflowResolutionModel(
            Id=e.id, ProjectWorkflowId=e.project_workflow_id,
            ResolutionId=e.resolution_id, ActiveStatus=e.active_status,
            **_audit_kwargs(e))


class ProjectWorkflowProgressMapper:
    @staticmethod
    def to_domain(m: ProjectWorkflowProgressModel) -> ProjectWorkflowProgress:
        return ProjectWorkflowProgress(
            id=m.Id, title=m.Title,
            start_project_workflow_status_id=m.StartProjectWorkflowStatusId,
            is_from_start_point=m.IsFromStartPoint,
            can_be_started_from_any_status=m.CanBeStartedFromAnyStatus,
            end_project_workflow_status_id=m.EndProjectWorkflowStatusId,
            is_workflow_end_point=m.IsWorkflowEndPoint,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: ProjectWorkflowProgress) -> ProjectWorkflowProgressModel:
        return ProjectWorkflowProgressModel(
            Id=e.id, Title=e.title,
            StartProjectWorkflowStatusId=e.start_project_workflow_status_id,
            IsFromStartPoint=e.is_from_start_point,
            CanBeStartedFromAnyStatus=e.can_be_started_from_any_status,
            EndProjectWorkflowStatusId=e.end_project_workflow_status_id,
            IsWorkflowEndPoint=e.is_workflow_end_point,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class IssueMapper:
    @staticmethod
    def to_domain(m: IssueModel) -> Issue:
        return Issue(
            id=m.Id, project_id=m.ProjectId, code=m.Code, title=m.Title,
            issue_type_id=m.IssueTypeId, current_status_id=m.CurrentStatusId,
            current_resolution_id=m.CurrentResolutionId,
            assignee_id=m.AssigneeId, description=m.Description,
            issue_size=_enum_or_none(IssueSize, m.IssueSize),
            priority_id=m.PriorityId, due_date=m.DueDate,
            parent_issue_id=m.ParentIssueId, epic_linked_id=m.EpicLinkedId,
            linked_issue_id=m.LinkedIssueId,
            linked_issue_type=_enum_or_none(LinkedIssueType, m.LinkedIssueType),
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: Issue) -> IssueModel:
        return IssueModel(
            Id=e.id, ProjectId=e.project_id, Code=e.code, Title=e.title,
            IssueTypeId=e.issue_type_id, CurrentStatusId=e.current_status_id,
            CurrentResolutionId=e.current_resolution_id,
            AssigneeId=e.assignee_id, Description=e.description,
            IssueSize=e.issue_size, PriorityId=e.priority_id,
            DueDate=e.due_date, ParentIssueId=e.parent_issue_id,
            EpicLinkedId=e.epic_linked_id, LinkedIssueId=e.linked_issue_id,
            LinkedIssueType=e.linked_issue_type,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class IssueWorkflowHistoryMapper:
    @staticmethod
    def to_domain(m: IssueWorkflowHistoryModel) -> IssueWorkflowHistory:
        return IssueWorkflowHistory(
            id=m.Id, issue_id=m.IssueId,
            issue_change_type=IssueChangeType(
                m.IssueChangeType.value if hasattr(m.IssueChangeType, "value") else m.IssueChangeType
            ),
            project_workflow_progress_id=m.ProjectWorkflowProgressId,
            status_from_id=m.StatusFromId, status_to_id=m.StatusToId,
            resolution_from_id=m.ResolutionFromId, resolution_to_id=m.ResolutionToId,
            assignee_from_id=m.AssigneeFromId, assignee_to_id=m.AssigneeToId,
            project_from_id=m.ProjectFromId, project_to_id=m.ProjectToId,
            issue_active_status_from=_enum_or_none(ActiveStatus, m.IssueActiveStatusFrom),
            issue_active_status_to=_enum_or_none(ActiveStatus, m.IssueActiveStatusTo),
            change_data_json=m.ChangeDataJson,
            active_status=active_from_model(m),
            create_date=m.CreateDate, creator_id=m.CreatorId,
        )
    @staticmethod
    def to_model(e: IssueWorkflowHistory) -> IssueWorkflowHistoryModel:
        return IssueWorkflowHistoryModel(
            Id=e.id, IssueId=e.issue_id, IssueChangeType=e.issue_change_type,
            ProjectWorkflowProgressId=e.project_workflow_progress_id,
            StatusFromId=e.status_from_id, StatusToId=e.status_to_id,
            ResolutionFromId=e.resolution_from_id, ResolutionToId=e.resolution_to_id,
            AssigneeFromId=e.assignee_from_id, AssigneeToId=e.assignee_to_id,
            ProjectFromId=e.project_from_id, ProjectToId=e.project_to_id,
            IssueActiveStatusFrom=e.issue_active_status_from,
            IssueActiveStatusTo=e.issue_active_status_to,
            ChangeDataJson=e.change_data_json,
            ActiveStatus=e.active_status,
            CreateDate=e.create_date, CreatorId=e.creator_id,
        )


class IssueCommentMapper:
    @staticmethod
    def to_domain(m: IssueCommentModel) -> IssueComment:
        return IssueComment(
            id=m.Id, issue_id=m.IssueId, comment_text=m.CommentText,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: IssueComment) -> IssueCommentModel:
        return IssueCommentModel(
            Id=e.id, IssueId=e.issue_id, CommentText=e.comment_text,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class IssueAttachmentMapper:
    @staticmethod
    def to_domain(m: IssueAttachmentModel) -> IssueAttachment:
        return IssueAttachment(
            id=m.Id, issue_id=m.IssueId, document_id=m.DocumentId,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: IssueAttachment) -> IssueAttachmentModel:
        return IssueAttachmentModel(
            Id=e.id, IssueId=e.issue_id, DocumentId=e.document_id,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class ProjectReleaseMapper:
    @staticmethod
    def to_domain(m: ProjectReleaseModel) -> ProjectRelease:
        return ProjectRelease(
            id=m.Id, project_id=m.ProjectId, version_number=m.VersionNumber,
            release_date=m.ReleaseDate, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: ProjectRelease) -> ProjectReleaseModel:
        return ProjectReleaseModel(
            Id=e.id, ProjectId=e.project_id, VersionNumber=e.version_number,
            ReleaseDate=e.release_date, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class ProjectReleaseIssueMapper:
    @staticmethod
    def to_domain(m: ProjectReleaseIssueModel) -> ProjectReleaseIssue:
        return ProjectReleaseIssue(
            id=m.Id, issue_id=m.IssueId, project_release_id=m.ProjectReleaseId,
            is_finalized=m.IsFinalized,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: ProjectReleaseIssue) -> ProjectReleaseIssueModel:
        return ProjectReleaseIssueModel(
            Id=e.id, IssueId=e.issue_id, ProjectReleaseId=e.project_release_id,
            IsFinalized=e.is_finalized, ActiveStatus=e.active_status,
            **_audit_kwargs(e))


class WorkLogMapper:
    @staticmethod
    def to_domain(m: WorkLogModel) -> WorkLog:
        return WorkLog(
            id=m.Id, issue_id=m.IssueId, log_date=m.LogDate,
            start_work_time=m.StartWorkTime, working_duration=m.WorkingDuration,
            time_unit_id=m.TimeUnitId, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: WorkLog) -> WorkLogModel:
        return WorkLogModel(
            Id=e.id, IssueId=e.issue_id, LogDate=e.log_date,
            StartWorkTime=e.start_work_time, WorkingDuration=e.working_duration,
            TimeUnitId=e.time_unit_id, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class WorkflowAllowedFileExtensionMapper:
    @staticmethod
    def to_domain(m: WorkflowAllowedFileExtensionModel) -> WorkflowAllowedFileExtension:
        return WorkflowAllowedFileExtension(
            id=m.Id, file_extension_id=m.FileExtensionId,
            project_workflow_id=m.ProjectWorkflowId,
            max_file_size_for_upload=m.MaxFileSizeForUpload,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: WorkflowAllowedFileExtension) -> WorkflowAllowedFileExtensionModel:
        return WorkflowAllowedFileExtensionModel(
            Id=e.id, FileExtensionId=e.file_extension_id,
            ProjectWorkflowId=e.project_workflow_id,
            MaxFileSizeForUpload=e.max_file_size_for_upload,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class WorkflowAllowedDocumentTypeMapper:
    @staticmethod
    def to_domain(m: WorkflowAllowedDocumentTypeModel) -> WorkflowAllowedDocumentType:
        return WorkflowAllowedDocumentType(
            id=m.Id, document_type_id=m.DocumentTypeId,
            project_workflow_id=m.ProjectWorkflowId,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: WorkflowAllowedDocumentType) -> WorkflowAllowedDocumentTypeModel:
        return WorkflowAllowedDocumentTypeModel(
            Id=e.id, DocumentTypeId=e.document_type_id,
            ProjectWorkflowId=e.project_workflow_id,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class ProjectMeetingMapper:
    @staticmethod
    def to_domain(m: ProjectMeetingModel) -> ProjectMeeting:
        return ProjectMeeting(
            id=m.Id, project_id=m.ProjectId, meeting_type_id=m.MeetingTypeId,
            meeting_date=m.MeetingDate, title=m.Title, location=m.Location,
            minutes_document_id=m.MinutesDocumentId, description=m.Description,
            schedule_start_time=m.ScheduleStartTime,
            schedule_end_time=m.ScheduleEndTime,
            actual_start_time=m.ActualStartTime, actual_end_time=m.ActualEndTime,
            is_cancelled=m.IsCanncelled,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: ProjectMeeting) -> ProjectMeetingModel:
        return ProjectMeetingModel(
            Id=e.id, ProjectId=e.project_id, MeetingTypeId=e.meeting_type_id,
            MeetingDate=e.meeting_date, Title=e.title, Location=e.location,
            MinutesDocumentId=e.minutes_document_id, Description=e.description,
            ScheduleStartTime=e.schedule_start_time,
            ScheduleEndTime=e.schedule_end_time,
            ActualStartTime=e.actual_start_time, ActualEndTime=e.actual_end_time,
            IsCanncelled=e.is_cancelled, ActiveStatus=e.active_status,
            **_audit_kwargs(e))


class MeetingInviteeMapper:
    @staticmethod
    def to_domain(m: MeetingInviteesModel) -> MeetingInvitee:
        return MeetingInvitee(
            id=m.Id, project_meeting_id=m.ProjectMeetingId,
            is_from_inside_company=m.IsFromInsideCompnay,
            profile_id=m.ProfileId, invitee_full_name=m.InviteeFullName,
            invitee_company_name=m.InviteeCompanyName,
            is_attended=m.IsAttanded,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: MeetingInvitee) -> MeetingInviteesModel:
        return MeetingInviteesModel(
            Id=e.id, ProjectMeetingId=e.project_meeting_id,
            IsFromInsideCompnay=e.is_from_inside_company,
            ProfileId=e.profile_id, InviteeFullName=e.invitee_full_name,
            InviteeCompanyName=e.invitee_company_name,
            IsAttanded=e.is_attended, ActiveStatus=e.active_status,
            **_audit_kwargs(e))


class MeetingMinuteMapper:
    @staticmethod
    def to_domain(m: MeetingMinutesModel) -> MeetingMinute:
        return MeetingMinute(
            id=m.Id, project_meeting_id=m.ProjectMeetingId,
            responsible_department_id=m.ResponsibleDepartmentId,
            resolution=m.Resolution, issue_id=m.IssueId, due_date=m.DueDate,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: MeetingMinute) -> MeetingMinutesModel:
        return MeetingMinutesModel(
            Id=e.id, ProjectMeetingId=e.project_meeting_id,
            ResponsibleDepartmentId=e.responsible_department_id,
            Resolution=e.resolution, IssueId=e.issue_id,
            DueDate=e.due_date, ActiveStatus=e.active_status,
            **_audit_kwargs(e))