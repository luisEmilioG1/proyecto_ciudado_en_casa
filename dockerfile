# Dockerfile

# Utilizamos una imagen base de Python
FROM python:3.11.4
RUN /opt/venv/bin/python -m pip install --upgrade pip
# Establecemos el directorio de trabajo en /app
RUN mkdir /app

# Copiamos el archivo requirements.txt al contenedor
COPY . /app

