# super_3 中提到super 是一个动态的过程，这里做进一步的解释

class A:
    def say(self):
        print("A")

class B(A):
    def say(self):
        super().say()

class C(A):
    def say(self):
        print("C")

class M(B, C):
    def say(self):
        super().say()

m = M()
m.say()

# 打印的结果会是"C"
# 这是因为m 的mro 是M-B-C-A
# M 中的super().say()等价于 B.say(self)
# 而B.say(self) 会执行B 中的super().say()
# B 中的super().say()又等价于super(B, self).say()
# 这个时候的self 对应的object，仍然是m
# 因为m 的mro 是M-B-C-A，紧跟在B 后面的是C
# 因此super(B, self).say()等价于C.say()，这也就是最终执行的语句