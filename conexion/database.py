import os
from dotenv import load_dotenv
load_dotenv()

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOST= os.getenv('HOST')
PORT= os.getenv('MYPORT')
USER= os.getenv('USER')
PASSWORD= os.getenv('PASSWORD')
DB= os.getenv('DB')
DRIVER = os.getenv('DRIVER')

engine = create_engine(f'mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

