网址：http://www.runoob.com/python/python-reg-expressions.html

汉字正则编码：例如：([\u4e00-\u9fa5]{2,4})
re.search方法
 re.search 扫描整个字符串并返回第一个成功的匹配。'.span'可以找到匹配的序号

re.match与re.search的区别
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
(?P...)' 分组匹配
例：身份证 1102231990xxxxxxxx
s = '1102231990xxxxxxxx'
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{3})',s)
print(res.groupdict())
此分组取出结果为：
{'province': '110', 'city': '223', 'born_year': '199'}
检索和替换
Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。
语法：re.sub(pattern, repl, string, count=0, flags=0)
repl : 替换的字符串，也可为一个函数。
实例 1
import re 
phone = "2004-959-559 # 这是一个国外电话号码" 
# 删除字符串中的 Python注释 
num = re.sub(r'#.*$', "", phone)
print "电话号码是: ", num 
# 删除非数字(-)的字符串 
num = re.sub(r'\D', "", phone)
print "电话号码是 : ", num
以上实例执行结果如下：
电话号码是:  2004-959-559 
电话号码是 :  2004959559
实例2
# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

 s= 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
执行输出结果为：A46G8HFD1134

re.compile 函数
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。

语法格式为：re.compile(pattern[, flags])
参数：pattern : 一个字符串形式的正则表达式
flags : 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
re.I 忽略大小写
re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
re.M 多行模式
re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
re.X 为了增加可读性，忽略空格和 # 后面的注释
也可开头？a下列字母['a', 'i', 'L', 'm', 's', 'u', 'x']放在开头，第一个字符对应 一种匹配标志
re-M多行式，re-I忽略大小写，，re-A只匹配ASCII字符。
#re.search ，在字符串中搜索正则表达式第一次出现的位置.的位置，是从零开始算起的。
#re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
groups()返回整个匹配组的元组。

例1

>>> pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写

>>> m = pattern.match('Hello World Wide Web')

>>> print m                               # 匹配成功，返回一个 Match 对象

<_sre.SRE_Match object at 0x10bea83e8>

>>> m.group(0)                            # 返回匹配成功的整个子串

'Hello World'

>>> m.span(0)                             # 返回匹配成功的整个子串的索引

(0, 11)

>>> m.group(1)                            # 返回第一个分组匹配成功的子串

'Hello'

>>> m.span(1)                             # 返回第一个分组匹配成功的子串的索引

(0, 5)

>>> m.group(2)                            # 返回第二个分组匹配成功的子串

'World'

>>> m.span(2)                             # 返回第二个分组匹配成功的子串

(6, 11)

>>> m.groups()                            # 等价于 (m.group(1), m.group(2), ...)

('Hello', 'World')

>>> m.group(3)                            # 不存在第三个分组

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

IndexError: no such group



findall
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。

注意： match 和 search 是匹配一次 findall 匹配所有。

语法格式为：findall(string[, pos[, endpos]])
pattern = re.compile(r'\d+')   # 查找数字

result1 = pattern.findall('runoob 123 google 456')

result2 = pattern.findall('run88oob123google456', 0, 10)

 

print(result1)

print(result2)

输出结果：

['123', '456']
['88', '12']


re.split
split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：

re.split(pattern, string[, maxsplit=0, flags=0])
