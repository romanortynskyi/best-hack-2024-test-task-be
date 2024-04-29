from marshmallow import Schema, fields, post_load

from modules.auth.dto.sign_up_request_dto import SignUpRequestDto

class SignUpRequestSchema(Schema):
  email = fields.Email(required = True)
  password = fields.String(required = True, validate = fields.Length(min = 6))
  first_name = fields.String(data_key = 'firstName', required = True)
  last_name = fields.String(data_key = 'lastName', required = True)

  @post_load
  def make_sign_up_request_dto(self, data, **kwargs):
    return SignUpRequestDto(**data)
