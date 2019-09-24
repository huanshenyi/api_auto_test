import sys
import os
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from Util.handle_excel import excel_data
from Util.handel_result import handel_result_json
from Util.handel_result import handel_result
from Base.base_request import request



# ['001', '登録', 'Yes', None, 'Login', 'Post', '{“username”:”111111”}', 'Yes', 'message', None, None, None]
class RunMain:
    def run_case(self):
        rows = excel_data.get_rows()
        for i in range(rows):
            data = excel_data.get_rows_value(i + 2)
            is_run = data[2]
            if is_run == "yes":
                method = data[5]
                url = data[4]
                data1 = data[6]
                # 予想結果判断の方法
                excepect_method = data[8]
                # 予想結果
                excepect_result = data[9]
                res = request.run_main(method, url, data1)
                # 結果と予想結果を比較する
                # サーバーのerrorCode
                code = str(res["errorCode"])
                message = res["errorDesc"]
                if excepect_method == "mec":
                    config_message = handel_result(url, str(code))
                    if message == config_message:
                        print("case通過")
                    else:
                        print("case失敗")
                if excepect_method == "errorcode":
                    if excepect_result == code:
                        print("テスト通過")
                    else:
                        print("テスト失敗")
                if excepect_method == "json":
                    # handel_result_json()
                    pass
                # break


if __name__ == "__main__":
    run = RunMain()
    run.run_case()
