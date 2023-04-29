from pydantic import BaseModel

class User(BaseModel):
    username:str
    id:int
    password:str

class Diagnostico(BaseModel):
    nombre_diagnostico: str
    descripcion: str
    
class Signo_vital(BaseModel):
    id: str
    presion_arterial: float
    hemogoblina: float
    temperatura: float
    pulso: float
    fecha_signo: int

class Paciente(BaseModel):
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