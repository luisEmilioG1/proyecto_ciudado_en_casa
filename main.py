from fastapi import FastAPI,APIRouter
from eschemas import User
from database import USUARIOS
from routers.usuario import user

app = FastAPI()

app.include_router(user,prefix='/user')

@app.get("/")
def hello_world():
    return {"message":"Servidor ejecutandose"}


@app.post("/diagnostico/adddiag/")
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




