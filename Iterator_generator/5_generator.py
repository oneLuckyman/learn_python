#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 用第三个文件中类似的例子来演示

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

    def __iter__(self):                 # 这里把iter()函数修改成了生成器的形式，也实现了目标，这样可以节省很多代码工作量
        node = self
        while node is not None:
            yield node 
            node = node.next

node1 = Node('node1')
node2 = Node('node2')
node3 = Node('node3')
node1.next = node2
node2.next = node3

for node in node1:
    print(node.name)