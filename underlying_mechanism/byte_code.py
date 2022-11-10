# python 的工作机制大致可以解释为：翻译 python 代码变为字节码，再用解释器进行读取和编译
# 使用 dis 库可以呈现人类可读的字节码
import dis

def f1(A = "Hello world!"):
    return A

# 显示 f1 函数的字节码
# dis.dis(f1)

def f2(a, b):
    return a + b

# 显示 f2 函数的字节码
# dis.dis(f2)

# 如果需要显示一个文件的字节码，可以这么做
import os 
import sys
os.chdir(sys.path[0])
s = open('test.py').read()
co = compile(s, 'test.py', 'exec')
dis.dis(co)   # 显示 test.py 的字节码
dis.dis(co, file=open('./test.txt', 'w'))   # 将字节码写入到 test.txt 文件里

# 或者，还有一个较为简单的方法，直接在终端中输入
# python -m dis test.py