import sys
import os
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from Util.handle_excel import excel_data
from Base.base_request import request


# ['001', '登録', 'Yes', None, 'Login', 'Post', '{“username”:”111111”}', 'Yes', 'message', None, None, None]
class RunMain:
    def run_case(self):
        rows = excel_data.get_rows()
        for i in range(rows):
            data = excel_data.get_rows_value(i + 2)
            is_run = data[2].lower()
            if is_run == "yes":
                method = data[5].lower()
                url = data[4].lower()
                data1 = data[6]
                request.run_main(method, url, data1)



if __name__ == "__main__":
    run = RunMain()
    run.run_case()