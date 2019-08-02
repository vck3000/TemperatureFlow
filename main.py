import matplotlib.pyplot as plt
import random
from Cell import Cell
from Board import Board
import COLORS
from matplotlib import cm

grid = []

im = plt.imread("5.png")
# plt.show(plt.imshow(im))
# print(im.shape)


for row in im:
    newRow = []
    for cellCol in row:  # cellCol = cell Colour, not column

        cellCol *= 255

        if len(list(cellCol)) == 3:
            cellCol = list(cellCol)
            cellCol.append(1)

        cellCol = tuple(cellCol)

        foundCell = False
        for category in COLORS.CategoryToData:

            val = COLORS.CategoryToData[category]
            if cellCol == val["color"]:
                initialTemp = val["initialTemp"]

                newRow.append(Cell(initialTemp, category))
                foundCell = True

        if not foundCell:
            raise ValueError("Invalid pixel colour: " + str(cellCol))

    # print(newRow)
    grid.append(newRow)

board = Board(grid)


try:
    plt.imshow(board.draw(), cmap=cm.get_cmap('bwr', 256))
    plt.clim(0, COLORS.MAX_TEMP)
    plt.colorbar()

    while True:
        plt.imshow(board.draw(), cmap=cm.get_cmap('bwr', 256))
        plt.ion()
        plt.show()

        plt.pause(0.001)

        for i in range(10):
            board.update()
        # print(str(board))

except KeyboardInterrupt:
    pass
