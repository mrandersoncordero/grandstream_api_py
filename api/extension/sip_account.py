from api.connection import get_session

def get_sip_account(url, cookie):
    """
    The “getSIPAccount” action will return information about specific extension.
    """
    session = get_session()

    request = {
        'request': {
            'action': 'getSIPAccount',
            'cookie': cookie,
            'extension': '1000',
        }
    }
    response = session.post(url, json=request, verify=False)
    response_data = response.json()
    return response_data


def update_sip_account(url, cookie):
    """
    This action will allow users to update an existing SIP account.
    """
    session = get_session()

    request = {
        'request': {
            'action': 'getSIPAccount',
            'cookie': cookie,
            'extension': '1000',
            "permission": "internal"
        }
    }
    response = session.post(url, json=request, verify=False)
    response_data = response.json()
    return response_data
