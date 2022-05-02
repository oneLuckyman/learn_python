#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gen(num):
    while num > 0:
        yield num               # 如果yield并没有赋给变量，那么send()方法就不会起作用，send(*)相当于send(None)
        num -= 1

g = gen(5)

first = next(g)                 # first = g.send(None)
print(f"first: {first}")

print(f"send: {g.send(10)}")

for i in g:
    print(i)