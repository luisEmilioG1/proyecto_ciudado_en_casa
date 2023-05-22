from sqlalchemy.orm import Session
from conexion.modelos import *
from conexion.schemas import *
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def crear_usuario(db: Session, usuario: UserBase):
    db_usuario = UserDB(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return parse_user(db_usuario)

def obtener_todos_usuarios(db: Session):
    return parse_user(db.query(UserDB).all())

def obtener_usuario(db: Session, email: str):
    return parse_user(db.query(UserDB).filter(UserDB.email == email).first())

def parse_user(user: User) -> UserGet:
    user_get = UserGet(
        id=user.id,
        nombre=user.nombre,
        apellido=user.apellido,
        cedula=user.cedula,
        edad=user.edad,
        telefono=user.telefono,
        email=user.email,
        direccion=user.direccion
    )
    return user_get