def rm(x):
    if x==1:
        return 1
    return x*rm(x-1)


def rt(x):
    if x <=2:
        return 1
    return rt(x-1)+rt(x-2)
print(rt(6))
# print(rm(20))
def h(a,b,c,n):

    if n==1:
        print(a,"-->",c)
    else:
        h(a,c,b,n-1)
        print(a,"-->",c)
        h(b, a, c, n - 1)


h("x","y","z",3)



