import random


def yellow(red):
    return red * 6 + 2


# TODO 回头我继续来这写
def add(a, b):
    return a + b


def sub(tony, chreey):
    return tony - chreey


def ma(li):
    """求最大值"""
    m = li[0]
    for i in li:
        if i > m:
            m = i
    return m


def mi(blue):
    backpack = blue[0]
    for t in blue:
        if t < backpack:
            backpack = t
    return backpack


#
#
a = [60, 81, 81, 2000, 91, 63, 0, 80, 9]
b = [60, 81, 81, 2000, 91, 63, 0, 80, 9, 8]


def de(ony):
    r = 0
    for k in ony:
        r = r + 1
    return r


def lianjia(v):
    s = 0
    for i in range ( 1, v + 1 ):
        s = s + i
    return s


b = lianjia ( 100 )
print ( b )

a = """
assasasasas
asad
ssdds
"""
# TODO
print ( a )
