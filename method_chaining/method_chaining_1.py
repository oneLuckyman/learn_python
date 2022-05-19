# method chaining 或称 method cascading 或 fluent API
# 学习自：https://www.bilibili.com/video/BV1na411e777
# 源地址：https://youtu.be/BY34Fe-2xgk

import numpy as np 

class Player:
    def __init__(self, name, position, fatigue=0) -> None:
        self.name = name
        self.position = position
        self.fatigue = fatigue

    def draw(self):
        print(f"drawing {self.name} to screen as {self.position}")

    def move(self, delta):
        self.position += delta
        self.fatigue += 1

    def rest(self):
        self.fatigue = 0

def main():
    james = Player("James", np.array([0.0, 0.0]))
    UP = np.array([0.0, 1.0])
    RIGHT = np.array([1.0, 0.0])

    james.move(UP)
    james.move(RIGHT)
    james.move(UP)
    james.rest()
    james.draw()

if __name__ == "__main__":
    main()