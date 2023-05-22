""" from fastapi import APIRouter
from conexion.schemas import Signo_vital
from controladores.signo_vital import SignoVitalControlador
from conexion.schemas import Fechas

controlador = SignoVitalControlador()

signo_vital = APIRouter()
 """

'''@signo_vital.get("/consultar_signos_vitales")
def listar_signos(fechas:Fechas):
    signos = controlador.get_signos_vitales_with_orm(fechas.id, fechas.fecha_inicio, fechas.fecha_fin)
    if signos:
        return signos
    return {"message":"No se encontraron signos para el paciente"}'''
