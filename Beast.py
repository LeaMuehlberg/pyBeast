class Beast:
    def __init__ (self, position, world, energy, sightdistance = 2):
        self.position = position
        self.world = world
        self.energy = energy
        self.sightdistance = sightdistance
        self.world.cells[self.position.x][self.position.y] = self # biest in die welt spawnen

    def deleteBeast(self):
        self.world.cells[self.position.x][self.position.y] = None
