class A():
    color="brown"
    def __init__(self,n):
        self.name=n
    def pt(self):
        print("Name is ",self.name)


class B(A):
    def __init__(self,n):
        super().__init__(n)
        self.n2=n+"7777"
    pass

x=B("xiaom")
x.pt()
setattr(x,"age",28)
print(x.color)
print(x.n2)
print(x.age)