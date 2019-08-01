import matplotlib.pyplot as plt
import random
from Cell import Cell
import COLOURS

grid = []


im = plt.imread("test.png")
# plt.show(plt.imshow(im))
# print(im.shape)

for row in im:
    newRow = []
    for cellCol in row:

        cellCol *= 255

        cellCol = tuple(cellCol)
        # cellCol = list(map(lambda x: int(x), cellCol))
        # print(cellCol)
       
        if cellCol == RED:
            newRow.append(Cell(100, "SOURCE"))
        elif cellCol == BLUE:
            newRow.append(Cell(0, "SINK"))
        elif cellCol == WHITE:
            newRow.append(Cell(50, "AIR"))
        elif cellCol == BLACK:
            newRow.append(Cell(None, "WALL"))
        else:
            raise ValueError("Invalid pixel colour: " + str(cellCol))

    # print(newRow)
    grid.append(newRow)


a = plt.imshow(grid)
plt.show(a)