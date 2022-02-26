
class Dot:
    def __init__(self, xpos=0, ypos=0, speed=1):
        self.xpos = xpos
        self.ypos = ypos
        self.speed = speed
        self.char = "#"

    def move(self, x, y):
        self.xpos += x
        self.ypos += y
