#!/bin/bash

# Ejecutar el script de subida de imágenes de la NASA
python /app/get_images.py

# Iniciar el servidor FastAPI en segundo plano
uvicorn app.main:app --host 0.0.0.0 --port 8000 &

# Esperar a que todos los procesos finalicen
wait