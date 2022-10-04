# type hint 还有一种特殊的标注，Literal，指的是变量必须是某几种类型
# 和 enum 有点类似，但是直接使用 enum 的话，一是麻烦，二是可能存在过度封装的问题
from ast import Return
from typing import Literal

class Person:
    def __init__(
        self,
        name: str,
        gender: Literal["male", "female"]
    ):
        self.name = name 
        self.gender = gender 

# 这两种是正确的
a = Person("Bob", "female")
b = Person("Bob", "male")

# 这种是不正确的
a = Person("Bob", "woman")

# 但是这可能会带来一个问题，下面的语句会被 mypy 提示有错误，因为变量 g1 被识别成是一个 string 
g1 = "female"
a1 = Person("Bob", g1)
b1 = Person("Bob", "male")

# 这就需要把变量标注成是这种 Literal
g2: Literal["male", "female"] = "female"
a2 = Person("Bob", g2)
b2 = Person("Bob", "male")

# 但是这样就会变得很麻烦，可能需要频繁为变量进行这种声明，而且这样的标注万一需要修改，就会同时需要修改所有使用此类 Literal 标注的变量标注
# 从前面的多次 import 中可以看出来，在 python 中，type hint 本身也是一个 python object，这就意味着它们可以被赋值到变量上
GenderType = Literal["male", "female"]
g: GenderType = "female"
a = Person("Bob", g)
b = Person("Bob", "male")

# 这不仅可以降低工作量，还可以增加代码的可读性
NameType = str
class Person_Record:
    def __init__(
        self,
        name: NameType,         # 可以直接提示 name 是一个字符串，但更有用的提示可能是提示 name 是一种 NameType
    ):
        self.name = name 

a = Person_Record("Bob")        # mypy 还可以在变量的数据类型发生转变时进行提示，因为变量被定义后最好不要发生数据类型的变化
c = Person_Record("Bob")