from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from crud import training as crud_training

router = APIRouter(prefix="/training", tags=["Entrenamiento"])

@router.get("/")
def read_training(db: Session = Depends(get_db)):
    return crud_training.get_training(db)

@router.get("/{training_id}")
def read_training_by_id(training_id: int, db: Session = Depends(get_db)):
    return crud_training.get_training_by_id(db, training_id)

@router.post("/")
def create_training(id_health: int, id_type_training: int, km_distance: float, kcal_active: int, kcal_total: int, pace, steps: int, heart_rate_AVG: int, db: Session = Depends(get_db)):
    return crud_training.create_training(db, id_health, id_type_training, km_distance, kcal_active, kcal_total, pace, steps, heart_rate_AVG)

@router.put("/{training_id}")
def update_training(training_id: int, id_health: int, id_type_training: int, km_distance: float, kcal_active: int, kcal_total: int, pace, steps: int, heart_rate_AVG: int, db: Session = Depends(get_db)):
    return crud_training.update_training(db, training_id, id_health, id_type_training, km_distance, kcal_active, kcal_total, pace, steps, heart_rate_AVG)

@router.delete("/{training_id}")
def delete_training(training_id: int, db: Session = Depends(get_db)):
    try:
        result = crud_training.delete_training(db, training_id)
        if result is None:
            raise HTTPException(status_code=404, detail="Entrenamiento no encontrado")
        return result
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))