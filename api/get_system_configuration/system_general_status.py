from api.connection import get_session

def get_system_general_status(url, cookie):
    """
    The “getSystemGeneralStatus” action will return the version information.
    """
    session = get_session()

    request = {
        "request": {
            "action": "getSystemGeneralStatus",
            'cookie': cookie
        }
    }
    response = session.post(url, json=request, verify=False)
    response_data = response.json()
    return response_data
