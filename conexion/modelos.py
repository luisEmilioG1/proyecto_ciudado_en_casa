from sqlalchemy import Column, Integer, String, DateTime, Boolean, CHAR, ForeignKey

from sqlalchemy.orm import relationship
from conexion.database import Base

class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20), nullable=False)
    apellido = Column(String(20), nullable=False)
    cedula = Column(Integer, nullable=False, unique=True)
    edad = Column(Integer, nullable=False)
    telefono = Column(String(10), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    passwd = Column(String(50), nullable=False)
    direccion = Column(String(50), nullable=False)

    #Lo que recibo como llave foránea para otras tablas
    paciente = relationship("Paciente", back_populates="user")
    familiar_designado = relationship("Familiar_designado", back_populates="user")
    personal_medico = relationship("Personal_medico", back_populates="user")
    auxiliar = relationship("Auxiliar", back_populates="user")
    
class Signo_vital(Base):

    __tablename__ = "signosVitales"

    id = Column(Integer, primary_key=True, index=True)
    nombre_signo = Column(String(20), nullable=False)
    unidad = Column(String(4), nullable=False)

    #Lo que recibo como llave foránea para otras tablas
    historial_signo_vital = relationship("Historial_signo_vital", back_populates="signo_vital")

class Paciente(Base):

    __tablename__ = "paciente"

    id = Column(Integer, primary_key=True, index=True)
    
    #FK
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    familiar_id = Column(Integer, ForeignKey("familiarDesignado.id"), nullable=False)

    #Lo que expongo como llave foránea para otras tablas
    familiar = relationship("Familiar_designado", back_populates="paciente")
    user = relationship("User", back_populates="paciente")

    #Lo que recibo como llave foránea para otras tablas
    historial_signo_vital = relationship("Historial_signo_vital", back_populates="paciente")
    historial_cuidados = relationship("Historial_ciudados", back_populates="paciente")
    historial_diagnostico = relationship("Historial_diagnostico", back_populates="paciente")
    personal_cargo = relationship("Personal_a_cargo", back_populates="paciente")


class Familiar_designado(Base):

    __tablename__ = "familiarDesignado"

    id = Column(Integer, primary_key=True, index=True)
    telefono_alt = Column(String(10), nullable=False)
    
    #FK
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    #Lo que expongo como llave foránea para otras tablas
    user = relationship("User", back_populates="familiar_designado")

    #Lo que recibo como llave foránea para otras tablas
    paciente = relationship("Paciente", back_populates="familiar")
""" 
class Personal_medico(Base):
    
    __tablename__ = "personalMedico"

    id = Column(Integer, primary_key=True, index=True)
    especialidad = Column(String(15), nullable=False)
    tajeta_profesional = Column(String(10), nullable=False)
    tipo_persona = Column(CHAR, nullable=False)
    
    #FK
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    #Lo que expongo como llave foránea para otras tablas
    user = relationship("User", back_populates="personal_medico")
    
    #Lo que recibo como llave foránea para otras tablas
    historial_cuidados = relationship("Historial_ciudados", back_populates="profesional")
    historial_diganostico = relationship("Historial_diganostico", back_populates="profesional")
    personal_cargo = relationship("Personal_a_cargo", back_populates="profesional")

class Auxiliar(Base):
         
    __tablename__ = "auxiliar"

    id = Column(Integer, primary_key=True, index=True)

    #FK
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    #Lo que expongo como llave foránea para otras tablas
    user = relationship("User", back_populates="auxiliar")

class Historial_diagnostico(Base):

    __tablename__ = "historialDiagnostico"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, nullable=False)

    #FK
    profesional_id = Column(Integer, ForeignKey("personalMedico.id"), nullable=False)
    paciente_id = Column(Integer, ForeignKey("paciente.id"), nullable=False)
    diagnostico_id = Column(Integer, ForeignKey("diagnostico.id"), nullable=False)
    
    #Lo que expongo como llave foránea para otras tablas
    paciente  = relationship("Paciente", back_populates="historial_diganostico")
    diagnostico = relationship("Diagnostico", back_populates="historial_diagnostico")
    profesional = relationship("Personal_medico", back_populates="historial_diganostico")
    

class Historial_ciudados(Base):
         
    __tablename__ = "historialCuidados"

    id = Column(Integer, primary_key=True, index=True)
    fecha_inicial = Column(DateTime, nullable=False)
    fecha_final = Column(DateTime, nullable=False)
    ciudado = Column(String(50), nullable=False)
    descripcion = Column(String(500), nullable=False)

    #FK
    paciente_id = Column(Integer, ForeignKey("paciente.id"), nullable=False)
    profesional_id = Column(Integer, ForeignKey("personalMedco.id"), nullable=False)

    #Lo que expongo como llave foránea para otras tablas
    paciente  = relationship("Paciente", back_populates="historial_cuidados")
    profesional = relationship("Personal_medico", back_populates="historial_cuidados")




class Historial_signo_vital(Base):
         
    __tablename__ = "historialSignoVital"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, nullable=False)
    valor = Column(Integer, nullable=False)

    #FK
    signo_id = Column(Integer, ForeignKey("signosVitales.id"), nullable=False)
    paciente_id = Column(Integer, ForeignKey("paciente.id"), nullable=False)

    #Lo que expongo como llave foránea para otras tablas
    paciente  = relationship("Paciente", back_populates="historial_signo_vital")
    signo_vital = relationship("Signo_vital", back_populates="historial_signo_vital")


class Diagnostico(Base):
          
    __tablename__ = "diagnostico"

    id = Column(Integer, primary_key=True, index=True)
    nombre_diagnostico = Column(String(50), nullable=False)
    descripcion = Column(String(100), nullable=False)
    
    #Lo que recibo como llave foránea para otras tablas
    historial_diagnostico = relationship("Historial_diagnostico", back_populates="diagnostico")

class Personal_a_cargo(Base):
        
    __tablename__ = "personalACargo"

    id = Column(Integer, primary_key=True, index=True)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_final = Column(DateTime, nullable=False)
    activo = Column(Boolean, default=False)
    
    #FK
    profesional_id = Column(Integer, ForeignKey("personalMedico.id"), nullable=False)
    paciente_id = Column(Integer, ForeignKey("paciente.id"), nullable=False)

    #Lo que expongo como llave foránea para otras tablas
    paciente  = relationship("Paciente", back_populates="personal_cargo")
    profesional = relationship("Personal_medico", back_populates="personal_cargo")
 """