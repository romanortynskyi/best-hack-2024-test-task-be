from werkzeug.exceptions import HTTPException

from enums.error_message_enum import ErrorMessageEnum

class WrongCredentialsException(HTTPException):
  code = 401
  message = ErrorMessageEnum.WRONG_CREDENTIALS
  description = 'The provided email or password is incorrect.'
