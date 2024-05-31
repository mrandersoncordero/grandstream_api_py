from api.connection import get_session

def get_system_status(url, cookie):
    """
    The “getSystemStatus” action will return the system information.
    """
    session = get_session()

    request = {
        "request": {
            "action": "getSystemStatus",
            'cookie': cookie
        }
    }
    response = session.post(url, json=request, verify=False)
    response_data = response.json()
    return response_data
