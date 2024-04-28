from flask_sqlalchemy import SQLAlchemy

from modules.advertisement.dto.add_advertisement_request_dto import AddAdvertisementRequestDto
from models.advertisement_model import AdvertisementModel
from models.user_model import UserModel

class AdvertisementService:
  db: SQLAlchemy

  def __init__(self, db):
    self.db = db

  def _parse_advertisement(self, advertisement: AdvertisementModel):
    return {
      'id': advertisement.id,
      'firstName': advertisement.first_name,
      'lastName': advertisement.last_name,
      'phoneNumber': advertisement.phone_number,
      'city': advertisement.city,
      'description': advertisement.description,
      'user': {
        'id': advertisement.user.id,
        'firstName': advertisement.user.first_name,
        'lastName': advertisement.user.last_name,
        'email': advertisement.user.email,
        'isProvider': advertisement.user.is_provider,
        'createdAt': advertisement.user.created_at,
        'updatedAt': advertisement.user.updated_at,
      },
      'createdAt': advertisement.created_at,
      'updatedAt': advertisement.updated_at,
    }

  def add_advertisement(self, dto: AddAdvertisementRequestDto, user_id: int):
    session = self.db.session

    advertisement = AdvertisementModel(
      first_name = dto.first_name,
      last_name = dto.last_name,
      phone_number = dto.phone_number,
      city = dto.city,
      description = dto.description,
      user_id = user_id,
    )
    session.add(advertisement)
    session.commit()

    session.refresh(advertisement)

    return {
      'id': advertisement.id,
      'firstName': advertisement.first_name,
      'lastName': advertisement.last_name,
      'phoneNumber': advertisement.phone_number,
      'city': advertisement.city,
      'description': advertisement.description,
      'user': {
        'id': advertisement.user.id,
        'firstName': advertisement.user.first_name,
        'lastName': advertisement.user.last_name,
        'email': advertisement.user.email,
        'isProvider': advertisement.user.is_provider,
        'createdAt': advertisement.user.created_at,
        'updatedAt': advertisement.user.updated_at,
      },
      'createdAt': advertisement.created_at.__str__(),
      'updatedAt': advertisement.updated_at.__str__(),
    }

  def get_advertisements(self, user):
    session = self.db.session
    advertisements = session.query(
      AdvertisementModel,
    ).join(
      UserModel,
      UserModel.id == AdvertisementModel.user_id,
    ).filter(
      AdvertisementModel.user_id != user['id'],
      UserModel.is_provider != user['isProvider'],
    ).all()

    return list(map(self._parse_advertisement, advertisements))
