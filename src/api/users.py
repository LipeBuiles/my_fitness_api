from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from crud import users as crud_users
from pydantic import BaseModel
from src.shemas.users import UserResponse

router = APIRouter(prefix="/users", tags=["Usuarios"])

@router.get("/")
def read_users(db: Session = Depends(get_db)):
    return crud_users.get_user(db)

@router.get("/{user_id}")
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return crud_users.get_user_by_id(db, user_id)

@router.post("/", response_model=UserResponse)
def create_user(name: str, user_name: str, email: str, password: str, state: str, db: Session = Depends(get_db)):
    return crud_users.create_user(db, name, user_name, email, password, state)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, name: str, user_name: str, email: str, password: str, state: str, db: Session = Depends(get_db)):
    return crud_users.update_user(db, user_id, name, user_name, email, password, state)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        result = crud_users.delete_user(db, user_id)
        if result is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return result
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))