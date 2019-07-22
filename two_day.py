import requests
import json
# ファイルアップロード
# url = "https://www.imoc.com/user/postpic"
# # 基本アプロードタグを参照
# file = {
#     "fileField": ("vuex.png", open(r"C:\Users\81906\Desktop\vuex.png", "rb"), "image/png"),
#     "type": "1"
# }
# cookie = {
#     "apsid":""
# }
#
# res = requests.post(url, files=file, cookies=cookie, verify=False).json()
# print(res)


# ファイルダウンロード
download_url = "http://file.mukewang.com/imoocweb/webroot/mobile/imooc7.2.010102001android.apk"
res = requests.get(url=download_url)
with open("mukewang.apk", "wb") as f:
    f.write(res.content)
print(res)