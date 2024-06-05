from dotenv import load_dotenv
import os

load_dotenv()


API_KEY = os.environ.get("EARTH_API")
BUCKET_NAME = os.environ.get("BUCKET_NAME")
DATE = os.environ.get("DATE")
HOST = os.environ.get("LOCALSTACK_HOSTNAME")
ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
REGION = os.environ.get("AWS_DEFAULT_REGION")
