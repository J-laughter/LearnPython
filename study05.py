'''
    列表生成器(List Comprehensions)
'''

# 生成简单的数字序列（1~10）
L1 = list(range(1,11))

# 生成 数字 的平方序列
L2 = [x*x for x in L1]
print(L2)      # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 双循环生成全排列
L1 = '123456'
L3 = [x+y for x in L1[:3] for y in L1[-3:]]
print(L3)      # ['14', '15', '16', '24', '25', '26', '34', '35', '36']

import os
fileList = [f for f in os.listdir('.')]
print(fileList)  #['.git', '.vscode', 'shudy01.py', 'study02.py', 'study03.py', 'study04.py', 'study05.py']

# for 循环使用多个变量
dic = {'A':1,'B':2,'C':3}
for key,value in dic.items():
    print(key,'=', value)

# 练习
L = ['Hello','World','IBM',21,'BAT']
L = [s.lower() for s in L if isinstance(s,str)]
print(L)    #['hello', 'world', 'ibm', 'bat']


'''
    生成器
    如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
    这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator
'''
# list与generator 比较
L = [x*x for x in range(10)]
print(L)
g = (x*x for x in range(10))  # generator 第一种定义方法 ，与list相比 [] -> ()
print(g)     # <generator object <genexpr> at 0x000001A74D05FC50>
next(g)      # 0
next(g)      # 1
for e in g:
    print(e)  #  4 9 16 25 36 49 64 81  （这里是从1的下一个值开始的）
# generator 保存的是算法，每次调用next（g）就计算出g的下一个元素的值。

# generator第二种定义方法 yield 关键字
# 实现斐波那契数列
# 每当执行到 yield 关键字就中断，即每次只计算下一个值
def fib(max):
    n,a,b = 0,0,1
    while(n<max):
        yield b
        a,b = b,a+b
        n+=1
    return 'done'
for x in fib(10):
    print(x)      # 1 1 2 3 5 8 13 21 34 55  返回值没有 done
# 要获取到 return 的内容，需要捕获 StopInteration 错误
f = fib(5)
while True:
    try:
        x = next(f)
        print('fib:',x)
    except StopIteration as e:
        print('GeneratorExit value：',e.value)
        break
# 输出如下：
# fib: 1
# fib: 1
# fib: 2
# fib: 3
# fib: 5
# GeneratorExit value： done

# 练习
def triangles():
    L = [1]
    while True:
        yield L
        L = [1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]

n = 0
res = []
for t in triangles():
    print(t)
    res.append(t)
    n+=1
    if(n==10):
        break

''' 输出如下：
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
[1, 7, 21, 35, 35, 21, 7, 1]
[1, 8, 28, 56, 70, 56, 28, 8, 1]
[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
'''

'''
    迭代器
    可以直接作用于for循环的对象统称为可迭代对象：Iterable
    可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
'''
# 生成器都是 Iterator 对象
# list、tuple、dic、str等都是 Iterable，但不是Iterator
# 使用 iter() 函数可将上述几种列表变成 Iterator
from collections import Iterator
print(isinstance(L,Iterator))         # False
print(isinstance(iter(L),Iterator))   # True

