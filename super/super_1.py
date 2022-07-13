from objprint import op

# BV1FL4y1E7xK

# 下面是一个最普通的调用super 的实例
class Person:
    def __init__(self, name):
        self.name = name

class Male(Person):
    def __init__(self, name):
        super().__init__(name)
        super(Male, self).__init__(name)
        self.gender = "male"

m = Male("Peter")
op(m)