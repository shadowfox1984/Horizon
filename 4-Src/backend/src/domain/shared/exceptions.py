# src/domain/shared/exceptions.py

class BusinessException(Exception):
    def __init__(self, error_code: int, message: str, http_status: int = 400):
        self.error_code = error_code
        self.message = message
        self.http_status = http_status
        super().__init__(message)

class ErrorCodes:
    # Unauthorized Errors
    INVALID_CREDENTIALS = (401001, "Username or password is incorrect.", 401)
    ACCESS_DENIED = (401002, "Access denied.", 403)
    TOKEN_EXPIRED = (401003, "The user token is expired.", 401)
    CAPTCHA_MISMATCH = (401004, "Inserted code is not match with CAPTCHA.", 400)
    USER_LOCKED = (401005, "The user account has been locked due to more than 5 unauthorized login attempts. Please contact the administrator.", 401)
    TOKEN_INCORRECT = (401006, "The user token is incorrect.", 401)
    SESSION_EXPIRED = (401007, "Your session has expired. Please log in again to continue.", 401)
    SESSION_TERMINATED = (401008, "The session has been terminated. Token refresh is not permitted. Please authenticate again to continue.", 401)
    OLD_PASSWORD_INCORRECT = (401009, "The old password is incorrect.", 400)
    
    # General Errors
    RECORD_NOT_FOUND = (701001, "Record not found", 404)
    CODE_EXISTS = (701002, "The code already exists", 400)
    INVALID_COLOR_FORMAT = (701007, "Color hex code is not valid.", 400)
    ORDERING_DUPLICATED = (701008, "Ordering number is duplicated.", 400)
    CASCADE_DELETE_ERROR = (701009, "System cannot delete a record with cascade data.", 400)
    ALREADY_ACTIVE = (701010, "The record is already activated.", 400)
    ALREADY_INACTIVE = (701011, "The record is already inactivated.", 400)
    NO_DATA_FOUND = (701012, "The request has no data.", 404)

    # User Management Errors
    PASSWORD_FORMAT_INVALID = (703001, "Password format is not touched.", 400)
    USERNAME_EXISTS = (703002, "Username already exists.", 400)
    PROFILE_PERMISSION_EXISTS = (703003, "Selected permission is already assigned to the profile.", 400)
    GROUP_PERMISSION_EXISTS = (703005, "Selected permission is already assigned to the group.", 400)
    PROFILE_GROUP_EXISTS = (703007, "The profile is already assigned to the group.", 400)
    PROFILE_DEACTIVATED = (703008, "The profile is deactivated.", 400)
    GROUP_DEACTIVATED = (703010, "The group is deactivated.", 400)
    PASSWORD_MISMATCH = (703011, "Password confirmation does not match the new password.", 400)
    ACTIVATION_DATE_INVALID = (703012, "The activation date and time must be later than the current system date and time.", 400)
    PROFILE_NOT_EXIST = (703013, "The profile does not exist.", 404)
    GROUP_NOT_EXIST = (703014, "The group does not exist.", 404)
    PERMISSION_NOT_EXIST = (703015, "The permission does not exist.", 404)
    PERMISSION_DEACTIVATED = (703016, "The permission is deactivated.", 400)

    # Basic Data Errors
    STATUS_EFFECT_INCORRECT = (702001, "Status effect is incorrect.", 400)
    FILE_EXTENSION_DUPLICATED = (702002, "File extension is duplicated", 400)
    CURRENCY_SYMBOL_UPPERCASE = (702003, "Symbol of the currency should be included just upper case alphabets.", 400)
    TEST_COMPLEXITY_DUPLICATED = (702004, "The value number of test complexity level is duplicated.", 400)
    CURRENCY_SYMBOL_DUPLICATED = (702005, "Symbol of the currency is duplicated.", 400)