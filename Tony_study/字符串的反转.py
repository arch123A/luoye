from functools import reduce

a="abcdef"

# 用递归的方法反转字符串
def reverse_string(str_p):
    if len(str_p)<=0:
        return str_p
    return str_p[1:]+str_p[0]

# 用堆栈的方法反转字符串
def reverse_string_stack(str_p):
    list_a=list(a)
    result=[]
    while list_a:
        result+=list_a.pop()
    return "".join(result)

# 用for循环的方法
def reverse_string_for(str_p):
    result=[]
    for i in str_p:
        result.insert(0,i)
    return "".join(result)



if __name__ == '__main__':
    # print ( reverse_string_for(a))
    print(reduce(lambda x,y: y+x,a))