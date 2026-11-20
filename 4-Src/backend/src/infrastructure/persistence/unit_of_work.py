from __future__ import annotations

from typing import Optional
from sqlalchemy.orm import Session

from src.domain.shared.unit_of_work import UnitOfWork

# --- Repositories ---
from src.infrastructure.persistence.repositories.basic_repository import (
    SqlAlchemyEducationLevelRepository, SqlAlchemyPriorityRepository,
    SqlAlchemyIssueTypeRepository, SqlAlchemyStatusRepository,
    SqlAlchemyResolutionRepository, SqlAlchemyMeetingTypeRepository,
    SqlAlchemyDocumentTypeRepository, SqlAlchemyFileExtensionRepository,
    SqlAlchemyStaffContractTypeRepository, SqlAlchemyTestApprovalRepository,
    SqlAlchemyTestComplexityLevelRepository, SqlAlchemyTimeUnitRepository,
    SqlAlchemyCurrencyRepository, SqlAlchemyCustomerContractTypeRepository,
)
from src.infrastructure.persistence.repositories.user_management_repository import (
    SqlAlchemyProfileRepository, SqlAlchemyGroupRepository,
    SqlAlchemyPermissionRepository, SqlAlchemyFormRepository,
)
from src.infrastructure.persistence.repositories.human_resource_repository import (
    SqlAlchemyDepartmentRepository, SqlAlchemyPositionRepository,
    SqlAlchemyHolidayRepository, SqlAlchemyAttendanceRepository,
    SqlAlchemyLeaveRepository, SqlAlchemyWorkMissionRepository,
)
from src.infrastructure.persistence.repositories.document_management_repository import (
    SqlAlchemyDocumentRepository,
)
from src.infrastructure.persistence.repositories.project_management_repository import (
    SqlAlchemyProjectRepository, SqlAlchemyIssueRepository,
    SqlAlchemyProjectMeetingRepository, SqlAlchemyWorkLogRepository,
    SqlAlchemyProjectReleaseRepository, SqlAlchemyProjectWorkflowRepository,
)
from src.infrastructure.persistence.repositories.finance_repository import (
    SqlAlchemyCustomerRepository, SqlAlchemySupplierRepository,
    SqlAlchemyStaffContractRepository, SqlAlchemyCostInvoiceRepository,
    SqlAlchemyCustomerContractRepository,
)
from src.infrastructure.persistence.repositories.quality_control_repository import (
    SqlAlchemyTestScenarioRepository, SqlAlchemyTestPlanRepository,
    SqlAlchemyTestResultRepository,
)
from src.infrastructure.persistence.repositories.evaluation_repository import (
    SqlAlchemyQuestionnaireRepository, SqlAlchemyQuestionRepository,
    SqlAlchemyQuestionnaireResultRepository,
)


class SqlAlchemyUnitOfWork(UnitOfWork):

    def __init__(self, session: Session) -> None:
        self._session = session
        self._repos: dict[str, object] = {}

    # ---------- helpers ----------
    def _get(self, key: str, factory):
        if key not in self._repos:
            self._repos[key] = factory(self._session)
        return self._repos[key]

    @property
    def session(self) -> Session:
        return self._session

    # ---------- Basic ----------
    @property
    def education_levels(self):
        return self._get("education_levels", SqlAlchemyEducationLevelRepository)
    @property
    def priorities(self):
        return self._get("priorities", SqlAlchemyPriorityRepository)
    @property
    def issue_types(self):
        return self._get("issue_types", SqlAlchemyIssueTypeRepository)
    @property
    def statuses(self):
        return self._get("statuses", SqlAlchemyStatusRepository)
    @property
    def resolutions(self):
        return self._get("resolutions", SqlAlchemyResolutionRepository)
    @property
    def meeting_types(self):
        return self._get("meeting_types", SqlAlchemyMeetingTypeRepository)
    @property
    def document_types(self):
        return self._get("document_types", SqlAlchemyDocumentTypeRepository)
    @property
    def file_extensions(self):
        return self._get("file_extensions", SqlAlchemyFileExtensionRepository)
    @property
    def staff_contract_types(self):
        return self._get("staff_contract_types", SqlAlchemyStaffContractTypeRepository)
    @property
    def test_approvals(self):
        return self._get("test_approvals", SqlAlchemyTestApprovalRepository)
    @property
    def test_complexity_levels(self):
        return self._get("test_complexity_levels", SqlAlchemyTestComplexityLevelRepository)
    @property
    def time_units(self):
        return self._get("time_units", SqlAlchemyTimeUnitRepository)
    @property
    def currencies(self):
        return self._get("currencies", SqlAlchemyCurrencyRepository)
    @property
    def customer_contract_types(self):
        return self._get("customer_contract_types", SqlAlchemyCustomerContractTypeRepository)

    # ---------- UserManagement ----------
    @property
    def profiles(self):
        return self._get("profiles", SqlAlchemyProfileRepository)
    @property
    def groups(self):
        return self._get("groups", SqlAlchemyGroupRepository)
    @property
    def permissions(self):
        return self._get("permissions", SqlAlchemyPermissionRepository)
    @property
    def forms(self):
        return self._get("forms", SqlAlchemyFormRepository)

    # ---------- HumanResource ----------
    @property
    def departments(self):
        return self._get("departments", SqlAlchemyDepartmentRepository)
    @property
    def positions(self):
        return self._get("positions", SqlAlchemyPositionRepository)
    @property
    def holidays(self):
        return self._get("holidays", SqlAlchemyHolidayRepository)
    @property
    def attendances(self):
        return self._get("attendances", SqlAlchemyAttendanceRepository)
    @property
    def leaves(self):
        return self._get("leaves", SqlAlchemyLeaveRepository)
    @property
    def work_missions(self):
        return self._get("work_missions", SqlAlchemyWorkMissionRepository)

    # ---------- DocumentManagement ----------
    @property
    def documents(self):
        return self._get("documents", SqlAlchemyDocumentRepository)

    # ---------- ProjectManagement ----------
    @property
    def projects(self):
        return self._get("projects", SqlAlchemyProjectRepository)
    @property
    def issues(self):
        return self._get("issues", SqlAlchemyIssueRepository)
    @property
    def project_meetings(self):
        return self._get("project_meetings", SqlAlchemyProjectMeetingRepository)
    @property
    def work_logs(self):
        return self._get("work_logs", SqlAlchemyWorkLogRepository)
    @property
    def project_releases(self):
        return self._get("project_releases", SqlAlchemyProjectReleaseRepository)
    @property
    def project_workflows(self):
        return self._get("project_workflows", SqlAlchemyProjectWorkflowRepository)

    # ---------- Finance ----------
    @property
    def customers(self):
        return self._get("customers", SqlAlchemyCustomerRepository)
    @property
    def suppliers(self):
        return self._get("suppliers", SqlAlchemySupplierRepository)
    @property
    def staff_contracts(self):
        return self._get("staff_contracts", SqlAlchemyStaffContractRepository)
    @property
    def cost_invoices(self):
        return self._get("cost_invoices", SqlAlchemyCostInvoiceRepository)
    @property
    def customer_contracts(self):
        return self._get("customer_contracts", SqlAlchemyCustomerContractRepository)

    # ---------- QualityControl ----------
    @property
    def test_scenarios(self):
        return self._get("test_scenarios", SqlAlchemyTestScenarioRepository)
    @property
    def test_plans(self):
        return self._get("test_plans", SqlAlchemyTestPlanRepository)
    @property
    def test_results(self):
        return self._get("test_results", SqlAlchemyTestResultRepository)

    # ---------- Evaluation ----------
    @property
    def questionnaires(self):
        return self._get("questionnaires", SqlAlchemyQuestionnaireRepository)
    @property
    def questions(self):
        return self._get("questions", SqlAlchemyQuestionRepository)
    @property
    def questionnaire_results(self):
        return self._get("questionnaire_results", SqlAlchemyQuestionnaireResultRepository)

    # ---------- UnitOfWork contract ----------
    def commit(self) -> None:
        self._session.commit()

    def rollback(self) -> None:
        self._session.rollback()

    def __enter__(self) -> "SqlAlchemyUnitOfWork":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type:
            self.rollback()
        else:
            self.commit()
        self._session.close()