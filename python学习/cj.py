import time
def outer(func):
    def inner():
        a=time.time()
        print("开始工作")
        func()
        b=time.time()
        print("工作结束:一共花了{}秒".format(b-a))
        print(a)
    return inner



@outer
def hi():
    time.sleep(1)
    print("hello")






if __name__ == '__main__':
    hi()

