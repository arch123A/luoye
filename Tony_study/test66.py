

# st="sadffsdafasdf"
# it=iter(st)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         print("finish!")
#         break


class Fl():
    a=0
    b=1

    def __iter__(self):
        return self

    def __next__(self):
        # self.c=self.a
        # self.a=self.b
        # self.b=self.b+self.c
        self.a,self.b=self.b,self.a+self.b
        if self.a>10000:
            raise StopIteration
        return self.a


# f=Fl()
# for e in f:
#     print(e)
#     # if e<1000 :
#     #     print(e)
#     # else:
#     #     break
#
