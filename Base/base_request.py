# すべてのrequestをパッケージ化
import requests
import json


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
        if method == "get":
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        try:
            res = json.loads(res)
        except:
            print("textの結果")
        return res


request = BaseRequest()