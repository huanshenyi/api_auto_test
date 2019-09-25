import sys
import os
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import configparser
import json
from deepdiff import DeepDiff
from Util.handle_json import get_value

# get_value("api3/getbanneradvertver2", "/Config/code_message.json")
#     {"1006": "token error"},
#     {"10001": "ユーザーネームエラー"},
#     {"10002": "パスワードエラー"}


def handel_result(url, code) -> any:
    """
    予測結果を取得
    :param url: configの内容を取得用のキー
    :param code: 実際サーバからのリスポンスのエラーcode
    :return: 状態メッセージを返す
    """
    data = get_value(url, "/Config/code_message.json")
    if data != None:
        for i in data:
            message = i.get(str(code))
            if message:
                return message
    return None


def get_result_json(url, status):
    """
    検証用のjsonデータを取得
    :param url: ターゲットになるjsonデーターを取得のキー
    :return:
    """
    data = get_value(url, "/Config/result.json")
    if data != None:
        for i in data:
            message = i.get(status)
            if message:
                return message
    return None


def handel_result_json(dict1, dict2):
    """
    json形式の確認
    :return:
    """
    # print(dict1, dict2)
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
        print(cmp_dict)
        if cmp_dict.get("dictionary_item_added"):
            return False
        else:
            return True
    return False


if __name__ == "__main__":
   dict1 = {"aaa": "AA1A", "bbb": "BB1B1", "DDD": [{"12", "22"}, {"35", "14"}]}
   dict2 = {"aaa": "AAA", "bbb": "BB1B", "DDD": [{"12", "22"}, {"35", "14"}]}
   # print(handel_result("api3/getbanneradvertver2", "10001"))
   # print(handel_result_json(dict1, dict2))
   print(get_result_json("api3/newcourseskill", "error"))
