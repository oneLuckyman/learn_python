#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 现在把练习3中的代码改进一下

import time 

def timeit(f):

    def wrapper(*args, **kwargs):
        '''
        计算函数f的运行时间，这个函数和装饰器输入的函数take相同的参数
        把该函数的输入参数改为可变参数和关键字参数，这样就可以接受任意多个参数
        或者说可以接受任意多个输入参数的函数f
        '''
        start = time.time()
        ret = f(*args, **kwargs)
        print(time.time() - start)
        return ret 

    return wrapper

@timeit 
def my_func(x):
    time.sleep(x)

@timeit
def add(x, y):
    return x + y

my_func(1)
print('-' * 20)
print(add(2,3))