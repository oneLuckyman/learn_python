# B站BV1V5411d7kb
# 生成一个二维数组

def createArray2D(w, h):
    return [[0] * w for _ in range(h)] 

def show(arr):
    for line in arr:
        print(line)
    print()

def main():
    a1 = createArray2D(5, 5)
    show(a1)
    a1[3][2] = 1
    show(a1)


if __name__ == '__main__':
    main()

# 需要注意的是，[0] * w 指向的全部都是同一个内存
# 所以如果[[0] * w for _ in range(h)] 中的[0]不是一个int，而是一个可变对象的话，会导致无法单独改变其中一个元素
tep = [[1,2]] * 5
print(tep)
tep[0][1] = 3
print(tep)