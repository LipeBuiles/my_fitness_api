from sqlalchemy.orm import Session
<<<<<<< HEAD
from sqlalchemy.exc import IntegrityError
=======
>>>>>>> 63a296d11029cc39196a561ceab89b89fb3e93e8
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
<<<<<<< HEAD
    return db_training

def update_type_training(db: Session, training_id: int, name: str):
    db_training = db.query(TypeTraining).filter(TypeTraining.id == training_id).first()
    if db_training:
        db_training.name = name
        db.commit()
        db.refresh(db_training)
    return db_training

def delete_type_training(db: Session, training_id: int):
    db_training = db.query(TypeTraining).filter(TypeTraining.id == training_id).first()
    if db_training:
        try:
            db.delete(db_training)
            db.commit()
            return {"mensaje": "Tipo de entrenamiento eliminado exitosamente", "id": training_id}
        except IntegrityError:
            db.rollback()
            raise ValueError("No se puede eliminar este tipo de entrenamiento porque está siendo utilizado en registros de entrenamiento existentes")
    return None
=======
    return db_training
>>>>>>> 63a296d11029cc39196a561ceab89b89fb3e93e8
