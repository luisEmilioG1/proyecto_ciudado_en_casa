
import sys
sys.path.append('../')

from fastapi import APIRouter
from conexion.database import USUARIOS
from conexion.eschemas import User

user = APIRouter()


@user.get("/all/")
def listar_allUsers():
    return USUARIOS

@user.get("/unique/{id_usuario}")
def listar_justOne(id_usuario:int):
    # buscar el usuario en la lista

    for user in USUARIOS:
        if user['id'] == id_usuario:
            return user
    return {"message":"No se encontró el usuario en la DB"}

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


@user.post("/login/")
def login(user:User):
    for usuario in USUARIOS:
        if (usuario["username"] == user.username) and (usuario["password"] == user.password):
            return {"message":"Acceso correcto",
                    "token": "ADIDCXCGT"}
    return {"message": "Verifique su usuario y contraseña"}

