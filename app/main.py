from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import StreamingResponse
from localstack_client.session import Session
import io
import zipfile
from dotenv import load_dotenv
import os

load_dotenv()

BUCKET_NAME = os.environ.get("BUCKET_NAME")

app = FastAPI()

@app.get("/download_images/{carpeta_id}")
async def download_images(carpeta_id: str = Path(...)):

    session = Session()

    s3 = session.client('s3', endpoint_url='http://localhost:4566')
    s3.create_bucket(Bucket=BUCKET_NAME)

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