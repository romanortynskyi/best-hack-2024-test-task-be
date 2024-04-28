from flask import Blueprint, request, current_app

from decorators import authenticated, timed
from modules.advertisement.advertisement_service import AdvertisementService
from request_handler import RequestHandler
from modules.advertisement.schemas.add_advertisement_request_schema import AddAdvertisementRequestSchema
from modules.advertisement.schemas.update_advertisement_request_schema import UpdateAdvertisementRequestSchema

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

@timed
@advertisement_bp.put('/<id>')
@authenticated(current_app)
def update_advertisement(user, id: int):
  advertisement_service = AdvertisementService(current_app.config['db'])

  return RequestHandler.handle_request(
    request = request,
    schema_class = UpdateAdvertisementRequestSchema,
    callback = lambda dto: advertisement_service.update_advertisement(id, dto, user['id']),
    success_status = 200,
  )

@timed
@advertisement_bp.delete('/<id>')
@authenticated(current_app)
def delete_advertisement(user, id: int):
  advertisement_service = AdvertisementService(current_app.config['db'])

  return RequestHandler.handle_request(
    request = request,
    callback = lambda: advertisement_service.delete_advertisement(id, user['id']),
    success_status = 204,
  )