def choose(name):
    if name=="foo":
        class Foo:
            pass
        return Foo
    else:
        class Bar():
            pass
        return Bar

class Test():
    n=1
    m=2
    def s(self):
        print("ssd")

if __name__ == '__main__':
    # A=choose("foo")
    # print(A)
    # a=A()
    # print(a)
    T2=type("T2",(),{"n":1,"m":2})
    tt=Test()
    print(tt.__dict__)
    print(Test.__dict__)