import requests
import pandas as pd
from localstack_client.session import Session
from dotenv import load_dotenv
import os

load_dotenv()

BUCKET_NAME = os.environ.get("BUCKET_NAME")
API_KEY = os.environ.get("EARTH_API")
DATE = os.environ.get("DATE")


def get_images():

    session = Session()

    s3 = session.client('s3', endpoint_url='http://localhost:4566')

    fields = pd.read_csv(r"C:\Users\Nicolas Montes G\OneDrive\Desktop\Proyectos\Python\prueba_tecnica\satellite_field_monitoring\fields.csv")
    date = '2021-02-01'
    for i in fields.index:

        field_id = str(fields["field_id"][i]) + "_" + str(fields["Nombre"][i])
        lon = fields["lon"][i]
        lat = fields["lat"][i]
        api_url = f"https://api.nasa.gov/planetary/earth/imagery?lon={lon}&lat={lat}&date={DATE}&api_key={API_KEY}"
        response = requests.get(api_url)
        if response.status_code == 200:
            print("A")
            image_name = '_imagery.png'
            upload_to_s3(image_name, response, field_id, s3)

def upload_to_s3(image_name, response, field_id, s3):

    key_name = f'{field_id}/{DATE}/{image_name}'
    s3.put_object(Bucket=BUCKET_NAME, Key=key_name, Body=response.content, ContentType='image/png')

    result = s3.get_object(Bucket=BUCKET_NAME, Key=key_name)

if __name__ == '__main__':
    get_images()

