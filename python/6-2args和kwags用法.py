def test2(a,b,*args,**kwargs):
    print ("-------------")
    print (a)
    print (b)
    print (args)
    print (kwargs)

def test1(a,b,*args,**kwargs):
    print (a)
    print (b)
    print (args)
    print (kwargs)
    # test2(a,b,args,kwargs)  # 相当于传递test(11,22,((33, 44), {'name': 'lili', 'age': 33}))
    # test2(a,b,*args,kwargs)  # 相当于传递test(11,22,(33, 44, {'name': 'lili', 'age': 33}))
    test2(a,b,*args,**kwargs) # 相当于传递test(11,22,33, 44,name='lili', age=33)

if __name__ == '__main__':
    test1(11,22,33,44,name="lili",age=33)



