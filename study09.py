'''
    匿名函数
    关键字 lambda 表示匿名函数，冒号前面的 x 表示函数参数
    匿名函数有个限制，就是只能有一个表达式，不用写 return，返回值就是表达式结果
'''
l1 = list(map(lambda x : x*x,[1,2,3,4,5,6,7,8,9]))
print(l1)

# 匿名函数也是一个函数对象，可以把匿名函数赋值给一个变量
f = lambda x: x*x
print(f(10))

# 匿名函数也可以作为返回值返回
def sum(x,y):
    return lambda: x*x+y*y
f1 = sum(3,4)
print(f1())

# 求偶数
l2 = list(filter(lambda x: x%2==0, range(1,20)))
print(l2)