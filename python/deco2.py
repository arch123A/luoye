# 有一个 字典{'a':1,'b':2,'c':3},现在有一个这个需求：
# 1).向字典中添加新的键值对，如果字典中的键，已经存在，则取消添加，打印提示：键已经存在。
#
# 2).如果键不存在，则添加到字典中。（请使用装饰器来实现,顺便复习下*args和**kwargs的用法）

def add_dict(fun):
    def inner(**kwargs):
        d1=fun()
        for b in kwargs:
            if b in d1.keys():
                print("{}该键已经存在。".format(b))
            else:
                d1[b]=kwargs[b]
            print(d1)
            return d1
    return inner


@add_dict
def a1(**kwargs):
    d1 = {'a': 1, 'b': 2, 'c': 3}
    return d1



if __name__ == '__main__':
    d2={'a':"sss",'b1':"ddsssd"}
    a1(**d2)