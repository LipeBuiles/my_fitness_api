from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from crud import type_training as crud_type_training

router = APIRouter(prefix="/type_training", tags=["Tipo de Entrenamiento"])

@router.get("/")
def read_type_training(db: Session = Depends(get_db)):
    return crud_type_training.get_type_training(db)

@router.get("/{training_id}")
def read_type_training_by_id(training_id: int, db: Session = Depends(get_db)):
    return crud_type_training.get_type_training_by_id(db, training_id)

@router.post("/")
def create_type_training(name: str, db: Session = Depends(get_db)):
    return crud_type_training.create_type_training(db, name)

@router.put("/{training_id}")
def update_type_training(training_id: int, name: str, db: Session = Depends(get_db)):
    return crud_type_training.update_type_training(db, training_id, name)

@router.delete("/{training_id}")
def delete_type_training(training_id: int, db: Session = Depends(get_db)):
    try:
        result = crud_type_training.delete_type_training(db, training_id)
        if result is None:
            raise HTTPException(status_code=404, detail="Tipo de entrenamiento no encontrado")
        return result
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))