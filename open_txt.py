import re
path='d:\\cd.txt'
p=re.compile(r'<option value="([\u4e00-\u9fa5]{1,5})">\1</option>',re.IGNORECASE)
try:
    # 编码为'gbk'错误可以换'utf-8',UTF,GBK不分大小写。汉字编码有三类，GBK，GB2312和Big5。
    with open(path,'r+',encoding='UTF-8',) as f:
        s=f.read()
        list1=p.findall(s)
        print(list1)
        # for each_line in f:
        #     print(each_line)
except OSError as reason:
    print(reason)

