from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from crud import dream as dream_crud
from datetime import time

router = APIRouter(prefix="/dream", tags=["Sueño"])

@router.get("/")
def read_dream(db: Session = Depends(get_db)):
    return dream_crud.get_dream(db)

@router.get("/{dream_id}")
def read_dream_by_id(dream_id: int, db: Session = Depends(get_db)):
    return dream_crud.get_dream_by_id(db, dream_id)

@router.post("/")
def create_dream( ligth: time, deep: time, rem: time, awake: int, heart_rate: int, total_dream: time, id_health: int, db: Session = Depends(get_db)):
    return dream_crud.create_dream(db, ligth, deep, rem, awake, heart_rate, total_dream, id_health)

@router.put("/{dream_id}")
def update_dream(dream_id: int, ligth: time, deep: time, rem: time, awake: int, heart_rate: int, total_dream: time, id_health: int, db: Session = Depends(get_db)):
    return dream_crud.update_dream(db, dream_id, ligth, deep, rem, awake, heart_rate, total_dream, id_health)

@router.delete("/{dream_id}")
def delete_dream(dream_id: int, db: Session = Depends(get_db)):
    try:
        result = dream_crud.delete_dream(db, dream_id)
        if result is None:
            raise HTTPException(status_code=404, detail="Registro de sueño no encontrado")
        return result
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))