import random
from Food import Food
from Position import Position
from Beast import Beast

class World:
    def __init__ (self, length, height):
        self.length = length
        self.height = height
        self.cells = [[None for _ in range(length)] for _ in range(height)]

    def get_length(self):
        return self.length
    
    def get_height(self):
        return self.height

    # spawnt nur ein food oder mehr?
    def spawn_food(self):
        free_cells = [(x,y) for y in range (self.height) for x in range(self.length) if self.cells[y][x] is None]
        if not free_cells: 
            return
        x, y = random.choice(free_cells)
        food = Food(Position(x, y), self, 10)
        return food

    def print_world(self):
        for row in self.cells:
            line = ""
            for r in row:
                if r is None:
                    line += "."
                elif isinstance(r, Beast):
                    line += "B"
                else:
                    line += "*"
            print(line)
        print()
