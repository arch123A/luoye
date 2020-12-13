import json
import re
from pprint import pprint

import requests
url=" https://36kr.com/"
h="""Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cache-Control: no-cache
Connection: keep-alive
Host: 36kr.com
Pragma: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36"""
headers={hl.split(":")[0].strip():hl.split(":",maxsplit=1)[1].strip() for hl in h.split("\n")}
print(headers)
response=requests.get(url,headers=headers)
data=response.content.decode()
with open("36K.html","w",encoding='utf-8') as f:
    f.write(data)
ret=re.search(r"window.initialState=({.*?})</script>",data)
if ret is not None:
    a=ret.group(1)
    dict_data=json.loads(ret[0])
    list_data=dict_data['home']['banner']
    print(len(list_data))
    pprint(list_data)
# film=dict_data['subject_collection_items']
# print(">"*100)
# print( len( film ) )
# pprint(dict_data)
# with open("douban.json","w",encoding="utf-8") as f:
#     json.dump(js)
# print(json_data)


