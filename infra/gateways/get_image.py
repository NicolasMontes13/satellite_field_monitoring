from core.entities.constants import API_KEY, DATE
import requests

def get_image(lon, lat):
    api_url = f"https://api.nasa.gov/planetary/earth/imagery?lon={lon}&lat={lat}&date={DATE}&api_key={API_KEY}"
    response = requests.get(api_url)
    if response.status_code == 200:
        image_name = "_imagery.png"
        return response, image_name
    else:
        return response, "<<<<ERROR>>>>"
