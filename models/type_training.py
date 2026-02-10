from sqlalchemy import Column, Integer, String
from core.database import Base

class TypeTraining(Base):
    __tablename__ = "type_training"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
