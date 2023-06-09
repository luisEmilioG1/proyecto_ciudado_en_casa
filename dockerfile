# Dockerfile

# Utilizamos una imagen base de Python
FROM python:3.11.4
RUN /opt/venv/bin/python -m pip install --upgrade pip
# Establecemos el directorio de trabajo en /app
RUN mkdir /app

# Copiamos el archivo requirements.txt al contenedor
COPY . /app

# Creamos un ambiente virtual e instalamos los requerimientos
RUN cd /app
RUN pip install -r requirements.txt

# Exponemos el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Iniciamos la aplicación FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
