import requests
import logging
import os,sys
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

token = admin_login_token()


headers = {'authorization': 'Bearer '+ token ,
           'content-type': 'application/json'}
list_json = {"condition": {"productId": None, "subProductId": None}, "page": 1, "size": 10}
list_url = "https://test-vlc-admin-api.kaikeba.com/operation/dramaLive/pageList"
res3 = requests.post(url=list_url, headers=headers, json=list_json)
result = res3.text.encode()
print(type(result))
code = res3.status_code
print(result)
print(type(code))
#print(res3.text)

def logger():
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.DEBUG)

    # 追加写入文件a ，设置utf-8编码防止中文写入乱码
    test_log = logging.FileHandler('test.log', 'a', encoding='utf-8')

    # 向文件输出的日志级别
    test_log.setLevel(logging.DEBUG)


    ch = logging.StreamHandler()  # 可以向屏幕发送日志

    #fm = logging.Formatter('%(asctime)s %(message)s')  # 打印格式
    # 向文件输出的日志信息格式
    formatter = logging.Formatter(
        '%(asctime)s - %(filename)s - line:%(lineno)d - %(levelname)s - %(message)s -%(process)s')

    test_log.setFormatter(formatter)

    #test_log.setFormatter(fm)
    #ch.setFormatter(fm)
    # 加载文件到logger对象中

    logger.addHandler(test_log)
    logger.addHandler(ch)
   #logger.setLevel('DEBUG')  # 设置级别

    # logger.info('info')
    # logger.debug('debug')
    # logger.warning('warning')
    # logger.error('error')
    # logger.critical('critical')
    return logger

logger = logger()



logging.error(code)