class Position:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def move_position(self, deltax, deltay, length, height):
        # falls es über den rand geht: %
        self.x = (self.x + deltax) % length 
        self.y = (self.y + deltay) % height