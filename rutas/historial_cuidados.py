from fastapi import APIRouter, HTTPException, Depends
from conexion.schemas import HistorialCuidadosBase, HistorialCuidados
from controladores import historial_cuidados as controlador_historial_cuidados
from sqlalchemy.orm import Session
from conexion.database import get_db

historial_cuidados_route = APIRouter()

@historial_cuidados_route.post("/post", response_model=HistorialCuidados)
def add_historial_cuidados(historial_cuidados: HistorialCuidadosBase, db: Session = Depends(get_db)):
    return controlador_historial_cuidados.crear_historial_cuidados(db, historial_cuidados)

@historial_cuidados_route.get("/get/{paciente_id}", response_model=HistorialCuidados)
def get_historial_cuidados(paciente_id: int, db: Session = Depends(get_db)):
    return controlador_historial_cuidados.obtener_historial_cuidados(db, paciente_id)

# @historial_cuidados_route.get("/get_all", response_model=HistorialCuidados)
# def get_historiales_cuidados(db: Session = Depends(get_db)):
#     return controlador_historial_cuidados.obtener_todos_historiales_cuidados(db)