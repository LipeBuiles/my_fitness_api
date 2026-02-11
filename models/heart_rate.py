from sqlalchemy import Column, Integer, String, Date, Float, Time
from core.database import Base

class HeartRate(Base):
    __tablename__ = "heart_rate"

    id = Column(Integer, primary_key=True, index=True)
    id_training = Column(Integer, nullable=False)
    heart_rate_avg = Column(Integer, nullable=False)
    heart_rate_max = Column(Integer, nullable=False)
    ligth_pace = Column(Time, nullable=False)
    intensive_pace = Column(Time, nullable=False)
    aerobic_pace = Column(Time, nullable=False)
    anaerobic_pace = Column(Time, nullable=False)
    vo2_max = Column(Time, nullable=False)
