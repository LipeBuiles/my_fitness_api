from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.stride_cm import StrideCm

def get_stride_cm(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(StrideCm).offset(skip).limit(limit).all()

def get_stride_cm_by_id(db: Session, stride_cm_id: int):
    return db.query(StrideCm).filter(StrideCm.id == stride_cm_id).first()

def create_stride_cm(db: Session, id_training: int, stride_avg: int, stride_max: int):
    db_stride_cm = StrideCm(id_training=id_training, stride_avg=stride_avg, stride_max=stride_max)
    db.add(db_stride_cm)
    db.commit()
    db.refresh(db_stride_cm)
    return db_stride_cm

def update_stride_cm(db: Session, stride_cm_id: int, id_training: int, stride_avg: int, stride_max: int):
    db_stride_cm = db.query(StrideCm).filter(StrideCm.id == stride_cm_id).first()
    if db_stride_cm:
        db_stride_cm.id_training = id_training
        db_stride_cm.stride_avg = stride_avg
        db_stride_cm.stride_max = stride_max
        db.commit()
        db.refresh(db_stride_cm)
    return db_stride_cm

def delete_stride_cm(db: Session, stride_cm_id: int):
    db_stride_cm = db.query(StrideCm).filter(StrideCm.id == stride_cm_id).first()
    if db_stride_cm:
        try:
            db.delete(db_stride_cm)
            db.commit()
            return {"mensaje": "StrideCm eliminado exitosamente", "id": stride_cm_id}
        except IntegrityError:
            db.rollback()
            raise ValueError("No se puede eliminar este StrideCm porque está siendo utilizado en registros de entrenamiento existentes")
    return None
