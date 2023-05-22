from fastapi import APIRouter, Depends
from controladores.paciente import get_paciente
from sqlalchemy.orm import Session
from conexion.schemas import Paciente_cedula
from conexion.database import get_db

paciente_route = APIRouter()

@paciente_route.get("/get_paciente")
def get_paciente(paciente:Paciente_cedula, db: Session = Depends(get_db)):
    paciente = get_paciente( db, paciente.cedula)
    # if paciente:
    #     return paciente
    return {"message":"No se encontro el paciente"}