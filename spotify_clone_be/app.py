import json
import os
from dotenv import load_dotenv
import logging
from logging.config import dictConfig
from flask import Flask
from werkzeug.exceptions import HTTPException
from flask_sqlalchemy import SQLAlchemy

from config import Config
from modules.auth.auth_controller import auth_bp
from modules.advertisement.advertisement_controller import advertisement_bp

dictConfig(Config.LOGGING)
LOGGER = logging.getLogger(__name__)

def create_app():
  LOGGER.debug('Configuring the app')
  app = Flask(__name__)

  app.config.from_object(Config)
  app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

  db = SQLAlchemy(app)
  app.config['db'] = db

  app.register_blueprint(auth_bp, url_prefix='/auth')
  app.register_blueprint(advertisement_bp, url_prefix='/advertisements')

  LOGGER.info(f'App started')

  return app


load_dotenv()

app = create_app()

@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    print(e)
    response.data = json.dumps({
      'message': e.message,
      'description': e.description,
    })
    response.content_type = 'application/json'
    
    return response

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
