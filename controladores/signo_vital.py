""" from conexion.database import SessionLocal
from conexion.modelos import Signo_vital as SignoVitalModelo
from datetime import datetime
import json

from conexion.schemas import Signo_vital

class SignoVitalControlador():
    data = None
    conect = None
    
    def __init__(self):
            self.conect = SessionLocal
            
     def get_signos_vitales(self, id: int, fecha_inicio: str, fecha_fin: str):
        date_format = "%Y-%m-%d %H:%i:%s"
        query = 'SELECT H.id, DATE_FORMAT(fecha, %s) AS fecha, S.nombre_signo, S.unidad, H.valor FROM signosVitales AS S INNER JOIN historialSignoVital AS H ON S.id = H.signo_id WHERE paciente_id = %s and (fecha BETWEEN %s AND %s)'
        # se previene SQL injection
        self.conect.execute(query, (date_format, id, fecha_inicio, fecha_fin))
        signos = self.conect.fetchall()
        signos_json = []
        for signo in signos:
            signo_dict = {}
            signo_dict['id'] = signo[0]
            signo_dict['fecha'] = datetime.strptime(signo[1], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
            signo_dict['nombre_signo'] = signo[2]
            signo_dict['unidad'] = signo[3]
            signo_dict['valor'] = signo[4]
            signos_json.append(signo_dict)
        return signos_json 




import sys
sys.path.append('../')

from fastapi import APIRouter, HTTPException, Depends
from conexion.schemas import SignoVitalBase, SignoVital
from controladores import signo_vital as controlador_signo_vital
from sqlalchemy.orm import Session
from conexion.database import get_db """





