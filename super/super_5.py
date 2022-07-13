from objprint import op

class Animal:
    def __init__(self, age):
        self.age = age

class Person(Animal):
    def __init__(self, age, name):
        super().__init__(age)
        self.name = name

class Male(Person):
    def __init__(self, age, name):
        super(Person, self).__init__(age)
        # 上面的形式虽然可以运行，但是无法获得name 属性，这里转到20行

        self.gender = "male"

m = Male(32, "Peter")
super(Male, m).__init__(32, "Peter")
# 如果添加了上面的语句，就可以达到完整的初始化
# 这说明，super 并不仅仅只能在class 的定义中才能使用，可以在任何地方使用，只要给定两个参数。
# 上面的语句就执行了完整的过程：先获得m 这个object 的mro，然后从Male 的下一个位置寻找__init__()方法并调用
op(m)