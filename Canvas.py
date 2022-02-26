class Canvas:
    def __init__(self, width=100, height=100):
        self.width = width
        self.height = height
        self.grid = []
        self.objects = []
        self.pixel = " "
        self.clean_grid()

    def clean_grid(self):
        self.grid = []
        for col in range(self.height):
            y_col = []
            for row in range(self.width):
                y_col.append(self.pixel)
            self.grid.append(y_col)

    def draw(self, clean=True):
        print("\033c", end="")

        if clean:
            self.clean_grid()

        for object in self.objects:
            try:
                self.grid[object.ypos][object.xpos] = object.char
            except Exception as e:
                # what to do if dots get out of screen
                object.xpos = int(self.width/2)
                object.ypos = int(self.height/2)
                continue

        for col in self.grid:
            print("".join(col))

    def add(self, obj):
        self.objects.append(obj)
