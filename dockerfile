# Dockerfile

# Utilizamos una imagen base de Python
FROM python:3.9

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos el archivo requirements.txt al contenedor
COPY requirements.txt .

# Creamos un ambiente virtual e instalamos los requerimientos
RUN python3 -m venv .venv
RUN source /app/.venv/bin/activate
RUN pip install -r requirements.txt

# Copiamos el resto de los archivos al contenedor
COPY . .

# Exponemos el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Iniciamos la aplicación FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
