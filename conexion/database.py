import os
from dotenv import load_dotenv
load_dotenv()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

HOST= os.getenv('HOST')
PORT= os.getenv('PORT')
USER= os.getenv('USER')
PASSWORD= os.getenv('PASSWORD')
DB= os.getenv('DB')
DRIVER = os.getenv('DRIVER')

connection_string = f"DRIVER={DRIVER};SERVER={HOST};DATABASE={DB};UID={USER};PWD={PASSWORD}"

# Crear el motor de SQLAlchemy
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={connection_string}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

