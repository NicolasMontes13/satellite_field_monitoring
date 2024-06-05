# Prueba técnica

Este proyecto consiste en la implementación de un proceso en Python que, dada una fecha específica y las coordenadas de una lista de campos, descarga las imágenes disponibles de la API Earth de la NASA,
tambien en elaborar un pequeño endpoint de API utilizando Python y FastAPI, que permite obtener imágenes asociadas a un field_id en un archivo zip.

## Requisitos Previos

Lista de los requisitos previos necesarios para ejecutar el proyecto, por ejemplo:

- Python 3.11
- Pip
- LocalStack

## Funcionamiento

El endpoint de API consta de los siguientes componentes:

1. **Entrada de Datos:** El usuario proporciona un `field_id` como parámetro de la solicitud.

2. **Consulta a la Base de Datos:** Utilizando el `field_id` proporcionado, se realiza una consulta al S3 para recuperar las imágenes asociadas a ese `field_id`.

3. **Creación del Archivo Zip:** Las imágenes recuperadas se empaquetan en un archivo zip.

4. **Respuesta de la API:** Se devuelve al usuario el archivo zip generado para su descarga.

## Funcionamiento API del NASA

El proceso consta de los siguientes pasos:

1. **Entrada de Datos:** Se proporciona una fecha específica y las coordenadas geográficas de una lista de campos.

2. **Consulta a la API Earth de la NASA:** Utilizando la fecha y las coordenadas proporcionadas, se realizan consultas a la API Earth de la NASA para recuperar las imágenes disponibles para esas ubicaciones en esa fecha.

3. **Descarga de Imágenes:** Se descargan las imágenes correspondientes a cada ubicación y se almacenan localmente para su posterior procesamiento o análisis.


## Instrucciones de ejecución

1. **Docker-compose** Para poder ejecutar el localstack y el uvicorn para la ejecucion de la fastapi; se hace la siguiente instruccion ---> **"docker-compose up --build"**

2. **Probar la API**


