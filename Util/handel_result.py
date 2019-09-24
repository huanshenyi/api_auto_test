import sys
import os
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import configparser
import json
from Util.handle_json import get_value

# get_value("api3/getbanneradvertver2", "/Config/code_message.json")
#     {"1006": "token error"},
#     {"10001": "ユーザーネームエラー"},
#     {"10002": "パスワードエラー"}


def handel_result(url, code) -> any:
    data = get_value(url, "/Config/code_message.json")
    if data != None:
        for i in data:
            message = i.get(str(code))
            if message:
                return message
    return None



if __name__ == "__main__":
   print(handel_result("api3/getbanneradvertver2", "10001"))
