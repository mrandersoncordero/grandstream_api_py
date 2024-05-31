# main.py

import os
import warnings
from dotenv import load_dotenv
from urllib3.exceptions import InsecureRequestWarning
from api.authenticated import get_challenge, authenticate

load_dotenv()

# Suprimir advertencias de solicitudes HTTPS sin verificar el certificado
warnings.simplefilter('ignore', InsecureRequestWarning)

def main():
    url = os.environ.get('URL')
    user = "cdrapi"
    password = os.environ.get('PASSWORD')

    desafio = get_challenge(url, user)
    print(desafio)

    if desafio['status'] == 0:
        challenge = desafio['response']['challenge']
        print("Challenge received:", challenge)

        autenticacion = authenticate(url, user, password, challenge)
        print(autenticacion)

        if autenticacion['status'] == 0:
            cookie = autenticacion['response']['cookie']
            print("Authentication successful, cookie:", cookie, '\n')

        else:
            print("Authentication failed:", autenticacion)
    else:
        print("Failed to get challenge:", desafio)


if __name__ == "__main__":
    main()
