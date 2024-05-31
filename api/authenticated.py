# grandstream_api/autenticacion.py

import hashlib
from .connection import get_session

def get_challenge(url, user):
    challenge_request = {
        "request": {
            "action": "challenge",
            "user": user,
            "version": "1.0"
        }
    }

    session = get_session()
    response = session.post(url, json=challenge_request, verify=False)
    response_data = response.json()
    return response_data


def authenticate(url, user, password, challenge):
    response_string = f"{challenge}{password}"
    response_hash = hashlib.md5(response_string.encode()).hexdigest()
    
    auth_request = {
        "request": {
            "action": "login",
            "token": response_hash,
            "url": url,
            "user": user
        }
    }

    session = get_session()
    auth_response = session.post(url, json=auth_request, verify=False)
    auth_response_data = auth_response.json()
    return auth_response_data
