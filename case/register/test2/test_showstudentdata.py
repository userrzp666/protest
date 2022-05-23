from common import get_token
from common.public import login_info
import requests
token = get_token.admin_login_token()
def test_shoudata():
    headers = {'authorization': 'Bearer ' + token,
               'content-type': 'application/json'}
    url = "https://test-vlc-admin-api.kaikeba.com/operation/dramaLive/userLearnList"
    jsons = {"condition":{"id":"1023"},"page":1,"size":10}

    res = requests.post(url=url, json=jsons, headers=headers)
    res_json = res.json()
    login_info(res)
    login_info(res_json)

    assert  res_json['code'] == '00000', '断言失败'


test_shoudata()