class Goods():
    """property的使用"""
    def __init__(self,size):
        self._size=size

    @property
    def size(self):
        return self._size
        # print(self._size)
        pass

    @size.setter
    def size(self,value):
        self._size=value

    @size.deleter
    def size(self):
        print("deleter")
        del self._size



if __name__ == '__main__':
    a=Goods(12)
    print(a.size)
    a.size=25
    print(a.size)
    del a.size
    print(a.size)




