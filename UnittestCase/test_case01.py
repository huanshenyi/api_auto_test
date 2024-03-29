import requests
import unittest
import os
import sys

base_path = os.getcwd()
sys.path.append(base_path)
from Base.base_request import request

url = "http://www.imooc.com"
data = {
    "username": "123",
    "password": '345'
}

host = "http://www.imooc.com"

class TestCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("caseクラス実行開始")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def setUp(self) -> None:
        print("case実行")

    def tearDown(self) -> None:
        print("tearDown実行")

    def test_01(self):
        print("01")
        #res = requests.get(url=url, params=data, verify=False).json()
        data1 = {
            "user": "11111"
        }
        self.assertDictEqual(data1, data, msg="一致しません")

    def test_02(self):
        print("02")
        data1 = {
            "username": "123",
            "password": '345'
        }
        self.assertDictEqual(data1, data)

    @unittest.skipIf(host != "http://www.imooc.com", "03実行しない")
    def test_03(self):
        print("test03")
        flag = True
        self.assertFalse(flag, msg="Trueではない")

    @unittest.skip("04実行しない")
    def test_04(self):
        flag = True
        self.assertTrue(flag)

    def test_05(self):
        print("test05")
        flag = "111"
        self.assertEqual(flag, "111")


    def test_06(self):
        res = request.run_main("get", url, data)
        print(res)


if __name__ == "__main__":
    # suite.addTest(TestCase01("test_01"))
    # suite.addTests()
    suite = unittest.TestSuite()
    tests = [TestCase01("test_06")]
    suite.addTests(tests)
    runner = unittest.TextTestRunner().run(suite)
