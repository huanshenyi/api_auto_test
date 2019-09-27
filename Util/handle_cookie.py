import json
import os
import sys
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from Util.handle_json import get_value, read_json, write_value
# 1.cookie取得　
# 2.cookieを記録　
# 3.cookie使用するかどうか


def get_cookie_value(cookie_key):
    """
    cookieを取得
    :param cookie_key:
    :return:
    """
    data = read_json("/Config/cookie.json")
    return data[cookie_key]


def write_cookie(data, cookie_key):
    """
    cookieを書き込む
    :param data:
    :param cookie_key:
    :return:
    """
    data1 = read_json("/Config/cookie.json")
    data1[cookie_key] = data
    write_value(data1)


if __name__ == "__main__":
    data = {
        "aaaa": "goodgood"
    }
    print(write_cookie(data, 'web'))

