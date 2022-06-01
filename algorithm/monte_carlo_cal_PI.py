# 蒙特卡洛法求圆周率Pi
import random 

def monte_carlo_cal_PI(total):
    count = 0
    for i in range(total):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 <= 1:
            count += 1
    return count / total * 4


print(monte_carlo_cal_PI(1000000))