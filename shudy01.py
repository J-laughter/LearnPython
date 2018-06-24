# list 列表 python内置的一种有序集合
fruits = ['apple','orange','watermelon']

# append()方法，追加元素到末尾
fruits.append("strawberry")
print(fruits)

# 索引从 0 开始， -1 表示最后一个，以此类推
print(fruits[-1])

# insert()方法，将元素插入到指定下标位置
fruits.insert(2,'lemon')
print(fruits)

# len() 方法，获取list长度
print(len(fruits))

# pop()方法，删除list末尾元素，pop(i) 方法，删除指定下标位置元素
fruits.pop()
fruits.pop(0)
print(fruits)

# list里面元素替换，直接用下标
fruits[1] = 'apple'
print(fruits)

# list中元素数据类型可以不同,也可以为list（这时可看做二维数组）
fruits.append(123)
print(fruits)
fruits.pop()
food = ['rice',fruits,'meat']
print(food)
print(food[1][1])
print(len(food))


# tuple 也是python内置的一种有序列表，但tuple一旦初始化就不能修改
vegetables = ('tomato','potato','cucumber',fruits)
print(vegetables)

# 所谓的一旦初始化就不能修改 是指 “指向不变”
# vegetables 中第四个元素是指向fruits的，而fruits是一个可变的list
# vegetables 初始化时指向了fruits，不能修改为别的对象
# 即 vegetables[3]不能修改，但是vegetables[3][i]可以修改
fruits.append('lemon')
print(vegetables)

