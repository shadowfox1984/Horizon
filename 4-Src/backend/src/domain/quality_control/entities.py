from dataclasses import dataclass, field
from datetime import date
from typing import Optional
from uuid import UUID, uuid4

from ..shared.enums import ActiveStatus
from ..shared.value_objects import AuditInfo


@dataclass
class TestScenario:
    project_id: UUID
    test_complexity_level_id: UUID
    title: str
    code: str
    id: UUID = field(default_factory=uuid4)
    users_and_roles: Optional[str] = None
    steps: Optional[str] = None
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class PrerequisiteTestScenario:
    test_scenario_id: UUID
    prerequisite_test_scenario_id: UUID
    id: UUID = field(default_factory=uuid4)
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class TestPlan:
    title: str
    code: str
    id: UUID = field(default_factory=uuid4)
    project_release_id: Optional[UUID] = None
    planning_date: Optional[date] = None
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class TestPlanScenario:
    test_scenario_id: UUID
    test_plan_id: UUID
    ordering: float
    id: UUID = field(default_factory=uuid4)
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class TestPlanScenarioIssueCoverage:
    test_plan_scenario_id: UUID
    issue_id: UUID
    id: UUID = field(default_factory=uuid4)
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class TestResult:
    test_plan_id: UUID
    test_date: date
    id: UUID = field(default_factory=uuid4)
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class TestResultDetail:
    test_result_id: UUID
    test_plan_scenario_id: UUID
    test_approval_id: UUID
    id: UUID = field(default_factory=uuid4)
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None