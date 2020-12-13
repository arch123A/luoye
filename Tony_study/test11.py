s1="""
01.马渝越
02.刘瀚阳
03.石瀚文
04.王文杰
05.张志诚
06.苟城豪
07.徐肃然
08.常瀚予
09.余俊昇
10.胡予宸
11.王世博
12.唐泓烨
13.曾海星
14.郑博文
15.何宇晨
16.李文瑞
17.赵元浩
18.文俊翔
19.吴锦阳
20.陈尚子
21.王若妍
22.王艺涵
23.闫妍 1
24.袁新然
25.董彦岭
26.骆彦希
27.汪子钧
28.杨涵雅
29.郑文沛
30.梁雅婷
31.徐翠敏
32.于跃悦
33.王若羲
34.向芷萱
35.裴浠为
36.曾可欣
37.郑茗予
38.陈伽余
39.王语欧
40.吴臻 
"""
s1=s1.strip("\n")
ls1=s1.splitlines()
namelist=[]
for i in ls1:
    namelist.append( i.split( "." )[1] )
print( namelist )
import pickle
import os
file_list=os.path.join("d:\\","test","namelist.pkl")
pf=open(file_list,'wb')
pickle.dump(namelist,pf)
print(file_list)
pf.close()
# print(len(ls2))

# def fx(x):
#     #闭包
#     def fy(y):
#         return x*y
#     return fy
#
#
# i=fx(2)
# print(i(5))
# print(i(6))


# g=lambda x:2*x+9
# for i in range(9):
#     print(g(i))
# # print(g(1))


# def odd(a):
#     return  not a%7

# g=lambda x: not x%7
# a1=list(filter(g,range(1,100)))
# print(a1)


g2=lambda x:2*x+5
a2=list(map(g2,range(1,10)))
print(a2)