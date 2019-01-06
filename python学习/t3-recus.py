import random as r

a=[r.choice(range(30)) for i in range(20)]
print(a)
def rs(x):
    a=[]
    for i in x:
        if i not in a:
            a.append(i)
    return a

def count(a):
    if a==[]:
        return 0
    return 1 +count(a[1:])

def max(a):
    if len(a)==2:
        return a[0] if a[0]>a[1] else a[1]
    m=max(a[1:])
    return  a[0] if a[0]>m else m

def ma (a):
    m=a[0]
    for i in a[1:]:
        if i>m:
            m=i
    return m

print(max(a))
print(ma(a))
print(rs(a))
print(count(a))


print(list(set(a)))
