# B站 BV1P5411S7B6 以及它的评论区

from time import sleep
import tqdm
import os 
import sys 

# print中的end参数，默认为\n
print('hello');print('world')

print('hello', end='\n');print('world')

print('hello', end='===');print('world')

# print中的sep参数，默认为空格
print('hello', 'world')

print('hello', 'world', sep=' ')

print('hello', 'world', sep='~~~')


for i in range(20):
    print('#', end='')
    sleep(0.1)


for i in tqdm.tqdm(range(20)):
    sleep(0.1)

# 可以使用print的file参数，指定输出的文件，默认为sys.stdout
print('hello', 'world', sep=' ', file=open(os.path.join(sys.path[0], 'test.txt'), 'w'))

# print的最后一个参数是flush，默认为False，如果为True，则输出后立即刷新缓冲区
print('Loading', end='')
for i in range(20):
    print('.', end='', flush=True)
    sleep(0.5)