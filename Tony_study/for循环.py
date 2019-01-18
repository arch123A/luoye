# 学习FOR循环怎么用的
#
# for i in range(1,3):
#     print(i)
#头有12只，脚有32只，假设有j只鸡，12-j只兔子
# 10，8 ，18个头，52只脚
#40,20,60,160只
#80,80,160,480只


# def jt(head,foot):
#     j=1
#     while j<=head:
#         t=head-j  # t是兔子的数量
#         if j*2+4*t==foot:
#             print("鸡有%d只，兔子有%d只！"%(j,t))
#             break
#         j=j+1


# # define function
# def jt(head,foot):
#     for j in range(0,head+1):
#         t=head-j  # t是兔子的数量
#         if j*2+4*t==foot:
#             print("鸡有%d只，兔子有%d只！"%(j,t))
#             break
#     else:
#         print("这道题没有答案")
#
#
#
#
# jt(18,60)


for i in range(100,-1,-2):
    print(i,end="@")





