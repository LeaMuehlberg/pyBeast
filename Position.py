class Position:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def movePosition(self, deltax, deltay, length, height):
        self.x = (self.x + deltax) % length
        self.y = (self.y + deltay) % height