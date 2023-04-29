import mysql.connector

CONEXION = mysql.connector.connect(
        host="34.134.64.128",
        port=3306,
        user="root",
        password="c/b[K>$tM\\6GYUx9",
        database="SOFT2"
      )

CURSOR = None

class conexionDB():  
    def __init__(self):
      self.CURSOR = CONEXION.cursor()
      self.CONEXION = CONEXION
