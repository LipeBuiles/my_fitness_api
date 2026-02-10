from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from crud import type_training as crud_type_training


app = FastAPI(title="My Fitness API")

@app.get("/type_training/")
def read_type_training(db: Session = Depends(get_db)):
    return crud_type_training.get_type_training(db)

@app.get("/type_training/{training_id}")
def read_type_training_by_id(training_id: int, db: Session = Depends(get_db)):
    return crud_type_training.get_type_training_by_id(db, training_id)

@app.post("/type_training/")
def create_type_training(name: str, db: Session = Depends(get_db)):
    return crud_type_training.create_type_training(db, name)
