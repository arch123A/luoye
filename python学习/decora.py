def d1(fun):
    print("装饰器2")
    def inner(*args,**kwargs):
        print("装饰器11111111")
        return fun(*args,**kwargs)
    return inner

def d2(fun):
    print("装饰器1")
    def inner(*args,**kwargs):
        print("装饰器2")
        return fun(*args,**kwargs)
    return inner

def fun(sd, b, *args, **kwargs):
    b=1
    print(b)
    print(b)
    print(args)
    print(kwargs)

class T():
    def __init__(self, cc):
        self.func=func

    def __call__(self, *args, **kwargs):
        print("这是一个类装饰器")
        return self.func(*args,**kwargs)



@T
def test1(a):
    print("test1%s"%(a))

def test2(*args,**kwargs):
    print("test2")
    print("name")
    print(*args)
    print(args)
    print(kwargs)
    print(kwargs)

if __name__ == '__main__':
    # test2('ttttt',1111,2222,name="ssddsds",b="dsdsdsds")
    test1(",args")