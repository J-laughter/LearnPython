'''
    高阶函数
'''

'''
    filter(function,Iterable) （function 返回bool值）  
    函数通过function依次作用于Iterable中的元素来决定是否保留该元素
    函数返回值为 Iterator 惰性序列
'''
# 过滤奇数
def is_odd(ele):
    return ele % 2 == 0
print(list(filter(is_odd,list(range(10)))))   # [0, 2, 4, 6, 8]


'''
    sorted
'''
# 对数字序列排序
print(sorted([2,4,1,5,7,11,3]))                    # [1, 2, 3, 4, 5, 7, 11]
# 指定reverse为True，进行反向排序
print(sorted([2,4,1,5,7,11,3],reverse = True))     # [11, 7, 5, 4, 3, 2, 1]

# 对字符串序列排序,按照首字母ASSCI排序
print(sorted(['jiang','zhao','qian','sun','li']))  # ['jiang', 'li', 'qian', 'sun', 'zhao']
print(sorted(['Jack','amanda','Bob','mike']))      # ['Bob', 'Jack', 'amanda', 'mike']
# 对序列用key指定的函数处理后的序列排序（['jack','amanda','bob','mike']）
print(sorted(['Jack','amanda','Bob','mike'],key = str.lower))    # ['amanda', 'Bob', 'Jack', 'mike']