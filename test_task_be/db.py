from flask_sqlalchemy import SQLAlchemy

class DB:
  instance: SQLAlchemy = None

  @staticmethod
  def get_instance(app = None):
    if DB.instance is None and app is not None:
      DB.instance = SQLAlchemy(app)

    return DB.instance