def r1():
    return 'xy'

x, y = 'x', 'y'

a1 = 'xy'
b1 = a1[:]
c1 = 'xy'
d1 = 'x' + 'y'
e1 = x + y 
exec("f1 = 'xy'")
g1 = r1()

print('a1', id(a1))
print('b1', id(b1))
print('c1', id(c1))
print('d1', id(d1))
print('e1', id(e1))
print('f1', id(f1))
print('g1', id(g1))

# 上面的语句只有 e1 的 id 与其他变量不同

def r2():
    return 'x y'

x, y = 'x', 'y'

a2 = 'x y'
b2 = a2[:]
c2 = 'x y'
d2 = 'x' + ' ' + 'y'
e2 = x + ' ' + y 
exec("f2 = 'x y'")
g2 = r2()

print('a2', id(a2))
print('b2', id(b2))
print('c2', id(c2))
print('d2', id(d2))
print('e2', id(e2))
print('f2', id(f2))
print('g2', id(g2))

# 上面的语句中 e2 和 f2 的 id 分别与其他变量不同