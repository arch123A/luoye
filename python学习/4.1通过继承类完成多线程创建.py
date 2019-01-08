import time
import threading

class A(threading.Thread):

    def __init__(self,name, *args, **kwargs):
        super(A, self).__init__(*args, **kwargs )
        self.name = name

    def run(self):
        time.sleep(1)
        print("这是线程%s" % (self.name),end="\n")


if __name__ == '__main__':
    print("开始运行。")
    a=A("1")
    b=A("2")
    #线程类会运行类中的run方法。
    a.start()
    print(threading.enumerate())  # 查看线程数。
    b.start()
    print(threading.enumerate())


