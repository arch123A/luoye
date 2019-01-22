
#a为Accept:后面的head内容
import re
import requests
from urllib import parse as pa
import time
import uuid
import random
def hd(a):
    """保存头文件设置"""
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


def save_html2_txt(a):
    """保存html文件到txt中去"""
    try:
        f=open('ab.txt','w+',encoding='utf-8')
        f.write(a)
        f.close()
    except OSError as r:
        print("打开文件出错了,原因是：",r)



def open_txt():
    """打开txt文件并且读取"""
        try:
            f=open('ab.txt','r+',encoding='utf-8')
            ra=f.read()
            f.close()
            return ra
        
        except OSError as r:
            print("打开文件出错了,原因是：",r)


def save_jpg(a):
    """保存图片"""
    name="./photo/"+str(uuid.uuid1())+".jpg"
    try:
        f=open(name,'wb')
        f.write(a)
        f.close()
    except OSError as r:
        print("文件出错了,原因是：",r)

##    head=dict(zip(l1,l2))
    
##
## for each in l:
##        l1.append(each.split(":")[0])
##        l2.append(each.split(":")[1])
##
##




a="""
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: max-age=0
cookie: dy_did=2812b94474059b7fc0d4159a00011501; acf_did=2812b94474059b7fc0d4159a00011501; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1548142081; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1548142092
referer: https://www.douyu.com/directory
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3534.4 Safari/537.36
"""
# i2=input('搜索内容：')
# i2=pa.quote(i2)




def open_jpg_url(url):
    """打开图片网址"""
    r = requests.get(url, headers=headers)
    save_jpg(r.content)



if __name__ == "__main__":

    url='https://www.douyu.com/directory/subCate/yz/790'
    headers=hd(a)
    r = requests.get(url, headers=headers)
    # save_html2_txt(r.text)
    # a=open_txt()
    url_list=re.findall(r"https://.*?_small\.jpg",r.text)
    print(url_list)
    for i in set(url_list):
        time.sleep(random.random())
        print("正在保存第%d张图片" % i)
        open_jpg_url(i)


    # print(url_list)
    # re.search(r"https://.*?\.jpg", test_str)
