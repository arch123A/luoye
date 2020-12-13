
def m1(a):
    max1 = a[0]
    for i in a:
        if i < max1:
            max1 = i
    return max1


import random
a=list(range(2,20))
random.shuffle(a)
print(a)
print(">"*100)
print(m1(a))






