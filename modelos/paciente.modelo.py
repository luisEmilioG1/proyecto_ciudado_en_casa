from modelos import Usuario, Familiar, Signo_vital

class Paciente(Usuario):
    familiar : Familiar
    historial_signos_vitales : list(Signo_vital)
    
    def __init__(self, id, nombre, apellido, direccion, telefono, correo, edad, cedula, password,familiar):
        super()._init_(id, nombre, apellido, direccion, telefono, correo, edad, cedula, password)
        self.familiar = familiar
        self.historial_signos_vitales = []
        
    def get_historial_signos_vitales(self):
        return self.historial_signos_vitales