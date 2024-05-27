import requests

url = "http://localhost:8000/download_images/2_Pampa_Humeda"
response = requests.get(url)

if response.status_code == 200:
    with open("imagenes.zip", "wb") as f:
        f.write(response.content)
    print("Archivo zip descargado exitosamente.")
else:
    print("Error al descargar el archivo zip:", response.text)