#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 迭代器和生成器还是有一些不同的
# 生成器可以使用send()方法

def gen(num):
    while num > 0:
        tmp = yield num
        if tmp is not None:
            num = tmp
        num -= 1

g = gen(5)

first = next(g)             # 等价于first = g.send(None)
print(f"first: {first}")

print(f"send: {g.send(10)}")  
# send()方法可以传递一个值给生成器函数，这个值会被当作上一次yield的返回值
# 在这个例子中就是tmp = yield num = 10，然后函数会继续运行，直到下一次遇到yield，然后返回应有的值，这里返回的结果是9
# 这样就可以理解send(None)的作用，用这个例子做解释就是，每一次tmp都会被赋值成None，然后运行到num -= 1，然后再运行到yeild，返回num -= 1的值，以此类推

for i in g:
    print(i)