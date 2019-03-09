      #9*9乘法倒序
for i in range(9,0,-1):
    for j in range(9,0,-1):
        if j>=i:
            print("{}*{}={}\t".format(j,i,i*j),end="")
    print("")
