# 但是如果需要对链表中间的元素进行操作，单向链表仍然很麻烦
# HEAD -> node0 -> node1 -> node2
# HEAD -> node0 -> node2
# 无法得知 node1 的前一个究竟是什么
# 所以单链表适合只需要对头部进行操作的情况
# 因此，可以再定义一种双向链表
# HEAD -> node0 -> node1 -> node2
#      <-       <-       <-

class ListNode:
    def __init__(self) -> None:
        self.next = None 
        self.prev = None 
    
    def is_empty(self):
        return self.next is None 
    
    def pop_head(self):
        ...

    def delete(self):
        self.prev.next = self.next 
        self.next.prev = self.prev 
        # 但是不知道 prev 和 next 是否真的有 next 和 prev

stack = ListNode()
stack.next = ListNode()

# HEAD -> node0 -> node1 -> node2 -> None
#      <-       <-       <-
# self.next.prev 不再合法 None 没有 prev
# 另外，由于始终握有 HEAD 所以找到 node0 很快，但是找到 node 尾很长时间，需要一直找到 None 才能找到
# 当然，对于 stack（栈）这点无所谓，但是对于 queue（队列），先入先出等这就有很大的问题了