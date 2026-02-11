from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from crud import health as crud_health
from src.shemas.health import HealthCreate, HealthUpdate, HealthResponse

router = APIRouter(prefix="/health", tags=["Salud"])

@router.get("/")
def read_health(db: Session = Depends(get_db)):
    return crud_health.get_health(db)

@router.get("/{health_id}")
def read_health_by_id(health_id: int, db: Session = Depends(get_db)):
    return crud_health.get_health_by_id(db, health_id)

@router.post("/", response_model=HealthResponse)
def create_health(health: HealthCreate, db: Session = Depends(get_db)):
    return crud_health.create_health(db, health.date, health.calories, health.steps, health.distance, health.moviment, health.in_training, health.id_user_create)

@router.put("/{health_id}", response_model=HealthResponse)
def update_health(health_id: int, health: HealthUpdate, db: Session = Depends(get_db)):
    return crud_health.update_health(db, health_id, health.date, health.calories, health.steps, health.distance, health.moviment, health.in_training, health.id_user_update)

@router.delete("/{health_id}")
def delete_health(health_id: int, db: Session = Depends(get_db)):
    try:
        result = crud_health.delete_health(db, health_id)
        if result is None:
            raise HTTPException(status_code=404, detail="Registro de salud no encontrado")
        return result
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))