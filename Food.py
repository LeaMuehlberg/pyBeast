class Food:
    def __init__ (self, position, world, energy):
        self.position = position
        self.world = world
        self.energylevel = energy
        self.world.cells[self.position.y][self.position.x] = self # futter in die welt spawnen

    def delete_food(self):
        self.world.cells[self.position.y][self.position.x] = None