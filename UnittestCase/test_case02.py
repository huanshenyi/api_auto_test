import requests
import unittest

url = "http://www.imooc.com"
data = {
    "username": "123",
    "password": '345'
}


class TestCase02(unittest.TestCase):
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

    def test_03(self):
        print("03")
        flag = True
        self.assertFalse(flag, msg="Trueではない")

    def test_04(self):
        print("04")
        flag = True
        self.assertTrue(flag)

    def test_05(self):
        flag = "111"
        self.assertEqual(flag, "111")

    def test_06(self):
        flag = "adfadda"
        s = "adf"
        self.assertIn(s, flag)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = [TestCase02("test_01")]
    suite.addTest(tests)
    # suite.addTest(TestCase01("test_01"))
    # suite.addTests()
    runner = unittest.TextTestRunner()
    runner.run(suite)