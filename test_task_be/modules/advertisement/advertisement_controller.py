from flask import Blueprint, request, current_app

from decorators import authenticated, timed
from modules.advertisement.advertisement_service import AdvertisementService
from request_handler import RequestHandler
from modules.advertisement.schemas.add_advertisement_request_schema import AddAdvertisementRequestSchema

advertisement_bp = Blueprint('adrvertisements', __name__)

@timed
@advertisement_bp.post('/')
@authenticated(current_app)
def add_advertisement(user):
  advertisement_service = AdvertisementService(current_app.config['db'])

  return RequestHandler.handle_request(
    request = request,
    schema_class = AddAdvertisementRequestSchema,
    callback = lambda dto: advertisement_service.add_advertisement(dto, user['id']),
    success_status = 201,
  )

@timed
@advertisement_bp.get('/')
@authenticated(current_app)
def get_advertisements(user):
  advertisement_service = AdvertisementService(current_app.config['db'])

  return RequestHandler.handle_request(
    request = request,
    callback = lambda: advertisement_service.get_advertisements(user),
    success_status = 200,
  )

@timed
@advertisement_bp.get('/<id>')
def get_advertisement_by_id(id: int):
  advertisement_service = AdvertisementService(current_app.config['db'])

  return RequestHandler.handle_request(
    request = request,
    callback = lambda: advertisement_service.get_advertisement_by_id(id),
    success_status = 200,
  )
