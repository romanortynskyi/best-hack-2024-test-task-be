from flask import Blueprint, request, current_app

from decorators import authenticated, timed
from modules.auth.auth_service import AuthService
from modules.auth.schemas.sign_up_request_schema import SignUpRequestSchema
from modules.auth.schemas.login_request_schema import LoginRequestSchema
from request_handler import RequestHandler
from modules.auth.schemas.update_user_request_schema import UpdateUserRequestSchema

auth_bp = Blueprint('auth', __name__)

@timed
@auth_bp.post('/signup')
def signup():
  auth_service = AuthService(current_app.config['db'])

  return RequestHandler.handle_request(
    request = request,
    schema_class = SignUpRequestSchema,
    callback = lambda dto: auth_service.signup(dto),
    success_status = 201,
  )

@timed
@auth_bp.post('/login')
def login():
  auth_service = AuthService(current_app.config['db'])

  return RequestHandler.handle_request(
    request = request,
    schema_class = LoginRequestSchema,
    callback = lambda dto: auth_service.login(dto),
    success_status = 200,
  )

@timed
@auth_bp.get('/me')
def get_me():
  auth_service = AuthService(current_app.config['db'])

  return RequestHandler.handle_request(
    request = request,
    callback = lambda: auth_service.get_user_by_token(request.headers.get('Authorization')),
    success_status = 200,
  )

@timed
@auth_bp.put('/me')
@authenticated(current_app)
def update_me(user):
  auth_service = AuthService(current_app.config['db'])

  return RequestHandler.handle_request(
    request = request,
    schema_class = UpdateUserRequestSchema,
    callback = lambda dto: auth_service.update_user(user['id'], dto),
    success_status = 200,
  )
