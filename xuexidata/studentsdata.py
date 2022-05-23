import requests
import json
import random
import threading
import time
###1. 获取所有的token    将token 传送到下个接口中 完成响应
###2. 做循环，  优化 入口  执行多少次，  输入输入对应的直播间id
def student_details(mobile, id):
    ###获取学员sso_token
    login_url = "https://test-api-passport.kaikeba.com/login"
    data = {'mobile': mobile, "verify_code": "111111", "remember": 1}
    req = requests.post(url=login_url, json=data)

    state = json.loads(req.text).get('data')
    print(state)
    sso_token = state['sso_token']

    ###获取学员token
    session_url = "https://test-api-passport.kaikeba.com/login/session"
    session_data = {"sso_token": sso_token, "app_id": "hky8659205629467", "platform": "pc", "expire_time": 2592000}
    res = requests.post(url=session_url, json=session_data)
    ress = res.json()
    access_token = ress['data']['access_token']
    authorization = "Bearer pc:" + access_token

    # 进入剧本直播间
    in_room_url = "https://test-vlc-live-api.kaikeba.com/drama/create-drama-live-room/" + str(id)

    headers = {
        "authorization": authorization,
        "accept": "application/json, text/plain, */*"
    }

    res = requests.get(url=in_room_url, headers=headers)
    res_json = res.json()

    print(res_json)
    return res_json

def func():


    for i in range(int(count)):
        tail_number = random.randint(999, 10000)

        mobile = "1883096" + str(tail_number)
        student_details(mobile, id)
        print("执行成功")
def things(th_count):
    for i in range(int(th_count)):
        th = threading.Thread(target=func, name="线程"+str(i),args=())
        th.start()
        time.sleep(30)
        #print("当前线程的信息:", threading.current_thread())
    print("线程数量为：", threading.active_count())

if __name__ == '__main__':
    th_count = input("请输入线程数量：")
    id = input("输入千人千面id：")
    count = input("一次执行要多少用户：")
    things(th_count)
    print("程序结束啦，总共有"+ str(int(th_count)*int(count)) +
          "个用户进入的直播间赶紧复制网址查看啦=== https://teststaff.kaikeba.com/vlc-live/live/drama/thousandsFace/detailData/" + str(id))

