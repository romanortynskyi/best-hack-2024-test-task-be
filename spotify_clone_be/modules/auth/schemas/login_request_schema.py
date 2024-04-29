from marshmallow import Schema, fields, post_load

from modules.auth.dto.login_request_dto import LoginRequestDto

class LoginRequestSchema(Schema):
  email = fields.Email(required = True)
  password = fields.String(required = True, validate = fields.Length(min = 6))
  
  @post_load
  def make_sign_up_request_dto(self, data, **kwargs):
    return LoginRequestDto(**data)
