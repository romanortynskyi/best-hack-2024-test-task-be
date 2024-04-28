from werkzeug.exceptions import HTTPException

from enums.error_message_enum import ErrorMessageEnum

class ForbiddenException(HTTPException):
  code = 403
  message = ErrorMessageEnum.FORBIDDEN
  description = 'Forbidden.'
