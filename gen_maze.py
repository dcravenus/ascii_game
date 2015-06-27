import random
import pickle
from screen import Screen

class Cell:
    visited = False
    up = "WALL"
    down = "WALL"
    left = "WALL"
    right = "WALL"

HEIGHT = 15
WIDTH = 35

grid = []
for i in range(HEIGHT):
    row = []
    for j in range(WIDTH):
        row.append(Cell())
    grid.append(row)

def check_visited(cell):
    if cell == None:
        return True
    else:
        return cell.visited

x=0
y=0

dirs = [0,1,2,3]
current_cell = grid[0][0]
current_cell.visited = True
is_beginning = True
path = []
while is_beginning or x!=0 or y!=0:
    random.shuffle(dirs)

    if len(dirs) == 0:
        if len(path) == 0:
            break
        pt = path.pop()
        current_cell.visited = True
        current_cell = grid[pt[0]][pt[1]]
        dirs = [0,1,2,3]
        y = pt[0]
        x = pt[1]
        continue

    if dirs[0] == 0:    #up case
        if y-1<0:
            dirs.remove(0)
        else:
            next_cell = grid[y-1][x]
            if next_cell.visited:
                dirs.remove(0)
            else:
                current_cell.up = "EMPTY"
                next_cell.down = "EMPTY"
                current_cell.visited = True
                path.append([y,x])
                current_cell = next_cell
                dirs = [0,2,3]
                y=y-1
    elif dirs[0] == 1:    #down case
        if y+1>HEIGHT-1:
            dirs.remove(1)
        else:
            next_cell = grid[y+1][x]
            if next_cell.visited:
                dirs.remove(1)
            else:
                current_cell.down = "EMPTY"
                next_cell.up = "EMPTY"
                current_cell.visited = True
                path.append([y,x])
                current_cell = next_cell
                dirs = [1,2,3]
                y=y+1
    elif dirs[0] == 2:    #left case
        if x-1<0:
            dirs.remove(2)
        else:
            next_cell = grid[y][x-1]
            if next_cell.visited:
                dirs.remove(2)
            else:
                current_cell.left = "EMPTY"
                next_cell.right = "EMPTY"
                current_cell.visited = True
                path.append([y,x])
                current_cell = next_cell
                dirs = [0,1,2]
                x=x-1
    elif dirs[0] == 3:    #right case
        if x+1>WIDTH-1:
            dirs.remove(3)
        else:
            next_cell = grid[y][x+1]
            if next_cell.visited:
                dirs.remove(3)
            else:
                current_cell.right = "EMPTY"
                next_cell.left = "EMPTY"
                current_cell.visited = True
                path.append([y,x])
                current_cell = next_cell
                dirs = [0,1,3]
                x=x+1

    if x!=0 or y!=0:
        is_beginning = False



screen_grid = []

for i in range((HEIGHT*2)+1):
    screen_grid.append([])
    for j in range((WIDTH*2)+1):
        screen_grid[i].append("")

for i in range(HEIGHT):
    for j in range(WIDTH):
        y = i*2+1
        x = j*2+1
        cell = grid[i][j]
        screen_grid[y-1][x] = cell.up
        screen_grid[y+1][x] = cell.down
        screen_grid[y][x-1] = cell.left
        screen_grid[y][x+1] = cell.right
        screen_grid[y-1][x-1] = "WALL"
        screen_grid[y-1][x+1] = "WALL"
        screen_grid[y+1][x-1] = "WALL"
        screen_grid[y+1][x+1] = "WALL"
        screen_grid[y][x] = "EMPTY"

screen = Screen()
screen.grid = screen_grid
screen.height = HEIGHT*2+1
screen.width = WIDTH*2+1

pickle.dump(screen, open("grids/gen_maze.p", "wb"))
