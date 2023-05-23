from fastapi import APIRouter, HTTPException, Depends
from controladores.signo_vital import get_signos_vitales
from sqlalchemy.orm import Session
from conexion.schemas import Fechas
from conexion.database import get_db

signo_vital_route = APIRouter()

@signo_vital_route.get("/consultar_signos_vitales")
def listar_signos(fechas:Fechas, db: Session = Depends(get_db)):
    signos = get_signos_vitales( db, fechas.id, fechas.fecha_inicio, fechas.fecha_fin)
    if signos:
        return signos
    return {"message":"No se encontraron signos para el paciente"}
