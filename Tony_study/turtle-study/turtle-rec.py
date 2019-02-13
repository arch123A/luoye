import time
import turtle
pen=turtle.Pen()
pen.speed(5)

i=0
a=6

while i<24:
    pen.forward(a)
    pen.right(90)
    pen.forward(a)
    a=a+10
    i=i+1

time.sleep(100)