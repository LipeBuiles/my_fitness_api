from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import defer
from models.health import Health

def get_health(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(Health).offset(skip).limit(limit).all()

def get_health_by_id(db: Session, health_id: int):
    return db.query(Health).filter(Health.id == health_id).first()


from datetime import datetime, date as date_type

def create_health(db: Session, date: date_type, calories: int, steps: int, distance: float, moviment: int, in_training: str, id_user_create: int):
    db_health = Health(
        date=date,
        calories=calories,
        steps=steps,
        distance=distance,
        moviment=moviment,
        in_training=in_training,
        id_user_create=id_user_create,
        create_date=datetime.now(),
        id_user_update=id_user_create,
        update_date=datetime.now()
    )
    db.add(db_health)
    db.commit()
    db.refresh(db_health)
    return db_health


def update_health(db: Session, health_id: int, date: date_type, calories: int, steps: int, distance: float, moviment: int, in_training: str, id_user_update: int):
    db_health = db.query(Health).filter(Health.id == health_id).first()
    if db_health:
        setattr(db_health, 'date', date)
        setattr(db_health, 'calories', calories)
        setattr(db_health, 'steps', steps)
        setattr(db_health, 'distance', distance)
        setattr(db_health, 'moviment', moviment)
        setattr(db_health, 'in_training', in_training)
        setattr(db_health, 'id_user_update', id_user_update)
        setattr(db_health, 'update_date', datetime.now())
        db.commit()
        db.refresh(db_health)
    return db_health

def delete_health(db: Session, health_id: int):
    db_health = db.query(Health).filter(Health.id == health_id).first()
    if db_health:
        try:
            db.delete(db_health)
            db.commit()
            return {"mensaje": "Registro de salud eliminado exitosamente", "id": health_id}
        except IntegrityError:
            db.rollback()
            raise ValueError("No se puede eliminar este registro de salud porque está siendo utilizado en registros de entrenamiento existentes")
    return None
