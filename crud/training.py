from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.training import Training

def get_training(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(Training).offset(skip).limit(limit).all()

def get_training_by_id(db: Session, training_id: int):
    return db.query(Training).filter(Training.id == training_id).first()

def create_training(db: Session, id_health: int, id_type_training: int, km_distance: float, kcal_active: int, kcal_total: int, pace, steps: int, heart_rate_AVG: int):
    db_training = Training(
        id_health=id_health,
        id_type_training=id_type_training,
        km_distance=km_distance,
        kcal_active=kcal_active,
        kcal_total=kcal_total,
        pace=pace,
        steps=steps,
        heart_rate_AVG=heart_rate_AVG
    )
    db.add(db_training)
    db.commit()
    db.refresh(db_training)
    return db_training

def update_training(db: Session, training_id: int, id_health: int, id_type_training: int, km_distance: float, kcal_active: int, kcal_total: int, pace, steps: int, heart_rate_AVG: int):
    db_training = db.query(Training).filter(Training.id == training_id).first()
    if db_training:
        db_training.id_health = id_health
        db_training.id_type_training = id_type_training
        db_training.km_distance = km_distance
        db_training.kcal_active = kcal_active
        db_training.kcal_total = kcal_total
        db_training.pace = pace
        db_training.steps = steps
        db_training.heart_rate_AVG = heart_rate_AVG
        db.commit()
        db.refresh(db_training)
    return db_training

def delete_training(db: Session, training_id: int):
    db_training = db.query(Training).filter(Training.id == training_id).first()
    if db_training:
        try:
            db.delete(db_training)
            db.commit()
            return {"mensaje": "Entrenamiento eliminado exitosamente", "id": training_id}
        except IntegrityError:
            db.rollback()
            raise ValueError("No se puede eliminar este entrenamiento porque está siendo utilizado en otros registros")
    return None