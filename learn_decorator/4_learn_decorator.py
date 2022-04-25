#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 根据上一个例子，可以发现，当不同的函数都需要执行同一个操作时，就可以使用装饰器来实现。

# 例如，有另外一个函数也需要计时

import time 

def timeit(f):

    def wrapper(x):
        '''
        计算函数f的运行时间，这个函数和装饰器输入的函数take相同的参数
        '''
        start = time.time()
        ret = f(x)
        print(time.time() - start)
        return ret 

    return wrapper

@timeit 
def my_func(x):
    time.sleep(x)

@timeit
def other_func(x):
    return x * 2

my_func(1)                  # 会打印该函数的用时
print(other_func(2))        # 会打印该函数的用时，并打印other_func的返回值

# 上面就等价于下面的代码：
print('-' * 20)

def my_func(x):
    time.sleep(x)

def other_func(x):
    return x * 2

my_func = timeit(my_func)
my_func(1)

other_func = timeit(other_func)
print(other_func(2))