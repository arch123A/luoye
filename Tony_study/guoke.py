import json
import os
import re

import requests


class Guoke():


    def __init__(self,  path=''):
        self.path = path
        self.url = 'https://www.guokr.com/ask/highlight/?page={}'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}

    def get_url_list(self):
        url_list = [self.url.format(i) for i in range(1,101)]
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

    def parse_url(self, url,header):
        r = requests.get(url,headers=header)
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
        request_header="""Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
                        Accept-Encoding:gzip, deflate, br
                        Accept-Language:zh-CN,zh;q=0.9
                        Connection:keep-alive
                        Host:www.guokr.com
                        Upgrade-Insecure-Requests:1
                        User-Agent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36"""

        url_list = self.get_url_list()
        header=self.hd(request_header)
        ret=re.compile(r'''<h2><a target="_blank" href="(.*?)">(.*?)</a></h2>''',re.DOTALL)
        result=[]
        # 循环得到数据
        for url in url_list:
            content=self.parse_url(url,header)
            result_list=ret.findall(content)
            result+=result_list
            # 保存数据

            print("完成了一页")
        with open ( "guoke.json", "a", encoding='utf-8' ) as f:
            json.dump ( result, f, ensure_ascii=False, indent=4 )
if __name__ == '__main__':
    g=Guoke()
    g.run()