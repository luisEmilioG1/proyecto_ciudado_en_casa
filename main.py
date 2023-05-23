from fastapi import FastAPI
from conexion.database import engine, SessionLocal
from conexion.modelos import Base
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import inspect
from rutas import diagnostico, signo_vital, usuario, historial_cuidados, paciente
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

origins = ['http://localhost:5173']

app = FastAPI()
# incluire cors para todos los dominios
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])

app.include_router(usuario.user_route, prefix='/user')
app.include_router(diagnostico.diagnostico_route, prefix='/diagnostico')
app.include_router(historial_cuidados.historial_cuidados_route, prefix='/historial_cuidados')
app.include_router(paciente.paciente_route, prefix='/paciente')
app.include_router(router=signo_vital.signo_vital_route, prefix='/signo_vital')

