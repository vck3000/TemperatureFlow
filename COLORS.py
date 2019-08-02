RED = (255, 0, 0, 1)
GREEN = (0, 255, 0, 1)
BLUE = (0, 0, 255, 1)
BLACK = (0, 0, 0, 1)
WHITE = (255, 255, 255, 1)

MAX_TEMP = 300

CategoryToData = {
    "SOURCE": {"color": RED, "initialTemp": MAX_TEMP},
    "SINK": {"color": BLUE, "initialTemp": 0},
    "WALL": {"color": BLACK, "initialTemp": None},
    "AIR": {"color": WHITE, "initialTemp": MAX_TEMP/2}
}
