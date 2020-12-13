import json
import os
import re

import requests
from lxml import etree

class Tieba2():


    def __init__(self,path=''):
        self.path = path
        self.url = 'https://www.zwdu.com/book/13452/'
        self.host = 'https://www.zwdu.com'
        # //a[text()="下一页>"]/@href
        #//div[@id="list"]/dl/dd
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}


    def get_url_list(self):
        request_header="""Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
                            Accept-Encoding:gzip, deflate, br
                            Accept-Language:zh-CN,zh;q=0.9
                            Connection:keep-alive
                            Cookie:bcolor=; font=; size=; fontcolor=; width=; PPad_id_PP=4
                            Host:www.zwdu.com
                            Pragma:no-cache
                            Referer:https://www.zwdu.com/book/13452/3238699.html
                            Upgrade-Insecure-Requests:1
                            User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"""
        header=self.hd(request_header)
        self.headers=header
        response=requests.get(self.url,headers=header).content
        html = etree.HTML ( response )
        url_list = html.xpath('//div[@id="list"]/dl/dd')
        url_dict={}
        for element in url_list:
            key=element.xpath('./a/text()')[0]
            value=element.xpath('./a/@href')[0]
            url_dict[key]=value

        print(url_dict)
        return url_dict

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
        return r.content

    def make_dir(self):
        """如果文件夹不存在则新建"""
        if not self.path:
            return ""
        dir = self.path
        if not os.path.exists(dir):
            os.mkdir(dir)

    def save_file(self, file, content):

        """保存到文件中去"""
        a=""
        for i in content:
            a+=i

        try:

            with open(file, 'w', encoding="utf-8") as f:
                f.write(a)

                print("完成")
        except OSError as r:
            print("打开文件出错了,原因是：", r)

    def run(self):
        """1获得贴吧网址列表"""
       # start_url
        # 发送请求获得响应
        # 提取数据，并获得下一页地址
        # 保存
        # 进入下一页循环
        url_dict = self.get_url_list()
        for key in url_dict.keys():
            url=url_dict[key]
            res=self.parse_url(self.host+url)
            html = etree.HTML ( res )
            content=html.xpath(r'//*[@id="content"]/text()')
            print(content)
            self.save_file(r"d:\test\xji"+ "\\"+key+r".txt",content)

if __name__ == '__main__':
    g=Tieba2()
    g.run()