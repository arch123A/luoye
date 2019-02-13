import time

import turtle as t
def rec(a):
    a.forward(100)
    a.left(90)
    a.fd(100)
    a.left(90)
    a.fd(100)
    a.left(90)
    a.fd(100)
a=t.Pen()
a.speed(10)
x=0
while x<=360:
    a.left(10)
    rec(a)
    x=x+10



time.sleep(10)