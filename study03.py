import math
# 定义函数 def 语句
# 定义一个求圆周长和面积的函数
def circular(r):
    perimeter = 2*math.pi*r
    print(perimeter)
    area = math.pi*math.pow(r,2)
    print(area)

circular(2.0)

# 函数返回值为多值时，返回的其实是一个tuple，可以用多个变量来接收
def move(x,y,z):
    x = x + 1
    y = y + 1
    z = z + 1
    return z,y,z

x,y,z = move(1,1,1)
print(x,y,z)
print(move(z,y,z))

# 求解二元一次方程函数
def quadratic(a,b,c):
    d = math.pow(b,2)-4*a*c
    if d > 0 :
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        return x1,x2
    elif d == 0 :
        x = -b/(2*a)
        return x
    else:
        return "无解"

print(quadratic(2,3,1))

# 默认参数的使用,默认参数必须指向不变对象
s = {}
def student(name,age,sex,grade=7,city='Hangzhou'):
    s[name]=[age,sex,grade,city]

student('Bob',10,'boy')
student('Jack',12,'boy',8)
student('Mary',11,'girl',city='Beijing')
print(s)

# 若默认参数指向 list 等可变对象，会出现默认参数发生改变的现象
# 错误示例：
'''
def num(L = []):
    L.append('#')
    print(L)

num()  # 输出结果为 ['#']
num()  # 输出结果为 ['#','#']
'''
'''
    这是因为默认参数 L 的值在函数定义是就被计算出来，
    即：L指向对象[]，当第一次调用时，L=['#'],第二次调用时，L=['#','#']
    因此，可修改为如下形式：
'''
def num(L=None):
    if L is None:
        L = []
    L.append('#')
    print(L)

num()
num()

'''
可变参数的使用
应用场景 计算：a2 + b2 + c2 + ...
'''
# 常规思路是传入一个list或tuple
def caculate1(number):
    num = 0
    for x in number:
        num += x*x
    print(num)

caculate1([1,2,3]) # 传入一个list
caculate1((1,2,3)) # 传入一个tuple

# 使用可变参数,在参数名前加上*，则传入参数将被自动组装为一个tuple
def caculate2(*number):
    num = 0
    for x in number:
        num += x*x
    print(num)

caculate2()
caculate2(1,2,3)
# 若要传入一个已定义的list或tuple，只需在传参时在其对象变量名前加上*
num = [1,2,3,4]
caculate2(*num)

'''
    关键字参数
'''
# 当我们声明一个双星号形数时，传入的所有键值对实参都将被自动组装为一个dict
def dictionary(**dic):
    print(dic)

dictionary(a=1,b=2,c=3)
kids = {'Mike':10,'Jack':11,'Ada':12}
dictionary(**kids)

'''
    命名关键字参数：即接收指定关键字参数
'''
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person('Tian',20,city='Hangzhou',job='Coder')