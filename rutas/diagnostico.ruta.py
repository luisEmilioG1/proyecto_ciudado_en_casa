import sys
sys.path.append('../')

from fastapi import APIRouter
from conexion.database import USUARIOS
from conexion.eschemas import User

user = APIRouter()


@user.get("/all/")
def listar_allUsers():
    return USUARIOS



@user.post("/addusr/")
def add_usr(user:User):
    #id
    #username
    #passwd
    for usuario in USUARIOS:
        if user.username == usuario['username']:
            return {"message":"Usuario ya existe"}
    
    # metodo para agregar en la base de datos
    USUARIOS.append(user)
    return {"message": "usuario añadido con éxito"}
