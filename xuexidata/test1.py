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
    id = input("请输入剧本ID：")
    token = admin_login_token()
    # 添加红包/货架
    url = "https://test-vlc-admin-api.kaikeba.com/program/edit/" + str(id)
    jsons = {"solution": 1,
              "metaData": {"source": 2, "version": 1, "id": 1477, "name": "新增回放剧本-zx", "description": "新增回放剧本-zx",
                           "createTime": 1651818146000, "status": 1, "contentId": 275236, "programLabel": None},
              "payLoad": {"messageTrackListGroup": None, "contentTrackListGroup": None,
                          "interactTrackListGroup": {"name": "互动分组1", "list": [
                              {"trackId": 3781, "trackName": "275236", "type": "redPacket", "priority": None,
                               "serializable": None, "list": [
                                  {"fragmentId": 2822, "interactName": "10s红包", "startOffset": 10000, "endOffset": "",
                                   "webUrl": "https://lichee.kaikeba.com/redpacket?passwordRedpackId=1121&content_id=123456",
                                   "mobileUrl": "https://lichee.kaikeba.com/redpacket?passwordRedpackId=1121&content_id=123456",
                                   "type": "redPacket"}]}]}}}
    headers = {'authorization': 'Bearer ' + token,
               'content-type': 'application/json'}
    payload = json.dumps(jsons)
    res1 = requests.put(url=url, headers=headers, data=payload)
    print(res1.text)
    # time.sleep(3)
    # 创建千人千面直播
    create_drama_url = "https://test-vlc-admin-api.kaikeba.com/operation/dramaLive"

    create_josns = {"name": "自动化测试abc", "businessId": "16", "type": 2, "businessName": "人才服务", "productName": "Java后端",
                    "subProductName": "java2", "spuName": "产品", "spuId": "21", "productId": "1", "subProductId": "216",
                    "programId": id, "programName": "测试zp0415", "updateUserName": "任泽鹏", "createUserName": "任泽鹏",
                    "duration": 696465}
   # res2 = requests.post(url=create_drama_url, json=create_josns, headers=headers)

    # print(res2.json())
    # 获取千人千面列表
    list_json = {"condition": {"productId": None, "subProductId": None}, "page": 1, "size": 10}
    list_url = "https://test-vlc-admin-api.kaikeba.com/operation/dramaLive/pageList"
    #res3 = requests.post(url=list_url, headers=headers, json=list_json)
   # data = res3.json().get('data')['records']
    # for i in url:
    #    print(i)
   # url = data[0]['url']
    print("该链接为：" + url)


if __name__ == '__main__':
    func_interact()
