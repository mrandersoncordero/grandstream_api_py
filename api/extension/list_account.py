from api.connection import get_session

def list_account(url, cookie):
    """
    The “listAccount” action will return information about the extensions
    created on the UCM, such as the extension’s number, its name etc
    """
    session = get_session()

    request = {
        'request': {
            'action': 'getSystemGeneralStatus',
            'cookie': cookie,
            'item_num':'30',
            'options':'extension,account_type,fullname,status,addr',
            'page': '1',
            'sidx': 'extension',
            'sord': 'asc'
        }
    }
    response = session.post(url, json=request, verify=False)
    response_data = response.json()
    return response_data
