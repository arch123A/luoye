# coding: utf-8
from gevent import monkey

monkey.patch_all()
import urllib.request
import gevent
import re


def downloader(img_name, img_url):
    content = urllib.request.urlopen(img_url)

    img_content = content.read()

    with open(str(img_name) + "_2018731200749.jpg", "wb") as img_file:
        img_file.write(img_content)


def main():
    # 读取文件中的内容
    with open("url_addr.txt", "rb") as f:
        content = f.read().decode("utf-8")
    # print(content)

    # 创建新列表，存储图片网址
    img_addr = re.findall(r"https://.*?\.jpg", content)
    # print(img_addr)

    for i in range(len(img_addr)):
        g = gevent.spawn(downloader, i + 1, img_addr[i])
        g.join()

    print("下载完毕！")


if __name__ == '__main__':
    main()
