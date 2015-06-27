import pickle
from screen import Screen

WALL_CHAR = "w"
PLAYER_CHAR = "x"
EMPTY_CHAR = "."

screen = Screen()

grid = []
with open('grids/gen5.txt', 'r') as f:
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

pickle.dump(screen, open("grids/gen5.p", "wb"))
