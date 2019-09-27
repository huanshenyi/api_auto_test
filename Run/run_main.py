import json
import sys
import os
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from Util.handle_excel import excel_data
from Util.handel_result import handel_result_json
from Util.handel_result import handel_result, get_result_json
from Base.base_request import request
from Util.handle_cookie import get_cookie_value


# ['001', '登録', 'Yes', None, 'Login', 'Post', '{“username”:”111111”}', 'Yes', 'message', None, None, None]
class RunMain:
    def run_case(self):
        rows = excel_data.get_rows()
        cookie = None
        for i in range(rows):
            data = excel_data.get_rows_value(i + 2)
            is_run = data[2]
            if is_run == "yes":
                method = data[5]
                # アクセスのapi
                url = data[4]
                data1 = data[6]
                # 予想結果判断の方法
                excepect_method = data[8]
                # 予想結果
                excepect_result = data[9]
                # クッキーの操作
                cookie_method = data[7]
                if cookie_method == "yes":
                    cookie = get_cookie_value("app")
                res = request.run_main(method, url, data1, cookie)
                # print(res)
                # 結果と予想結果を比較する
                # サーバーのerrorCode
                code = str(res["errorCode"])
                message = res["errorDesc"]
                if excepect_method == "mec":
                    config_message = handel_result(url, str(code))
                    if message == config_message:
                        excel_data.excel_write_data(i+2, 11, "成功")
                        print("テスト成功")
                    else:
                        excel_data.excel_write_data(i + 2, 11, "失敗")
                        # 失敗する場合は結果値も記入
                        excel_data.excel_write_data(i + 2, 12, json.dumps(res))
                        print("case失敗")
                elif excepect_method == "errorcode":
                    if excepect_result == code:
                        excel_data.excel_write_data(i + 2, 11, "成功")
                        print("テスト成功")
                    else:
                        excel_data.excel_write_data(i + 2, 11, "失敗")
                        # 失敗する場合は結果値も記入
                        excel_data.excel_write_data(i + 2, 12, json.dumps(res))
                        print("case失敗")
                elif excepect_method == "json":
                    # err_codeに基づいての判断
                    if code == "1000":
                        status_str = "success"
                    else:
                        status_str = "error"
                    excepect_result = get_result_json(url, status_str)
                    # サーバーからのリスポンスとjsonデータ比較
                    result = handel_result_json(res, excepect_result)
                    if result:
                        excel_data.excel_write_data(i + 2, 11, "成功")
                        print("テスト成功")
                    else:
                        excel_data.excel_write_data(i + 2, 11, "失敗")
                        # 失敗する場合は結果値も記入
                        excel_data.excel_write_data(i + 2, 12, json.dumps(res))
                        print("case失敗")
                # break


if __name__ == "__main__":
    run = RunMain()
    run.run_case()
