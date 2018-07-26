'''
    返回函数
    高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
'''

# 求和
def lazy_sum(*args):
    def sum():
        s = 0
        for x in args:
            s = s + x
        return s
    return sum

# 返回结果为 sum（）函数
print(lazy_sum(1,2,3,4,5))     # <function lazy_sum.<locals>.sum at 0x00000260ACFBABF8>
f1 = lazy_sum(1,2,3,4,5)
f2 = lazy_sum(1,2,3,4,5)

# 调用函数 f() 时，才返回结果
print(f1())                    # 15

# 每次调用 lazy_sum() 函数，都会返回一个新函数，因此f1和f2的调用结果互不影响
print(f1 == f2)                # False

'''
    闭包
    上述 lazy_sum() 函数中定义了一个sum()函数，内部sum()函数可以引用外部lazy_sum()函数的参数和局部变量，当lazy_sun()函数
    返回sum()函数时，相关参数和变量都保存在返回的函数中，这种程序结构称为“闭包”。
'''
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f3,f4,f5 = count()
# 这里在count()函数中生成了三个函数，i=1、2、3时各一个，但输出结果却是 9,9,9
# 原因在于 返回的函数并没有在返回时执行，而是在调用时才执行，而在调用的时候，count()函数已经执行完，此时i=3
print(f3(),f4(),f5())       # 9 9 9
''' 因此要注意，返回闭包时，返回函数尽量不要引用任何循环变量，或者会发生变化的变量 '''

# 如果一定要引用循环变量，就需要再创建一个函数，用于将该函数的参数绑定循环变量当前的值

# 修改上面的代码如下
def count_1():
    fs = []
    def f(k):
        def g():
            return k*k
        return g
    for i in range(1,4):
        fs.append(f(i))          # 这里f(i)被执行，因此i的当前值与g()函数绑定
    return fs

g1,g2,g3 = count_1()
print(g1(),g2(),g3())            # 1 4 9

