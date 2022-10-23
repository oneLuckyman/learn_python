# 使用有头链表，即人为规定链表的第一个 Node 没有意义，是链表的头
# 使用链表时，所有引用者拿到的都是链表的头，无论进行任何操作都不会改变它
# HEAD -> None
# HEAD -> node0 -> node1 -> ...

class ListNode:
    def __init__(self) -> None:
        self.next = None
    
    def is_empty(self):
        return self.next is None

    # 如果需要取出第一个元素，可以在链表内部实现
    def pop_head(self):
        if self.is_empty():
            return None
        ret = self.next 
        self.next = self.next.next
        return ret 

stack = ListNode()
stack.next = ListNode()

# 这样 stack 永远都是 ListNode 类型，并且它本身没有发生改变
node = stack.pop_head()

