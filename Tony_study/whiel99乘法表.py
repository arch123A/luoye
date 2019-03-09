def 打印99表():
    j=1
    while j<=9:
        i=1
        while i<=j:
            print ( "%d×%d=%d" % (i, j, i * j), end="\t" )
            i+=1
        j=j+1
        print()
