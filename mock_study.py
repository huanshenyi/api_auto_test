import mock
import requests
import unittest


def post_request(url, data):
    res = requests.post(url, data, verify=False)
    return res


def get_request(url, data):
    # url="http://www.imooc.com/login/register?user=111&222"
    # url+data
    res = requests.get(url, params=data).json()
    return res


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        print("start")

    def tearDown(self) -> None:
        print("case_end")

    def test_01(self):
        url = "http://www.imooc.com/login/register"
        data = {
            "username": "11111"
        }
        sucess_test = mock.Mock(return_value=data)
        post_request = sucess_test
        res = post_request
        self.assertEqual("11222", res())

if __name__ =="__main__":
   unittest.main()
