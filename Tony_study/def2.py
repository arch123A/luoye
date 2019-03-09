def max2(a,b):
    if a>b:
        return a
    else:
        return b


def max3(a,s,d):
    x=max2(a,s)
    y=max2(x,d)
    return y

a=max3(13,222,1)
print(a)

