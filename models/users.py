from sqlalchemy import Column, Integer, String
from core.database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    user_name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
    state = Column(String, index=True)  # Enum values: '0', '1', '2', '3'
