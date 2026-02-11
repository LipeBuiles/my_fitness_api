from sqlalchemy import Column, Integer, String, Time
from core.database import Base

class Dream(Base):
    __tablename__ = "dream"

    id = Column(Integer, primary_key=True, index=True)
    ligth = Column(Time, nullable=False)
    deep = Column(Time, nullable=False)
    rem = Column(Time, nullable=False)
    awake = Column(Integer, nullable=False)
    heart_rate = Column(Integer, nullable=False)
    total_dream = Column(Time, nullable=False)
    id_health = Column(Integer, nullable=False)
