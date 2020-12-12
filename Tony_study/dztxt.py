import os
import random
import time

import requests
from lxml import etree

class Tieba():


    def __init__(self,  path='',filename='',url="http://www.dztxt.org/book_3116/"):
        self.url = url
        self.path = path
        self.filename=filename
        self.host=r'https://www.dswx.cc/html/18/18986/'
        # self.url = 'https://tieba.baidu.com/f?ie=utf-8&kw={}'.format(theme)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}

    def get_url_list(self):

        h="""Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
            Accept-Encoding: gzip, deflate
            Accept-Language: zh-CN,zh;q=0.9
            Cache-Control: max-age=0
            Connection: keep-alive
            Host: www.dztxt.org
            Upgrade-Insecure-Requests: 1
            User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"""
        hd=self.hd(h)
        r= requests.get(self.url,headers=hd).content.decode("gbk")
        html=etree.HTML(r)
        mlist=html.xpath(r"//body/div[3]/div[3]/div[2]/ul/li/a")
        # print(r)
        print(len(mlist))
        url_list=[]
        for i in mlist:
            k=i.text
            v=i.xpath(r"./@href")[0] if len(i.xpath(r"./@href"))>0 else None
            url_list.append((k,v))
        print(url_list)
        return url_list

    def hd(self, headers):
        """处理文件头"""
        a = headers.strip('\n')
        try:
            l = a.split("\n")
            l1 = []
            l2 = []
            head = dict()

            for each in l:
                key = each.split(":")[0].strip()
                val = each.split(":", maxsplit=1)[1].strip()
                head[key] = val
            print(head)
            return head
        except:
            print("输入的header有错误")

    def parse_url(self, url):
        r = requests.get(url,headers=self.headers)
        return r.content.decode('gbk')

    def make_dir(self):
        """如果文件夹不存在则新建"""
        if not self.path:
            return ""
        dir = self.path
        if not os.path.exists(dir):
            os.mkdir(dir)

    def save_file(self, file, content):

        """保存到文件中去"""


        try:
            with open(file, 'a', encoding="utf-8") as f:
                f.write(content)
                print("完成")
        except OSError as r:
            print("打开文件出错了,原因是：", r)

    def run(self):
        """1获得贴吧网址列表"""
        url_list = self.get_url_list()
        # 如果没有则新建一个
        self.make_dir()
        file_path=os.path.join(self.path,self.filename)
        # 列表循环取内容
        chapter_num=0
        # 显示进度条
        j=len(url_list)
        for url in url_list:
            chapter_num+=1
            # 取回网址解析结果
            content = self.parse_url(url[1])
            html = etree.HTML(content)
            mlist = html.xpath(r'//div[@id="htmlContent"]/text()')
            c="\n\r"+url[0]+"\n\r"
            for i in mlist:
                c+=i
            # 写入文件
            self.save_file(file_path, c)
            print('共{}章，已经完成了{}章'.format(j,chapter_num))
            time.sleep(random.randint(3,6))

if __name__ == '__main__':
    url=r'http://www.dztxt.org/book_10595/'
    # url=r'http://www.dztxt.org/book_3116/'
    t = Tieba(path=r"d:\360Downloads",filename=r"ll.txt",url=url)
    t.run()