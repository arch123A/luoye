
#a为Accept:后面的head内容

import requests
from urllib import parse as pa
def hd(a):
    a=a.strip('\n')
    try:
        l=a.split("\n")
        l1=[]
        l2=[]
        head=dict()

        for each in l:
            key=each.split(":")[0].strip()
            val=each.split(":")[1].strip()
            head[key]=val
            
        return head
    except:
        print("输入的header有错误")

##    head=dict(zip(l1,l2))
    
##
## for each in l:
##        l1.append(each.split(":")[0])
##        l2.append(each.split(":")[1])
##
##




a="""
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.9
Host:www.pansou.com
Proxy-Connection:keep-alive
Referer:http://www.pansou.com/?q=%E7%94%B5%E5%BD%B1
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36
"""
i2=input('搜索内容：')
i2=pa.quote(i2)

url='http://www.pansou.com/'
url=url+'?q='+i2
headers=hd(a)
r = requests.get(url, headers=headers)

print(r.text)


