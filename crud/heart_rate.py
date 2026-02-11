from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.heart_rate import HeartRate
from datetime import time

def get_heart_rate(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(HeartRate).offset(skip).limit(limit).all()

def get_heart_rate_by_id(db: Session, heart_rate_id: int):
    return db.query(HeartRate).filter(HeartRate.id == heart_rate_id).first()

def create_heart_rate(db: Session, id_training: int, heart_rate_avg: int, heart_rate_max: int, ligth_pace: time, intensive_pace: time, aerobic_pace: time, anaerobic_pace: time, vo2_max: time):
    db_heart_rate = HeartRate(
        id_training=id_training,
        heart_rate_avg=heart_rate_avg,
        heart_rate_max=heart_rate_max,
        ligth_pace=ligth_pace,
        intensive_pace=intensive_pace,
        aerobic_pace=aerobic_pace,
        anaerobic_pace=anaerobic_pace,
        vo2_max=vo2_max
    )
    db.add(db_heart_rate)
    db.commit()
    db.refresh(db_heart_rate)
    return db_heart_rate


def update_heart_rate(db: Session, heart_rate_id: int, id_training: int, heart_rate_avg: int, heart_rate_max: int, ligth_pace: time, intensive_pace: time, aerobic_pace: time, anaerobic_pace: time, vo2_max: time):
    db_heart_rate = db.query(HeartRate).filter(HeartRate.id == heart_rate_id).first()
    if db_heart_rate:
        setattr(db_heart_rate, 'id_training', id_training)
        setattr(db_heart_rate, 'heart_rate_avg', heart_rate_avg)
        setattr(db_heart_rate, 'heart_rate_max', heart_rate_max)
        setattr(db_heart_rate, 'ligth_pace', ligth_pace)
        setattr(db_heart_rate, 'intensive_pace', intensive_pace)
        setattr(db_heart_rate, 'aerobic_pace', aerobic_pace)
        setattr(db_heart_rate, 'anaerobic_pace', anaerobic_pace)
        setattr(db_heart_rate, 'vo2_max', vo2_max)
        db.commit()
        db.refresh(db_heart_rate)
    return db_heart_rate

def delete_heart_rate(db: Session, heart_rate_id: int):
    db_heart_rate = db.query(HeartRate).filter(HeartRate.id == heart_rate_id).first()
    if db_heart_rate:
        try:
            db.delete(db_heart_rate)
            db.commit()
            return {"mensaje": "Registro de frecuencia cardíaca eliminado exitosamente", "id": heart_rate_id}
        except IntegrityError:
            db.rollback()
            raise ValueError("No se puede eliminar este registro de frecuencia cardíaca porque está siendo utilizado en registros de entrenamiento existentes")
    return None
