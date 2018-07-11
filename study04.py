L = list(range(100))  # list
T = tuple(range(100))  # tuple

'''
    切片
    切片操作可对list、tuple、string等进行
    切片操作的结果和原来的数据类型相同
'''
# 索引为0可以省略不写，下面两个等同(左闭右开)
print(L[:3])
print(T[0:3])
# 倒数切片  最后一个元素索引为-1，
print(L[-3:-1])
# 左闭右开，所以要取到最后一个，就省略-1不写
print(L[-3:])

# 间隔取数
# 每5个取一个
print(L[::5])

# 截取字符串，结果依旧是字符串
print('ABCDEFG'[-5:])

# 练习：去除字符串首尾空格
def trim(str):
    while(str[:1]==' '):
        str = str[1:]
    while(str[-1:]==' '):
        str = str[:-1]
    return str

print(trim('  jia  jiand '))


'''
    迭代,即遍历
'''
# 遍历list或tuple
for ele in T[:5]:
    print(ele)

# 遍历dict
D = {'a':1,'b':2,'c':3}
# 迭代key
for key in D:
    print(key)
# 迭代value
for value in D.values():
    print(value)
# 迭代key-value对
for key,value in D.items():
    print(key,value)

# enumerate 函数  将list变成 索引-元素 对
for index,value in enumerate(L[:5]):
    print(index,value)


# 练习 寻找list中的max和min
def maxAndMin(L):
    min = max = L[0]
    for x in L:
        if(x<min):
            min = x
        elif(x>max):
            max = x
    return min,max

print(maxAndMin(L))