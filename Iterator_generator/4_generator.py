#!/usr/bin/env python
# -*- coding: utf-8 -*-

# B站“BV1KS4yD7Qb”学习
# generator 是一种特殊的Iterator

# 这是一个生成器函数
def gen(num):
    while num > 0:
        yield num       # 当一个函数里有yield的时候，这个函数会被python视为一个生成器函数
        num -= 1
    return              # 这里的return等价于raise StopIteration

# 当使用生成器函数时，会产生一个生成器对象，但实际上这个时候还没有执行函数的内部
g = gen(5)

# 只有运行next()的时候才会真正的执行
first = next(g)
# 运行完一次next()之后，函数会暂停在yield的位置并记录状态，等待下一次next()的时候再继续执行

# generator 也可以使用for循环来遍历
for i in g:
    print(i)

