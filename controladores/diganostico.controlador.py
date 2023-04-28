from ..conexion import database

def obtener_id_max():
    database.CURSOR.execute("SELECT MAX(ID) FROM diagnostico")

    return database.CURSOR.fetchone()


print(obtener_id_max())



