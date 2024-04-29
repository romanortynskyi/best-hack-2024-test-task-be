from enum import Enum

class AlbumTypeEnum(str, Enum):
  LONG_PLAY = 'LONG_PLAY'
  EXTENDED_PLAY = 'EXTENDED_PLAY'
  SINGLE = 'SINGLE'
