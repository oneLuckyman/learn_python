# 如果某函数传入的参数可能有多种数据类型

def f1(x):
    if x is None:
        return 0
    return x 

f1(None)
f1(0)

# 可以使用 Union
import re
from typing import Union

def f2(x: Union[int, None]) -> int:
    if x is None:
        return 0
    return x 

f2(None)
f2(0)

# python-3.10 之后，可以使用 | 代替 Union

def f3(x: int | None) -> int:
    if x is None:
        return 0
    return x 

f3(None)
f3(0)

# 如果一个变量的数据类型有可能是 None 或者另一某种数据类型，可以使用 Optional
from typing import Optional

def f4(x: Optional[int]) -> int:        # x 是 int 或者 None
    if x is None:
        return 0
    return x 

f4(None)
f4(0)