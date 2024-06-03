import sys
sys.path.append(r'C:\Users\Nicolas Montes G\OneDrive\Desktop\Proyectos\Python\prueba_tecnica\satellite_field_monitoring')

from core.entities.constants import BUCKET_NAME, DATE
from infra.gateways.get_image import get_image
from localstack_client.session import Session
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)


def get_images():

    session = Session()

    s3 = session.client('s3', 
                        endpoint_url='http://localhost.localstack.cloud:4566')

    fields = pd.read_csv(r'C:\Users\Nicolas Montes G\OneDrive\Desktop\Proyectos\Python\prueba_tecnica\satellite_field_monitoring\fields.csv')
    logging.info("CSV readed")
    for i in fields.index:

        logging.info(f"Starting fields: {i}")
        field_id = str(fields["field_id"][i]) + "_" + str(fields["Nombre"][i])
        lon = fields["lon"][i]
        lat = fields["lat"][i]
        response, image_name = get_image(lon, lat)
        logging.info(response.status_code)
        upload_to_s3(image_name, response, field_id, s3)

def upload_to_s3(image_name, response, field_id, s3):

    key_name = f'{field_id}/{DATE}/{image_name}'
    s3.put_object(Bucket=BUCKET_NAME, Key=key_name, Body=response.content, ContentType='image/png')

    result = s3.get_object(Bucket=BUCKET_NAME, Key=key_name)

if __name__ == '__main__':
    get_images()

