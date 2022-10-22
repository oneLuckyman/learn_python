# python 是如何实现变量私有化的
class A:
    def __init__(self) -> None:
        self.__v = 0

# 实际上 python 只是在“编译期”把 __v 变成了 _A__v
# 所谓编译就是将 python 代码转换为 python 虚拟机要运行的字节码
# 即在私有变量前加上_class-name → _class-name__private-variable，直接访问该变量即可访问私有成员
o1 = A()
print(o1._A__v)

# 所以 python 的私有化成员只是为了防止成员的误用以及避免不希望发生的继承，而非强制不允许访问

# 同时，因为这些成员是在“编译期”私有化的，所以要避免使用类似以下几种用法
class B:
    def __init__(self) -> None:
        setattr(self, "__v", "0")

o2 = B()
print(o2.__v)       # 这是可以调用的

class C:
    def __init__(self) -> None:
        pass

o3 = C()
o3.__dict__["__v"] = 0
print(o3.__v)       # 这也是可以调用的

def f(self):
    self.__v = 0
class D:
    __init__ = f

o4 = D()
print(o4.__v)       # 这也会发生调用