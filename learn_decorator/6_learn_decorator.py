#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 现在再来进阶一下，给装饰器本身再加上参数

import time 

def timeit(iteration):
    '''
    这里装饰器本身接受一个参数iteration
    这样就为装饰器多增加了一层
    '''
    def inner(f):
        '''
        这个inner函数就和之前不带参数的装饰器，timeit函数是等价的
        '''
        def wrapper(*args, **kwargs):
            '''
            计算函数f的运行时间，这个函数和装饰器输入的函数take相同的参数
            把该函数的输入参数改为可变参数和关键字参数，这样就可以接受任意多个参数
            或者说可以接受任意多个输入参数的函数f
            '''
            start = time.time()
            for _ in range(iteration):
                ret = f(*args, **kwargs)
            print(time.time() - start)
            return ret 
        return wrapper
    
    return inner

@timeit(1000000)
def double(x):
    return x * 2

double(2)       # 这行语句相当于执行了1000000次不加装饰器的double(2)

# 这就相当于下面的代码：
print('-' * 20)

def double(x):
    return x * 2

double = timeit(1000000)(double)
double(2)

# 继续拆解这个语句，就等价于下面这种最直观的写法
print('-' * 20)

def double(x):
    return x * 2

inner = timeit(1000000)
double = inner(double)
double(2)
