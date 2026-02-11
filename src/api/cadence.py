from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from crud import cadence as crud_cadence

router = APIRouter(prefix="/cadence", tags=["Cadencia"])

@router.get("/")
def read_cadence(db: Session = Depends(get_db)):
    return crud_cadence.get_cadence(db)

@router.get("/{cadence_id}")
def read_cadence_by_id(cadence_id: int, db: Session = Depends(get_db)):
    return crud_cadence.get_cadence_by_id(db, cadence_id)

@router.post("/")
def create_cadence(id_training: int, cadence_AVG: float, cadence_MAX: float, db: Session = Depends(get_db)):
    return crud_cadence.create_cadence(db, id_training, cadence_AVG, cadence_MAX)

@router.put("/{cadence_id}")
def update_cadence(cadence_id: int, id_training: int, cadence_AVG: float, cadence_MAX: float, db: Session = Depends(get_db)):
    return crud_cadence.update_cadence(db, cadence_id, id_training, cadence_AVG, cadence_MAX)

@router.delete("/{cadence_id}")
def delete_cadence(cadence_id: int, db: Session = Depends(get_db)):
    try:
        result = crud_cadence.delete_cadence(db, cadence_id)
        if result is None:
            raise HTTPException(status_code=404, detail="Registro de cadencia no encontrado")
        return result
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))