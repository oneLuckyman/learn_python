# 一个简单的马尔科夫链搜索一个圆

import random 
import pandas as pd 
import matplotlib.pyplot as plt 

def estimate_state(point):
    if point[0] ** 2 + point[1] ** 2 <= 1:
        return True
    else:
        return False

def state_transition(point):
    x = point[0] + random.uniform(-0.1, 0.1)
    y = point[1] + random.uniform(-0.1, 0.1)
    return [x, y]

def reward_point(Points, point):
    if estimate_state(point):
        Points.append(point)
    else:
        pass

def policy(point_i, point_j):
    for i in range(5):
        if estimate_state(point_j):
            point_k = state_transition(point_j)
        else:
            point_k = state_transition(point_i)
            
        if estimate_state(point_k):
            return point_k
        else:
            continue
    return state_transition(point_j)

def search_circle(total, targets):
    point_i = [random.uniform(-1, 1), random.uniform(-1, 1)]
    point_j = state_transition(point_i)
    Points = []
    for i in range(total):
        point_k = policy(point_i, point_j)
        if estimate_state(point_k):
            reward_point(Points, point_k)
        else:
            pass
        point_i = point_j
        point_j = point_k

        if i >= targets:
            print("get the circle")
            return Points
    print("MAX points")
    return Points

def main():
    Points = search_circle(10000000, 10000)
    df = pd.DataFrame(Points)
    df.columns = ['x', 'y']
    # df.plot.scatter(x='x', y='y', c='b', s=1)
    plt.scatter(df['x'], df['y'], s=1)
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    # plt.gcf().gca().add_artist(plt.Circle((0, 0), 1, color='r', fill=False))
    plt.show()

if __name__ == '__main__':
    main()

# 效果并不好，还需要改进，尽量不要让点互相离得太近
