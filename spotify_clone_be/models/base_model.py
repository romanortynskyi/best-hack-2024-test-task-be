from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.sql import func

class BaseModel(DeclarativeBase):
  __abstract__ = True

  id: Mapped[int] = Column(Integer, primary_key = True)
  created_at = Column(DateTime(timezone = True), server_default = func.now())
  updated_at = Column(
    DateTime(timezone = True),
    server_default = func.now(),
    onupdate = func.now(),
  )
