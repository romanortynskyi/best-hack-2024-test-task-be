from pprint import pprint
from flask_sqlalchemy import SQLAlchemy

from modules.album.dto.add_album_request_dto import AddAlbumRequestDto

class AlbumService:
  db: SQLAlchemy

  def __init__(self, db):
    self.db = db

  def add_album(self, dto: AddAlbumRequestDto):
    session = self.db.session
    pprint(dto)
    pass
