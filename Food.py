class Food:
    def __init__ (self, position, world, energylevel):
        self.position = position
        self.world = world
        self.energylevel = energylevel
        self.world.cells[self.position.y][self.position.x] = self # futter in die welt spawnen

    def deleteFood(self):
        self.world.cells[self.position.y][self.position.x] = None