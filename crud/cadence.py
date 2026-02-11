from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import defer
from models.cadence import Cadence


def get_cadence(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(Cadence).offset(skip).limit(limit).all()

def get_cadence_by_id(db: Session, cadence_id: int):
    return db.query(Cadence).filter(Cadence.id == cadence_id).first()

def create_cadence(db: Session, id_training: int, cadence_AVG: int, cadence_MAX: int):
    db_cadence = Cadence(
        id_training=id_training,
        cadence_AVG=cadence_AVG,
        cadence_MAX=cadence_MAX
    )
    db.add(db_cadence)
    db.commit()
    db.refresh(db_cadence)
    return db_cadence


def update_cadence(db: Session, cadence_id: int, id_training: int, cadence_AVG: int, cadence_MAX: int):
    db_cadence = db.query(Cadence).filter(Cadence.id == cadence_id).first()
    if db_cadence:
        setattr(db_cadence, 'id_training', id_training)
        setattr(db_cadence, 'cadence_AVG', cadence_AVG)
        setattr(db_cadence, 'cadence_MAX', cadence_MAX)
        db.commit()
        db.refresh(db_cadence)
    return db_cadence

def delete_cadence(db: Session, cadence_id: int):
    db_cadence = db.query(Cadence).filter(Cadence.id == cadence_id).first()
    if db_cadence:
        try:
            db.delete(db_cadence)
            db.commit()
            return {"mensaje": "Registro de cadencia eliminado exitosamente", "id": cadence_id}
        except IntegrityError:
            db.rollback()
            raise ValueError("No se puede eliminar este registro de cadencia porque está siendo utilizado en registros de entrenamiento existentes")
    return None
