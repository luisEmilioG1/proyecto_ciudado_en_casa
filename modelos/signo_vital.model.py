class Signo_vital:
    id: str
    nombre_signo: str
    fecha_signo: int
    unidad:str
    valor: float
    
    def __init__(self, id, fecha_signo, nombre_signo, unidad, valor):
        self.id = id
        self.fecha_signo = fecha_signo
        self.nombre_signo = nombre_signo
        self.unidad = unidad
        self.valor = valor
        