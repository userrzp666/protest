import requests
import json
import calendar;
import time


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


def func_interact():
    token = admin_login_token()
    headers = {'authorization': 'Bearer ' + token,
               'content-type': 'application/json'}

    list_json = {"condition":{"productId":None, "subProductId":None}, "page":1,"size":10}
    list_url = "https://test-vlc-admin-api.kaikeba.com/operation/dramaLive/pageList"
    res3 = requests.post(url=list_url, headers=headers, json=list_json)
    #     contentId = (response.json().get('data'))['content_id']
    data = res3.json().get('data')['records']
    #for i in url:
    #    print(i)
    url = data[0]['url']
    print(url)


    #print(res3.json())
if __name__ == '__main__':
    func_interact()
