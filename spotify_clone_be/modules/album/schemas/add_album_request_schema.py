from marshmallow import Schema, fields, post_load

from modules.auth.dto.login_request_dto import LoginRequestDto
from modules.album.dto.add_album_request_dto import AddAlbumRequestDto
from enums.album_type_enum import AlbumTypeEnum
from schemas.add_song_request_schema import AddSongRequestSchema

class AddAlbumRequestSchema(Schema):
  name = fields.Str(required = True, validate = fields.Length(min = 1, max = 256))
  released_at = fields.Date(data_key = 'releasedAt', required = True)
  type = fields.Enum(enum = AlbumTypeEnum, required = True)
  songs = fields.List(fields.Nested(AddSongRequestSchema), required = True)

  @post_load
  def make_add_album_request_dto(self, data, **kwargs):
    return AddAlbumRequestDto(**data)
