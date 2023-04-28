import mysql.connector

CONEXION = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Admin123",
        database="SOFT2"
      )

CURSOR = None

class conexionDB():  
    def __init__(self):
      self.CURSOR = CONEXION.cursor()
      self.CONEXION = CONEXION
