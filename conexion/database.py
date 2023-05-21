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

# Crear el motor de SQLAlchemy
engine = create_engine(f"mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

Base = declarative_base()

