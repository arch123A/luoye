import time
import turtle
pen=turtle.Pen()
pen.speed(0)
j=40
y=400
def io(pen,x,y,length):
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.fd(length)
for w in range(19):
    io(pen,-400,y,720 )
    y=y-j
x=-400

pen.right(90)
for w in range(19):
    io(pen,x,400,720)
    x=x+j

for u in [280,40,-200]:
    for w in [3,9,15]:
        pen.up()
        pen.goto(-400+w*40-10,u)
        pen.begin_fill()
        pen.down()
        pen.circle(10)
        pen.end_fill()
time.sleep(10)