def maxfactor(n):
    # 求最大约数
    c=n//2
    while c>1:
        if n%c==0:
            print("maxfactor is %d"%c)
            return c
        c -= 1
    else:
        print("maxfactor is 1")
        return 1

# def maxgb(m,n):
#     #求两个数的最大公约数
#     c=min(m,n)
#     while c>1:
#         if m%c==0 and n%c==0:
#             return c
#         c-=1
#     else:
#         return 1

def zclist(list1,m):
    #求一个列表所有数是否都能被一个整数整除，是则返回真
    c=len(list1)-1
    while c>=0:
        if list1[c] % m !=0:
            return False
        c-=1
    else:
        return True




def maxgb(*p):
    #求几个数的最大公约数
    c=min(p)
    # print(p)
    # print(c)
    while c>1:
        if zclist(p,c):
            return c
        else:
            c=c-1
    else:
        return 1

# print(maxfactor((99)))
list2=[48,36,24,12]
# print(zclist(list2,4))
print(maxgb(*list2))