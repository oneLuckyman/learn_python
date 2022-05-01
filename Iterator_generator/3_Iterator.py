#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 然而，在python中，Iterator 也是有__iter__() 方法的，这个意思就是说Iterator 本身肯定也是一个Iterable。
# 继续看前面那个例子的改进

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

    def __iter__(self):
        return self

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

# 如果要实现，一个Iterator 不要第一个值，从第二个值开始输出，可以写成下面这样

it = iter(node1)
first = next(it)

for node in it:
    print(node.name)

# 但是如果直接使用上一个文件中的写法，就会报错，因为for 循环的对象必须是Iterable 类型
# 所以，一个Iterator 类一定要有__iter__() 方法
# 写法也很简单，绝大多数情况下，只要让其返回其自身，即self，就可以了
# 但是，实际使用python的时候，可能会发现很多Iterator 其实也并不是一个Iterable 这表明python官方自己也并没有严格执行这个标准