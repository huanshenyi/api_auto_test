import sys
import os
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from Util.handle_json import read_json


def get_header():
    data = read_json("/Config/header.json")
    return data


def header_md5():
    pass