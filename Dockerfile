# Utilizar una imagen base de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar los archivos de la aplicación
COPY app/ .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Asegurarse de que el script de entrada tenga permisos de ejecución
RUN chmod +x entrypoint.sh

# Exponer el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["./entrypoint.sh"]