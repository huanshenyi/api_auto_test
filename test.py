# import os
# package = str(input("Please input the package which you want to install!\n"))
# command = "pip install %s -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn" % package
# os.system(command)

import requests
from datetime import datetime

url = "https://user.bell-face.local/staff/login"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"_method\"\r\n\r\nPOST\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"data[_Token][key]\"\r\n\r\n1d780fcca001bf9467d2b50930f054659b75c44c7ab08362a7a0619895d0eca47245705fd84a16da58f63d69c78d19fa45e8c60d91cd1b8fe2ff79911986bc39\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"data[Staff][account]\"\r\n\r\n123\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"data[Staff][password]\"\r\n\r\n111\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"data[Staff][memory_password]\"\r\n\r\n0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"data[_Token][fields]\"\r\n\r\ne2ce96d858d6841536bec1598daa95156c5a2e17%3A\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"data[_Token][unlocked]:\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cookie': "_ga=GA1.2.1185148173.1554088856; _mkto_trk=id:498-VMZ-912&token:_mch-bell-face.com-1554088855897-80106; _fbp=fb.1.1554088855982.561051733; brightfilters=%7B%22rtc_on%22%3A1.6%2C%22rtc_off%22%3A1.3%2C%22flash_on%22%3A50%2C%22flash_off%22%3A25%7D; __ulfpc=201904101232387272; _vwo_uuid_v2=D45D2A32248754B4B0FF97478D79EF937|d1f1b4bd0e991b89efdc22acbb116f21; fs_uid=rs.fullstory.com`KJYME`5951735090184192:6468233227468800; intercom-id-pj8llt54=f097de9c-4544-46f4-bfee-e3c03033c56e; __adroll_fpc=0159528b9b6e9aefe0a271149c899c3b-s2-1554867169039; _gcl_au=1.1.291869524.1564466486; optimizelyEndUserId=oeu1564566077743r0.7073948975601938; optimizelySegments=%7B%7D; optimizelyBuckets=%7B%7D; __adroll_fpc=0159528b9b6e9aefe0a271149c899c3b-s2-1554867169039; pt_s_5b0bb8ec=vt=1565229331033&cad=; tutorials_64129=%7B%22start_connect%22%3A3%7D; pt_5b0bb8ec=uid=8FDGzh-v9F-xYPpL3Gk3yg&nid=0&vid=qZSAR/Db8vbN/o4VveTfzg&vn=96&pvn=9&sact=1565229336014&to_flag=0&pl=rLKt4PGgdrVWeaoUKiQu3g*pt*1565229331033; __cv_tech__uuid=889621dec9854f4bbc44bdc570554bbb; CakeCookie[beforeDocHash]=Q2FrZQ%3D%3D.r5d9vkE73KZh1SCJW7jyDYSW0svOvSLGea5rkckquj8kJBlsL8N%2BLIst3LbZB7fM4gkkbtM%2BHeAGkWir6byfVA0K9TXcu9MOtQufg0wKpWmbzl5aBwK2Vy34uqsYlyyDczw%3D; tutorials_198=%7B%22start_connect%22%3A3%7D; _gaexp=GAX1.2.MMmckYAlSciqaxpNYQeCLA.18238.1; _gid=GA1.2.1815090214.1569807710; __cv_tech__session_id_f3d90a9a425a463a890533217d7e0507=840e00f5d23e4bc0a0c259153c04b9f9; __ar_v4=336IPLAAENBM5NDKEENIGN%3A20190930%3A2%7CROOWORJ2GBHKBDUW4PRZKV%3A20190930%3A2%7CHEGH7TGI7FDWZGXJBUD4B5%3A20190930%3A2; intercom-session-pj8llt54=WVVlQWpTQ0dXZUZXOHNWaU1qT1NhZ3FWbDcwSHpVWDRDdWM3UUkxRXJ6QVVoY1RESnMzVlNHWUtkM2dHYkRGWS0tcFRGRjhkUmdpK0wwVmV2a0pZUEUyQT09--d03a992cb9748a27f3c365d4856b624f961a0049; _gat_UA-84538011-3=1; BELLFACE=g9dfgqtaqeae00rh23q2e1o13s; mp_a3b1d9d7fcc8687f2a8a657d81da706a_mixpanel=%7B%22distinct_id%22%3A%20%22169d6ea0924c00-0d3d8517df25dc-12376d51-13c680-169d6ea0925bb5%22%2C%22%24device_id%22%3A%20%22169d6ea0924c00-0d3d8517df25dc-12376d51-13c680-169d6ea0925bb5%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22mp_keyword%22%3A%20%22https%3A%2F%2Fuser.bell-face.com%2Fstaff%2Fcard%2F%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2Furl%3Fq%3Dhttps%253A%252F%252Fuser.bell-face.com%252Fstaff%252Fcard%252F%26sa%3DD%26ust%3D1554520532100000%26usg%3DAFQjCNHYCmxMzXVF9gGdOFTcyl0zLwFjdQ%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D; __ar_v4=336IPLAAENBM5NDKEENIGN%3A20190930%3A3%7CROOWORJ2GBHKBDUW4PRZKV%3A20190930%3A2%7CHEGH7TGI7FDWZGXJBUD4B5%3A20190930%3A2",
    'cache-control': "no-cache",
    'postman-token': "03994b6a-df5b-3fbf-6f67-268e7e2dc2d0"
    }
begin_time = datetime.now()
response = requests.request("POST", url, data=payload, headers=headers, verify=False)
end_time = datetime.now()
print(begin_time)
print(end_time)
print((end_time-begin_time).total_seconds())

print(response.text)