import pickle
def a():
    try:
        f=open('ab.txt','r+',encoding='utf-8')
        print(f.readline())
    except OSError as r:
        print("打开文件出错了,原因是：",r)

m='sdsdsddfdfdf因'
def pk_dump(file,v):
    "打开文件file，若文件不存在则新建，存在则覆盖,保存变量v"
    try:
        with open(file,'wb') as p:
            pickle.dump(v,p)
            p.close()
    except OSError as r:
        print("打开文件出错了,原因是：",r)

def pk_load(file):
    "打开文件file,从文件中读取变量"
    try:
        with open(file, 'rb') as p:
            v=pickle.load(p)
            p.close()
            return v
    except OSError as r:
        print("打开文件出错了,原因是：",r)



try:
    # int('abc')
    a=1+'1'
    f=open("aas.txt",'r+')
    f.close()
except(ValueError,TypeError,OSError) as r:
    print('错误的原因是：',r)

f="ab.pk"
pk_dump(f,m)
a=pk_load(f)
print(a)


