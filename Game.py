from World import World
from Beast import Beast
from Position import Position
from Food import Food

class Game:
    def __init__(self):
        self.world = World(11,7)
        self.beast = Beast(Position(5,3), self.world, energy = 50, sightdistance = 2)
        self.food = self.world.spawn_food()
        self.world.print_world()
        #self.food.delete_food()
        #self.beast.delete_beast()
        self.beast.move(-6, -3)
        self.world.print_world()
        print(self.beast.get_string())

    def run(self):
        self.world.print_world()

if __name__ == "__main__":
    game = Game()
    #game.run()