#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 来看一个实际的例子

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

my_func(1)

# 上面的代码等价于下面的代码：

def my_func(x):
    time.sleep(x)

my_func = timeit(my_func)
my_func(1)
