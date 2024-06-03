from dotenv import load_dotenv
import os

load_dotenv()


API_KEY = os.environ.get("EARTH_API")
BUCKET_NAME = os.environ.get("BUCKET_NAME")
DATE = os.environ.get("DATE")
