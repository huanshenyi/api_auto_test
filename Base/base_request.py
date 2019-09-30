# すべてのrequestをパッケージ化
import requests
import json
import sys
import os
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from Util.handle_init import handle_init
from datetime import datetime
from Util.handle_cookie import write_cookie



class BaseRequest:
    def __init__(self):
        pass

    def send_post(self, url, data, cookie=None, get_cookie=None, herader=None) -> object:
        """
        post_request
        :param url:
        :param data:
        :return:
        """
        data = json.dumps(data)
        print(datetime.now())
        response = requests.post(url=url, data=data, cookies=cookie, heraders=herader)
        print(datetime.now())
        if get_cookie != None:
            """
            {"is_cookie":"app"}
            """
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie['is_cookie'])
        res = response.text
        return res

    def send_get(self, url, data, cookie=None, get_cookie=None, herader=None) -> object:
        """
        get_request
        :param url:
        :param data:
        :return:
        """
        response = requests.get(url=url, params=data, verify=False, cookies=cookie, heraders=herader)
        if get_cookie != None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie['is_cookie'])
        res = response.text
        return res

    def run_main(self, method, url, data, cookie=None, get_cookie=None, herader=None):
        """
        入口
        :param method:
        :param url:
        :param data:
        :return:
        """
        # return get_value(url)
        base_url = handle_init.get_value("host")
        if "http" not in url:
            url = base_url + url
        # print(url)
        if method == "get":
           res = self.send_get(url, data, cookie, get_cookie, herader)

        else:
           res = self.send_post(url, data, cookie, get_cookie, herader)

        try:
            res = json.loads(res)
        except:
            # res = None
            print("textの結果")
        return res


request = BaseRequest()

if __name__ == "__main__":
    request = BaseRequest()
    request.run_main('post', 'login', "{'username':'wawda'}")