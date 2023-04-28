from pydantic import BaseModel

class User(BaseModel):
    username:str
    id:int
    password:str

class Diagnostico(BaseModel):
    nombre_diagnostico: str
    descripcion: str

