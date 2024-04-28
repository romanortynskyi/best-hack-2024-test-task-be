from werkzeug.exceptions import HTTPException

from enums.error_message_enum import ErrorMessageEnum

class AdvertisementNotFoundException(HTTPException):
  code = 404
  message = ErrorMessageEnum.ADVERTISEMENT_NOT_FOUND
  description = 'An advertisement with the specified id does not exist.'
