from fastapi import APIRouter, Depends
from controladores.paciente import get_paciente_controlador, get_paciente_all_controlador
from controladores.usuario import get_user
from sqlalchemy.orm import Session
from conexion.schemas import Paciente_cedula
from conexion.database import get_db

paciente_route = APIRouter()

@paciente_route.post("/get_paciente")
def get_paciente(paciente:Paciente_cedula, db: Session = Depends(get_db)):
    paciente = get_paciente_controlador( db, paciente.cedula )
    if paciente:
        return paciente
    return {"message":"No se encontro el paciente"}

@paciente_route.get("/get_pacientes")
def get_paciente(db: Session = Depends(get_db)):
    pacientes = get_paciente_all_controlador( db )
    if pacientes:
        return pacientes
    return {"message":"No se encontro pacientes"}