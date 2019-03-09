num=1000
count=0
while num<10000:
    qianwei=num//1000
    baiwei=(num//100)%10
    shiwei=(num//10)%10
    gewei=num%10

    if qianwei==gewei and baiwei==shiwei:
        print(num)
        count+=1
    num=num+1
print(count)