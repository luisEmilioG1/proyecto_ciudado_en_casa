from sqlalchemy.orm import Session
from conexion.modelos import UserDB as UserModelo, PacienteDB as PacienteModelo
  
def get_paciente_controlador(db: Session, cedula: str ):
    paciente = db.query(PacienteModelo).all()
    user = filter(lambda x : str(x.user.cedula) == cedula , paciente)
    user=list(user)
    if len(user) == 0:
        return 
    user=user[0] 
    user.user.id = user.id
    return user.user

def get_paciente_all_controlador(db: Session):
    pacientes = db.query(PacienteModelo).all()
    if not pacientes:
        return
    for paciente in pacientes:
        paciente.user.id = paciente.id
    pacientes = list(map(lambda x : x.user, pacientes))
    return pacientes
