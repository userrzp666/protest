from common import get_token
from common.public import login_info
import requests

token = get_token.admin_login_token()

print(token)
def test_qianren_list():

    headers = {'authorization': 'Bearer ' + token,
               'content-type': 'application/json'}
    url = "https://test-vlc-admin-api.kaikeba.com/operation/dramaLive/pageList"
    jsons = {"condition":{"productId":None,"subProductId":None},"page":1,"size":10}
    res = requests.post(url=url, headers=headers, json=jsons)

    res_json = res.json()
    login_info(res)
    login_info(res_json)
    assert res_json['code'] == '00000', '断言失败'


test_qianren_list()