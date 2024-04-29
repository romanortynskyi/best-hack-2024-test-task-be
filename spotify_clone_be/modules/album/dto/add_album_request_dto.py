from datetime import datetime

from enums.album_type_enum import AlbumTypeEnum

class AddAlbumRequestDto:
  name: str
  released_at: datetime
  type: AlbumTypeEnum
  

  def __init__(self, name, released_at, type):
    self.name = name
    self.released_at = released_at
    self.type = type
