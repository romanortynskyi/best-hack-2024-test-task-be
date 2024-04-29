from marshmallow import Schema, fields, post_load

from modules.auth.dto.update_user_request_dto import UpdateUserRequestDto

class UpdateUserRequestSchema(Schema):
  email = fields.Email(required = True)
  first_name = fields.String(data_key = 'firstName', required = True)
  last_name = fields.String(data_key = 'lastName', required = True)
  is_provider = fields.Boolean(data_key = 'isProvider', required = True)

  @post_load
  def make_sign_up_request_dto(self, data, **kwargs):
    return UpdateUserRequestDto(**data)
