class Game:
    def __init__(self):
        self.world = World(10,6)
        self.beast = Beast(Position(5,3), self.world, energy = 50, sightdistance = 2)
        self.world.spawn_food(5)

    def run(self):
        self.world.print_ascii()

if __name__ == "__main__":
    game = Game()
    game.run()