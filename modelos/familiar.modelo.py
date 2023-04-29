from modelos import Usuario

class Familiar(Usuario):
    telefono_alterno: str
    def __init__(self, id, nombre, apellido, direccion, telefono, correo, edad, cedula, password, telefono_alterno):
        super().__init__(id, nombre, apellido, direccion, telefono, correo, edad, cedula, password)
        self.telefono_alterno = telefono_alterno