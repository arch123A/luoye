import sys
import os
import requests
import json
from bs4 import BeautifulSoup


class Translate():



    def __init__(self, content, path=''):
        self.path = path
        self.content = content
        self.url = 'http://m.youdao.com/translate'


    def hd(self, headers):
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

            return head
        except:
            print("输入的header有错误")


    def query_dict(self):
        params = {
            "inputtext": self.content,
            "type": "AUTO"
        }
        return params

    def parse_url(self, url, data):
        headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        }

        r = requests.post(url, data=data, headers=headers)
        return r.content.decode()

    def run(self):
        """获得百度翻译列表"""

        data = self.query_dict()
        response = self.parse_url(self.url, data=data)

        soup = BeautifulSoup(response, 'html.parser')
        title = soup.find('ul', id='translateResult').li.text
        # print(soup)
        print(title)


if __name__ == '__main__':
    content=sys.argv[1]
    t = Translate(content)
    t.run()
