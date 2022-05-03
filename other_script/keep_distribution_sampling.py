
from pickle import FALSE




import random
import numpy as np 
# 从一组数据中随机抽取n个数据，保持数据的分布

def random_sample(data, n):
    """
    :param data:
    :param n:
    :return:
    """
    if len(data) < n:   
        raise ValueError('Sample size is too large.')
    result = []
    for i in range(n):
        index = int(random.random() * (len(data) - i))
        result.append(data[index])
        data[index] = data[len(data) - i - 1]
    return result

# accept-reject 抽样，从一组数据中抽取n个数据

def accept_reject_sample(data, n):
    """
    :param data:
    :param n:
    :return:
    """
    if len(data) < n:
        raise ValueError('Sample size is too large.')
    result = []
    for i in range(n):
        x = random.random() * (data[-1] - data[0]) + data[0]
        y = random.random()
        index = np.searchsorted(data, x)
        if y <= (data[index] - x) / (data[index] - data[index - 1]):
            result.append(data[index])
        else:
            result.append(data[index - 1])
    return result
