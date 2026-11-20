from sqlalchemy import Column, String, Date, Time, Boolean, ForeignKey, Float, Integer, func, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.infrastructure.persistence.base_model import (
    Base, UUIDPrimaryKeyMixin, AuditColumnsMixin
)
from src.infrastructure.persistence.enums_pg import (
    active_status, issue_size, linked_issue_type, issue_change_type
)

SCHEMA = "ProjectManagement"


class RoleModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Role"
    __table_args__ = {"schema": SCHEMA}
    Code = Column(String(20), nullable=False, unique=True)
    Title = Column(String(200), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class ProjectModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Project"
    __table_args__ = {"schema": SCHEMA}
    Title = Column(String(255), nullable=False)
    Code = Column(String(20), nullable=False, unique=True)
    StartDate = Column(Date)
    EndDate = Column(Date)
    Description = Column(String(4000))
    ActiveStatus = active_status


class ProjectRoleMemberModel(Base, UUIDPrimaryKeyMixin):
    __tablename__ = "ProjectRoleMember"
    __table_args__ = {"schema": SCHEMA}
    ProfileId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Profile.Id"), nullable=False)
    ProjectId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Project.Id"), nullable=False)
    RoleId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Role.Id"), nullable=True)
    IsProjectAdmin = Column(Boolean, nullable=False)
    IsActive = Column(Boolean, nullable=False, server_default="true")
    IsDeleted = Column(Boolean, nullable=False, server_default="false")
    CreateDate = Column(DateTime, nullable=False, server_default=func.now())
    CreatorId = Column(UUID(as_uuid=True), nullable=False)
    ModifyDate = Column(DateTime)
    ModifierId = Column(UUID(as_uuid=True))


class ProjectGroupMemberModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "ProjectGroupMember"
    __table_args__ = {"schema": SCHEMA, "sqlite_autoincrement": False}
    ProjectId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Project.Id"), nullable=False)
    GroupId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Groups.Id"), nullable=False)
    ActiveStatus = active_status


class ProjectDepartmentMemberModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "ProjectDepartmentMember"
    __table_args__ = {"schema": SCHEMA}
    ProjectId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Project.Id"), nullable=False)
    DepartmentId = Column(UUID(as_uuid=True), ForeignKey("HumanResource.Department.Id"), nullable=False)
    ActiveStatus = active_status


class ProjectWorkflowModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "ProjectWorkflow"
    __table_args__ = {"schema": SCHEMA}
    ProjectId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Project.Id"), nullable=False)
    Title = Column(String(255), nullable=False)
    Code = Column(String(20), nullable=False, unique=True)
    Description = Column(String(4000))
    ActiveStatus = active_status


class ProjectWorkflowStatusModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "ProjectWorkflowStatus"
    __table_args__ = {"schema": SCHEMA}
    ProjectWorkflowId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.ProjectWorkflow.Id"), nullable=False)
    StatusId = Column(UUID(as_uuid=True), ForeignKey("Basic.Status.Id"), nullable=False)
    ActiveStatus = active_status


class ProjectWorkflowResolutionModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "ProjectWorkflowResolution"
    __table_args__ = {"schema": SCHEMA}
    ProjectWorkflowId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.ProjectWorkflow.Id"), nullable=False)
    ResolutionId = Column(UUID(as_uuid=True), ForeignKey("Basic.Resolution.Id"), nullable=False)
    ActiveStatus = active_status


class ProjectWorkflowProgressModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "ProjectWorkflowProgress"
    __table_args__ = {"schema": SCHEMA}
    Title = Column(String(255), nullable=False)
    StartProjectWorkflowStatusId = Column(
        UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.ProjectWorkflowStatus.Id"), nullable=True
    )
    IsFromStartPoint = Column(Boolean, nullable=False)
    CanBeStartedFromAnyStatus = Column(Boolean, nullable=False)
    EndProjectWorkflowStatusId = Column(
        UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.ProjectWorkflowStatus.Id"), nullable=True
    )
    IsWorkflowEndPoint = Column(Boolean, nullable=False)
    ActiveStatus = active_status


class IssueModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Issue"
    __table_args__ = {"schema": SCHEMA}
    ProjectId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Project.Id"), nullable=False)
    AssigneeId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Profile.Id"), nullable=True)
    Code = Column(String(20), nullable=False, unique=True)
    Title = Column(String(200), nullable=False)
    Description = Column(String(4000))
    IssueSize = issue_size
    PriorityId = Column(UUID(as_uuid=True), ForeignKey("Basic.Priority.Id"), nullable=True)
    DueDate = Column(Date)
    IssueTypeId = Column(UUID(as_uuid=True), ForeignKey("Basic.IssueType.Id"), nullable=False)
    ParentIssueId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Issue.Id"), nullable=True)
    EpicLinkedId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Issue.Id"), nullable=True)
    LinkedIssueId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Issue.Id"), nullable=True)
    LinkedIssueType = linked_issue_type
    CurrentStatusId = Column(
        UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.ProjectWorkflowStatus.Id"), nullable=False
    )
    CurrentResolutionId = Column(
        UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.ProjectWorkflowResolution.Id"), nullable=False
    )
    ActiveStatus = active_status


class IssueWorkflowHistoryModel(Base, UUIDPrimaryKeyMixin):
    __tablename__ = "IssueWorkflowHistory"
    __table_args__ = {"schema": SCHEMA}
    IssueId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Issue.Id"), nullable=False)
    IssueChangeType = issue_change_type
    ProjectWorkflowProgressId = Column(
        UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.ProjectWorkflowProgress.Id"), nullable=True
    )
    StatusFromId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.ProjectWorkflowStatus.Id"), nullable=True)
    StatusToId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.ProjectWorkflowStatus.Id"), nullable=True)
    ResolutionFromId = Column(
        UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.ProjectWorkflowResolution.Id"), nullable=True
    )
    ResolutionToId = Column(
        UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.ProjectWorkflowResolution.Id"), nullable=True
    )
    AssigneeFromId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Profile.Id"), nullable=True)
    AssigneeToId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Profile.Id"), nullable=True)
    ProjectFromId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Project.Id"), nullable=True)
    ProjectToId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Project.Id"), nullable=True)
    IssueActiveStatusFrom = active_status
    IssueActiveStatusTo = active_status
    ChangeDataJson = Column(String(4000))
    ActiveStatus = active_status
    CreateDate = Column(DateTime, nullable=False, server_default=func.now())
    CreatorId = Column(UUID(as_uuid=True), nullable=False)


class IssueCommentModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "IssueComment"
    __table_args__ = {"schema": SCHEMA}
    IssueId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Issue.Id"), nullable=False)
    CommentText = Column(String(4000), nullable=False)
    ActiveStatus = active_status


class IssueAttachmentModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "IssueAttachment"
    __table_args__ = {"schema": SCHEMA}
    IssueId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Issue.Id"), nullable=False)
    DocumentId = Column(UUID(as_uuid=True), ForeignKey("DocumentManagement.Document.Id"), nullable=False)
    ActiveStatus = active_status


class ProjectReleaseModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "ProjectRelease"
    __table_args__ = {"schema": SCHEMA}
    ProjectId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Project.Id"), nullable=False)
    VersionNumber = Column(String(20), nullable=False, unique=True)
    ReleaseDate = Column(Date)
    Description = Column(String(4000))
    ActiveStatus = active_status


class ProjectReleaseIssueModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "ProjectReleaseIssue"
    __table_args__ = {"schema": SCHEMA}
    IssueId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Issue.Id"), nullable=False)
    ProjectReleaseId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.ProjectRelease.Id"), nullable=False)
    IsFinalized = Column(Boolean)
    ActiveStatus = active_status


class WorkLogModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "WorkLog"
    __table_args__ = {"schema": SCHEMA}
    IssueId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Issue.Id"), nullable=False)
    LogDate = Column(Date, nullable=False)
    StartWorkTime = Column(Time, nullable=False)
    WorkingDuration = Column(Float, nullable=False)
    TimeUnitId = Column(UUID(as_uuid=True), ForeignKey("Basic.TimeUnit.Id"), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class WorkflowAllowedFileExtensionModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "WorkflowAllowedFileExtension"
    __table_args__ = {"schema": SCHEMA}
    FileExtensionId = Column(UUID(as_uuid=True), ForeignKey("Basic.FileExtension.Id"), nullable=False)
    ProjectWorkflowId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.ProjectWorkflow.Id"), nullable=False)
    MaxFileSizeForUpload = Column(Integer, nullable=False, server_default="5242880")
    ActiveStatus = active_status


class WorkflowAllowedDocumentTypeModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "WorkflowAllowedDocumentType"
    __table_args__ = {"schema": SCHEMA}
    DocumentTypeId = Column(UUID(as_uuid=True), ForeignKey("Basic.DocumentType.Id"), nullable=False)
    ProjectWorkflowId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.ProjectWorkflow.Id"), nullable=False)
    ActiveStatus = active_status


class ProjectMeetingModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "ProjectMeeting"
    __table_args__ = {"schema": SCHEMA}
    ProjectId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Project.Id"), nullable=False)
    MeetingTypeId = Column(UUID(as_uuid=True), ForeignKey("Basic.MeetingType.Id"), nullable=False)
    MeetingDate = Column(Date, nullable=False)
    Title = Column(String(255), nullable=False)
    Location = Column(String(255), nullable=False)
    MinutesDocumentId = Column(UUID(as_uuid=True), ForeignKey("DocumentManagement.Document.Id"), nullable=True)
    Description = Column(String(4000))
    ScheduleStartTime = Column(Time)
    ScheduleEndTime = Column(Time)
    ActualStartTime = Column(Time)
    ActualEndTime = Column(Time)
    IsCanncelled = Column(Boolean, nullable=False, server_default="false")
    ActiveStatus = active_status


class MeetingInviteesModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "MeetingInvitees"
    __table_args__ = {"schema": SCHEMA}
    ProjectMeetingId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.ProjectMeeting.Id"), nullable=False)
    IsFromInsideCompnay = Column(Boolean, nullable=False)
    ProfileId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Profile.Id"), nullable=True)
    InviteeFullName = Column(String(255))
    InviteeCompanyName = Column(String(