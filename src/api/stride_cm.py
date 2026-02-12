from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from crud import stride_cm as stride_cm_crud
from pydantic import BaseModel

router = APIRouter(prefix="/stride_cm", tags=["Stride en cm"])

@router.get("/")
def read_stride_cm(db: Session = Depends(get_db)):
    return stride_cm_crud.get_stride_cm(db)

@router.get("/{stride_cm_id}")
def read_stride_cm_by_id(stride_cm_id: int, db: Session = Depends(get_db)):
    return stride_cm_crud.get_stride_cm_by_id(db, stride_cm_id)

@router.post("/")
def create_stride_cm(id_training: int, stride_avg: int, stride_max: int, db: Session = Depends(get_db)):
    return stride_cm_crud.create_stride_cm(db, id_training, stride_avg, stride_max)

@router.put("/{stride_cm_id}")
def update_stride_cm(stride_cm_id: int, id_training: int, stride_avg: int, stride_max: int, db: Session = Depends(get_db)):
    return stride_cm_crud.update_stride_cm(db, stride_cm_id, id_training, stride_avg, stride_max)

@router.delete("/{stride_cm_id}")
def delete_stride_cm(stride_cm_id: int, db: Session = Depends(get_db)):
    try:
        result = stride_cm_crud.delete_stride_cm(db, stride_cm_id)
        if result is None:
            raise HTTPException(status_code=404, detail="StrideCm no encontrado")
        return result
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))