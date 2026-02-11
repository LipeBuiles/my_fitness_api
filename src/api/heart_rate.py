from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from crud import heart_rate as heart_rate_crud
from datetime import time

router = APIRouter(prefix="/heart_rate", tags=["Frecuencia Cardíaca"])

@router.get("/")
def read_heart_rate(db: Session = Depends(get_db)):
    return heart_rate_crud.get_heart_rate(db)

@router.get("/{heart_rate_id}")
def read_heart_rate_by_id(heart_rate_id: int, db: Session = Depends(get_db)):
    return heart_rate_crud.get_heart_rate_by_id(db, heart_rate_id)

@router.post("/")
def create_heart_rate(id_training: int, heart_rate_avg: int, heart_rate_max: int, ligth_pace: time, intensive_pace: time, aerobic_pace: time, anaerobic_pace: time, vo2_max: time, db: Session = Depends(get_db)):
    return heart_rate_crud.create_heart_rate(db, id_training, heart_rate_avg, heart_rate_max, ligth_pace, intensive_pace, aerobic_pace, anaerobic_pace, vo2_max)

@router.put("/{heart_rate_id}")
def update_heart_rate(heart_rate_id: int, id_training: int, heart_rate_avg: int, heart_rate_max: int, ligth_pace: time, intensive_pace: time, aerobic_pace: time, anaerobic_pace: time, vo2_max: time, db: Session = Depends(get_db)):
    return heart_rate_crud.update_heart_rate(db, heart_rate_id, id_training, heart_rate_avg, heart_rate_max, ligth_pace, intensive_pace, aerobic_pace, anaerobic_pace, vo2_max)

@router.delete("/{heart_rate_id}")
def delete_heart_rate(heart_rate_id: int, db: Session = Depends(get_db)):
    try:
        result = heart_rate_crud.delete_heart_rate(db, heart_rate_id)
        if result is None:
            raise HTTPException(status_code=404, detail="Registro de frecuencia cardíaca no encontrado")
        return result
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))