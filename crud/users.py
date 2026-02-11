from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import defer
from models.users import Users
import bcrypt

def get_user(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(Users).options(defer(Users.password)).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(Users).filter(Users.id == user_id).first()

def create_user(db: Session, name: str, user_name: str, email: str, password: str, state: str):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    db_user = Users(name=name, user_name=user_name, email=email, password=hashed_password, state=state)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, name: str, user_name: str, email: str, password: str, state: str):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    db_user = db.query(Users).filter(Users.id == user_id).first()
    if db_user:
        db_user.name = name
        db_user.user_name = user_name
        db_user.email = email
        db_user.password = hashed_password
        db_user.state = state
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(Users).filter(Users.id == user_id).first()
    if db_user:
        try:
            db.delete(db_user)
            db.commit()
            return {"mensaje": "Usuario eliminado exitosamente", "id": user_id}
        except IntegrityError:
            db.rollback()
            raise ValueError("No se puede eliminar este usuario porque está siendo utilizado en registros de entrenamiento existentes")
    return None
