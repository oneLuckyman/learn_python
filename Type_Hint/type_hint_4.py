# 对于 container 还有一种情况。
# 也许程序本身允许几种相似的 container 可以同时作为某函数的输入并生效，比如 list 和 tuple

def my_sum1(lst: list[int]) -> int:
    total = 0
    for i in lst:
        total += i
    return total 

my_sum1([0, 1, 2])
my_sum1((0, 1, 2))

# 这种时候，除非要传入的参数确定是 list，否则应该标注 Sequence
from typing import Sequence

def my_sum2(lst: Sequence[int]) -> int:
    total = 0
    for i in lst:
        total += i
    return total 

my_sum2([0,1,2])
my_sum2((0,1,2))
my_sum2(b"012")
my_sum2(range(3))

# 对于字典(dictionary)这种container，它同时有 key 和 value

def my_sum3(d: dict[str, int]) -> int:
    total = 0
    for i in d.values():
        total += 1
    return total

my_sum3({"a": 1, "b": 2, "c": 3})
my_sum3({"a": 1, "b": 2, "c": "3"})
