from sqlalchemy import Column, Integer, String, Date, Float, DateTime
from core.database import Base

class Health(Base):
    __tablename__ = "health"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    calories = Column(Integer, nullable=False)
    steps = Column(Integer, nullable=False)
    distance = Column(Float, nullable=False)
    moviment = Column(Integer, nullable=False)
    in_training = Column(String, nullable=False)  # Enum values: '0', '1'
    id_user_create = Column(Integer, nullable=False)
    create_date = Column(DateTime, nullable=False)
    id_user_update = Column(Integer, nullable=True)
    update_date = Column(DateTime, nullable=True)