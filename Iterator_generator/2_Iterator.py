#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 下面看一个例子，实现一个链表

class NodeIter:
    '''
    一个Iterator 类
    '''
    def __init__(self, node):
        self.curr_node = node

    def __next__(self):
        if self.curr_node is None:
            raise StopIteration
        node, self.curr_node = self.curr_node, self.curr_node.next
        return node

class Node:
    '''
    一个Iterable 类
    '''
    def __init__(self, name):
        self.name = name
        self.next = None

    def __iter__(self):
        return NodeIter(self)

node1 = Node('node1')
node2 = Node('node2')
node3 = Node('node3')
node1.next = node2
node2.next = node3

for node in node1:
    print(node.name)

