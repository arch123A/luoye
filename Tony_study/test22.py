# def dg(n):
#     if n<=1:
#         return 1
#     else:
#         return n*dg(n-1)
#
#
# print(dg(5))

# def dg(n):
#     if n<1:
#         print("error")
#         return -1
#     if n==1 or n==2:
#         return 1
#     else:
#         return dg(n-1)+dg(n-2)
#
#
#
# print(dg(4))

# import random as r
# ls1=[]
# for i in range(20):
#     ls1.append(r.randint(1,10))
#
# print(ls1)
# print(set(ls1))
import os
curreng_dir=os.getcwd()
ls1=os.listdir(curreng_dir)
j=1
for i in ls1:

    s1=i.endswith("txt")
    if s1:
        # os.rename(curreng_dir+os.sep+i,"班级名单1"+ str(j)+".txt")
        os.rename(os.path.join(curreng_dir,i),"班级名单ww"+ str(j)+".txt")

    j+=1
# print(ls1)