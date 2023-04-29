from conexion.database import conexionDB
from conexion.schemas import Diagnostico
import json

data = None
conect = None

class DiagnosticoControlador():

    def __init__(self):
        self.data = conexionDB()
        self.conect = self.data.CURSOR

    def get_diagnostico(self, id: int):
        self.conect.execute('SELECT * FROM diagnostico WHERE id = {0}'.format(id))

        return json.dumps(self.conect.fetchone())

    def obtener_id_max(self):
        self.conect.execute("SELECT MAX(ID) FROM diagnostico")

        result = self.conect.fetchone()

        return result[0] + 1 if result and result[0] is not None else 1

    def agregar_diagnostico(self, diagnostico: Diagnostico):
        print(diagnostico)
        print(self.obtener_id_max())

        id_diagnostico = self.obtener_id_max()

        self.conect.execute('INSERT INTO Diagnostico VALUES({0}, "{1}", "{2}")'.format(id_diagnostico, diagnostico.nombre_diagnostico, diagnostico.descripcion))
        self.data.CONEXION.commit()

        diagnostico_generado = self.get_diagnostico(id_diagnostico)

        self.data.CURSOR.close()
        self.data.CONEXION.close()

        return diagnostico_generado
    
     
