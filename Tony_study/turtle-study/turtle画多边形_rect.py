import time
import turtle as t

n = int ( input ( "你想画几边形？" ) )
a = t.Pen ()
a.speed ( 0 )
i = 1
while i <= n:
    a.fd ( 400 / n )
    a.left ( 360 / n )
    i = i + 1

time.sleep ( 10 )
