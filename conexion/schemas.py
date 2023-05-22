from pydantic import BaseModel
from datetime import *

class UserGet(BaseModel):
    nombre: str
    apellido: str
    cedula: str
    edad: int
    telefono: str
    email: str
    direccion: str

class UserBase(UserGet):
    psswd: str

    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    

    class Config:
        orm_mode = True

class HistorialCuidadosBase(BaseModel):
    fecha_inicial : datetime
    fecha_final : datetime
    profesional_id: int
    paciente_id: int
    cuidado: str
    descripcion: str

class HistorialCuidados(HistorialCuidadosBase):
    id: int

    class Config:
        orm_mode = True
    

class DiagnosticoBase(BaseModel):
    nombre_diagnostico: str
    descripcion: str

class Diagnostico(DiagnosticoBase):
    id:  int
    
    class Config:
        orm_mode = True
    
class SignoVitalBase(BaseModel):
    nombre_signo: str
    unidad: str

class SignoVital(SignoVitalBase):
    id: int

    class Config:
        orm_mode = True

class Paciente(UserBase):
    id: str
    nombre: str
    apellido: str
    direccion: str
    telefono: str
    correo: str
    edad: int
    
class Paciente_cedula(UserBase):
    cedula:str
    
class Fechas(BaseModel):
    id: str
    fecha_inicio: str
    fecha_fin: str