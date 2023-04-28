import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",
  port=3306,
  user="root",
  password="Admin123",
  database="SOFT2"
)

CURSOR: str

class conexionDB():
  
  

# crear un cursor para realizar consultas
    def __init__(self):
    
      self.CURSOR = conexion.cursor()

    def obtener_conexion():
        return CURSOR
 
'''
cursor.execute("SELECT * FROM signosVitales")

# obtener los resultados de la consulta
resultados = cursor.fetchall()

# imprimir los resultados
for resultado in resultados:
  print(resultado)

# cerrar la conexión
conexion.close()
'''