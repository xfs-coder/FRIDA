import requests
import time
import json


def get_login_auth_cipher_asymmertric(username, password, timestamp):
    url = "http://127.0.0.1:5000/auth/"
    params = {
        "clienttype": "LGE Nexus 5X",
        "systemversion": "6.0.1",
        "deviceUid": "xxx", #抓包获取
        "userLoginName": username, # account
        "timestamp": timestamp, 
        "authentication": password, # password
        "v": "100",
        "t": "234"
    }
    login_auth_cipher_asymmertric = requests.get(url, params=params).json()['ret']
    return login_auth_cipher_asymmertric


def login(username, password, timestamp):
    login_url = "https://***/login/client/userLoginNormal" # 抓包获取登陆url
    headers = {
        "Accept": "application/json",
        "User-Agent": "LGE Nexus 5X/7.7.0",
        "Content-Type": "application/json; charset=UTF-8",
        "Content-Length": "687",
        "Host": "***", # 抓包获取
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"

    }
    login_auth_cipher_asymmertric = get_login_auth_cipher_asymmertric(username, password, timestamp)
    # 抓包获取替换部分字段信息
    data = {"headerInfos":{"code":"userLoginNormal","timestamp":timestamp,"clientType":"#7.7.0#channel27#LGE Nexus 5X#","shopId":"20002","source":"110003","sourcePassword":"Sid98s","token":"null","userLoginName":username},"content":{"attach":"test","fieldData":{"systemVersion":"6.0.1","androidId":"xxx","loginAuthCipher":"","loginType":"4","phoneNum":username,"loginAuthCipherAsymmertric":login_auth_cipher_asymmertric,"authentication":password,"deviceUid":"xxx","isChinatelecom":"","accountType":""}}}
    response = requests.post(login_url, data=json.dumps(data), headers=headers)
    print(response.json())


if __name__ == '__main__':
    username = "xxx" # 登陆账号
    password = "xxx" # 登陆密码
    timestamp = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    login(usename, password, timestamp)