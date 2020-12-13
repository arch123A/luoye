import json
from pprint import pprint

import requests



url=" https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start={}&count=18&loc_id=108288"
h="""Referer: https://m.douban.com/movie/nowintheater?loc_id=108288
User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36"""
headers={hl.split(":")[0].strip():hl.split(":",maxsplit=1)[1].strip() for hl in h.split("\n")}
print(headers)
n=0
while True:
    url=url.format(n)
    response=requests.get(url,headers=headers)
    json_data=response.content.decode()
    dict_data=json.loads(json_data)
    film=dict_data['subject_collection_items']
    print(">"*100)
    with open('douban.json','a',encoding="utf-8") as f:
        for filmx in film:
            json.dump(filmx,f,ensure_ascii=False,indent=4)
            f.write(",\n")
        print("完成保存")
    if len( film ) <18:
        break
    n+=18



