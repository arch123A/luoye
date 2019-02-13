import  time
import turtle
pen=turtle.Pen()
pen.speed(0)

def draw_line(pen,x,y,length):
    """用来画横线的函数"""
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.forward(length)

d=40
y=400
x=-400
pen.right(90)
for i in range(19):
    pen.right(270)
    draw_line(pen,-400,y,720)
    y=y-d
    pen.right(90)
    draw_line ( pen, x, 400, 720 )
    x = x + d



#画天元和星位
for j in [280,40,-200]:
    for i in [3,9,15]:
        pen.up()
        pen.goto(-400+i*40-10,j)
        pen.begin_fill ()
        # pen.fillcolor" ")
        pen.down()
        pen.circle ( 10)
        pen.end_fill ()


time.sleep(10)
