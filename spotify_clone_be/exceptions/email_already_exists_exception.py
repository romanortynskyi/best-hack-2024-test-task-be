from werkzeug.exceptions import HTTPException

from enums.error_message_enum import ErrorMessageEnum

class EmailAlreadyExistsException(HTTPException):
  code = 409
  message = ErrorMessageEnum.EMAIL_ALREADY_EXISTS
  description = 'A user with the specified email address already exists.'