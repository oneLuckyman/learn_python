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
        # super()的两个参数都是可选的，因此还有以下这种用法，但是并不多见
        ubo = super(Male)
        ubo.__get__(self).__init__(age, name)
        # 这里只给了super()一个参数，需要再进行一次操作把super() bind 到一个object 上才可以正常使用
        self.gender = "male"

m = Male(32, "Peter")
op(m)