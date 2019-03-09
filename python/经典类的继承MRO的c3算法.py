#经典类的继承MRO的c3算法
# 按照深度遍历，其顺序为 [D, B, A, object, C, A, object]，
# 重复类只保留最后一个，因此变为 [D, B, C, A, object]。
class A(object):
    def show(self):
        print ("A.show()")
        print ("AAAAA")


class B(A):
    pass


class C(A):
    def show(self):
        print ("C.show()")

class D(B, C): pass


print(D.__mro__)
d=D()
d.show()

