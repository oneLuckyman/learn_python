# python 的 string 是一种不可变变量

# python 中的赋值操作正是将 b0 指向 a0 指向的对象
a0 = 'xy'
b0 = a0

# 在给列表做 [:] 时，是做复制操作，但是对 string 不是
# 当起始点是0，结束点是 string 的长度是 [:] 会直接返回这个 string 本身
# 详见  unicodeobject.c 的  PyUnicode_Substring 函数
a1 = 'xy'
b1 = a1[:]


# 编译成字节码时，python 会把 'xy' 装入一个常量的内存中，此后所有调用都是对此常量进行调用
a2 = 'xy'
b2 = 'xy'

# 下面语句的字节码与上面的语句完全相同，python 在编译字节码时会做优化，把所有常量优先计算出来并把相同的指向同一个对象
a3 = 'xy'
b3 = 'x' + 'y'

# 字节码显示，变量之间求和的运算只能在程序运行期间执行，因此在编译期无法先验的优化，因此新产生的 b4 就和 a4 不同了
x, y = 'x', 'y'
a4 = 'xy'
b4 = x + y 

# python 在编译期会建立一个 const_cache 用于缓存各种常量
# 每当程序中出现新的常量，python 就会从缓存中寻找该常量是否出现过，如果有就会指向它
# 详见 compile.c 
def g():
    return 'xy'

a5 = 'xy' 
b5 = g()
# 事实上 python 中的常量和变量名采用了相同缓存机制
def f():
    xy = 'xy'
    return xy

def xy():
    pass

c = 'xy'

print(id(f.__code__.co_varnames[0]))    # 查看 f 函数保存 xy 这个名字的变量
print(id(xy.__code__.co_name))          # 查看 保存 xy 这个函数名的变量
print(id(c))                            # 查看保存 'xy' 这个 string 的变量 c 时
# 上面三者的 id 相同，指向了同一个 object

# 直接赋值和 exec 的对比
a6 = 'xy'
exec("b6 = 'xy'")
c6 = 'x y'
exec("d6 = 'x y'")

print(id(a6), id(b6))   # 没有空格的时候二者相同
print(id(c6), id(d6))   # 有空格的时候二者不同

# 在交互界面输入
# a = 'x y'
# b = 'x y'
# a is b
# False

# 但是
# a = 'xy'
# b = 'xy'
# a is b
# True

# 背后的机制称为 string interning
# 前面提到的其他机制都是在编译期完成的
# 使用 exec 函数会重新编译其内部的代码
# 所以 a6 和 b6, c6 和 d6 都不是在同一个编译期编译出来的，所以所有存在于编译期的优化对于 exec 都是没用的
# 在交互界面每一次回车都是一次新的编译，所以交互界面不使用 exec 也可以复现同样的效果

# 为什么 a6 和 b6 相同
# 在 python 的运行期，每次建立一个新的 code object 的时候，python 都会把它里面的名字和常量做一个 intern
# intern 可以理解为缓存，这表明在编译期之外的运行期，python 还有一层 string 的缓存机制
# 缓存前，对所有的常量 python 会先检查 all_name_chars()
# all_name_chars() 就是检查这个 string 是否匹配 [a-zA-Z0-9_]* 即合法变量名要求
# 在 python 中，所有的变量名和属性名都以 string 的形式保存在一个地方
# 所以为了节省内存当被检查的常量符合这样的要求时，python 才会去缓存它
# 因此，尽管 a6 和 b6, c6 和 d6 的编译期不同，在运行期仍有些许不同
# a6 与 b6 相同，因为 b6 匹配 [a-zA-Z0-9_]* 
# c6 和 d6 不同，因为 d6 不匹配 [a-zA-Z0-9_]* 