import sys
import os
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import configparser


file_path = base_path+"/Config/server.ini"
cf = configparser.ConfigParser()
cf.read(file_path)
data = cf.get("server", "host")
print(data)