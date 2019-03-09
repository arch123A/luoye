# 求一千以内的回文数
num=100
count=0
while num <1000 :
    baiwei= num // 100
    gewei= num % 10
    if baiwei==gewei:
        print(num)
        count+=1
    num+=1

print("1000以内一共有%d个数字"%count)