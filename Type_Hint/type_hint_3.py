# python 有一类本身就包含数据的被称为容器(container)的数据类型，例如list,dictionary
# 如果直接标注变量类型为 list 等，会造成信息不足

def my_sum1(lst: list) -> int:
    total = 0
    for i in lst:
        total += i
    return total 

my_sum1([0,1,2])
my_sum1([0,1,"2"])

# python-3.9 之后可以
def my_sum2(lst: list[int]) -> int:
    total = 0
    for i in lst:
        total += i
    return total 

my_sum2([0,1,2])
my_sum2([0,1,"2"])

# python-3.9 之前
from typing import List

def my_sum3(lst: List[int]) -> int:
    total = 0
    for i in lst:
        total += i
    return total 

my_sum3([0,1,2])
my_sum3([0,1,"2"])
