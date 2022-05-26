import dataclasses
from dataclasses import dataclass
import inspect



@dataclass(frozen=True, order=True)
# frozen 参数为True 时输入的数值被冻结，不可更改，即可哈希
# order 参数为True 时，输入的数值被排序
class Message:
    id: int 
    text: str 
    user: str = 'default'       # 可以为属性设置默认值，但是不能为可变类型，如list, dict, set等，否则每次实例化都会指向同一个内存
    numbers: list = dataclasses.field(default_factory=list)                 # 想要设置可变类型的默认值，可以使用field()函数
    replies: list = dataclasses.field(default_factory=list, repr=False)     # 可以设置一些参数，让该参数不参与某些方法，例如设置repr=False，就不会打印这个属性



def main():
    msg = Message(1, 'a')
    print(msg)

    print(dataclasses.astuple(msg))     # astuple()将对象转换为元组输出
    print(dataclasses.asdict(msg))      # asdict()方法将对象转换为字典输出

    # 可以使用inspect模块来查看类的属性
    print(inspect.getmembers(Message, inspect.isfunction))

    # 可以通过dataclass.replace()方法更新数据
    copy_msg = dataclasses.replace(msg, id = 2)
    print(copy_msg.id)



if __name__ == '__main__':
    main()