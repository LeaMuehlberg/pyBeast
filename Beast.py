from Food import Food

class Beast:
    def __init__ (self, position, world, energy, sightdistance = 2):
        self.position = position
        self.world = world
        self.energy = energy
        self.sightdistance = sightdistance
        self.world.cells[self.position.y][self.position.x] = self # biest in die welt spawnen

    def delete_beast(self):
        self.world.cells[self.position.y][self.position.x] = None

    def move(self, deltax, deltay): # deltax -> nach rechts. deltay -> nach unten
        self.world.cells[self.position.y][self.position.x] = None # alte position ist free
        self.position.move_position(deltax, deltay, self.world.get_length(), self.world.get_height()) # neue position
        self.world.cells[self.position.y][self.position.x] = self # biest in die welt spawnen

    # erstellt ein mini 2D feld von der welt (zentrum beast)
    def get_sight_area(self):
        N = self.sightdistance
        area = []
        for deltay in range(-N, N + 1): # -N inklusiv. N+1 exklusiv
            row = []
            for deltax in range(-N, N + 1): # geht jede zeile durch
                x = (self.position.x + deltax) % self.world.get_length()
                y = (self.position.y + deltay) % self.world.get_height()
                row.append(self.world.cells[y][x])
            area.append(row)
        return area
    

    # kann ich das ganze nicht in so ne art schnittstelle packen?

    # generiert die symbole für den string
    def gen_symbols(self, area):
        line = []
        for row in area:
            for cell in row:
                if cell is None:
                    line.append(".")
                elif isinstance(cell, Beast):
                    if cell.energy > self.energy:
                        line.append(">")
                    elif cell.energy < self.energy:
                        line.append("<")
                    else:
                        line.append("=")
                elif isinstance(cell, Food):
                    line.append("*")
        return "".join(line)

    def get_string(self):
        area = self.get_sight_area()
        return self.gen_symbols(area)