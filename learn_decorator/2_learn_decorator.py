#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 用作装饰器的函数，可以输出函数也可以输出别的数据，但一般不会让装饰器输出别的数据。

def dec(f):
    return 1

@dec
def double(x):
    return x * 2

# 上面这个函数完全等价为以下代码：
double = dec(double)
# 因为dec(f)最后return了1，所以下面这行代码会打印1
print(double)
