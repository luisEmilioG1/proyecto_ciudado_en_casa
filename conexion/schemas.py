from pydantic import BaseModel

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
    
class Fechas(BaseModel):
    id: str
    fecha_inicio: str
    fecha_fin: str