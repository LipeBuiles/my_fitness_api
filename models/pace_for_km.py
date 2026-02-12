from sqlalchemy import Column, Integer, Time
from core.database import Base

class PaceForKm(Base):
    __tablename__ = "pace_for_km"

    id = Column(Integer, primary_key=True, index=True)
    id_training = Column(Integer, nullable=False)
    km = Column(Integer, nullable=False)
    pace = Column(Time, nullable=False)