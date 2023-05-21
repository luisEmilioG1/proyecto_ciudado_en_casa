class Usuario:
    id: str
    nombre: str
    apellido: str
    direccion: str
    telefono: str
    correo: str
    edad: int
    cedula:int
    password:str
    
    def __init__(self, id, nombre, apellido, direccion, telefono, correo, edad, cedula, password):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.edad = edad
        self.password = password
        
        