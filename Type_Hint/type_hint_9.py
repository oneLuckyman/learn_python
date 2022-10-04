# 再看一个例子，下面这个函数返回一个 tuple，它的第一个元素是返回码(return code)，第二个值是错误信息，可能是 string 也可能是 None
# 如果不定义一个变量把这种可能多次使用的标注类型存储起来，代码的繁杂程度可能会很高，可读性就会很低，
# 甚至可能存在返回相同标注类型但意义却不同的情况
# 例如，该例子下 tuple 的第一个元素是 int，第二个元素是 string 可能在其他函数中指代一个人的年龄和姓名
from typing import Optional

ReturnType = tuple[int, Optional[str]]

def f(a) -> ReturnType:
    if a > 0:
        print(a)
        return 0, None
    else:
        return 1, "input is <= 0"

retcode, errmsg = f(0)

# 但是这可能带来新的问题，下面两种标注类型都是 int
UserId = int 
AttackPoint = int 

class Player:
    def __init__(
        self,
        uid: UserId,
        attack: AttackPoint
    ):
        self.uid = uid
        self.attack = attack

    def update_attack(self, atk: AttackPoint):      # 假设这里不小心写错成把 atk 赋值给了 self.uid
        self.uid = atk                              # 因为 UserId 和 AttackPoint 都是 int 所以这里 mypy 的静态检查就把这个错误错过了

# 这个时候需要用到 NewType 完全建立一种新的 type
from typing import NewType
UserId_New = NewType("UserId_New", int)                 # 第一个参数是一个 string 代表实际名字，第二个表示具体是哪种类型
AttackPoint_New = NewType("AttackPoint_New", int) 

class Player_New:
    def __init__(
        self,
        uid: UserId_New,
        attack: AttackPoint_New
    ):
        self.uid = uid
        self.attack = attack

    def update_attack(self, atk: AttackPoint_New):
        self.uid = atk      # 这里 mypy 的静态检查就可以检查出来错误了，因为 UserId_New 和 AttackPoint_New 已经 python 视为两种不同的类型

# 但这又会产生一个新问题，不能用 int 直接赋值了，会被 mypy 认为是错误
# 因为 UserId_New 和 AttackPoint_New 已经被认为不是 int 而是上面定义的那种新类型，尽管它们实际上就是 int
p = Player_New(1, 100)

# 这个时候必须显式的把 int 转变成上面定义的 NewType，虽然这种行为在实际运行时很可能根本不会有任何实际操作
p = Player_New(UserId_New(1), AttackPoint_New(100))

# 最后吐槽一下，用到这个地步，python 简直和 C++ 一样麻烦了
# 但是这些标注 python 并不强制使用，具体怎么用用多少可以视情况而定