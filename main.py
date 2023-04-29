from fastapi import FastAPI
from rutas.diagnostico import diagnostico
from rutas.signo_vital import signo_vital

app = FastAPI()

app.include_router(diagnostico,prefix='/diagnostico')
app.include_router(signo_vital,prefix='/signo_vital')

