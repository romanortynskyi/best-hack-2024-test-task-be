from http.client import HTTPException
from flask import Request, jsonify
from marshmallow import ValidationError

from enums.error_message_enum import ErrorMessageEnum

class RequestHandler:
  @staticmethod
  def handle_request(
    request: Request,
    callback,
    success_status: int,
    schema_class = None,
  ):
    try:
      if schema_class is None:
        result = callback()

      else:
        dto = schema_class().load(request.get_json())
        result = callback(dto)

      return jsonify(result), success_status

    except ValidationError as error:
      first_message_key = list(error.messages.keys())[0]

      return jsonify({
        'message': ErrorMessageEnum.INVALID_PAYLOAD.value,
        'description': error.messages[first_message_key][0],
        'location': first_message_key,
      }), 400
    
    except HTTPException as exception:
      return jsonify({
        'message': exception.message,
        'description': exception.description,
      }), exception.code
