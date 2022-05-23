import  requests

def admin_login_token():
    headers = {
        'appid': '1010',
        'tenantid': '6XWFVymtaB68REyRBuf',
        'authorization': 'Basic MTAxMDptcHM=',
    }
    params = {
        'mobile': 18830967737,
        'grant_type': 'mobile',
        'code': 1111,
        'clientId': None,
        'state': 'STATE'
    }
    url = 'https://kmos-api-test.kaikeba.com/corgi/auth/oauth/login'
    response = requests.post(url=url, headers=headers, params=params)
    try:
        access_token = eval(response.text)['data']['access_token']
    except:
        print('出错了！接口返回：' + response.text)
    return access_token
