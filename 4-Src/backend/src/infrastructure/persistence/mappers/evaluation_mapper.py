from src.domain.evaluation.entities import (
    Question, QuestionOption, Questionnaire,
    QuestionnaireTargetDepartment, QuestionnaireItem,
    QuestionnaireResult, QuestionnaireResultDetail,
    StaffSatisfactionEvaluation, ProjectProductivityEvaluation,
    CustomerSatisfactionEvaluation, CustomerFeedback,
)
from src.domain.shared.enums import AnswerType, QuestionnaireAudience
from src.infrastructure.persistence.models.evaluation import (
    QuestionModel, QuestionOptionModel, QuestionnaireModel,
    QuestionnaireTargetDepartmentModel, QuestionnaireItemModel,
    QuestionnaireResultModel, QuestionnaireResultDetailModel,
    StaffSatisfactionEvaluationModel, ProjectProductivityEvaluationModel,
    CustomerSatisfactionEvaluationModel, CustomerFeedbackModel,
)
from ._helpers import audit_from_model, active_from_model


def _audit_kwargs(e):
    if e.audit:
        return dict(
            CreatorId=e.audit.creator_id, CreateDate=e.audit.create_date,
            ModifierId=e.audit.modifier_id, ModifyDate=e.audit.modify_date,
        )
    return {}


def _enum(cls, raw):
    if raw is None:
        return None
    return cls(raw.value if hasattr(raw, "value") else raw)


class QuestionMapper:
    @staticmethod
    def to_domain(m: QuestionModel) -> Question:
        return Question(
            id=m.Id, score=m.Score, code=m.Code, question=m.Question,
            answer_type=_enum(AnswerType, m.AnswerType),
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: Question) -> QuestionModel:
        return QuestionModel(
            Id=e.id, Score=e.score, Code=e.code, Question=e.question,
            AnswerType=e.answer_type, ActiveStatus=e.active_status,
            **_audit_kwargs(e))


class QuestionOptionMapper:
    @staticmethod
    def to_domain(m: QuestionOptionModel) -> QuestionOption:
        return QuestionOption(
            id=m.Id, question_id=m.QuestionId, score=float(m.Score),
            title=m.Title, is_description_required=m.IsDescriptionRequired,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: QuestionOption) -> QuestionOptionModel:
        return QuestionOptionModel(
            Id=e.id, QuestionId=e.question_id, Score=e.score, Title=e.title,
            IsDescriptionRequired=e.is_description_required,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class QuestionnaireMapper:
    @staticmethod
    def to_domain(m: QuestionnaireModel) -> Questionnaire:
        return Questionnaire(
            id=m.Id, title=m.Title, code=m.Code,
            questionnaire_audience=_enum(QuestionnaireAudience, m.QuestionnaireAduience),
            total_score=float(m.TotalScore),
            acceptable_score=float(m.AcceptableScore),
            warning_score=float(m.WarningScore),
            disaster_score=float(m.DisasterScore),
            project_id=m.ProjectId, description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: Questionnaire) -> QuestionnaireModel:
        return QuestionnaireModel(
            Id=e.id, Title=e.title, Code=e.code,
            QuestionnaireAduience=e.questionnaire_audience,
            TotalScore=e.total_score, AcceptableScore=e.acceptable_score,
            WarningScore=e.warning_score, DisasterScore=e.disaster_score,
            ProjectId=e.project_id, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class QuestionnaireTargetDepartmentMapper:
    @staticmethod
    def to_domain(m: QuestionnaireTargetDepartmentModel) -> QuestionnaireTargetDepartment:
        return QuestionnaireTargetDepartment(
            id=m.Id, questionnaire_id=m.QuestionnaireId,
            department_id=m.DepartmentId,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: QuestionnaireTargetDepartment) -> QuestionnaireTargetDepartmentModel:
        return QuestionnaireTargetDepartmentModel(
            Id=e.id, QuestionnaireId=e.questionnaire_id,
            DepartmentId=e.department_id,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class QuestionnaireItemMapper:
    @staticmethod
    def to_domain(m: QuestionnaireItemModel) -> QuestionnaireItem:
        return QuestionnaireItem(
            id=m.Id, questionnaire_id=m.QuestionnaireId,
            question_id=m.QuestionId,
            is_active=m.IsActive, is_deleted=m.IsDeleted,
            create_date=m.CreateDate, creator_id=m.CreatorId,
            modify_date=m.ModifyDate, modifier_id=m.ModifierId)
    @staticmethod
    def to_model(e: QuestionnaireItem) -> QuestionnaireItemModel:
        return QuestionnaireItemModel(
            Id=e.id, QuestionnaireId=e.questionnaire_id,
            QuestionId=e.question_id,
            IsActive=e.is_active, IsDeleted=e.is_deleted,
            CreateDate=e.create_date, CreatorId=e.creator_id,
            ModifyDate=e.modify_date, ModifierId=e.modifier_id)


class QuestionnaireResultMapper:
    @staticmethod
    def to_domain(m: QuestionnaireResultModel) -> QuestionnaireResult:
        return QuestionnaireResult(
            id=m.Id, questionnaire_id=m.QuestionnaireId,
            profile_id=m.ProfileId, customer_id=m.CustomerId,
            questionnaire_date=m.QuestionnaireDate,
            total_score=float(m.TotalScore),
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: QuestionnaireResult) -> QuestionnaireResultModel:
        return QuestionnaireResultModel(
            Id=e.id, QuestionnaireId=e.questionnaire_id,
            ProfileId=e.profile_id, CustomerId=e.customer_id,
            QuestionnaireDate=e.questionnaire_date,
            TotalScore=e.total_score,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class QuestionnaireResultDetailMapper:
    @staticmethod
    def to_domain(m: QuestionnaireResultDetailModel) -> QuestionnaireResultDetail:
        return QuestionnaireResultDetail(
            id=m.Id, questionnaire_result_id=m.QuestionnaireResultId,
            questionnaire_item_id=m.QuestionnaireItemId,
            choosed_question_option_id=m.ChoosedQuestionOptionId,
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: QuestionnaireResultDetail) -> QuestionnaireResultDetailModel:
        return QuestionnaireResultDetailModel(
            Id=e.id, QuestionnaireResultId=e.questionnaire_result_id,
            QuestionnaireItemId=e.questionnaire_item_id,
            ChoosedQuestionOptionId=e.choosed_question_option_id,
            Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class StaffSatisfactionEvaluationMapper:
    @staticmethod
    def to_domain(m: StaffSatisfactionEvaluationModel) -> StaffSatisfactionEvaluation:
        return StaffSatisfactionEvaluation(
            id=m.Id, profile_id=m.ProfileId, evalation_date=m.EvalationDate,
            evaluated_value=float(m.EvaluatedValue),
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: StaffSatisfactionEvaluation) -> StaffSatisfactionEvaluationModel:
        return StaffSatisfactionEvaluationModel(
            Id=e.id, ProfileId=e.profile_id, EvalationDate=e.evalation_date,
            EvaluatedValue=e.evaluated_value, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class ProjectProductivityEvaluationMapper:
    @staticmethod
    def to_domain(m: ProjectProductivityEvaluationModel) -> ProjectProductivityEvaluation:
        return ProjectProductivityEvaluation(
            id=m.Id, project_id=m.ProjectId, evalation_date=m.EvalationDate,
            evaluated_value=float(m.EvaluatedValue),
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: ProjectProductivityEvaluation) -> ProjectProductivityEvaluationModel:
        return ProjectProductivityEvaluationModel(
            Id=e.id, ProjectId=e.project_id, EvalationDate=e.evalation_date,
            EvaluatedValue=e.evaluated_value, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class CustomerSatisfactionEvaluationMapper:
    @staticmethod
    def to_domain(m: CustomerSatisfactionEvaluationModel) -> CustomerSatisfactionEvaluation:
        return CustomerSatisfactionEvaluation(
            id=m.Id, customer_id=m.CustomerId, project_id=m.ProjectId,
            evalation_date=m.EvalationDate,
            evaluated_value=float(m.EvaluatedValue),
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: CustomerSatisfactionEvaluation) -> CustomerSatisfactionEvaluationModel:
        return CustomerSatisfactionEvaluationModel(
            Id=e.id, CustomerId=e.customer_id, ProjectId=e.project_id,
            EvalationDate=e.evalation_date,
            EvaluatedValue=e.evaluated_value, Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))


class CustomerFeedbackMapper:
    @staticmethod
    def to_domain(m: CustomerFeedbackModel) -> CustomerFeedback:
        return CustomerFeedback(
            id=m.Id, customer_id=m.CustomerId, project_id=m.ProjectId,
            feedback_date=m.FeedbackDate,
            feedback_value=float(m.FeedbackValue),
            description=m.Description,
            active_status=active_from_model(m), audit=audit_from_model(m))
    @staticmethod
    def to_model(e: CustomerFeedback) -> CustomerFeedbackModel:
        return CustomerFeedbackModel(
            Id=e.id, CustomerId=e.customer_id, ProjectId=e.project_id,
            FeedbackDate=e.feedback_date, FeedbackValue=e.feedback_value,
            Description=e.description,
            ActiveStatus=e.active_status, **_audit_kwargs(e))