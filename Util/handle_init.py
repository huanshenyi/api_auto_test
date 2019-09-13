import sys
import os
import configparser
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class HandleInit:

    def load_ini(self):
       file_path = base_path+"/Config/server.ini"
       cf = configparser.ConfigParser()
       cf.read(file_path, encoding="utf-8-sig")
       return cf

    def get_value(self, key, node=None):
        """
        iniのvalueを取得
        :return:
        """
        if node == None:
            node = "server"
        cf = self.load_ini()
        try:
            data = cf.get(node, key)
        except Exception:
            print("値に誤りがあります")
            data = None
        return data


handle_init = HandleInit()

if __name__ == "__main__":
    h = HandleInit()
    print(h.get_value(key="は", node="test"))
