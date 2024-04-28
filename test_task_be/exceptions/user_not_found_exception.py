from werkzeug.exceptions import HTTPException

from enums.error_message_enum import ErrorMessageEnum

class UserNotFoundException(HTTPException):
  code = 404
  message = ErrorMessageEnum.USER_NOT_FOUND
  description = 'A user with the specified id does not exist.'
