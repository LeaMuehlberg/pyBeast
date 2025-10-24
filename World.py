import random

class World:
    def __init__ (self, length, height):
        self.length = length
        self.height = height
        self.cells = [[None for _ in range(length)] for _ in range(height)]

    def spawn_food(self, size):
        free_cells = [(x,y) for y in range (self.height) for x in range(self.length) if self.cells[x][y] is None]
        for i in range(size):
            if len(free_cells) == 0:
                break
            x,y = random.choice(free_cells)
            Food(Position(x, y), self)
            free_cells.remove((x,y))

    def print_ascii(self):
        for row in self.cells:
            print("".join(
                "." if r is None else "*" if isinstance(r, Food) else "B" for r in row
            ))
        print()