""" from fastapi import APIRouter
from conexion.schemas import Signo_vital
from controladores.signo_vital import SignoVitalControlador
from conexion.schemas import Fechas

controlador = SignoVitalControlador()

signo_vital = APIRouter()
 """