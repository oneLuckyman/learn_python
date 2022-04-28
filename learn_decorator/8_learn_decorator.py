#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 准确的说，这种方式应该被称作装饰器是一个类

import time 

class Timer:
    def __init__(self, prefix) -> None:             # 如果装饰器本身就有参数，这里的输入就不能是函数了
        self.prefix = prefix 

    def __call__(self, func):                       # 因为装饰器本身有参数，所以类的callable输入参数就变成了函数
        def wrapper(*args, **kwargs):               
            start = time.time()
            ret = func(*args, **kwargs)
            end = time.time()
            print('%s %s' % (self.prefix, end - start))
            return ret
        return wrapper

@Timer(prefix='curr_time: ')
def add(a, b):
    return a + b 

# 这时@Timer等价于 add = Timer(prefix='curr_time: ')(add)

print(add(2, 3))