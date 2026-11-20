from dataclasses import dataclass, field
from datetime import date, time
from typing import Optional
from uuid import UUID, uuid4

from ..shared.enums import (
    ActiveStatus, IssueSize, LinkedIssueType, IssueChangeType
)
from ..shared.value_objects import AuditInfo


@dataclass
class Role:
    code: str
    title: str
    id: UUID = field(default_factory=uuid4)
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class Project:
    title: str
    code: str
    id: UUID = field(default_factory=uuid4)
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class ProjectRoleMember:
    profile_id: UUID
    project_id: UUID
    is_project_admin: bool
    id: UUID = field(default_factory=uuid4)
    role_id: Optional[UUID] = None
    is_active: bool = True
    is_deleted: bool = False
    create_date: Optional[date] = None
    creator_id: Optional[UUID] = None
    modify_date: Optional[date] = None
    modifier_id: Optional[UUID] = None


@dataclass
class ProjectGroupMember:
    project_id: UUID
    group_id: UUID
    id: UUID = field(default_factory=uuid4)
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class ProjectDepartmentMember:
    project_id: UUID
    department_id: UUID
    id: UUID = field(default_factory=uuid4)
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class ProjectWorkflow:
    project_id: UUID
    title: str
    code: str
    id: UUID = field(default_factory=uuid4)
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class ProjectWorkflowStatus:
    project_workflow_id: UUID
    status_id: UUID
    id: UUID = field(default_factory=uuid4)
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class ProjectWorkflowResolution:
    project_workflow_id: UUID
    resolution_id: UUID
    id: UUID = field(default_factory=uuid4)
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class ProjectWorkflowProgress:
    title: str
    is_from_start_point: bool
    can_be_started_from_any_status: bool
    is_workflow_end_point: bool
    id: UUID = field(default_factory=uuid4)
    start_project_workflow_status_id: Optional[UUID] = None
    end_project_workflow_status_id: Optional[UUID] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class Issue:
    project_id: UUID
    code: str
    title: str
    issue_type_id: UUID
    current_status_id: UUID
    current_resolution_id: UUID
    id: UUID = field(default_factory=uuid4)
    assignee_id: Optional[UUID] = None
    description: Optional[str] = None
    issue_size: Optional[IssueSize] = None
    priority_id: Optional[UUID] = None
    due_date: Optional[date] = None
    parent_issue_id: Optional[UUID] = None
    epic_linked_id: Optional[UUID] = None
    linked_issue_id: Optional[UUID] = None
    linked_issue_type: Optional[LinkedIssueType] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class IssueWorkflowHistory:
    issue_id: UUID
    issue_change_type: IssueChangeType
    id: UUID = field(default_factory=uuid4)
    project_workflow_progress_id: Optional[UUID] = None
    status_from_id: Optional[UUID] = None
    status_to_id: Optional[UUID] = None
    resolution_from_id: Optional[UUID] = None
    resolution_to_id: Optional[UUID] = None
    assignee_from_id: Optional[UUID] = None
    assignee_to_id: Optional[UUID] = None
    project_from_id: Optional[UUID] = None
    project_to_id: Optional[UUID] = None
    issue_active_status_from: Optional[ActiveStatus] = None
    issue_active_status_to: Optional[ActiveStatus] = None
    change_data_json: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    create_date: Optional[date] = None
    creator_id: Optional[UUID] = None


@dataclass
class IssueComment:
    issue_id: UUID
    comment_text: str
    id: UUID = field(default_factory=uuid4)
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class IssueAttachment:
    issue_id: UUID
    document_id: UUID
    id: UUID = field(default_factory=uuid4)
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class ProjectRelease:
    project_id: UUID
    version_number: str
    id: UUID = field(default_factory=uuid4)
    release_date: Optional[date] = None
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class ProjectReleaseIssue:
    issue_id: UUID
    project_release_id: UUID
    id: UUID = field(default_factory=uuid4)
    is_finalized: Optional[bool] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class WorkLog:
    issue_id: UUID
    log_date: date
    start_work_time: time
    working_duration: float
    time_unit_id: UUID
    id: UUID = field(default_factory=uuid4)
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class WorkflowAllowedFileExtension:
    file_extension_id: UUID
    project_workflow_id: UUID
    id: UUID = field(default_factory=uuid4)
    max_file_size_for_upload: int = 5242880
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class WorkflowAllowedDocumentType:
    document_type_id: UUID
    project_workflow_id: UUID
    id: UUID = field(default_factory=uuid4)
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class ProjectMeeting:
    project_id: UUID
    meeting_type_id: UUID
    meeting_date: date
    title: str
    location: str
    id: UUID = field(default_factory=uuid4)
    minutes_document_id: Optional[UUID] = None
    description: Optional[str] = None
    schedule_start_time: Optional[time] = None
    schedule_end_time: Optional[time] = None
    actual_start_time: Optional[time] = None
    actual_end_time: Optional[time] = None
    is_cancelled: bool = False
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class MeetingInvitee:
    project_meeting_id: UUID
    is_from_inside_company: bool
    id: UUID = field(default_factory=uuid4)
    profile_id: Optional[UUID] = None
    invitee_full_name: Optional[str] = None
    invitee_company_name: Optional[str] = None
    is_attended: Optional[bool] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class MeetingMinute:
    project_meeting_id: UUID
    responsible_department_id: UUID
    resolution: str
    id: UUID = field(default_factory=uuid4)
    issue_id: Optional[UUID] = None
    due_date: Optional[date] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None