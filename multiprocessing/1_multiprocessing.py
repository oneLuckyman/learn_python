#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 两种最基础的multiprocessing使用方法
# 注意，如果在windows下运行，需要使用if __name__ == '__main__':

import multiprocessing
import os 

print(os.getpid())

def f():
    print(os.getpid())

# 第一种方法，通过直接使用Process类来创建进程，直接给它一个target参数，这个target参数就是要执行的函数

p = multiprocessing.Process(target=f)
p.start()
p.join()

# 第二种方法，通过继承Process类来创建进程，然后重载run方法

class MyProcess(multiprocessing.Process):
    def run(self):
        f()

p = MyProcess()
p.start()
p.join()