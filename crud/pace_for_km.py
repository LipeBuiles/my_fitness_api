from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.pace_for_km import PaceForKm
from datetime import time

def get_pace(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(PaceForKm).offset(skip).limit(limit).all()

def get_pace_by_id(db: Session, pace_id: int):
    return db.query(PaceForKm).filter(PaceForKm.id == pace_id).first()

def create_pace(db: Session, id_training: int, km: int, pace: time):
    db_pace = PaceForKm(
        id_training=id_training,
        km=km,
        pace=pace
    )
    db.add(db_pace)
    db.commit()
    db.refresh(db_pace)
    return db_pace

def update_pace(db: Session, pace_id: int, id_training: int, km: int, pace: time):
    db_pace = db.query(PaceForKm).filter(PaceForKm.id == pace_id).first()
    if db_pace:
        setattr(db_pace, 'id_training', id_training)
        setattr(db_pace, 'km', km)
        setattr(db_pace, 'pace', pace)
        db.commit()
        db.refresh(db_pace)
    return db_pace

def delete_pace(db: Session, pace_id: int):
    db_pace = db.query(PaceForKm).filter(PaceForKm.id == pace_id).first()
    if db_pace:
        try:
            db.delete(db_pace)
            db.commit()
            return {"mensaje": "Registro de ritmo eliminado exitosamente", "id": pace_id}
        except IntegrityError:
            db.rollback()
            raise ValueError("No se puede eliminar este registro de ritmo porque está siendo utilizado en registros de entrenamiento existentes")
    return None