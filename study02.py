# dict python内置的字典 key-value对 ，查询算法为哈希算法，查询速度快 
score = {'math':100,'English':60,'Chinese':80}
print(score)

# 可以根据 key 查询对应的 value，key值必须是不可变对象 key不重复
# 可以直接查询（key不存在时会报错），为避免错误，可先用 in 判断
print(score['math'])
if 'PE' in score:
    print(score['PE'])
else:
    print('PE is not in score')

# 也可使用get方法，get()方法可以传递一个参数或两个参数，若传递一个参数，key不存在时返回None；
print(score.get('PE'))
# 若传递两个参数，则第二个参数用来指定key不存在时的返回值
print(score.get('PE',-1))

# 插入键值对
score['PE'] = 90
print(score)

# 删除一个键值对可用 pop() 方法
score.pop('math')
print(score)


# set 集合 无重复元素 无序  只能存放不可变的对象，如：字符串、常量
grade = set([8,2,1,2,3,4,4,5,6,1,'a','b'])
print(grade)

# 向set中添加元素,添加重复元素无效果
grade.add(10)
grade.add(1)
print(grade)

# 从set中删除元素
grade.remove(10)
print(grade)

# 弹出 set 中最左边的元素，并返回
grade.pop()
grade.pop()
print(grade)

# set可进行取交集、并集的操作
s1 = set([1,2,3,4,5])
s2 = set([3,4,5,6,7])
print(s1 & s2)
print(s1 | s2)