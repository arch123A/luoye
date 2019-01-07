#a为Accept:后面的head内容

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


import requests
from urllib import parse as pa
from bs4 import BeautifulSoup as bs
##import lxml
import re

a="""

Accept: application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*
Referer: http://jzzb.cqjsxx.com/CQCollect/Qy_Query/Ryxxbs/Rybabs_List.aspx
Accept-Language: zh-CN
User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; InfoPath.3)
Accept-Encoding: gzip, deflate
Host: jzzb.cqjsxx.com
Connection: Keep-Alive
Pragma: no-cache

"""

##i2=input('搜索内容：')
##i2=pa.quote(i2)

url='http://jzzb.cqjsxx.com/CQCollect/Qy_Query/Ryxxbs/Rybabs_List.aspx'

headers=hd(a)

r = requests.get(url, headers=headers)

f=open('cdc.txt','w+')
f.write(r.text)
f.close()
    
soup=bs(r.text,'html.parser')
v_state= soup.find('input', {'name': '__VIEWSTATE'}).get('value')
v_generator= soup.find('input', {'name': '__VIEWSTATEGENERATOR'}).get('value')

print(v_state)


