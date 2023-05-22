from sqlalchemy.orm import Session
from conexion.modelos import UserDB as UserModelo, PacienteDB as PacienteModelo
  
def get_paciente_controlador(db: Session, cedula: str ):
    paciente = db.query(PacienteModelo).all()
    user = filter(lambda x : str(x.user.cedula) == cedula , paciente)
    return list(user)


