import COLOURS

class Board:
    def __init__(self, grid):
        self.grid = grid



    def draw(self):
        newGrid = []

        for row in self.grid:
            newRow = []
            for cell in row:
                if cell.category == "WALL":
                    newRow.append()
