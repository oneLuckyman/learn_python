from objprint import op

class Person:
    def __init__(self, name):
        self.name = name

class Male(Person):
    def __init__(self, name):
        # super(Male, self).__init__(name)

        # 于是，上面的语句在此处等价于下面的形式
        Person.__init__(self, name)
        # 为什么不直接使用该形式，而使用super。
        # 是因为程序编写过程中父类的名字和继承的方式可能会更改，如果使用上面这种形式会导致大量的修改从而导致不必要的错误和麻烦
        # 另一方面，super 是一个动态的过程，因为super 的第二个参数是动态的，可能发生改变的。转super_3-1

        self.gender = "male"

m = Male("Peter")
op(m)