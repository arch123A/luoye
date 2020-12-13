import os
b=os.getcwd()

for i in os .walk("."):
    for j in i[2]:
        a=os.path.join(b,i[0],j)
        c=os.path.dirname(a)
        print(c+j)
        # print(a,end=":  ")
        print(os.path.getsize(a))
        # print(os.path.exists(a))







