from sqlalchemy import Column, DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped

from models.base_model import BaseModel

class UserModel(BaseModel):
  __tablename__ = 'users'

  id: Mapped[int] = Column(Integer, primary_key = True)
  created_at = Column(DateTime(timezone = True), server_default = func.now())
  updated_at = Column(
    DateTime(timezone = True),
    server_default = func.now(),
    onupdate = func.now(),
  )

  first_name = Column(String(255), nullable = False)
  last_name = Column(String(255), nullable = False)
  email = Column(
    String(120),
    unique = True,
    nullable = False,
  )
  password = Column(Text, nullable = False)
