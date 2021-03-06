import time
import threading

g_n = 0
mutex = threading.Lock ()


def test1():
    global g_n

    for i in range ( 1000000 ):
        mutex.acquire ()
        g_n += 1
        mutex.release ()
    print ( "test1中的NUM=%d" % (g_n ))


def test2():
    global g_n
    mutex.acquire ()
    for i in range ( 1000000 ):
        g_n += 1
    mutex.release ()
    print ( "test2中的NUM=%d" % g_n )


if __name__ == '__main__':
    print ( "start........" )
    t1 = threading.Thread ( target=test1 )
    t2 = threading.Thread ( target=test2 )
    t1.start ()
    t2.start ()
    time.sleep (3)
    print ( "main中的NUM=%d" % g_n )
