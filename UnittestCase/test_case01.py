import requests
import unittest


class TestCase01(unittest.TestCase):
    def setUp(self) -> None:
        print("case実行")

    def tearDown(self) -> None:
        print("casedown")

    @classmethod
    def setUpClass(cls) -> None:
        print("caseクラス実行開始")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def test_01(self):
        print("case01")

    def test_02(self):
        print("case02")


if __name__ == "__main__":
   unittest.main()