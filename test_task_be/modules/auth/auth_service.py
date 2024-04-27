import os
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

from exceptions.email_already_exists_exception import EmailAlreadyExistsException
from modules.auth.dto.sign_up_request_dto import SignUpRequestDto
from models.user_model import UserModel
from exceptions.wrong_credentials_exception import WrongCredentialsException
from modules.auth.dto.login_request_dto import LoginRequestDto
from exceptions.invalid_token_exception import InvalidTokenException

class AuthService:
  db: SQLAlchemy

  def __init__(self, db):
    self.db = db

  def signup(self, dto: SignUpRequestDto):
    session = self.db.session

    user_by_email = session.query(UserModel).filter(UserModel.email == dto.email).first()

    if user_by_email is not None:
      raise EmailAlreadyExistsException()
    
    password = generate_password_hash(dto.password)
    
    user = UserModel(
      first_name = dto.first_name,
      last_name = dto.last_name,
      email = dto.email,
      password = password,
      is_provider = dto.is_provider,
    )
    session.add(user)
    session.commit()

    session.refresh(user)

    user_dict = {
      'id': user.id,
      'firstName': user.first_name,
      'lastName': user.last_name,
      'email': user.email,
      'isProvider': user.is_provider,
      'createdAt': user.created_at.__str__(),
      'updatedAt': user.updated_at.__str__(),
    }

    token = jwt.encode(user_dict, os.environ.get('JWT_SECRET_KEY'), algorithm = 'HS256')

    return {
      **user_dict,
      'token': token,
    }

  def login(self, dto: LoginRequestDto):
    session = self.db.session

    user = session.query(UserModel).filter(UserModel.email == dto.email).first()

    if user is None:
      raise WrongCredentialsException()

    password_is_correct = check_password_hash(user.password, dto.password)

    if not password_is_correct:
      raise WrongCredentialsException()
    
    user_dict = {
      'id': user.id,
      'firstName': user.first_name,
      'lastName': user.last_name,
      'email': user.email,
      'isProvider': user.is_provider,
      'createdAt': user.created_at.__str__(),
      'updatedAt': user.updated_at.__str__(),
    }

    token = jwt.encode(user_dict, os.environ.get('JWT_SECRET_KEY'), algorithm = 'HS256')

    return {
      **user_dict,
      'token': token,
    }

  def get_user_by_token(self, bearer_token: str):
    session = self.db.session

    _, token = bearer_token.split(' ')

    try:
      id = jwt.decode(token, os.environ.get('JWT_SECRET_KEY'), algorithms=['HS256'])['id']

      user = session.get(UserModel, id)

      if user is None:
        raise InvalidTokenException()

      return {
        'id': id,
        'firstName': user.first_name,
        'lastName': user.last_name,
        'email': user.email,
        'isProvider': user.is_provider,
        'createdAt': user.created_at.__str__(),
        'updatedAt': user.updated_at.__str__(),
      }
    
    except jwt.exceptions.DecodeError:
      raise InvalidTokenException()
