from sqlalchemy.orm import Session
from conexion.modelos import Signo_vitalDB as SignoVitalModelo, PacienteDB as PacienteModelo
from datetime import datetime
import json


def str_to_date(fecha: str):
    return datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")
            
def get_signos_vitales(db: Session, id: int, fecha_inicio: str, fecha_fin: str):
    paciente = db.query(PacienteModelo).filter(PacienteModelo.id == id).first()
    # obtiene los signos vitales del paciente
    signos_vitales = paciente.historial_signo_vital
    
    fecha_inicio = str_to_date(fecha_inicio).timestamp()
    fecha_fin = str_to_date(fecha_fin).timestamp()

    # obtiene los signos vitales en el rango de fechas indicadas
    signos_vitales = filter(lambda x: (x.fecha.timestamp() >= fecha_inicio and x.fecha.timestamp() <= fecha_fin), signos_vitales)
    return list(signos_vitales)





