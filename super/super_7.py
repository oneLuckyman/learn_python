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
        # 现在回到最常用的这种用法上
        super().__init__(age, name)
        # 这种不传入任何参数的用法只能在类的方法定义中使用
        # 如果不传入任何参数，super()会自动寻找自己所在的类，放入第一个参数，然后寻找自己所在的函数，把函数的第一个参数放入自己的第二个参数

        self.gender = "male" 

m = Male(32, "Peter")
op(m)