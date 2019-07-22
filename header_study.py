import requests
import json
# header = {
#
# }
#
# res = requests.get(url="url", headers=header, verify=False)

import hashlib
imooc = "imooc.com"
md5 = hashlib.md5()
md5.update(imooc.encode("utf-8"))
res = md5.hexdigest()
print(res)# 56d6dcc0629aa84a7184966129560997