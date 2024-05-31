# grandstream_api/autenticacion.py

import hashlib
from .connection import get_session

def get_challenge(url, user):
    """
    The HTTP authentication is based on challenge/response authentication 
    protocol. The client sends a request for a challenge.
    """
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
    """
    Upon obtaining the challenge string, the client then creates an 
    MD5 hash consisting of the challenge and the user password. 
    By sending a login command with the username and MD5 hash, the 
    client will be able to log in. User information will be returned 
    upon successful login.
    """
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
