import json
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

        url='https://www.qiushibaike.com/text/page/{}/'
        return [url.format(i) for i in range(1,14)]


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
        return r.content.decode()

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
            with open(file, 'w', encoding="utf-8") as f:
                f.write(content)
                print("完成")
        except OSError as r:
            print("打开文件出错了,原因是：", r)

    def run(self):
        """1获得贴吧网址列表"""

        hd="""Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
                Accept-Encoding: gzip, deflate, br
                Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
                Cache-Control: no-cache
                Connection: keep-alive
                Host: www.qiushibaike.com
                Pragma: no-cache
                Upgrade-Insecure-Requests: 1
                User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"""
        self.headers=self.hd(hd)
        url_list=self.get_url_list()
        # 列表循环取内容
        content_list = []
        for url in url_list:
            content=self.parse_url(url)
            html = etree.HTML ( content )
            mlist = html.xpath ( r'//div[@id="content-left"]/div' )

            for eliment in mlist:
                item = {}
                item['text_context_list']=eliment.xpath('./a/div[@class="content"]/span/text()')
                item['user']=eliment.xpath('.//h2/text()')[0]
                content_list.append(item)
                print(item)

        # 如果没有则新建一个
        self.make_dir()
        file_path=os.path.join(self.path,self.filename)
        content=json.dumps(content_list,ensure_ascii=False,indent=4)
        self.save_file (file_path,content)


if __name__ == '__main__':
    url=r'https://www.qiushibaike.com/text/'
    t = Tieba(path=r"d:\360Downloads",filename=r"aa.txt",url=url)
    t.run()