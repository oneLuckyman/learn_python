#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 现在看一看类的装饰器
# 通常来说，直接print一个实例不会打印任何有价值的信息，但是通过重载__str__方法，就可以打印出来
# 但是，每个类都写一遍的话就很麻烦，所以这里可以通过为类写装饰器实现简单的复用

def add_str(cls):                           # 这个函数作为一个类的装饰器，输入参数是一个类，返回值也是一个类
    def __str__(self):
        return str(self.__dict__)           # 自定义的__str__方法，返回__dict__的字符串形式
    cls.__str__ = __str__                   # 将类自带的__str__方法替换成自定义的__str__方法
    return cls

@add_str 
class Myobject:
    def __init__(self, a, b):
        self.a = a 
        self.b = b

# @add_str同样是等价于Myobject = add_str(Myobject)

o = Myobject(1, 2)
print(o)                    