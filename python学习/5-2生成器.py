def gen(n):
    """生成器生成N个数的序列"""
    a, b = 0, 1
    for i in range ( n ):
        a, b = b, a + b
        yield a


c = list ( gen ( 21 ) )
print ( c )
print ( len ( c ) )
