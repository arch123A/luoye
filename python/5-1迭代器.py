class Fib():
    """迭代器的组成
"""
    def __init__(self,n):
        self.n=n
        self.num=0
        self.a,self.b=0,1

    def __iter__(self):
        return self

    def __next__(self):
        while self.num<self.n:
            self.a,self.b=self.b,self.a+self.b
            self.num+=1
            return self.a
        else:
            raise StopIteration




if __name__ == '__main__':
    f=Fib(5)
    a=list(f)
    print(a)
    # for i in f:
    #     print(i)