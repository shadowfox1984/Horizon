from sqlalchemy import Column, String, Integer, Numeric, Boolean, Date, ForeignKey, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID

from src.infrastructure.persistence.base_model import (
    Base, UUIDPrimaryKeyMixin, AuditColumnsMixin
)
from src.infrastructure.persistence.enums_pg import (
    active_status, answer_type, questionnaire_audience
)

SCHEMA = "Evaluation"


class QuestionModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Question"
    __table_args__ = {"schema": SCHEMA}
    Score = Column(Integer, nullable=False)
    Code = Column(String(20), nullable=False, unique=True)
    Question = Column(String(4000), nullable=False)
    AnswerType = answer_type
    ActiveStatus = active_status


class QuestionOptionModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "QuestionOption"
    __table_args__ = {"schema": SCHEMA}
    QuestionId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Question.Id"), nullable=False)
    Score = Column(Numeric(22, 2), nullable=False)
    Title = Column(String(4000), nullable=False)
    IsDescriptionRequired = Column(Boolean, nullable=False)
    ActiveStatus = active_status


class QuestionnaireModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "Questionnaire"
    __table_args__ = {"schema": SCHEMA}
    Title = Column(String(255), nullable=False)
    Code = Column(String(20), nullable=False, unique=True)
    ProjectId = Column(UUID(as_uuid=True), ForeignKey("ProjectManagement.Project.Id"), nullable=True)
    QuestionnaireAduience = questionnaire_audience
    TotalScore = Column(Numeric(22, 2), nullable=False)
    AcceptableScore = Column(Numeric(22, 2), nullable=False)
    WarningScore = Column(Numeric(22, 2), nullable=False)
    DisasterScore = Column(Numeric(22, 2), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class QuestionnaireTargetDepartmentModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "QuestionnaireTargetDepartment"
    __table_args__ = {"schema": SCHEMA}
    QuestionnaireId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Questionnaire.Id"), nullable=False)
    DepartmentId = Column(UUID(as_uuid=True), ForeignKey("HumanResource.Department.Id"), nullable=False)
    ActiveStatus = active_status


class QuestionnaireItemModel(Base, UUIDPrimaryKeyMixin):
    __tablename__ = "QuestionnaireItem"
    __table_args__ = {"schema": SCHEMA}
    QuestionnaireId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Questionnaire.Id"), nullable=False)
    QuestionId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Question.Id"), nullable=False)
    IsActive = Column(Boolean, nullable=False, server_default="true")
    IsDeleted = Column(Boolean, nullable=False, server_default="false")
    CreateDate = Column(Date, server_default="now()")
    CreatorId = Column(UUID(as_uuid=True), nullable=False)
    ModifyDate = Column(Date)
    ModifierId = Column(UUID(as_uuid=True))


class QuestionnaireResultModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "QuestionnaireResult"
    __table_args__ = {"schema": SCHEMA}
    QuestionnaireId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.Questionnaire.Id"), nullable=False)
    ProfileId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Profile.Id"), nullable=True)
    CustomerId = Column(UUID(as_uuid=True), ForeignKey("Finance.Customer.Id"), nullable=True)
    QuestionnaireDate = Column(Date)
    TotalScore = Column(Numeric(22, 2), nullable=False)
    ActiveStatus = active_status


class QuestionnaireResultDetailModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "QuestionnaireResultDetail"
    __table_args__ = {"schema": SCHEMA}
    QuestionnaireResultId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.QuestionnaireResult.Id"), nullable=False)
    QuestionnaireItemId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.QuestionnaireItem.Id"), nullable=False)
    ChoosedQuestionOptionId = Column(UUID(as_uuid=True), ForeignKey(f"{SCHEMA}.QuestionOption.Id"), nullable=True)
    Description = Column(String(4000))
    ActiveStatus = active_status


class StaffSatisfactionEvaluationModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "StaffSatisfactionEvaluation"
    __table_args__ = (
        CheckConstraint("EvaluatedValue BETWEEN 0 AND 100", name="chk_staff_eval_value"),
        {"schema": SCHEMA},
    )
    ProfileId = Column(UUID(as_uuid=True), ForeignKey("UserManagement.Profile.Id"), nullable=False)
    EvalationDate = Column(Date, nullable=False)
    EvaluatedValue = Column(Numeric(3, 2), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class ProjectProductivityEvaluationModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "ProjectProductivityEvaluation"
    __table_args__ = (
        CheckConstraint("EvaluatedValue BETWEEN 0 AND 100", name="chk_project_eval_value"),
        {"schema": SCHEMA},
    )
    ProjectId = Column(UUID(as_uuid=True), ForeignKey("ProjectManagement.Project.Id"), nullable=False)
    EvalationDate = Column(Date, nullable=False)
    EvaluatedValue = Column(Numeric(3, 2), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class CustomerSatisfactionEvaluationModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "CustomerSatisfactionEvaluation"
    __table_args__ = (
        CheckConstraint("EvaluatedValue BETWEEN 0 AND 100", name="chk_customer_sat_value"),
        {"schema": SCHEMA},
    )
    CustomerId = Column(UUID(as_uuid=True), ForeignKey("Finance.Customer.Id"), nullable=False)
    ProjectId = Column(UUID(as_uuid=True), ForeignKey("ProjectManagement.Project.Id"), nullable=False)
    EvalationDate = Column(Date, nullable=False)
    EvaluatedValue = Column(Numeric(3, 2), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status


class CustomerFeedbackModel(Base, UUIDPrimaryKeyMixin, AuditColumnsMixin):
    __tablename__ = "CustomerFeedback"
    __table_args__ = (
        CheckConstraint("FeedbackValue BETWEEN 0 AND 10", name="chk_customer_feedback_value"),
        {"schema": SCHEMA},
    )
    CustomerId = Column(UUID(as_uuid=True), ForeignKey("Finance.Customer.Id"), nullable=False)
    ProjectId = Column(UUID(as_uuid=True), ForeignKey("ProjectManagement.Project.Id"), nullable=False)
    FeedbackDate = Column(Date, nullable=False)
    FeedbackValue = Column(Numeric(2, 2), nullable=False)
    Description = Column(String(4000))
    ActiveStatus = active_status