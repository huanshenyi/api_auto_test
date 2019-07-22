import requests
import ssl
import json
from lxml.html import etree
import urllib3
urllib3.disable_warnings()
context = ssl._create_unverified_context()
url = "https://www.imooc.com/search/hotwords"
# data = {
#     'Name':'Value',
#     'content':'<p>this is test22222<br/></p>',
#     'ques_id':'352227'
# }
res = requests.post(url, verify=False)
print((res.text).encode('utf-8').decode("unicode_escape"))
json_res = res.json()
print(json.dumps(json_res, indent=4, ensure_ascii=False))


# url = "https://www.imooc.com/"
# res = requests.get(url, verify=False).text
# html = etree.HTML(res)
# test = html.xpath("//*[@id='nav']/ul/li[2]/a/text()")
# print(test)
