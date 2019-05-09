# import timeit
#
# print timeit.timeit("sum(x)","x=(i for i in range(100))")

from timeit import timeit
from timeit import  Timer


def t1():
    li=[]
    for i in range(10000):
        li.append(i)


def t2():
    li=[]
    for i in range(1000):
        li.insert(0,i)

def t3():
    li = []
    for i in range(1000):
        li.extend([i])


# timeit(函数名_字符串，运行环境_字符串，number=运行次数)
te1 = timeit('t1()', 'from __main__ import t1', number=1000)
print(te1)
# te2 = timeit('t2()', 'from __main__ import t2', number=1000)
# print(te2)

te3=Timer('t1()', 'from __main__ import t1')
print(te3.timeit(1000))
