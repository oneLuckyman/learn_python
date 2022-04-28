#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从B站视频'BV19U4y1d79C'学习：Python类装饰器

import time 

class Timer:
    def __init__(self, func) -> None:
        self.func = func 

    def __call__(self, *args, **kwargs):            # 定义__call__方法，可以将Timer对象的实例变成一个callable对象
        start = time.time()
        ret = self.func(*args, **kwargs)
        end = time.time()
        print('time cost: %s' % (end - start))
        return ret

@Timer
def add(a, b):
    return a + b 

# @Timer等价于 add = Timer(add)
# 这就相当于，把 add 转变成了Timer类的一个实例

print(type(add))
print(add(2, 3))