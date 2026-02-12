from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import defer
from models.objetives_day import ObjetivesDay
from datetime import datetime, date as date_type

def get_objetives_day(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(ObjetivesDay).offset(skip).limit(limit).all()

def get_objetives_day_by_id(db: Session, objetives_day_id: int):
    return db.query(ObjetivesDay).filter(ObjetivesDay.id == objetives_day_id).first()

def create_objetives_day(db: Session, date: date_type, obj_calories: int, obj_steps: int, obj_moviment: int, obj_dream: float, id_user_create: int):
    db_objetives_day = ObjetivesDay(
        date=date,
        obj_calories=obj_calories,
        obj_steps=obj_steps,
        obj_moviment=obj_moviment,
        obj_dream=obj_dream,
        id_user_create=id_user_create,
        create_date=datetime.now(),
        id_user_update=id_user_create,
        update_date=datetime.now()
    )
    db.add(db_objetives_day)
    db.commit()
    db.refresh(db_objetives_day)
    return db_objetives_day

def update_objetives_day(db: Session, objetives_day_id: int, date: date_type, obj_calories: int, obj_steps: int, obj_moviment: int, obj_dream: float, id_user_update: int):
    db_objetives_day = db.query(ObjetivesDay).filter(ObjetivesDay.id == objetives_day_id).first()
    if db_objetives_day:
        setattr(db_objetives_day, 'date', date)
        setattr(db_objetives_day, 'obj_calories', obj_calories)
        setattr(db_objetives_day, 'obj_steps', obj_steps)
        setattr(db_objetives_day, 'obj_moviment', obj_moviment  )
        setattr(db_objetives_day, 'obj_dream', obj_dream)
        setattr(db_objetives_day, 'id_user_update', id_user_update)
        setattr(db_objetives_day, 'update_date', datetime.now())
        db.commit()
        db.refresh(db_objetives_day)
    return db_objetives_day

def delete_objetives_day(db: Session, objetives_day_id: int):
    db_objetives_day = db.query(ObjetivesDay).filter(ObjetivesDay.id == objetives_day_id).first()
    if db_objetives_day:
        try:
            db.delete(db_objetives_day)
            db.commit()
            return {"mensaje": "Registro de objetivos del día eliminado exitosamente", "id": objetives_day_id}
        except IntegrityError:
            db.rollback()
            raise ValueError("No se puede eliminar este registro de objetivos del día porque está siendo utilizado en registros de entrenamiento existentes")
    return None