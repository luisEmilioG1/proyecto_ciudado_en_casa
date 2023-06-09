# Utiliza la imagen oficial de Python como imagen base
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido del directorio actual al directorio de trabajo en el contenedor
COPY . .

# Expone el puerto 8000 (el puerto por defecto de FastAPI)
EXPOSE 8000

# Define el comando a ejecutar cuando se inicie el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
