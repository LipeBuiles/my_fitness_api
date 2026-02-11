from sqlalchemy import Column, Integer, String
from core.database import Base

class Cadence(Base):
    __tablename__ = "cadence"

    id = Column(Integer, primary_key=True, index=True)
    id_training = Column(Integer, index=True)
    cadence_AVG = Column(Integer)
    cadence_MAX = Column(Integer)