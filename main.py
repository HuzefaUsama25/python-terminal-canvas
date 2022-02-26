import time
import random
from Canvas import Canvas
from Dot import Dot
import math


def main():
    canvas = Canvas(900, 150, " ")
    dot = Dot(math.sin(canvas.width)*10, math.cos(canvas.height)*5)
    canvas.add(dot)

    count = 0

    #make a circle
    while True:
        time.sleep(0.1)
        canvas.pixel = "#"
        canvas.draw(clean=False)
        width = 4
        dot.move(int(math.sin(count)*10*width), int(math.cos(count)*5*width))
        count+=1


if __name__=="__main__":
    main()
