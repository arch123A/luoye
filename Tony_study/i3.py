def max2(a,b):
    if a>b:
        return a
    else:
        return b

def max3(a,b,c):
    m=max2(a,b)
    m=max2(m,c)
    return m

def man(*args):
    for i in args:
        if m<i:
            m=i
    return m


list1=[4,6,7,8,19,21,0,-3,31,2,4,1,399,7]
print(man(1))


