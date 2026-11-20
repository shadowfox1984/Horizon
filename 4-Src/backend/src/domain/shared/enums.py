from enum import Enum


class ActiveStatus(Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    DELETED = "Deleted"


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"


class Weekday(Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class EnteranceType(Enum):
    ENTER = "Enter"
    EXIT = "Exit"


class IssueSize(Enum):
    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"


class LeaveType(Enum):
    FULL_DAY = "FullDay"
    PART_OF_DAY = "PartOfDay"


class CalculationType(Enum):
    PERCENTAGE = "Percentage"
    FIXED_AMOUNT = "FixedAmount"


class StatusLevel(Enum):
    TO_DO = "To Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"


class HolidayType(Enum):
    NATIONAL = "National"
    GOVERNMENT_OR_FEDERAL = "GovernmentOrFederal"
    PROVINCIAL_OR_STATE = "ProvincialOrState"
    ORGANIZATIONAL = "Organizational"


class LinkedIssueType(Enum):
    BLOCKS = "Blocks"
    RELATES_TO = "RelatesTo"
    DUPLICATES = "Duplicates"
    CLONES = "Clones"


class QuestionnaireAudience(Enum):
    STAFFS = "Staffs"
    CUSTOMERS = "Customers"
    STAKEHOLDERS = "Stackholders"
    SENIOR_MANAGERS = "SeniorManagers"


class AnswerType(Enum):
    SINGLE_CHOICE = "SignleChoice"
    MULTI_CHOICE = "MultiChoice"
    DESCRIPTION = "Description"


class IssueChangeType(Enum):
    UPDATE_DATE = "UpdateDate"
    CHANGE_STATUS = "ChangeStatus"
    CHANGE_RESOLUTION = "ChangeResolution"
    DEACTIVATION = "Deactivation"
    ACTIVATION = "Activation"
    CHANGE_ASSIGNEE = "ChangeAssignee"
    MOVE_TO_ANOTHER_PROJECT = "MoveToAnotherProject"