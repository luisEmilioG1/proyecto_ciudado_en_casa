from sqlalchemy.orm import Session
from conexion.modelos import *
from conexion.schemas import *
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def crear_diagnostico(db: Session, diagnostico: DiagnosticoBase):
    db_diagnostico = DiagnosticoDB(**diagnostico.dict())
    db.add(db_diagnostico)
    db.commit()
    db.refresh(db_diagnostico)
    return db_diagnostico

def obtener_diagnostico(db: Session, id: int):
    return db.query(DiagnosticoDB).filter(DiagnosticoDB.id == id).first()

def obtener_todos_diagnosticos(db: Session):
    return db.query(DiagnosticoDB).all()