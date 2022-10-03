# 在自定义类型中使用 type hint

class A:
    name = "A"

def get_name(o: A) -> str:
    return o.name

get_name(A)
get_name(A())

# 一种特殊情况，当自定义类中使用类型是自身的变量时不能直接标注，因为此时这个类还没有被定义，这时需要把变量名加上引号变成字符串。
class Node:
    def __init__(self, prev: "Node") -> None:
        self.prev = prev 
        self.next = None