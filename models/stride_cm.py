from sqlalchemy import Column, Integer, String
from core.database import Base

class StrideCm(Base):
    __tablename__ = "stride_cm"

    id = Column(Integer, primary_key=True, index=True)
    id_training = Column(Integer, nullable=False)
    stride_avg = Column(Integer, nullable=False)
    stride_max = Column(Integer, nullable=False)
