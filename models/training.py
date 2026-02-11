from sqlalchemy import Column, Integer, String, Float, DateTime
from core.database import Base

class Training(Base):
    __tablename__ = "training"

    id = Column(Integer, primary_key=True, index=True)
    id_health = Column(Integer, nullable=False)
    id_type_training = Column(Integer, nullable=False)
    km_distance = Column(Float, nullable=False)
    kcal_active = Column(Integer, nullable=False)
    kcal_total = Column(Integer, nullable=False)
    pace = Column(DateTime, nullable=False)
    steps = Column(Integer, nullable=False)
    heart_rate_AVG = Column(Integer, nullable=False)