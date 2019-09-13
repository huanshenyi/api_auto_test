import json
import os
import sys
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


def read_json():
    with open(base_path+"/Config/user_data.json") as f:
        data = json.load(f)
    return data


def get_value(key):
    data = read_json()
    return data[key]