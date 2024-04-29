import json
from dotenv import load_dotenv
import logging
from logging.config import dictConfig
from flask import Flask
from werkzeug.exceptions import HTTPException

from config import Config
from modules.auth.auth_controller import auth_bp
from db import DB

dictConfig(Config.LOGGING)
LOGGER = logging.getLogger(__name__)

def create_app():
  LOGGER.debug('Configuring the app')
  app = Flask(__name__)

  app.config.from_object(Config)

  app.register_blueprint(auth_bp, url_prefix='/auth')

  LOGGER.info('App started')

  return app


load_dotenv()

app = create_app()
db = DB.get_instance(app)

@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    
    response.data = json.dumps({
      'message': e.message,
      'description': e.description,
    })
    response.content_type = 'application/json'
    
    return response

if __name__ == '__main__':
    db.init_app(app)
    db.create_all()
    
    app.run()
