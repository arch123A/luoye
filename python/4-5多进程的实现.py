import multiprocessing
import os
import time


def test1(n):
    time.sleep(1)
    print("---test1------")
    print("---test1------%d" % os.getpid())
    print (n)


if __name__ == '__main__':
    start=time.time()
    p1=multiprocessing.Process(target=test1,args=(1,))
    p2=multiprocessing.Process(target=test1,args=(2,))
    print("开始主进程了,主进程pid是%d" %os.getpid())
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("一共用了%s秒"% (time.time()-start))