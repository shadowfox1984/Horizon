from dataclasses import dataclass, field
from datetime import date
from typing import Optional
from uuid import UUID, uuid4

from ..shared.enums import (
    ActiveStatus, AnswerType, QuestionnaireAudience
)
from ..shared.value_objects import AuditInfo


@dataclass
class Question:
    score: int
    code: str
    question: str
    answer_type: AnswerType
    id: UUID = field(default_factory=uuid4)
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class QuestionOption:
    question_id: UUID
    score: float
    title: str
    is_description_required: bool
    id: UUID = field(default_factory=uuid4)
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class Questionnaire:
    title: str
    code: str
    questionnaire_audience: QuestionnaireAudience
    total_score: float
    acceptable_score: float
    warning_score: float
    disaster_score: float
    id: UUID = field(default_factory=uuid4)
    project_id: Optional[UUID] = None
    description: Optional[str] = None
    active_status: ActiveStatus = ActiveStatus.ACTIVE
    audit: Optional[AuditInfo] = None


@dataclass
class QuestionnaireTargetDepartment:
    questionnaire_id: UUID
    department_id: UUID
    id: UUID = field(default_factory=uuid4