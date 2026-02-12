from sqlalchemy import Column, Integer, Time, Float, ForeignKey
from core.database import Base

class Pace(Base):
    __tablename__ = "pace"

    id = Column(Integer, primary_key=True, index=True)
    id_training = Column(Integer, nullable=False)
    pace = Column(Time, nullable=False)
    pace_max = Column(Time, nullable=False)