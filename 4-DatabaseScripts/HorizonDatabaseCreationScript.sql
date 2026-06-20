/* 
	Note: This script is created specifically for PostgreSQL database.
	Last Version : 26.6.20
	User Guide for Creating Database : 
	1. Please create a database with "horizondb" name.
	2. Open connection to created databse.
	3. Then run the following script. 
*/

CREATE SCHEMA Basic;
CREATE SCHEMA UserManagement;
CREATE SCHEMA HumanResource;
CREATE SCHEMA DocumentManagement;
CREATE SCHEMA ProjectManagement;
CREATE SCHEMA Finance;
CREATE SCHEMA Evaluation;
CREATE SCHEMA QualityControl;


CREATE TYPE activeStatus AS ENUM ('Active', 'Inactive', 'Deleted');
CREATE TYPE gender AS ENUM ('Male', 'Female');
CREATE TYPE weekday AS ENUM ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday');
CREATE TYPE enteranceType AS ENUM ('Enter', 'Exit');
CREATE TYPE issueSize AS ENUM ('XS', 'S', 'M', 'L', 'XL');
CREATE TYPE leaveType AS ENUM ('FullDay', 'PartOfDay');
CREATE TYPE calculationType AS ENUM ('Percentage', 'FixedAmount');
CREATE TYPE statusLevel AS ENUM ('To Do', 'In Progress', 'Done');
CREATE TYPE holidayType AS ENUM ('National', 'GovernmentOrFederal', 'ProvincialOrState', 'Organizational');
CREATE TYPE linkedIssueType AS ENUM ('Blocks', 'RelatesTo', 'Duplicates', 'Clones');
CREATE TYPE questionnaireAduience AS ENUM ('Staffs', 'Customers', 'Stackholders', 'SeniorManagers');
CREATE TYPE answerType AS ENUM ('SignleChoice', 'MultiChoice', 'Description');



CREATE TABLE Basic.EducationLevel(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
    Code varchar(20) NOT NULL UNIQUE,
    Title varchar(200) NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE Basic.Priority(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
    Code varchar(20) NOT NULL UNIQUE,
    Title varchar(200) NOT NULL,
	Ordering int NOT NULL,
	Color varchar(7) NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE Basic.IssueType(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
    Code varchar(20) NOT NULL UNIQUE,
    Title varchar(200) NOT NULL,
	IconAddress varchar(1000) NOT NULL,
	Color varchar(7) NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE Basic.Status(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    Code varchar(20) NOT NULL UNIQUE,
    Title varchar(200) NOT NULL,
	Color varchar(7) NOT NULL,
	StatusEffect statusLevel NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE Basic.Resolution(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    Code varchar(20) NOT NULL UNIQUE,
    Title varchar(200) NOT NULL,
	Color varchar(7) NOT NULL,
	IsResolved boolean NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE Basic.MeetingType(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    Code varchar(20) NOT NULL UNIQUE,
    Title varchar(200) NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE Basic.DocumentType(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    Code varchar(20) NOT NULL UNIQUE,
    Title varchar(200) NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE Basic.FileExtension(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    Code varchar(20) NOT NULL UNIQUE,
    Title varchar(200) NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE Basic.ContractType(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    Code varchar(20) NOT NULL UNIQUE,
    Title varchar(200) NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE Basic.TestApproval(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    Code varchar(20) NOT NULL UNIQUE,
    Title varchar(200) NOT NULL,
	IsApproved boolean NOT NULL,
	Color varchar(10) NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE Basic.TestComplexityLevel(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    Code varchar(20) NOT NULL UNIQUE,
    Title varchar(200) NOT NULL,
	ValueNumber float NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE Basic.TimeUnit(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    Code varchar(20) NOT NULL UNIQUE,
    Title varchar(200) NOT NULL,
	ValueBasedOnMillisecond bigint NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE Basic.Currency(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    Code varchar(20) NOT NULL UNIQUE,
	Symbol varchar(20) NOT NULL UNIQUE,
    Title varchar(200) NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE UserManagement.Role(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    Code varchar(20) NOT NULL UNIQUE,
    Title varchar(200) NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE UserManagement.Groups(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    Code varchar(20) NOT NULL UNIQUE,
    Title varchar(200) NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE UserManagement.Permission(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    Code varchar(20) NOT NULL UNIQUE,
    Title varchar(200) NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE UserManagement.Form(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    Code varchar(20) NOT NULL UNIQUE,
    Title varchar(200) NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE UserManagement.FormPermission(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    FormId uuid NOT NULL,
	PermissionId uuid NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (FormId) REFERENCES UserManagement.Form(Id),
    FOREIGN KEY (PermissionId) REFERENCES UserManagement.Permission(Id)
);

CREATE TABLE UserManagement.RolePermission(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    FormPermissionId uuid NOT NULL,
	RoleId uuid NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (RoleId) REFERENCES UserManagement.Role(Id),
    FOREIGN KEY (FormPermissionId) REFERENCES UserManagement.FormPermission(Id)
);

CREATE TABLE UserManagement.GroupPermission(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    FormPermissionId uuid NOT NULL,
	GroupId uuid NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (GroupId) REFERENCES UserManagement.Groups(Id),
    FOREIGN KEY (FormPermissionId) REFERENCES UserManagement.FormPermission(Id)
);

CREATE TABLE HumanResource.Department(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    Code varchar(20) NOT NULL UNIQUE,
    Title varchar(255) NOT NULL,
	Description varchar(4000),
	ParentId uuid,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ParentId) REFERENCES HumanResource.Department(Id)
);

CREATE TABLE HumanResource.Position(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    Code varchar(10) NOT NULL UNIQUE,
    Title varchar(255) NOT NULL,
	Description varchar(4000),
	ParentId uuid,
	DepartmentId uuid NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ParentId) REFERENCES HumanResource.Position(Id),
	FOREIGN KEY (DepartmentId) REFERENCES HumanResource.Department(Id)
);

CREATE TABLE UserManagement.Profile(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	FirstName varchar(200) NOT NULL,
	LastName varchar(200) NOT NULL,
	Gender gender NOT NULL,
	StaffNumber varchar(20) NOT NULL UNIQUE,
	ActiveFrom timestamp NOT NULL,
	ActiveTo timestamp,
	PositionId uuid,
	Avatar varchar(1000),
	Birthday date,
	PhoneNumber varchar(20),
	MobileNumber varchar(20),
	EmailAddress varchar(200),
	Address varchar(1000),
	PostalCode varchar(20),
	Username varchar(200) NOT NULL UNIQUE,
	Pass varchar(255) NOT NULL,
	PassSalt varchar(5),
	LastLogInDate timestamp,
	LogInCount int NOT NULL DEFAULT 0,
	WrongLogInCount int NOT NULL DEFAULT 0,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (PositionId) REFERENCES HumanResource.Position(Id)
);

CREATE TABLE UserManagement.ProfilePermission(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    FormPermissionId uuid NOT NULL,
	ProfileId uuid NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProfileId) REFERENCES UserManagement.Profile(Id),
    FOREIGN KEY (FormPermissionId) REFERENCES UserManagement.FormPermission(Id)
);

CREATE TABLE UserManagement.ProfileRole(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    ProfileId uuid NOT NULL,
	RoleId uuid NOT NULL,
    IsActive boolean NOT NULL DEFAULT true,
    IsDeleted boolean NOT NULL DEFAULT false,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (RoleId) REFERENCES UserManagement.Role(Id),
    FOREIGN KEY (ProfileId) REFERENCES UserManagement.Profile(Id)
);

CREATE TABLE UserManagement.ProfileGroup(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    ProfileId uuid NOT NULL,
	GroupId uuid NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (GroupId) REFERENCES UserManagement.Groups(Id),
    FOREIGN KEY (ProfileId) REFERENCES UserManagement.Profile(Id)
);

CREATE TABLE DocumentManagement.Document(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
    TableId uuid NOT NULL,
    TableName varchar(255) NOT NULL,
	FileAddress varchar(4000) NOT NULL,
	DocumentTypeId uuid NOT NULL,
	FileExtensionId uuid NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (DocumentTypeId) REFERENCES Basic.DocumentType(Id),
	FOREIGN KEY (FileExtension) REFERENCES Basic.FileExtension(Id)
);

CREATE TABLE HumanResource.ProfileEducation(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	ProfileId uuid NOT Null,
	EducationLevelId uuid NOT NULL,
	DocumentId uuid,
	Title varchar(255) NOT NULL,
	CollageName varchar(255),
	StartDate date,
	EndDate date,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProfileId) REFERENCES UserManagement.Profile(Id),
	FOREIGN KEY (DocumentId) REFERENCES DocumentManagement.Document(Id),
	FOREIGN KEY (EducationLevelId) REFERENCES Basic.EducationLevel(Id)
);

CREATE TABLE HumanResource.ProfileJobExperience(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	ProfileId uuid NOt Null,
	JobTitle varchar(255) NOT NULL,
	CompanyName varchar(255) NOT NULL,
	StartDate date,
	EndDate date,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProfileId) REFERENCES UserManagement.Profile(Id)
);

CREATE TABLE HumanResource.ProfileCertificate(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	ProfileId uuid NOt Null,
	Title varchar(255) NOT NULL,
	InstituteName varchar(255) NOT NULL,
	HasCertificate boolean NOT NULL,
	DocumentId uuid,
	StartDate date,
	EndDate date,
	Description varchar(4000),
	CertificateFileAddress varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProfileId) REFERENCES UserManagement.Profile(Id),
	FOREIGN KEY (DocumentId) REFERENCES DocumentManagement.Document(Id)
);


CREATE TABLE HumanResource.WorkingTimeTable(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	ContractTypeId uuid NOt Null,
	WorkingDay weekday NOT NULL,
	StartTime time NOT NULL,
	EndTime time NOT NULL,
	FloatingStartTime time,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ContractTypeId) REFERENCES Basic.ContractType(Id)
);

CREATE TABLE HumanResource.Holiday(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	Title varchar(255) NOT NULL,
	HolidayType holidayType NOT NULL,
	HolidayDate date NOT NULL UNIQUE,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE HumanResource.Attendance(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	ProfileId uuid Not Null,
	WorkingDate date NOT NULL,
	EnteranceType enteranceType NOT NULL,
	EnternaceTime time NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProfileId) REFERENCES UserManagement.Profile(Id)
);

CREATE TABLE HumanResource.Leave(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	ProfileId uuid Not Null,
	LeaveType leaveType NOT NULL,
	LeavingStartDate date NOT NULL,
	LeavingEndDate date,
	LeavingStartTime time NOT NULL,
	LeavingEndTime time NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProfileId) REFERENCES UserManagement.Profile(Id)
);


CREATE TABLE HumanResource.WorkMission(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	ProfileId uuid Not Null,
	MissionStartDate date NOT NULL,
	MissionEndDate date,
	MissionStartTime time NOT NULL,
	MissionEndTime time NOT NULL,
	MissionLocation varchar(255),
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProfileId) REFERENCES UserManagement.Profile(Id)
);


CREATE TABLE ProjectManagement.Project(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	Title varchar(255) NOT NULL,
	Code varchar(20) NOT NULL UNIQUE,
	StartDate date,
	EndDate date,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE ProjectManagement.ProjectProfileMember(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	ProjectId uuid NOT NULL,
	ProfileId uuid NOT NULL,
	IsProjectManager boolean NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProjectId) REFERENCES ProjectManagement.Project(Id),
	FOREIGN KEY (ProfileId) REFERENCES UserManagement.Profile(Id),
	UNIQUE (ProjectId, ProfileId)
);

CREATE TABLE ProjectManagement.ProjectGroupMember(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	ProjectId uuid NOT NULL,
	GroupId uuid NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProjectId) REFERENCES ProjectManagement.Project(Id),
	FOREIGN KEY (GroupId) REFERENCES UserManagement.Groups(Id),
	UNIQUE (ProjectId, GroupId)
);

CREATE TABLE ProjectManagement.ProjectRoleMember(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	ProjectId uuid NOT NULL,
	RoleId uuid NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProjectId) REFERENCES ProjectManagement.Project(Id),
	FOREIGN KEY (RoleId) REFERENCES UserManagement.Role(Id),
	UNIQUE (ProjectId, RoleId)
);

CREATE TABLE ProjectManagement.ProjectDepartmentMember(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	ProjectId uuid NOT NULL,
	DepartmentId uuid NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProjectId) REFERENCES ProjectManagement.Project(Id),
	FOREIGN KEY (DepartmentId) REFERENCES HumanResource.Department(Id),
	UNIQUE (ProjectId, DepartmentId)
);

CREATE TABLE ProjectManagement.ProjectWorkflow(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	ProjectId uuid NOT NULL,
	Title varchar(255) NOT NULL,
	Code varchar(20) NOT NULL UNIQUE,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProjectId) REFERENCES ProjectManagement.Project(Id)
);

CREATE TABLE ProjectManagement.ProjectWorkflowStatus(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	ProjectWorkflowId uuid NOT NULL,
	StatusId uuid NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProjectWorkflowId) REFERENCES ProjectManagement.ProjectWorkflow(Id),
	FOREIGN KEY (StatusId) REFERENCES Basic.Status(Id)
);

CREATE TABLE ProjectManagement.ProjectWorkflowResolution(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	ProjectWorkflowId uuid NOT NULL,
	ResolutionId uuid NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProjectWorkflowId) REFERENCES ProjectManagement.ProjectWorkflow(Id),
	FOREIGN KEY (ResolutionId) REFERENCES Basic.Resolution(Id)
);

CREATE TABLE ProjectManagement.ProjectWorkflowProgress(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	Title varchar(255) NOT NULL,
	StartProjectWorkflowStatusId uuid,
	IsFromStartPoint boolean NOT NULL
	CanBeStartedFromAnyStatus boolean NOT NULL,
	EndProjectWorkflowStatusId uuid,
	IsWorkflowEndPoint boolean NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (StartProjectWorkflowStatusId) REFERENCES ProjectManagement.ProjectWorkflowStatus(Id),
	FOREIGN KEY (EndProjectWorkflowStatusId) REFERENCES ProjectManagement.ProjectWorkflowStatus(Id)
);



CREATE TABLE ProjectManagement.Issue(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	ProjectId uuid NOT NULL,
	AssigneeId uuid,
	Code varchar(20) NOT NULL UNIQUE,
    Title varchar(200) NOT NULL,
	Description varchar(4000),
	IssueSize issueSize,
	PriorityId uuid,
	DueDate date,
	IssueTypeId uuid NOT NULL,
	ParentIssueId uuid,
	EpicLinkedId uuid,
	LinkedIssueId uuid,
	LinkedIssueType linkedIssueType,
	CurrentStatusId uuid NOT NULL,
	CurrentResolutionId uuid NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (AssigneeId) REFERENCES UserManagement.Profile(Id),
	FOREIGN KEY (ProjectId) REFERENCES ProjectManagement.Project(Id),
	FOREIGN KEY (IssueTypeId) REFERENCES Basic.IssueType(Id),
	FOREIGN KEY (CuurentStatusId) REFERENCES ProjectManagement.ProjectWorkflowStatus(Id),
	FOREIGN KEY (CurrentResolutionId) REFERENCES ProjectManagement.ProjectWorkflowResolution(Id)
	FOREIGN KEY (LinkedIssueId) REFERENCES ProjectManagement.Issue(Id)
	FOREIGN KEY (EpicLinkedId) REFERENCES ProjectManagement.Issue(Id)
	FOREIGN KEY (ParentIssueId) REFERENCES ProjectManagement.Issue(Id)
);

CREATE TABLE ProjectManagement.IssueComment(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	IssueId uuid NOT NULL,
	CommentText varchar(4000) NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (IssueId) REFERENCES ProjectManagement.Issue(Id)
);

CREATE TABLE ProjectManagement.IssueAttachment(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	IssueId uuid NOT NULL,
	DocumentId uuid NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (IssueId) REFERENCES ProjectManagement.Issue(Id),
	FOREIGN KEY (DocumentId) REFERENCES DocumentManagement.Document(Id),
	UNIQUE(IssueId, DocumentId)
);

CREATE TABLE ProjectManagement.ProjectRelease(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	ProjectId uuid NOT NULL,
	VersionNumber varchar(20) NOT NULL UNIQUE,
    ReleaseDate date,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProjectId) REFERENCES ProjectManagement.Project(Id)
);

CREATE TABLE ProjectManagement.ProjectReleaseIssue(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	IssueId uuid NOT NULL,
	ProjectReleaseId uuid NOT NULL,
	IsFinalized boolean,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (IssueId) REFERENCES ProjectManagement.Issue(Id),
	FOREIGN KEY (ProjectReleaseId) REFERENCES ProjectManagement.ProjectRelease(Id),
	UNIQUE(IssueId, ProjectReleaseId)
);

CREATE TABLE ProjectManagement.WorkLog(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	IssueId uuid NOT NULL,
	LogDate date NOT NULL,
	StartWorkTime time NOT NULL,
	WorkingDuration float NOT NULL, 
	TimeUnitId uuid NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (IssueId) REFERENCES ProjectManagement.Issue(Id),
	FOREIGN KEY (TimeUnitId) REFERENCES Basic.TimeUnit(Id)
	
);

CREATE TABLE ProjectManagement.WorkflowAllowedFileExtension(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	FileExtensionId uuid NOT NULL,
	ProjectWorkflowId uuid NOT NULL,
	MaxFileSizeForUpload integer NOT NULL DEFAULT 5242880,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (FileExtensionId) REFERENCES DocumentManagement.FileExtension(Id),
	FOREIGN KEY (ProjectWorkflowId) REFERENCES ProjectManagement.ProjectWorkflow(Id),
	UNIQUE(FileExtensionId, ProjectWorkflowId)
);

CREATE TABLE ProjectManagement.WorkflowAllowedDocumentType(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	DocumentTypeId uuid NOT NULL,
	ProjectWorkflowId uuid NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (DocumentTypeId) REFERENCES DocumentManagement.DocumentType(Id),
	FOREIGN KEY (ProjectWorkflowId) REFERENCES ProjectManagement.ProjectWorkflow(Id),
	UNIQUE(DocumentTypeId, ProjectWorkflowId)
);

CREATE TABLE ProjectManagement.IssueWorkflowHistory(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	IssueId uuid NOT NULL,
	StartStatusId uuid NOT NULL,
	EndStatusId uuid NOT NULL,
	ProjectWorkflowProgressId uuid NOT NULL,
	ProjectWorkflowResolutionId uuid,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (IssueId) REFERENCES ProjectManagement.Issue(Id),
	FOREIGN KEY (StartStatusId) REFERENCES ProjectManagement.StartStatus(Id),
	FOREIGN KEY (EndStatusId) REFERENCES ProjectManagement.EndStatus(Id),
	FOREIGN KEY (ProjectWorkflowProgressId) REFERENCES ProjectManagement.ProjectWorkflowProgress(Id),
	FOREIGN KEY (ProjectWorkflowResolutionId) REFERENCES ProjectManagement.ProjectWorkflowResolution(Id)
);

CREATE TABLE ProjectManagement.ProjectMeeting(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	ProjectId uuid NOT NULL,
	MeetingTypeId uuid NOT NULL,
	MeetingDate date NOT NULL,
	Title varchar(255) NOT NULL,
	Location varchar(255) NOT NULL,
	MinutesDocumentId uuid,
	Description varchar(4000),
	ScheduleStartTime time,
	ScheduleEndTime time,
	ActualStartTime time,
	ActualEndTime time,
	IsCanncelled boolean NOT NULL DEFAULT false,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProjectId) REFERENCES ProjectManagement.Project(Id),
	FOREIGN KEY (MeetingTypeId) REFERENCES ProjectManagement.MeetingType(Id),
	FOREIGN KEY (MinutesDocumentId) REFERENCES DocumentManagement.Document(Id)
);

CREATE TABLE ProjectManagement.MeetingInvitees(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	ProjectMeetingId uuid NOT NULL,
	IsFromInsideCompnay boolean NOT NULL,
	ProfileId uuid,
	InviteeFullName varchar(255),
	InviteeCompanyName varchar(255),
	IsAttanded boolean,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProjectMeetingId) REFERENCES ProjectManagement.ProjectMeeting(Id),
	FOREIGN KEY (ProfileId) REFERENCES HumanResource.Profile(Id)
);

CREATE TABLE ProjectManagement.MeetingMinutes(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	ProjectMeetingId uuid NOT NULL,
	ResponsibleDepartmentId uuid NOT NULL,
	Resolution varchar(4000) NOT NULL,
	IssueId uuid,
	DueDate datetime,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProjectMeetingId) REFERENCES ProjectManagement.ProjectMeeting(Id),
	FOREIGN KEY (IssueId) REFERENCES ProjectManagement.Issue(Id),
	FOREIGN KEY (ResponsibleDepartmentId) REFERENCES HumanResource.Department(Id)
);

CREATE TABLE Finance.StaffContract(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	ProfileId uuid NOT NULL,
	ContractTypeId uuid NOT NULL,
	StartDate date NOT NULL,
	EndDate date NOT NULL,
	Title varchar(255) NOT NULL,
	Description varchar(4000),
	AutoRenewal boolean,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (PofileId) REFERENCES UserManagement.Profile(Id),
	FOREIGN KEY (ContractTypeId) REFERENCES Basic.ContractType(Id)
);

CREATE TABLE Finance.ContractSalaryItem(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	StaffContractId uuid NOT NULL,
	CalculationTimeUnitId uuid NOT NULL,
	Title varchar(255) NOT NULL,
	Amount numeric(22, 2) NOT NULL,
	CurrencyId uuid NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ContractId) REFERENCES Finance.StaffContract(Id),
	FOREIGN KEY (CurrencyId) REFERENCES Basic.Currency(Id),
	FOREIGN KEY (CalculationTimeUnitId) REFERENCES Basic.TimeUnit(Id)
);

CREATE TABLE Finance.ContractDeductionItem(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	CalculationType calculationType NOT NULL,
	StaffContractId uuid NOT NULL,
	CalculationTimeUnitId uuid NOT NULL,
	Title varchar(255) NOT NULL,
	DeductionPercentage numeric(3,2),
	FixedAmount numeric(22, 2),
	FixedAmountCurrencyId uuid,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ContractId) REFERENCES Finance.StaffContract(Id),
	FOREIGN KEY (FixedAmountCurrencyId) REFERENCES Basic.Currency(Id),
	FOREIGN KEY (CalculationTimeUnitId) REFERENCES Basic.TimeUnit(Id)
);

CREATE TABLE Finance.Supplier(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	Title varchar(255) NOT NULL,
	PhoneNumber varchar(20),
	MobileNumber varchar(20),
	FaxNumber varchar(20),
	Email varchar(100),
	PostalCode varchar(20),
	City varchar(255),
	Address varchar(4000),
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE Finance.CostInvoice(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	InvoiceNumber varchar(20) NOT NULL,
	SupplierId uuid NOT NULL,
	DocumentId uuid NOT NULL,
	CompnayId uuid NOT NULL,
	InvoiceDate date NOT NULL,
	TotalAmount numeric(22, 2) NOT NULL,
	CurrencyId uuid NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (SupplierId) REFERENCES Finance.Supplier(Id),
	FOREIGN KEY (DocumentId) REFERENCES DocumentManagement.Document(Id),
	FOREIGN KEY (CurrencyId) REFERENCES Basic.Currency(Id),
	FOREIGN KEY (CompnayId) REFERENCES HumanResource.Compnay(Id)
);

CREATE TABLE Finance.CostInvoiceItem(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	CostInvoiceId uuid NOT NULL,
	ItemTitle varchar(255) NOT NULL,
	UnitAmount numeric(22, 2) NOT NULL,
	CurrencyId uuid NOT NULL,
	Quantity float NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (CostInvoiceId) REFERENCES Finance.CostInvoice(Id),
	FOREIGN KEY (CurrencyId) REFERENCES Basic.Currency(Id)
);

CREATE TABLE Finance.ProjectDirectCostItem(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	ProjectId uuid NOT NULL,
	CostInvoiceItemId uuid NOT NULL,
	AllocatedQuantity float NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProjectId) REFERENCES ProjectManagement.Project(Id),
	FOREIGN KEY (CostInvoiceItemId) REFERENCES Finance.CostInvoiceItem(Id)
);

CREATE TABLE Finance.CostPaymentReceipt(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	ReceiptNumber varchar(20) NOT NULL,
	CostInvoiceId uuid NOT NULL,
	DocumentId uuid NOT NULL,
	PaymentDate date NOT NULL,
	Amount numeric(22, 2) NOT NULL,
	CurrencyId uuid NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (CostInvoiceId) REFERENCES Finance.CostInvoice(Id),
	FOREIGN KEY (CurrencyId) REFERENCES Basic.Currency(Id),
	FOREIGN KEY (DocumentId) REFERENCES DocumentManagement.Document(Id)
);

CREATE TABLE Finance.SalaryPaymentReceipt(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	ReceiptNumber varchar(20) NOT NULL,
	StaffContractId uuid NOT NULL,
	DocumentId uuid NOT NULL,
	PaymentDate date NOT NULL,
	Amount numeric(22, 2) NOT NULL,
	CurrencyId uuid NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (StaffContractId) REFERENCES Finance.StaffContract(Id),
	FOREIGN KEY (CurrencyId) REFERENCES Basic.Currency(Id),
	FOREIGN KEY (DocumentId) REFERENCES DocumentManagement.Document(Id)
);


CREATE TABLE Finance.StaffAdditionalPaymentReceipt(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	ProfileId uuid NOT NULL,
	Title varchar(255) NOT NULL,
	DocumentId uuid NOT NULL,
	PaymentDate date NOT NULL,
	Amount numeric(22, 2) NOT NULL,
	CurrencyId uuid NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProfileId) REFERENCES HumanResource.Profile(Id),
	FOREIGN KEY (CurrencyId) REFERENCES Basic.Currency(Id),
	FOREIGN KEY (DocumentId) REFERENCES DocumentManagement.Document(Id)
);

CREATE TABLE Finance.Customer(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	Title varchar(255) NOT NULL,
	PhoneNumber varchar(20),
	MobileNumber varchar(20),
	FaxNumber varchar(20),
	Email varchar(100),
	PostalCode varchar(20),
	City varchar(200),
	Address varchar(4000),
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE Finance.CustomerContract(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	CustomerId uuid NOT NULL,
	ProjectId uuid NOT NULL,
	ContractNumber varchar(20) NOT NULL,
	StartDate date,
	ScheduledEndDate date,
	RealEndDate date,
	IsDevelopmentContract boolean,
	IsSupportContract boolean,
	TotalAmount numeric(22, 2) NOT NULL,
	CurrencyId uuid NOT NULL,
	DocumentId uuid NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (CustomerId) REFERENCES Finance.Customer(Id),
	FOREIGN KEY (ProjectId) REFERENCES ProjectManagement.Project(Id),
	FOREIGN KEY (CurrencyId) REFERENCES Basic.Currency(Id),
	FOREIGN KEY (DocumentId) REFERENCES DocumentManagement.Document(Id)
);

CREATE TABLE Finance.CustomerContractPaymentSchedule(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	CustomerContractId uuid NOT Null,
	PaymentTitle varchar(255) NOT NULL,
	ProjectReleaseId uuid,
	ScheduledPaymentDate date,
	Amount numeric(22, 2) NOT NULL,
	CurrencyId uuid NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (CustomerContractId) REFERENCES Finance.CustomerContarct(Id),
	FOREIGN KEY (ProjectReleaseId) REFERENCES ProjectManagement.ProjectRelease(Id),
	FOREIGN KEY (CurrencyId) REFERENCES Basic.Currency(Id)
);

CREATE TABLE Finance.CustomerContractPaymentReceipt(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	CustomerContractPaymentScheduleId uuid NOT Null,
	ReceiptNumber varchar(20) NOT NULL,
	ReceiptDocumentId uuid,
	PaymentDate date,
	Amount numeric(22, 2) NOT NULL,
	CurrencyId uuid NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (CustomerContractPaymentScheduleId) REFERENCES Finance.CustomerContractPaymentSchedule(Id),
	FOREIGN KEY (ReceiptDocumentId) REFERENCES DocumentManagement.Document(Id),
	FOREIGN KEY (CurrencyId) REFERENCES Basic.Currency(Id)
);

CREATE TABLE QualityControl.TestScenario(
    Id uuid NOT uuid DEFAULT gen_random_uuid(), 
	ProjectId uuid NOT Null,
	TestComplexityLevelId uuid NOT Null,
	Title varchar(255) NOT NULL,
	Code varchar(10) NOT NULL UNIQUE,
	UsersAndRoles varchar(4000),
	Steps varchar(4000),
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProjectId) REFERENCES ProjectManagement.Project(Id),
	FOREIGN KEY (TestComplexityLevelId) REFERENCES Finance.TestComplexityLevel(Id)
);

CREATE TABLE QualityControl.PrerequisiteTestScenario(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	TestScenarioId uuid NOT Null,
	PrerequisiteTestScenarioId uuid NOT Null,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (TestScenarioId) REFERENCES QualityControl.TestScenario(Id),
	FOREIGN KEY (PrerequisiteTestScenarioId) REFERENCES QualityControl.TestScenario(Id)
);

CREATE TABLE QualityControl.TestPlan(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	ProjectReleaseId uuid,
	Title varchar(255) NOT NULL,
	Code varchar(20) NOT NULL UNIQUE,
	PlanningDate date,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProjectReleaseId) REFERENCES ProjectManagement.ProjectRelease(Id)
);

CREATE TABLE QualityControl.TestPlanScenario(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	TestScenarioId uuid NOT NULL,
	TestPlanId uuid NOT NULL,
	Ordering float NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (TestScenarioId) REFERENCES QualityControl.TestScenario(Id),
	FOREIGN KEY (TestPlanId) REFERENCES QualityControl.TestPlan(Id),
	UNIQUE(TestScenarioId, TestPlanId, Ordering)
);

CREATE TABLE QualityControl.TestPlanScenarioIssueCoverage(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	TestPlanScenarioId uuid NOT NULL,
	IssueId uuid NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (TestPlanScenarioId) REFERENCES QualityControl.TestPlanScenario(Id),
	FOREIGN KEY (IssueId) REFERENCES ProjectManagement.Issue(Id),
	UNIQUE(TestPlanScenarioId, IssueId)
);

CREATE TABLE QualityControl.TestResult(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	TestPlanId uuid NOT NULL,
	TestDate date NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (TestPlanId) REFERENCES QualityControl.TestPlan(Id)
);

CREATE TABLE QualityControl.TestResultDetail(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	TestPlanScenarioId uuid,
	TestApprovalId uuid NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (TestPlanScenarioId) REFERENCES QualityControl.TestPlanScenario(Id),
	FOREIGN KEY (TestApprovalId) REFERENCES Basic.TestApproval(Id)
);

CREATE TABLE Evaluation.Question(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	Score int NOT NULL,
	Code varchar(20) NOT NULL UNIQUE,
	Question varchar(4000) NOT NULL,
	AnswerType answerType NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id)
);

CREATE TABLE Evaluation.QuestionOption(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	QuestionId uuid NOT Null,
	Score int NOT NULL,
	Title varchar(4000) NOT NULL,
	IsDescriptionRequired boolean NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (QuestionId) REFERENCES Evaluation.Question(Id)
);

CREATE TABLE Evaluation.Questionnaire(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	Title varchar(255) NOT NULL,
	Code varchar(20) NOT NULL UNIQUE,
	ProjectId uuid,
	QuestionnaireAduience questionnaireAduience NOT NULL,
	TotalScore numeric(22,2) NOT NULL,
	AcceptableScore numeric(22,2) NOT NULL,
	WarningScore numeric(22,2) NOT NULL,
	DisasterScore numeric(22,2) NOT NULL,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProjectId) REFERENCES ProjectManagement.Project(Id)
);

CREATE TABLE Evaluation.QuestionnaireTargetDepartment(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	QuestionnaireId uuid NOT Null,
	DepartmentId uuid NOT Null,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (QuestionnaireId) REFERENCES Evaluation.Questionnaire(Id),
	FOREIGN KEY (DepartmentId) REFERENCES HumanResource.Department(Id)
);

CREATE TABLE Evaluation.QuestionnaireItem(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	QuestionnaireId uuid NOT Null,
	QuestionId uuid NOT Null,
    IsActive boolean NOT NULL DEFAULT true,
    IsDeleted boolean NOT NULL DEFAULT false,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (QuestionnaireId) REFERENCES Evaluation.Questionnaire(Id),
	FOREIGN KEY (QuestionId) REFERENCES Evaluation.Question(Id)
);

CREATE TABLE Evaluation.QuestionnaireResult(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	QuestionnaireId uuid NOT Null,
	ProfileId uuid,
	CustomerId uuid,
	TotalScore int NOT NULL,
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (QuestionnaireId) REFERENCES Evaluation.Questionnaire(Id),
	FOREIGN KEY (ProfileId) REFERENCES UserManagement.Profile(Id),
	FOREIGN KEY (CustomerId) REFERENCES Finance.Customer(Id)
);

CREATE TABLE Evaluation.QuestionnaireResultDetail(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	QuestionnaireResultDetailId uuid NOT NULL,
	QuestionnaireItemId uuid NOT NULL,
	ChoosedQuestionOptionId uuid,
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (QuestionnaireResultDetailId) REFERENCES Evaluation.QuestionnaireResultDetail(Id),
	FOREIGN KEY (QuestionnaireItemId) REFERENCES Evaluation.QuestionnaireItem(Id),
	FOREIGN KEY (ChoosedQuestionOptionId) REFERENCES Evaluation.QuestionOption(Id)
);

CREATE TABLE Evaluation.StaffSatisfactionEvaluation(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	ProfileId uuid NOT NULL,
	EvalationDate date NOT NULL,
	EvaluatedValue numeric(3, 2) NOT NULL CHECK(EvaluatedValue BETWEEN 1 AND 100),
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProfileId) REFERENCES UserManagement.Profile(Id)
);

CREATE TABLE Evaluation.ProjectProductivityEvaluation(
    Id uuid NOT NULL DEFAULT gen_random_uuid(),  
	ProjectId uuid NOT NULL,
	EvalationDate date NOT NULL,
	EvaluatedValue numeric(3, 2) NOT NULL CHECK(EvaluatedValue BETWEEN 1 AND 100),
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (ProjectId) REFERENCES ProjectManagement.Project(Id)
);

CREATE TABLE Evaluation.CustomerSatisfactionEvaluation(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	CustomerId uuid NOT NULL,
	ProjectId uuid NOT NULL,
	EvalationDate date NOT NULL,
	EvaluatedValue numeric(3, 2) NOT NULL CHECK(EvaluatedValue BETWEEN 1 AND 100),
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (CustomerId) REFERENCES Finance.Customer(Id),
	FOREIGN KEY (ProjectId) REFERENCES ProjectManagement.Project(Id)
);

CREATE TABLE Evaluation.CustomerFeedback(
    Id uuid NOT NULL DEFAULT gen_random_uuid(), 
	CustomerId uuid NOT NULL,
	ProjectId uuid NOT NULL,
	FeedbackDate date NOT NULL,
	FeedbackValue numeric(2, 2) NOT NULL CHECK(EvaluatedValue BETWEEN 1 AND 10),
	Description varchar(4000),
    ActiveStatus activeStatus NOT NULL DEFAULT activeStatus.Active,
    CreateDate timestamp NOT NULL DEFAULT NOW(),
	CreatorId uuid NOT NULL,
    ModifyDate timestamp,
	ModifierId uuid,
	PRIMARY KEY(Id),
	FOREIGN KEY (CustomerId) REFERENCES Finance.Customer(Id),
	FOREIGN KEY (ProjectId) REFERENCES ProjectManagement.Project(Id)
);