from sqlalchemy import Column, String, Date, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from src.infrastructure.persistence.base_model import (
    Base, UUIDPrimaryKeyMixin, AuditColumnsMixin
)
from src.infrastructure.persistence.enums_pg import active_status

SCHEMA = "QualityControl"


class TestScenarioModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "TestScenario"
    __table_args__ = {"schema": SCHEMA}
    ProjectId = Column(UUID(as_uuid=True), ForeignKey("ProjectManagement.Project.Id"), nullable=False)
    TestComplexityLevelId = Column(UUID(as_uuid=True), ForeignKey("Basic.TestComplexityLevel.Id"), nullable=False)
    Title = Column(String(255), nullable=False)
    Code = Column(String(10), nullable=False, unique=True)
    UsersAndRoles = Column(String(4000))
    Steps = Column(String(4000))
    Description = Column(String(4000))
    ActiveStatus = active_status


class PrerequisiteTestScenarioModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "PrerequisiteTestScenario"
    __table_args__ = {"schema": SCHEMA}
    TestScenarioId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.TestScenario.Id"), nullable=False)
    PrerequisiteTestScenarioId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.TestScenario.Id"), nullable=False)
    ActiveStatus = active_status


class TestPlanModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "TestPlan"
    __table_args__ = {"schema": SCHEMA}
    ProjectReleaseId = Column(UUID(as_uuid=True), ForeignKey("ProjectManagement.ProjectRelease.Id"), nullable=True)
    Title = Column(String(255), nullable=False)
    Code = Column(String(20), nullable=False, unique=True)
    PlanningDate = Column(Date)
    Description = Column(String(4000))
    ActiveStatus = active_status


class TestPlanScenarioModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "TestPlanScenario"
    __table_args__ = {"schema": SCHEMA}
    TestScenarioId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.TestScenario.Id"), nullable=False)
    TestPlanId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.TestPlan.Id"), nullable=False)
    Ordering = Column(Float, nullable=False)
    ActiveStatus = active_status


class TestPlanScenarioIssueCoverageModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "TestPlanScenarioIssueCoverage"
    __table_args__ = {"schema": SCHEMA}
    TestPlanScenarioId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.TestPlanScenario.Id"), nullable=False)
    IssueId = Column(UUID(as_uuid=True), ForeignKey("ProjectManagement.Issue.Id"), nullable=False)
    ActiveStatus = active_status


class TestResultModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "TestResult"
    __table_args__ = {"schema": SCHEMA}
    TestPlanId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.TestPlan.Id"), nullable=False)
    TestDate = Column(Date, nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class TestResultDetailModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "TestResultDetail"
    __table_args__ = {"schema": SCHEMA}
    TestResultId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.TestResult.Id"), nullable=False)
    TestPlanScenarioId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.TestPlanScenario.Id"), nullable=False)
    TestApprovalId = Column(UUID(as_uuid=True), ForeignKey("Basic.TestApproval.Id"), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status