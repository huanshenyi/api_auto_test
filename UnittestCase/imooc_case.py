import unittest
import sys
import os
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import mock
import json
import HTMLTestRunner
from Base.base_request import request

host = "http://www.imooc.com/"

def read_json():
    with open(base_path+"/Config/user_data.json") as f:
        data = json.load(f)
    return data

def get_value(key):
    data = read_json()
    return data[key]


class ImoocCase(unittest.TestCase):
    def test_banner(self):
        url = host + 'api3/beta4'
        data = {
           # 'token': '',
           # 'type': '1',
           # 'marking': '',
           # 'secrect': ''
        }
        mock_method = mock.Mock(return_value=get_value("api3/beta4"))
        request.run_main = mock_method
        res = request.run_main('post', url, data)
        self.assertEqual(res['id'], 2)

    def test_search(self):
        url = host + "search/hotwords"
        data = {

        }
        mock_method = mock.Mock(return_value=get_value("search/hotwords"))
        request.run_main = mock_method
        res = request.run_main('post', url, data)
        self.assertEqual(res['result'], 10)

    def test_new_register(self):
        username = '123111'
        url = 'register'
        data = {
            'user': username
        }



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(ImoocCase('test_banner'))
    suite.addTest(ImoocCase('test_search'))
    file_path = base_path+'/report/report.html'
    with open(file_path, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="this is title", description="Huanshenyi test")
        runner.run(suite)
    f.close()
    # unittest.main()