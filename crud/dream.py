from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.dream import Dream
from datetime import time


def get_dream(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(Dream).offset(skip).limit(limit).all()

def get_dream_by_id(db: Session, dream_id: int):
    return db.query(Dream).filter(Dream.id == dream_id).first()

def create_dream(db: Session, ligth: time, deep: time, rem: time, awake: int, heart_rate: int, total_dream: time, id_health: int):
    db_dream = Dream(
        ligth=ligth,
        deep=deep,
        rem=rem,
        awake=awake,
        heart_rate=heart_rate,
        total_dream=total_dream,
        id_health=id_health
    )
    db.add(db_dream)
    db.commit()
    db.refresh(db_dream)
    return db_dream


def update_dream(db: Session, dream_id: int, ligth: time, deep: time, rem: time, awake: int, heart_rate: int, total_dream: time, id_health: int):
    db_dream = db.query(Dream).filter(Dream.id == dream_id).first()
    if db_dream:
        setattr(db_dream, 'ligth', ligth)
        setattr(db_dream, 'deep', deep)
        setattr(db_dream, 'rem', rem)
        setattr(db_dream, 'awake', awake)
        setattr(db_dream, 'heart_rate', heart_rate)
        setattr(db_dream, 'total_dream', total_dream)
        setattr(db_dream, 'id_health', id_health)
        db.commit()
        db.refresh(db_dream)
    return db_dream

def delete_dream(db: Session, dream_id: int):
    db_dream = db.query(Dream).filter(Dream.id == dream_id).first()
    if db_dream:
        try:
            db.delete(db_dream)
            db.commit()
            return {"mensaje": "Registro de sueño eliminado exitosamente", "id": dream_id}
        except IntegrityError:
            db.rollback()
            raise ValueError("No se puede eliminar este registro de sueño porque está siendo utilizado en registros de entrenamiento existentes")
    return None
