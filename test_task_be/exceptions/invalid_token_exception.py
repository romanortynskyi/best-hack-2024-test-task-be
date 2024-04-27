from werkzeug.exceptions import HTTPException

from enums.error_message_enum import ErrorMessageEnum

class InvalidTokenException(HTTPException):
  code = 401
  message = ErrorMessageEnum.INVALID_TOKEN
  description = 'The provided token is invalid.'
