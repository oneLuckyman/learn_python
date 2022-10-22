# 变量和方法私有化的好处

class A1:
    valid_kwds = ["a"]
    def __init__(self, **kwargs) -> None:
        for key, val in kwargs.items():
            if key in self.valid_kwds:
                print(key, val)

class B1(A1):
    valid_kwds = ["b"]
    def __init__(self, **kwargs) -> None:
        left_kwargs = {}
        for key, val in kwargs.items():
            if key in self.valid_kwds:
                print(key ,val)
            else:
                left_kwargs[key] = val
        super().__init__(**left_kwargs)

o1 = B1(a=2, b=3)     # 因为这里的 self 是 B 类，所以运行到 super().__init__() 的时候会导致函数访问 B 类的 valid_kwds 从而无法把 a=2 传给 A 类执行

# 通过把 valid_kwds 私有化可以解决这样的问题，因为私有成员不会被继承和覆盖
class A2:
    __valid_kwds = ["a"]
    def __init__(self, **kwargs) -> None:
        for key, val in kwargs.items():
            if key in self.__valid_kwds:
                print(key, val)

class B2(A2):
    __valid_kwds = ["b"]
    def __init__(self, **kwargs) -> None:
        left_kwargs = {}
        for key, val in kwargs.items():
            if key in self.__valid_kwds:
                print(key ,val)
            else:
                left_kwargs[key] = val
        super().__init__(**left_kwargs)

o2 = B2(a=2, b=3)

# 对于方法也是同样的道理，这可以防止继承类重载函数
class A:
    def __pri_show(self):
        print("A")
    def pub_show(self):
        print("A")
    def show_pri(self):
        self.__pri_show()
    def show_pub(self):
        self.pub_show()

class B(A):
    def __pri_show(self):
        print("B")
    def pub_show(self):
        print("B")

o = B()
o.show_pri()           # 这里就会打印 A 而不是 B
o.show_pub()           # 但这里会打印 B 而不是 A