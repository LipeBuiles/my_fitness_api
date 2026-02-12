from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, DateTime
from core.database import Base

class ObjetivesDay(Base):
    __tablename__ = "objetives_day"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    obj_calories = Column(Integer, nullable=False)
    obj_steps = Column(Integer, nullable=False)
    obj_moviment = Column(Integer, nullable=False)
    obj_dream = Column(Float, nullable=False)
    id_user_create = Column(Integer, nullable=False)
    create_date = Column(DateTime, nullable=False)
    id_user_update = Column(Integer, nullable=True)
    update_date = Column(DateTime, nullable=True)