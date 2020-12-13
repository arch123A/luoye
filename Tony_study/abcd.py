# 1 打开网页
# import urllib.request as rq
# rs=rq.urlopen("http://www.baidu.com/")
# html=rs.read()
# html=html.decode("utf-8")
# print(html)

# 2  保存图片
# import urllib.request as rq
#
# rs = rq.urlopen ( "http://tiebapic.baidu.com/forum/pic/item/26d62a738bd4b31c4ba561ff90d6277f9f2ff891.jpg" )
# content = rs.read ()
# try:
#     with open ( "gif1.gif", "wb" ) as f:
#         f.write ( content )
#         f.close()
# except:
#     print ( "open file error!" )


def hd(a):
    """
    头文件处理函数，
    :param a: request请求的字符串
    :return: 一个字典，head
    """
    a = a.strip ( '\n' )
    try:
        l = a.split ( "\n" )
        l1 = []
        l2 = []
        head = dict ()

        for each in l:
            key = each.split ( ":" )[0].strip ()
            val = each.split ( ":" )[1].strip ()
            head[key] = val

        return head
    except:
        print ( "输入的header有错误" )

