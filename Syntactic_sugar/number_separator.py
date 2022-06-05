# 语法糖：数字分隔符(number separator)

# 如果想表示一个很大的数字，例如10亿

# 普通表示法
a = 1000000000
print(a)

# 使用数字分隔符
a = 1_000_000_000
# 或者
a = 10_0000_0000

# 对于10亿这个数，当然也可以使用科学计数法
a = 1e9

# 但是如果要表示10亿零1，或者其他很大但又不整的数的时候，使用科学计数法就不方便了，但是数字分隔符仍然很好用
a = 10_0000_0001
b = 10_0000_0000.0000_0000_1          # 10亿点000000001，当然这只是个例子，实际上python的精度达不到这么高