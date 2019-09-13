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
from Util.handle_json import get_value



class BaseRequest:
    def __init__(self):
        pass

    def send_post(self, url, data) -> object:
        """
        post_request
        :param url:
        :param data:
        :return:
        """
        res = requests.post(url=url, data=data, verify=False).text
        return res

    def send_get(self, url, data) -> object:
        """
        get_request
        :param url:
        :param data:
        :return:
        """
        res = requests.get(url=url, params=data, verify=False).text
        return res

    def run_main(self, method, url, data):
        """
        入口
        :param method:
        :param url:
        :param data:
        :return:
        """
        return get_value(url)
        base_url = handle_init.get_value("host")
        print(base_url)
        if "http" not in url:
            url = base_url + url
        print(url)
        if method == "get":
             try:
                res = self.send_get(url, data)
             except Exception:
                print("get request中にエラー出ました", url, data)
        else:
            try:
                res = self.send_post(url, data)
            except:
                print("post request中にエラー出ました", url, data)
        try:
            res = json.loads(res)
        except:
            res = None
            print("textの結果")
        return res


request = BaseRequest()

if __name__ == "__main__":
    request = BaseRequest()
    request.run_main('post', 'login', "{'username':'wawda'}")