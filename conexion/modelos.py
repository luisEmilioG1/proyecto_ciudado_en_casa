from sqlalchemy import Column, Integer, String, DateTime, Boolean, CHAR, ForeignKey
from sqlalchemy.orm import relationship

from conexion.database import Base

class UserDB(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20), nullable=False)
    apellido = Column(String(20), nullable=False)
    cedula = Column(String(11), nullable=False, unique=True)
    edad = Column(Integer, nullable=False)
    telefono = Column(String(10), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    psswd = Column(String(50), nullable=False)
    direccion = Column(String(50), nullable=False)

    #Lo que recibo como llave foránea para otras tablas
    paciente = relationship("PacienteDB", back_populates="user")
    familiar_designado = relationship("Familiar_designadoDB", back_populates="user")
    personal_medico = relationship("Personal_medicoDB", back_populates="user")
    auxiliar = relationship("AuxiliarDB", back_populates="user")
    

class DiagnosticoDB(Base):

    __tablename__ = "diagnostico"

    id = Column(Integer, primary_key=True, index=True)
    nombre_diagnostico = Column(String(50), nullable=False)
    descripcion = Column(String(100), nullable=False)

    #Lo que recibo como llave foránea para otras tablas
    historial_diagnostico = relationship("Historial_diagnosticoDB", back_populates="diagnostico")

    
class Signo_vitalDB(Base):

    __tablename__ = "signosVitales"

    id = Column(Integer, primary_key=True, index=True)
    nombre_signo = Column(String(20), nullable=False)
    unidad = Column(String(4), nullable=False)

    #Lo que recibo como llave foránea para otras tablas
    historial_signo_vital = relationship("Historial_signo_vitalDB", back_populates="signo_vital")

class PacienteDB(Base):

    __tablename__ = "paciente"

    id = Column(Integer, primary_key=True, index=True)
    
    #FK
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    familiar_id = Column(Integer, ForeignKey("familiarDesignado.id"), nullable=False)

    #Lo que expongo como llave foránea para otras tablas
    familiar = relationship("Familiar_designadoDB", back_populates="paciente")
    user = relationship("UserDB", back_populates="paciente")

    #Lo que recibo como llave foránea para otras tablas
    historial_signo_vital = relationship("Historial_signo_vitalDB", back_populates="paciente")
    historial_cuidados = relationship("Historial_ciudadosDB", back_populates="paciente")
    historial_diagnostico = relationship("Historial_diagnosticoDB", back_populates="paciente")
    personal_cargo = relationship("Personal_a_cargoDB", back_populates="paciente")


class Familiar_designadoDB(Base):

    __tablename__ = "familiarDesignado"

    id = Column(Integer, primary_key=True, index=True)
    telefono_alt = Column(String(10), nullable=False)
    
    #FK
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    #Lo que expongo como llave foránea para otras tablas
    user = relationship("UserDB", back_populates="familiar_designado")

    #Lo que recibo como llave foránea para otras tablas
    paciente = relationship("PacienteDB", back_populates="familiar")

class Personal_medicoDB(Base):
    
    __tablename__ = "personalMedico"

    id = Column(Integer, primary_key=True, index=True)
    especialidad = Column(String(15), nullable=False)
    tajeta_profesional = Column(String(10), nullable=False)
    tipo_persona = Column(CHAR, nullable=False)
    
    #FK
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    #Lo que expongo como llave foránea para otras tablas
    user = relationship("UserDB", back_populates="personal_medico")
    
    #Lo que recibo como llave foránea para otras tablas
    historial_cuidados = relationship("Historial_ciudadosDB", back_populates="profesional")
    historial_diagnostico = relationship("Historial_diagnosticoDB", back_populates="profesional")
    personal_cargo = relationship("Personal_a_cargoDB", back_populates="profesional")

class AuxiliarDB(Base):
         
    __tablename__ = "auxiliar"

    id = Column(Integer, primary_key=True, index=True)

    #FK
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    #Lo que expongo como llave foránea para otras tablas
    user = relationship("UserDB", back_populates="auxiliar")

class Historial_diagnosticoDB(Base):

    __tablename__ = "historialDiagnostico"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, nullable=False)

    #FK
    profesional_id = Column(Integer, ForeignKey("personalMedico.id"), nullable=False)
    paciente_id = Column(Integer, ForeignKey("paciente.id"), nullable=False)
    diagnostico_id = Column(Integer, ForeignKey("diagnostico.id"), nullable=False)
    
    #Lo que expongo como llave foránea para otras tablas
    paciente  = relationship("PacienteDB", back_populates="historial_diagnostico")
    diagnostico = relationship("DiagnosticoDB", back_populates="historial_diagnostico")
    profesional = relationship("Personal_medicoDB", back_populates="historial_diagnostico")
    

class Historial_ciudadosDB(Base):
         
    __tablename__ = "historialCuidados"

    id = Column(Integer, primary_key=True, index=True)
    fecha_inicial = Column(DateTime, nullable=False)
    fecha_final = Column(DateTime, nullable=False)
    cuidado = Column(String(50), nullable=False)
    descripcion = Column(String(500), nullable=False)

    #FK
    paciente_id = Column(Integer, ForeignKey("paciente.id"), nullable=False)
    profesional_id = Column(Integer, ForeignKey("personalMedico.id"), nullable=False)

    #Lo que expongo como llave foránea para otras tablas
    paciente  = relationship("PacienteDB", back_populates="historial_cuidados")
    profesional = relationship("Personal_medicoDB", back_populates="historial_cuidados")

class Historial_signo_vitalDB(Base):
         
    __tablename__ = "historialSignoVital"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, nullable=False)
    valor = Column(Integer, nullable=False)

    #FK
    signo_id = Column(Integer, ForeignKey("signosVitales.id"), nullable=False)
    paciente_id = Column(Integer, ForeignKey("paciente.id"), nullable=False)

    #Lo que expongo como llave foránea para otras tablas
    paciente  = relationship("PacienteDB", back_populates="historial_signo_vital")
    signo_vital = relationship("Signo_vitalDB", back_populates="historial_signo_vital")


'''class DiagnosticoDB(Base):
          
    __tablename__ = "diagnosticos"

    id = Column(Integer, primary_key=True, index=True)
    nombre_diagnostico = Column(String(50), nullable=False)
    descripcion = Column(String(100), nullable=False)
    
    #Lo que recibo como llave foránea para otras tablas
    historial_diagnostico = relationship("Historial_diagnosticoDB", back_populates="diagnostico")'''

class Personal_a_cargoDB(Base):
        
    __tablename__ = "personalACargo"

    id = Column(Integer, primary_key=True, index=True)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_final = Column(DateTime, nullable=False)
    activo = Column(Boolean, default=False)
    
    #FK
    profesional_id = Column(Integer, ForeignKey("personalMedico.id"), nullable=False)
    paciente_id = Column(Integer, ForeignKey("paciente.id"), nullable=False)

    #Lo que expongo como llave foránea para otras tablas
    paciente  = relationship("PacienteDB", back_populates="personal_cargo")
    profesional = relationship("Personal_medicoDB", back_populates="personal_cargo")
