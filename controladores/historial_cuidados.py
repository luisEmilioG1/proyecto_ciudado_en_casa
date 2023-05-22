from sqlalchemy.orm import Session
from conexion.modelos import *
from conexion.schemas import *
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def crear_historial_cuidados(db: Session, historial_cuidados: HistorialCuidadosBase):
    db_historial_cuidados = Historial_ciudadosDB(**historial_cuidados.dict())
    db.add(db_historial_cuidados)
    db.commit()
    db.refresh(db_historial_cuidados)
    return db_historial_cuidados

def obtener_historial_cuidados(db: Session, id_paciente: int):
    return db.query(Historial_ciudadosDB).filter(Historial_ciudadosDB.paciente_id == id_paciente).first()

# def obtener_todos_historiales_cuidados(db: Session):
#     return db.query(Historial_ciudadosDB).all()