import time
import turtle as t
a=t.Pen()
a.speed(1)
a.up()
a.goto(0,400)
a.down()
for h in range(4):
    a.forward(100)
    a.right(90)
    a.forward(100)
    a.right(90)
    a.forward(100)
    a.left(90)
    a.forward(100)
    a.left(90)


time.sleep(10)