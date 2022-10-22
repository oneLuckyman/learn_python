# 一般的类成员变量可以通过外部访问的方式进行修改
class A:
    def __init__(self) -> None:
        self.v = 0

o1 = A()
o1.v = 1

# 通过在变量前增加至少两个下划线，尾部增加至多一个下划线的方式可以将其转变为私有变量
# 最常见的方式是在变量前增加两个下划线
class B:
    def __init__(self) -> None:
        self.__v = 0

o2 = B()
print(o2.__v)           # 这里会报错，提示没有这个属性

# 但是通过类内部的方法可以调用该属性
class C:
    def __init__(self) -> None:
        self.__v = 0

    def print_v(self):
        print(self.__v)

o3 = C()
o3.print_v()

# 也可以私有方法
class D:
    def __init__(self) -> None:
        self.__v = 0

    def __print_v(self):
        print(self.__v)

o4 = D()
o4.__print_v()