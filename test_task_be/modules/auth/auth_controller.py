from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from decorators import timed
from modules.auth.auth_service import AuthService
from modules.auth.schemas.sign_up_request_schema import SignUpRequestSchema
from modules.auth.schemas.login_request_schema import LoginRequestSchema
from request_handler import RequestHandler

auth_bp = Blueprint('auth', __name__)

auth_service = AuthService()

@timed
@auth_bp.post('/signup')
def signup():
  return RequestHandler.handle_request(
    request = request,
    schema_class = SignUpRequestSchema,
    callback = lambda dto: auth_service.signup(dto),
    success_status = 201,
  )

@timed
@auth_bp.post('/login')
def login():
  return RequestHandler.handle_request(
    request = request,
    schema_class = LoginRequestSchema,
    callback = lambda dto: auth_service.login(dto),
    success_status = 200,
  )

@timed
@auth_bp.get('/me')
def get_me():
  return RequestHandler.handle_request(
    request = request,
    callback = lambda: auth_service.get_user_by_token(request.headers.get('Authorization')),
    success_status = 200,
  )
