from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from crud import objetives_day as objetives_day_crud
from datetime import date as date_type

router = APIRouter(prefix="/objetives_day", tags=["Objetivos del día"])

@router.get("/")
def read_objetives_day(db: Session = Depends(get_db)):
    return objetives_day_crud.get_objetives_day(db)

@router.get("/{objetives_day_id}")
def read_objetives_day_by_id(objetives_day_id: int, db: Session = Depends(get_db)):
    return objetives_day_crud.get_objetives_day_by_id(db, objetives_day_id)

@router.post("/")
def create_objetives_day(date: date_type, obj_calories: int, obj_steps: int, obj_moviment: int, obj_dream: float, id_user_create: int, db: Session = Depends(get_db)):
    return objetives_day_crud.create_objetives_day(db, date, obj_calories, obj_steps, obj_moviment, obj_dream, id_user_create)

@router.put("/{objetives_day_id}")
def update_objetives_day(objetives_day_id: int, date: date_type, obj_calories: int, obj_steps: int, obj_moviment: int, obj_dream: float, id_user_update: int, db: Session = Depends(get_db)):
    return objetives_day_crud.update_objetives_day(db, objetives_day_id, date, obj_calories, obj_steps, obj_moviment, obj_dream, id_user_update)

@router.delete("/{objetives_day_id}")
def delete_objetives_day(objetives_day_id: int, db: Session = Depends(get_db)):
    try:
        result = objetives_day_crud.delete_objetives_day(db, objetives_day_id)
        if result is None:
            raise HTTPException(status_code=404, detail="Registro de objetivos del día no encontrado")
        return result
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))