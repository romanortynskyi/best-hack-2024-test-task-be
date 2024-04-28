from sqlalchemy import Column, DateTime, Integer, String, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base_model import BaseModel

class AdvertisementModel(BaseModel):
  __tablename__ = 'advertisements'

  id: Mapped[int] = Column(Integer, primary_key = True)
  created_at = Column(DateTime(timezone = True), server_default = func.now())
  updated_at = Column(
    DateTime(timezone = True),
    server_default = func.now(),
    onupdate = func.now(),
  )

  first_name = Column(String(255), nullable = False)
  last_name = Column(String(255), nullable = False)
  phone_number = Column(String(255), nullable = False)
  city = Column(String(255), nullable = False)
  description = Column(String(255), nullable = False)
  user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
  user: Mapped['UserModel'] = relationship(back_populates = 'advertisements')
