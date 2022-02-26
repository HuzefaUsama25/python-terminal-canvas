import time
import random
from Canvas import Canvas
from Dot import Dot
import math


def main():
    canvas = Canvas(200, 60)
    dot = Dot(int(canvas.width/2), int(canvas.height/2))
    canvas.add(dot)

    while True:
        time.sleep(0.1)
        canvas.draw()
        dot.move(random.randint(-1,1),random.randint(-1,1))


if __name__=="__main__":
    main()
