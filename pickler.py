import os
import glob
import pickle
from screen import Screen

WALL_CHAR = "w"
PLAYER_CHAR = "x"
EMPTY_CHAR = "."

path = 'grids/'

screen = Screen()

for filename in glob.glob(os.path.join(path, '*.grid')):
    grid = []
    print("Pickling " + filename)
    with open(filename, 'r') as f:
        for line in f:
            row = []
            for char in line:
                if char == WALL_CHAR:
                    row.append("WALL")
                elif char == PLAYER_CHAR:
                    row.append("PLAYER")
                elif char == EMPTY_CHAR:
                    row.append("EMPTY")
                elif char == "\n" or char == " ":
                    pass
                else:
                    print("Unrecognized character: " + char)
            grid.append(row)


    screen.height = len(grid)
    screen.width = len(grid[0])
    screen.grid = grid

    new_filename = os.path.splitext(filename)[0] + ".p"
    print("Creating pickle " + new_filename)
    pickle.dump(screen, open(new_filename, "wb"))
