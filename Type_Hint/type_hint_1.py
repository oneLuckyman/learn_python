# python 从3.5之后允许可选的标注变量类型

def f(a: int, b: int) -> int:
    return a + b

print(f(1,2))

# 在类型标注的基础下，可以使用静态分析工具 mypy 执行 mypy ***.py 检查文件中的错误数据类型使用
print(f('p','y'))

# type_hint_1.py:9: error: Argument 1 to "f" has incompatible type "str"; expected "int"
# type_hint_1.py:9: error: Argument 2 to "f" has incompatible type "str"; expected "int"
# 在 vscode 中使用 Ctrl + Shift + p 打开工作区设置加上以下语句
# "python.linting.mypyEnabled": true
# 即可在 vscode 中直接启用 mypy 检查