URL_DICT={}

def  add_dict(url):
    def outer(fun):
        URL_DICT[url]=fun
        def inner(*args,**kwargs):
            return fun(*args,**kwargs)
        return inner
    return outer




@add_dict("a")
def a():
    print("aaaaaaaa")

@add_dict("b")
def b():
    print("bbbbbbb")

@add_dict("c")
def c():
    print("cccccccccccc")


if __name__ == '__main__':
    print(URL_DICT)