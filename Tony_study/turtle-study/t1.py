c=0
m=1000
for i in range(m+1):
    for j in range(m+1):
        if j-i>0:
            c+=1
print(c)