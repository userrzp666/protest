from common import get_token
from common.public import login_info
token = get_token.admin_login_token()
import requests

def test_getjuben():

    url = "https://test-vlc-admin-api.kaikeba.com/program/list"
    jsons ={"page":1,"size":10,
            "condition":{"solution":1,"name":"zp0520001","programLabels":{"productId":"","subProductId":""}
                         }}

    headers = {'authorization': 'Bearer ' + token,
               'content-type': 'application/json'}

    res = requests.post(url=url, json=jsons,headers=headers)

    res_json = res.json()
    login_info(res)
    login_info(res_json)

    assert res_json['code'] == '00000', '断言失败'


test_getjuben()
