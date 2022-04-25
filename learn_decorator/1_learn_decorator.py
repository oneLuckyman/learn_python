#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从B站视频'BV1Gu411Q7JV'学习：Python装饰器


# 函数可以作为其他函数的输入参数，同时一个函数的返回值也可以是一个函数。

def dec(f):
    pass

@dec   # 这就是一个装饰器，它将上面定义的dec函数作为一个装饰器使用
def double(x):
    return x * 2

# 上面这个函数完全等价为以下代码：
double = dec(double)

