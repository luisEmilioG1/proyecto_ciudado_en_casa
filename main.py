from fastapi import FastAPI
from conexion.database import engine, Base
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import inspect
from conexion.modelos import User

'''from rutas.diagnostico import diagnostico
from rutas.signo_vital import signo_vital'''

Base.metadata.create_all(bind=engine)

inspector = inspect(engine)
table_names = inspector.get_table_names()

print(table_names)


'''def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()'''

app = FastAPI()

'''app.include_router(diagnostico,prefix='/diagnostico')
app.include_router(signo_vital,prefix='/signo_vital')
'''
