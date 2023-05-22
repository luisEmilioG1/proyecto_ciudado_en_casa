from fastapi import APIRouter, Depends
from conexion.database import get_db
from conexion.schemas import *
from conexion.schemas import *
from controladores import usuario as controlador_usuario
from sqlalchemy.orm import Session

user_route = APIRouter()

@user_route.get("/get", response_model=UserGet)
def get_user(email: str, db: Session = Depends(get_db)):
    return controlador_usuario.obtener_usuario(db, email)

@user_route.post("/post", response_model=UserGet)
def add_user(user: UserBase, db: Session = Depends(get_db)):
    return controlador_usuario.crear_usuario(db, user)



