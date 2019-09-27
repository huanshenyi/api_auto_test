import json
import os
import sys
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


def read_json(file_name=None):
    if file_name == None:
        file_path = base_path+"/Config/user_data.json"
    else:
        file_path = base_path+file_name
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
    return data


def get_value(key, file_name=None):
    data = read_json(file_name)
    return data.get(key)


def write_value(data):
    data_value = json.dumps(data)
    with open(base_path + "/Config/cookie.json", "w") as f:
        f.write(data_value)


if __name__ == "__main__":
    data = {
        "app": {
            "aaaa": "bbbb"
        }
    }
    write_value(data)
