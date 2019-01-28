import re

email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
def is_email():
    """判断是否是163邮箱"""
    for email in email_list:
        ret = re.match("^[\w]{4,20}@163\.com$", email)
        if ret:
            print("%s 是符合规定的邮件地址,匹配后的结果是:%s" % (email, ret.group()))
        else:
            print("%s 不符合要求" % email)




def is_good_tel(tels):
    """提取不是4或者7结尾的电话号码 """
    for tel in tels:
        ret = re.match("1\d{9}[0-35-68-9]", tel)
        if ret:
            print(ret.group())
        else:
            print("%s不是想要的手机号" % tel)

def find_html():
    """html中查找"""
    ret = re.match(r"^<([a-zA-Z]*?)>\w*</\1>$", "<html>hh</html>")

    if ret:
        print(ret.group())
        print(ret.group(1))


def find_html2(labels):
    for label in labels:
        ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", label)
        if ret:
            print("%s 是符合要求的标签" % ret.group())
        else:
            print("%s 不符合要求" % label)


def test_findall():
    ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
    print(ret)

if __name__ == '__main__':
    tels = ["13100001234", "18912344321", "10086", "18800007777"]
    # labels = ["<html><h1>www.itcast.cn</h1></html>", "<html><h1>www.itcast.cn</h2></html>"]
    # find_html2(labels)

    ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>","<html><h1>www.itcast.cn</h1></html>")
    print(ret.group())
    print(ret.groupdict())
    print(ret.name1)

    # ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>",
    #                "<html><h1>www.itcast.cn</h2></html>")
    # ret.group()



