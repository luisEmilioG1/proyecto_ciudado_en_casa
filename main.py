from fastapi import FastAPI
from rutas.diagnostico import diagnostico

app = FastAPI()

app.include_router(diagnostico,prefix='/diagnostico')

