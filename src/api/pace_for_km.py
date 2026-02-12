from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from crud import pace_for_km as pace_crud
from datetime import time

router = APIRouter(prefix="/pace_for_km", tags=["Ritmo for km"])

@router.get("/")
def read_pace(db: Session = Depends(get_db)):
    return pace_crud.get_pace(db)

@router.get("/{pace_id}")
def read_pace_by_id(pace_id: int, db: Session = Depends(get_db)):
    return pace_crud.get_pace_by_id(db, pace_id)

@router.post("/")
def create_pace(id_training: int, km: int, pace: time, db: Session = Depends(get_db)):
    return pace_crud.create_pace(db, id_training, km, pace)

@router.put("/{pace_id}")
def update_pace(pace_id: int, id_training: int, km: int, pace: time, db: Session = Depends(get_db)):
    return pace_crud.update_pace(db, pace_id, id_training, km, pace)

@router.delete("/{pace_id}")
def delete_pace(pace_id: int, db: Session = Depends(get_db)):
    try:
        result = pace_crud.delete_pace(db, pace_id)
        if result is None:
            raise HTTPException(status_code=404, detail="Registro de ritmo no encontrado")
        return result
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
