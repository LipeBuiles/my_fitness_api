from sqlalchemy.orm import Session
from models.type_training import TypeTraining

def get_type_training(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TypeTraining).offset(skip).limit(limit).all()

def get_type_training_by_id(db: Session, training_id: int):
    return db.query(TypeTraining).filter(TypeTraining.id == training_id).first()

def create_type_training(db: Session, name: str):
    db_training = TypeTraining(name=name)
    db.add(db_training)
    db.commit()
    db.refresh(db_training)
    return db_training