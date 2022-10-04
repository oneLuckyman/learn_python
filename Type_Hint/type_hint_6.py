# 除了可以对函数做 type hint 对变量也同样可行

users: list[str] = []
users.append(1)

# Any 表示除 None 外的任何类型，不标注的情况下，默认就是此值，如果确实有传入 Any 的情况，建议还是标注出来，因为多数时候显式总比隐式好
from typing import Any

def f1(a: Any) -> Any:
    return a 

# 当函数没有返回值时，返回值时 None 而不是 Any，下面这种写法是错误的
def f2(a: list) -> Any:
    a.append(1)

lst2: list = []
i2: int = f2(lst2)        # 这里应该报错，因为 f2 没有一个 int

# 正确的写法
def f3(a: list) -> None:
    a.append(1)

lst3: list = []
i3: int = f3(lst3)          # 此处 mypy 报错

# 如果不标注，等同于 Any
def f4(a: list):
    a.append(1)

lst4: list = []
i4: int = f4(lst4)          # 等同于标注 Any

# 还有一种函数，确实没有返回，而不是因为没有显式的返回而返回 None
# 例如 raise 或者 exit()，此时应该标注 NoReturn

from typing import NoReturn

def error() -> NoReturn:
    raise ValueError 

error()
a = 3
print(a)