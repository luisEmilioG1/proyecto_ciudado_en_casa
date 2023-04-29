import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

HOST= os.getenv('HOST')
PORT= os.getenv('PORT')
USER= os.getenv('USER')
PASSWORD= os.getenv('PASSWORD')
DB= os.getenv('DB')

CONEXION = mysql.connector.connect(
  host = HOST,
  port= PORT,
  user= USER,
  password= PASSWORD,
  database= DB
)

class conexionDB():  
  CURSOR = None
  def __init__(self):
    self.CURSOR = CONEXION.cursor()
    
  # patron singelton
  @staticmethod
  def get_instance():
      if conexionDB.CURSOR is None:
          return conexionDB()
      return conexionDB

