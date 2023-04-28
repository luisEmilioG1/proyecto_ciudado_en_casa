import sys
sys.path.append('../')

from fastapi import APIRouter
from conexion.eschemas import Diagnostico
from controladores.diganostico import DiagnosticoControlador

controlador = DiagnosticoControlador()

diagnostico = APIRouter()

@diagnostico.post("/diagnostico/")
def add_diag(diagnostico: Diagnostico):
    return controlador.agregar_diagnostico(diagnostico)
