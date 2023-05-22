from fastapi import APIRouter, HTTPException, Depends
from conexion.schemas import DiagnosticoBase, Diagnostico
from controladores import diagnostico as controlador_diagnostico
from sqlalchemy.orm import Session
from conexion.database import get_db

diagnostico_route = APIRouter()

@diagnostico_route.post("/post", response_model=Diagnostico)
def add_diag(diagnostico: DiagnosticoBase, db: Session = Depends(get_db)):
    return controlador_diagnostico.crear_diagnostico(db, diagnostico)

@diagnostico_route.get("/get/{id}", response_model=Diagnostico)
def get_diag(id: int, db: Session = Depends(get_db)):
    return controlador_diagnostico.obtener_diagnostico(db, id)

@diagnostico_route.get("/get_all", response_model=Diagnostico)
def get_diags(db: Session = Depends(get_db)):
    return controlador_diagnostico.obtener_todos_diagnosticos(db)