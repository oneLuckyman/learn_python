# 下面的代码会运行出什么结果？

lst = [1,2,3,4,5]
g = (n for n in lst if n in lst)
lst = [0,1,2]
print(list(g))

# 结果是[1,2]
# 原因是g中的第一个lst在g被定义时就已经确定，而第二个lst在g被运行时才确定。
# 等价于下面的代码

lst1 = [1,2,3,4,5]
g = (n for n in lst1 if n in lst2)
lst2 = [0,1,2]
print(list(g))

# 练习
lst = [1,2,3]
g = ((a, b) for a in lst for b in lst)
lst = [1,2]
print(list(g))

# 结果是[(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]