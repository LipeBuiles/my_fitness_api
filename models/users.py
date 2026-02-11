from sqlalchemy import Column, Integer, String
from core.database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    user_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    state = Column(String, nullable=False)  # Enum values: '0', '1', '2', '3'
