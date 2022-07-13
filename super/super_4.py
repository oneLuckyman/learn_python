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
        # 这里为父类增加了一个祖父类，如果使用下面的语句，整个过程会正确的运行下去，即先调用Person 的__init__()再调用Animal 的__init__()
        super(Male, self).__init__(age, name) 
        # 如果改为下面的语句，就会报错
        # super(Person, self).__init__(age, name) 
        # 这是因为第一个参数改为Person 后，调用的函数变成了Animal 的__init__()而这个函数只接受一个参数，而上面的语句输入了两个，但是改为下面的语句就是正确的了
        # super(Person, self).__init__(age)

        self.gender = "male"

m = Male(32, "Peter")
op(m)