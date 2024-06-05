# import sys
# sys.path.append(r'C:\Users\Nicolas Montes G\OneDrive\Desktop\Proyectos\Python\prueba_tecnica\satellite_field_monitoring')

from core.use_cases.get_images import get_images
from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import StreamingResponse
from localstack_client.session import Session
import boto3
from contextlib import asynccontextmanager
from core.entities.constants import BUCKET_NAME, HOST
import io
import zipfile
import logging


logging.basicConfig(level=logging.INFO)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("EJECUTANDO GET_IMAGES")
    
    get_images()
    yield

    logging.info("APP CERRANDOSE")


app = FastAPI(lifespan=lifespan)

@app.get("/download_images/{carpeta_id}")
async def download_images(carpeta_id: str = Path(...)):

    session = Session()

    s3 = boto3.client('s3', 
                        endpoint_url=F'http://{HOST}:4566')

    response = s3.list_objects(Bucket=BUCKET_NAME, Prefix=f'{carpeta_id}')

    if 'Contents' not in response:
        raise HTTPException(status_code=404, detail=f"No se encontraron imagenes en la carpeta '{carpeta_id}'")
    
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED, False) as zip_file:
        for obj in response['Contents']:
            image_obj = s3.get_object(Bucket=BUCKET_NAME, Key=obj['Key'])
            image_data = image_obj['Body'].read()

            zip_file.writestr(obj['Key'], image_data)

    zip_buffer.seek(0)


    return StreamingResponse(io.BytesIO(zip_buffer.read()), media_type="application/octet-stream", headers={"Content-Disposition": f"attachement;filename={carpeta_id}.zip"})