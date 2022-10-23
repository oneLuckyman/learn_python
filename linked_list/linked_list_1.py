# 一个普通的单向链表
class ListNode:
    def __init__(self) -> None:
        self.next = None

class DataNode(ListNode):
    def __init__(self, data) -> None:
        super().__init__()
        self.data = data 

# 但是单向链表有一些不便，下面是一个例子
# 做一个栈顶出栈操作，从一个单链表里拿一个 node 出来
stack = ListNode()
# 把 stack 给 node，下一个再变成头
node = stack
stack = stack.next
# 但是这样做的话，该逻辑在链表自身逻辑之外而不是链表自身的操作
# 并且，单链表的头发生了改变，该链表不再是之前的链表，stack 的数据类型可能已经发生改变
# 如果该链表有多个引用，这就会造成很多麻烦，许多引用者无法知道链表已经发生了改变
# 另外，空链表用 None 表示，这就会导致所有调用链表的函数都需要优先判断链表是否为空
