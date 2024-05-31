import os
import requests
from .connection import get_session

def recapi(url, cookie, download_path):
    session = get_session()

    request = {
        "request": {
            "action": "recapi",
            "cookie": cookie,
            "filedir": "monitor",
            "filename": "auto-1717093784-1001-2100.wav"
        }
    }

    response = session.post(url, json=request, verify=False)
    if response.status_code == 200:
        file_data = response.content
        # Combinar la ruta de descarga con el nombre del archivo
        file_path = os.path.join(download_path, "audio.wav")
        # Guardar el archivo descargado en la ruta especificada
        with open(file_path, "wb") as audio_file:
            audio_file.write(file_data)
        print(f"El archivo de audio se ha descargado y guardado en: {file_path}")
    else:
        print("Error al descargar el archivo de audio:", response.text)
