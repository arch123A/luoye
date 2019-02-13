import time
import turtle as t
a=t.Pen()
a.speed(1)
d=60
for i in range(10):
    a.up()
    a.goto(0, d)
    a.down()
    a.forward(180)
    d=d-20

time.sleep(10)
