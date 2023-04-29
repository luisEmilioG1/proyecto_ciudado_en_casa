from conexion.database import conexionDB
from datetime import datetime
import json

from conexion.eschemas import Signo_vital

data = None
conect = None

class SignoVitalControlador():
    def __init__(self):
            self.data = conexionDB()
            self.conect = self.data.CURSOR
            
    def get_signos_vitales(self, id: int, fecha_inicio: str, fecha_fin: str):
        self.conect.execute(f'SELECT H.id, DATE_FORMAT(fecha, "%Y-%m-%d %H:%i:%s") AS fecha, S.nombre_signo, S.unidad, H.valor FROM signosVitales AS S INNER JOIN historialSignoVital AS H ON S.id = H.signo_id WHERE paciente_id = {id} and (fecha BETWEEN "{fecha_inicio}" AND "{fecha_fin}")')
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


