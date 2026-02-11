from pydantic import BaseModel
from datetime import date, datetime

class HealthCreate(BaseModel):
    date: date
    calories: int
    steps: int
    distance: float
    moviment: int
    in_training: str
    id_user_create: int

class HealthUpdate(BaseModel):
    date: date
    calories: int
    steps: int
    distance: float
    moviment: int
    in_training: str
    id_user_update: int

class HealthResponse(BaseModel):
    id: int
    date: date
    calories: int
    steps: int
    distance: float
    moviment: int
    in_training: str
    id_user_create: int
    create_date: datetime
    id_user_update: int
    update_date: datetime

    class Config:
        from_attributes = True
