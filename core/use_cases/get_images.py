from core.entities.constants import BUCKET_NAME, DATE, HOST
from infra.gateways.get_image import get_image
import boto3
from botocore.exceptions import ClientError
import pandas as pd
import logging


logging.basicConfig(level=logging.INFO)

def get_images():

    s3 = boto3.client('s3', 
                        endpoint_url=f'http://{HOST}:4566')
    
    try:
        s3.head_bucket(Bucket=BUCKET_NAME)

    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            logging.info(f"el Bucket {BUCKET_NAME} no existe. Creándolo...")

            s3.create_bucket(Bucket=BUCKET_NAME)

            logging.info(f"Bucket {BUCKET_NAME} creado exitosamente.")
        else:
            logging.info(f"Error al verificar la existencia del bucket.")
            raise

    fields = pd.read_csv("/app/fields.csv")
    logging.info("CSV readed")
    for i in fields.index:

        field_id = str(fields["field_id"][i]) + "_" + str(fields["Nombre"][i])
        lon = fields["lon"][i]
        lat = fields["lat"][i]
        response, image_name = get_image(lon, lat)

        if response.status_code == 400:
            continue
        upload_to_s3(image_name, response, field_id, s3)

def upload_to_s3(image_name, response, field_id, s3):

    key_name = f'{field_id}/{DATE}/{image_name}'
    s3.put_object(Bucket=BUCKET_NAME, Key=key_name, Body=response.content, ContentType='image/png')

    result = s3.get_object(Bucket=BUCKET_NAME, Key=key_name)


