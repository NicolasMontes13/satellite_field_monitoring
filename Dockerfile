# Utilizar una imagen base de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar los archivos de la aplicación
COPY requirements.txt .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "infra.api.fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]
