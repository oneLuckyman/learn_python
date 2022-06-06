# 判断一个变量的范围
a = 97 
if (a >= 90 & a <= 100):
    print('成绩优秀')

if 90 <= a <= 100:
    print('成绩优秀')

# 字符串乘法
print('-' * 50)

# 列表拼接，本质是重载 __add__ 方法
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)

# 列表切片，切片居然也是语法糖
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(a[:4])
print(a[3:-3])
print(a[2::2])

# 元祖打包和解包，这个居然也是语法糖
a = (1, 2, 3)

x,y,z = a
print(x, y, z)
b = (x, y, z)
print(b)

# with语句
file_name = ''
f = open(file_name, 'r')
data = f.read()
f.close()

with open(file_name, 'r') as f:
    data = f.read()

# 列表推导式 or 列表解析式
a = [1, 2, 3, 4]
b = []
for i in a:
    b.append(i * 2)

b = [i * 2 for i in a]
print(b)