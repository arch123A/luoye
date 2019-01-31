import turtle as t
n=int(input("你想画几边形？"))
a=t.Pen()
a.speed(1)
i=1
while i<=n:
    a.fd(50)
    a.left(360/n)
    i=i+11
    
    
