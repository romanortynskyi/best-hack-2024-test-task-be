from marshmallow import Schema, fields, post_load

from modules.auth.dto.update_user_request_dto import UpdateUserRequestDto
from dto.add_song_request_dto import AddSongRequestDto

class AddSongRequestSchema(Schema):
  name = fields.String(required = True, validate = fields.Length(min = 1, max = 256))
  featured_artist_ids = fields.List(fields.Integer(required = True), required = True)
  
  @post_load
  def make_add_song_request_dto(self, data, **kwargs):
    return AddSongRequestDto(**data)
