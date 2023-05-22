from sqlalchemy.orm import Session
from conexion.modelos import UserDB as UserModelo, PacienteDB as PacienteModelo
  
def get_paciente_controlador(db: Session, cedula: str ):
    user = db.query(PacienteModelo).filter(UserModelo.cedula == cedula).first()
    return user
