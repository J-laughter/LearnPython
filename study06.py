'''
    高阶函数
'''

# 变量可以指向函数
print(abs(-10))       # 函数调用   10
print(abs)            # 函数本身   <built-in function abs>
f = abs 
print(f(-10))         # 变量指向函数  10


# 函数名也是变量
# abs = 10
print(abs(-10))       # 执行前一句后，运行报错，因为abs指向10，而不再指向绝对值函数

# 传入函数
def sum(L1,L2,f):
    return f(L1)+f(L2)

L = list(range(10))
print(L)
print(sum(L[:5],L[-5:],max))     # 将函数作为参数传入   13


'''
    map(function，Iterable)函数  
    用function对Iterable中的每个元素处理，返回一个Iterator
'''
# 求平方
# 列表生成器实现
L1 = [x*x for x in range(11)]
print(L1)                        # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# map()函数实现
def func(x):
    return x*x
L2 = list(map(func,list(range(11))))
print(L2)                        # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


'''
    reduce(function,Iterable)函数  （此处的function必须接受两个参数）
    将function作用在Iterable上，从前两个元素开始，将结果继续与下一个元素做累计计算
'''
# 求阶乘
from functools import reduce
def factorial(x,y):
    return x*y
print(reduce(factorial,list(range(11))[1:]))         # 3628800
# 字符拼接
def strAdd(x,y):
    return x+y
print(reduce(strAdd,['1','2','3','4','5','6','7','8']))   #12345678

# 将字符串list中的元素全部处理成大写字母开头
def strHandle(l):
    def strLower(s):
        return s.lower()
    def strUpper(s):
        return s[:1].upper()+s[1:]
    return list(map(strUpper,map(strLower,l)))
print(strHandle(['AmaAnda','MbT','HiGHer']))      # ['Amaanda', 'Mbt', 'Higher']

def handle(s):
    index = s.index('.')
    s = s.replace('.','')
    def char2int(c):
        return int(c)
    def mul(x,y):
        return x*10+y
    return reduce(mul,list(map(char2int,s)))/pow(10,index-1)
print(handle('1234.567'))


