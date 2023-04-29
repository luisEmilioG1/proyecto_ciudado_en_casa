import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()



CONEXION = mysql.connector.connect(
        host = os.getenv("HOST"),
        port= os.getenv("DB_PORT"),
        user= os.getenv("USER"),
        password= os.getenv("PASSWORD"),
        database= os.getenv("DB")
)

CURSOR = None

class conexionDB():  
    def __init__(self):
      self.CURSOR = CONEXION.cursor()
      self.CONEXION = CONEXION
