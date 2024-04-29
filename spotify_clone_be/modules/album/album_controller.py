from flask import Blueprint, request, current_app

from decorators import authenticated, timed
from request_handler import RequestHandler
from modules.album.schemas.add_album_request_schema import AddAlbumRequestSchema
from modules.album.album_service import AlbumService

album_bp = Blueprint('album', __name__)

@timed
@album_bp.post('/')
@authenticated(current_app)
def add_album(user):
  album_service = AlbumService(current_app.config['db'])

  return RequestHandler.handle_request(
    request = request,
    schema_class = AddAlbumRequestSchema,
    callback = lambda dto: album_service.add_album(dto, user['id']),
    success_status = 201,
  )
