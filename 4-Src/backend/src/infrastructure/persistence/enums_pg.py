from sqlalchemy import Enum as SAEnum
from src.domain.shared import enums as de

def pg_enum(enum_cls, name: str, create_type: bool = False) -> SAEnum:
    return SAEnum(
        enum_cls,
        name=name,
        create_type=create_type,
        values_callable=lambda x: [e.value for e in x],
        native_enum=True,
    )

active_status = pg_enum(de.ActiveStatus, "activeStatusEnum")
gender = pg_enum(de.Gender, "genderEnum")
weekday = pg_enum(de.Weekday, "weekdayEnum")
enterance_type = pg_enum(de.EnteranceType, "enteranceTypeEnum")
issue_size = pg_enum(de.IssueSize, "issueSizeEnum")
leave_type = pg_enum(de.LeaveType, "leaveTypeEnum")
calculation_type = pg_enum(de.CalculationType, "calculationTypeEnum")
status_level = pg_enum(de.StatusLevel, "statusLevelEnum")
holiday_type = pg_enum(de.HolidayType, "holidayTypeEnum")
linked_issue_type = pg_enum(de.LinkedIssueType, "linkedIssueTypeEnum")
questionnaire_audience = pg_enum(de.QuestionnaireAudience, "questionnaireAduienceEnum")
answer_type = pg_enum(de.AnswerType, "answerTypeEnum")
issue_change_type = pg_enum(de.IssueChangeType, "issueChangeTypeEnum")