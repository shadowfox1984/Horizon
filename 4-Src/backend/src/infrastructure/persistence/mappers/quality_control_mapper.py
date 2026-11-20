from src.domain.quality_control.entities import (
    TestScenario, PrerequisiteTestScenario, TestPlan, TestPlanScenario,
    TestPlanScenarioIssueCoverage, TestResult, TestResultDetail,
)
from src.infrastructure.persistence.models.quality_control import (
    TestScenarioModel, PrerequisiteTestScenarioModel, TestPlanModel,
    TestPlanScenarioModel, TestPlanScenarioIssueCoverageModel,
    TestResultModel, TestResultDetailModel,
)
from ._helpers import audit_from_model, active_from_model


def _audit_kwargs(e):
    if e.audit:
        return dict(
            CreatorId=e.audit.creator_id, CreateDate=e.audit.create_date,
            ModifierId=e.audit.modifier_id, ModifyDate=e.audit.modify_date,
        )
    return {}


class TestScenarioMapper:
    @staticmethod
    def to_domain(m: TestScenarioModel) -> TestScenario:
        return TestScenario(
            id=m.Id, project_id=m.ProjectId,
            test_complexity_level_id=m.TestComplexityLevelId,
            title=m.Title, code=m.Code,
            users_and_roles=m.UsersAndRoles, steps=m.Steps,
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: TestScenario) -> TestScenarioModel:
        return TestScenarioModel(
            Id=e.id, ProjectId=e.project_id,
            TestComplexityLevelId=e.test_complexity_level_id,
            Title=e.title, Code=e.code, UsersAndRoles=e.users_and_roles,
            Steps=e.steps, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class PrerequisiteTestScenarioMapper:
    @staticmethod
    def to_domain(m: PrerequisiteTestScenarioModel) -> PrerequisiteTestScenario:
        return PrerequisiteTestScenario(
            id=m.Id, test_scenario_id=m.TestScenarioId,
            prerequisite_test_scenario_id=m.PrerequisiteTestScenarioId,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: PrerequisiteTestScenario) -> PrerequisiteTestScenarioModel:
        return PrerequisiteTestScenarioModel(
            Id=e.id, TestScenarioId=e.test_scenario_id,
            PrerequisiteTestScenarioId=e.prerequisite_test_scenario_id,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class TestPlanMapper:
    @staticmethod
    def to_domain(m: TestPlanModel) -> TestPlan:
        return TestPlan(
            id=m.Id, title=m.Title, code=m.Code,
            project_release_id=m.ProjectReleaseId,
            planning_date=m.PlanningDate, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: TestPlan) -> TestPlanModel:
        return TestPlanModel(
            Id=e.id, Title=e.title, Code=e.code,
            ProjectReleaseId=e.project_release_id,
            PlanningDate=e.planning_date, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class TestPlanScenarioMapper:
    @staticmethod
    def to_domain(m: TestPlanScenarioModel) -> TestPlanScenario:
        return TestPlanScenario(
            id=m.Id, test_scenario_id=m.TestScenarioId,
            test_plan_id=m.TestPlanId, ordering=m.Ordering,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: TestPlanScenario) -> TestPlanScenarioModel:
        return TestPlanScenarioModel(
            Id=e.id, TestScenarioId=e.test_scenario_id,
            TestPlanId=e.test_plan_id, Ordering=e.ordering,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class TestPlanScenarioIssueCoverageMapper:
    @staticmethod
    def to_domain(m: TestPlanScenarioIssueCoverageModel) -> TestPlanScenarioIssueCoverage:
        return TestPlanScenarioIssueCoverage(
            id=m.Id, test_plan_scenario_id=m.TestPlanScenarioId,
            issue_id=m.IssueId,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: TestPlanScenarioIssueCoverage) -> TestPlanScenarioIssueCoverageModel:
        return TestPlanScenarioIssueCoverageModel(
            Id=e.id, TestPlanScenarioId=e.test_plan_scenario_id,
            IssueId=e.issue_id, ActiveStatus=e.active_status,
            **_audit_kwargs(e))


class TestResultMapper:
    @staticmethod
    def to_domain(m: TestResultModel) -> TestResult:
        return TestResult(
            id=m.Id, test_plan_id=m.TestPlanId, test_date=m.TestDate,
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: TestResult) -> TestResultModel:
        return TestResultModel(
            Id=e.id, TestPlanId=e.test_plan_id, TestDate=e.test_date,
            Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class TestResultDetailMapper:
    @staticmethod
    def to_domain(m: TestResultDetailModel) -> TestResultDetail:
        return TestResultDetail(
            id=m.Id, test_result_id=m.TestResultId,
            test_plan_scenario_id=m.TestPlanScenarioId,
            test_approval_id=m.TestApprovalId,
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: TestResultDetail) -> TestResultDetailModel:
        return TestResultDetailModel(
            Id=e.id, TestResultId=e.test_result_id,
            TestPlanScenarioId=e.test_plan_scenario_id,
            TestApprovalId=e.test_approval_id, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))