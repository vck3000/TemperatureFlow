import COLORS
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap
from Cell import Cell


# Generate colourmap from blue to red
N = 256
vals = np.ones((N, 4))
vals[:, 0] = np.linspace(0/256, 255/256, N)
vals[:, 1] = np.linspace(0/256, 0/256, N)
vals[:, 2] = np.linspace(255/256, 0/256, N)
newcmp = ListedColormap(vals)


bwr = cm.get_cmap('bwr', 256)


# Override the cm
newcmp = bwr


class Board:
    def __init__(self, grid):
        self.grid = grid

    def draw(self):
        colGrid = []

        for row in self.grid:
            newRow = []
            for cell in row:
                # print(cell.category)
                if cell.get_category() != "AIR":
                    newRow.append(
                        COLORS.CategoryToData[cell.get_category()]["color"])
                else:
                    col = list(newcmp(cell.get_temp()/COLORS.MAX_TEMP))
                    # Reduce the alpha channel a bit
                    # col[3] = 0.5
                    col = tuple(col)
                    newRow.append(col)

            colGrid.append(newRow)

        return colGrid

    def __str__(self):
        rows = []

        for row in self.grid:
            newStrRow = []
            for cell in row:
                newStrRow.append(str(cell.get_temp()))

            newStrRow = "\t".join(newStrRow)

            rows.append(newStrRow)

        return "\n".join(rows)

    def update(self):
        newGrid = []

        i = 0
        while i < len(self.grid):
            if i == 0:
                prevRow = None
            else:
                prevRow = self.grid[i-1]

            currRow = self.grid[i]

            if i == len(self.grid) - 1:
                nextRow = None
            else:
                nextRow = self.grid[i+1]

            newRow = []

            j = 0
            while j < len(currRow):
                # A cell's new temperature is the average of its surrounding 8 cells
                surrCells = []
                currCell = currRow[j]

                if currCell.get_category() == "AIR":
                    if prevRow:
                        if j != 0:
                            # top left cell
                            surrCells.append(prevRow[j-1])
                        # top cell
                        surrCells.append(prevRow[j])
                        if j != len(currRow) - 1:
                            # top right cell
                            surrCells.append(prevRow[j+1])

                    if j != 0:
                        # mid left cell
                        surrCells.append(currRow[j-1])
                    # Skip our own cell
                    if j != len(currRow) - 1:
                        surrCells.append(currRow[j+1])

                    if nextRow:
                        if j != 0:
                            # bottom left cell
                            surrCells.append(nextRow[j-1])
                        # bottom cell
                        surrCells.append(nextRow[j])
                        if j != len(currRow) - 1:
                            # bottom right cell
                            surrCells.append(nextRow[j+1])

                    # Average the temps of all the surr non-wall cells:
                    surrCellsNonWall = filter(
                        lambda cell: cell.get_category() != "WALL", surrCells)

                    temps = list(
                        map(lambda cell: cell.get_temp(), surrCellsNonWall))

                    avgTemp = sum(temps)/len(temps)

                    newRow.append(Cell(avgTemp, currCell.get_category()))

                # For all other categories, just add them
                else:
                    newRow.append(currCell)

                j += 1
            newGrid.append(newRow)
            i += 1

        self.grid = newGrid
