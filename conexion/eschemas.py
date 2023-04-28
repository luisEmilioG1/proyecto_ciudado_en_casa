from pydantic import BaseModel

class User(BaseModel):
    username:str
    id:int
    password:str

class diagnostico(BaseModel):
    id: int
    nombre_diagnostico: str
    descripcion: str

