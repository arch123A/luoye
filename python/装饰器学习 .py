from decorator  import decorator
from functools import wraps
def outer(x):
    a=x
    def inner(y):
        b=a+y
        print(b)
    return inner

def d1(func):
    @wraps(func)
    def inner(*args,**kwargs):
        print("开始装饰器。")
        print("{}函数正在运行".format(func.__name__))
        return func(*args,**kwargs)
    return inner


@decorator
def d2(func,*args,**kwargs):
    print("{}正在运行中".format(func.__name__))
    return func(*args,**kwargs)


def d3(auth):
    def outer(func):
        @wraps(func)
        def inner(*args,**kwargs):
            print("作者是{}".format(auth))
            print("{}正在运行中".format(func.__name__))
            return func(*args,**kwargs)
        return inner
    return outer



@d3("王二")
def hi(a):
    print(a)


if __name__ == '__main__':
    hi('你好吧')
