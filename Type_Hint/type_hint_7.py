# 除了 container 以外还有一种较为特殊的类型，可调用类型(callable)，其本身就具有输入和输出可以进行标注
from typing import Callable

def my_dec1(func: Callable):
    def wrapper(*args, **kwargs):
        print("start")
        ret = func(*args, **kwargs)
        print("end")
        return ret 
    return wrapper

# 1 并不是一个 Callable
my_dec1(1)

# 正常的写法不会被 mypy 提示错误
@my_dec1
def add1(a: int, b: int) -> int:
    return a + b

# 如果需要更进一步做更多要求，比如下面这个装饰器会打印：输入是两个 int，输出是一个 int，这种类型的函数的输入和输出
def my_dec2(func: Callable):
    def wrapper(a: int, b: int) -> int:
        print(f"args = {a}, {b}")
        ret = func(a, b)
        print(f"result = {ret}")
        return ret 
    return wrapper

# 这样不会报错
@my_dec2
def add2(a: int, b: int) -> int:
    return a + b

add2(1, 2)

# 但是如果这个装饰器装饰了不是对应类型的函数时，就会报错
@my_dec2
def absolute2(a: int) -> int:
    return abs(a)

absolute2(1, 2)

# 这时候，我们需要标注装饰器所装饰的 callable，take 什么类型，return 什么类型
# 通过形如 Callable[[int, int], int]，类指定 callable，take 什么类型，return 什么类型
def my_dec3(func: Callable[[int, int], int]):
    def wrapper(a: int, b: int) -> int:
        print(f"args = {a}, {b}")
        ret = func(a, b)
        print(f"result = {ret}")
        return ret 
    return wrapper

# 这里 mypy 就会直接根据标注提示错误
@my_dec3
def add3(a: str, b: str) -> str:
    return a + b 

@my_dec3
def absolute3(a: int) -> int:
    return abs(a)

absolute3(1, 2)