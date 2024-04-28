from marshmallow import Schema, fields, post_load

from modules.advertisement.dto.add_advertisement_request_dto import AddAdvertisementRequestDto

class AddAdvertisementRequestSchema(Schema):
  first_name = fields.String(data_key = 'firstName', required = True)
  last_name = fields.String(data_key = 'lastName', required = True)
  phone_number = fields.String(data_key = 'phoneNumber', required = True)
  city = fields.String(data_key = 'city', required = True)
  description = fields.String(data_key = 'description', required = True)

  @post_load
  def make_sign_up_request_dto(self, data, **kwargs):
    return AddAdvertisementRequestDto(**data)
