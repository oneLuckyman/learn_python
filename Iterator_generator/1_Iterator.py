#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 从B站视频 "BV1ca411t7A9" 中学习。
# 在python中，for 循环和Iterator 是紧密相关的。

lst = [1,2,3]
for i in lst:           # for 循环后的lst 必须是一个iterable 可迭代对象
    print(i)

# Iterator 和Iterable 很相似但并不一样
# Iterator 是一个表示数据流的对象，可以使用next()方法不断从这个对象中获取数据
# 对于一个Iterable 来说，它可以没有状态，可以根据一个Iterable 产生一个Iterator。
# 而Iterator 必须有状态，即当前迭代到的位置，而且它没有用于修改内部数据的接口
# 从实现上来看，一个Iterable 一定要有__iter__() 方法，或者__getitem__() 方法，这是为了保证这个Iterable 可以被iter() 函数转换成Iterator。
# 而Iterator 必须要有__next__() 方法，使其可以被next() 函数调用，迭代出数据。
# 而for 循环可以理解成，在循环开始前，创建了一个Iterable 对应的Iterator
