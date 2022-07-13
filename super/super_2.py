from objprint import op

class Person:
    def __init__(self, name):
        self.name = name

class Male(Person):
    def __init__(self, name):
        # super().__init__(name)  
        
        # 但其实super 是一个class，有两个参数，第一个参数是一个type，第二个参数是一个type 或者一个object
        # super().__init__(name) 等价于下面的形式
        super(Male, self).__init__(name)
        # 这行语句具体做了什么：
        # 首先从第二个参数self 拿到它的mro，也就是(Male, Person, object)
        # 然后找到第一个参数在mro 中的位置，然后在该位置的下一个位置寻找是否有将要调用的函数，如果有就会进行调用，如果没有就会继续寻找再下一个位置直到找到
        # 本例中也就是：Person（Male 的下一个位置）的__init__()（将要调用的函数）

        self.gender = "male"

m = Male("Peter")
op(m)