from fastapi import FastAPI
from conexion.database import engine, SessionLocal
from conexion.modelos import Base
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import inspect
from rutas import diagnostico, signo_vital, usuario, historial_cuidados, paciente


Base.metadata.create_all(bind=engine)

""" inspector = inspect(engine)
table_names = inspector.get_table_names()

print(table_names) """

app = FastAPI()

app.include_router(usuario.user_route, prefix='/user')
app.include_router(diagnostico.diagnostico_route, prefix='/diagnostico')
app.include_router(historial_cuidados.historial_cuidados_route, prefix='/historial_cuidados')
app.include_router(paciente.paciente_route, prefix='/paciente')
#app.include_router(signo_vital.signo_vital_route, prefix='/signo_vital')
