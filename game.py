import pickle
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from player import Player

PLAYER = Player()
WALL_CHAR = '█'

def load_screen(filename):
    return pickle.load(open(filename, "rb"))

from screen import Screen
SCREEN = Screen()

import mapping
SCREEN = load_screen("grids/"+mapping.mapping[0][0])
CURRENT_MAPPING = [0,0]    

def get_opposite_direction(direction):
    if direction == "up":
        return "down"
    elif direction == "down":
        return "up"
    elif direction == "left":
        return "right"
    elif direction == "right":
        return "left"

def change_screen(win, pt, direction):
    if direction == "up":
        CURRENT_MAPPING[0] = CURRENT_MAPPING[0]-1
        pt[0] = SCREEN.height
    elif direction == "down":
        CURRENT_MAPPING[0] = CURRENT_MAPPING[0]+1
        pt[0] = 1
    elif direction == "left":
        CURRENT_MAPPING[1] = CURRENT_MAPPING[1]-1
        pt[1] = SCREEN.width
    elif direction == "right":
        CURRENT_MAPPING[1] = CURRENT_MAPPING[1]+1
        pt[1] = 1

    map_coords = mapping.mapping[CURRENT_MAPPING[0]][CURRENT_MAPPING[1]]
    screen = load_screen("grids/"+map_coords)
    SCREEN.grid = screen.grid   
    win.erase()
    win.border(0)
    for i in range(SCREEN.height):
        for j in range(SCREEN.width):
            draw_grid_obj(win, [i,j], SCREEN.grid[i][j])

    win.addch(pt[0], pt[1], PLAYER.char)

    if not is_move_valid(pt):
        return move_char(win, pt, PLAYER.char, get_opposite_direction(direction))

    return pt
          

def remove_char(win,location):
    win.addch(location[0],location[1],' ')

def is_move_valid(pt):
    is_valid = True
    if SCREEN.grid[pt[0]-1][pt[1]-1] == "WALL":
        is_valid = False
    return is_valid

def is_point_offscreen(pt):
    is_offscreen = False
    if pt[0] < 1 or pt[0] > SCREEN.height:
        is_offscreen = True
    if pt[1] < 1 or pt[1] > SCREEN.width:
        is_offscreen = True   
    return is_offscreen

def move_char(win, pt, char, direction):
    new_pt = pt
    if direction == "up":
        new_pt = [pt[0]-1, pt[1]]
    elif direction == "down":
        new_pt = [pt[0]+1, pt[1]]
    elif direction == "left":
        new_pt = [pt[0], pt[1]-1]
    elif direction == "right":
        new_pt = [pt[0], pt[1]+1]        

    if is_point_offscreen(new_pt):
        return change_screen(win, new_pt, direction)
    else:
        if is_move_valid(new_pt):
            remove_char(win, pt)
            win.addch(new_pt[0], new_pt[1], char)
            return new_pt
    return pt

def draw_grid_obj(win, pt, obj):
    char = " "
    if obj == "PLAYER":
        char = PLAYER.char
    if obj == "WALL":
        char = WALL_CHAR
    if obj == "EMPTY":
        char = " "
    win.addch(pt[0]+1, pt[1]+1, char)

curses.initscr()
win = curses.newwin(SCREEN.height+2, SCREEN.width+2, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)


key = 0

for i in range(SCREEN.height):
    for j in range(SCREEN.width):
        draw_grid_obj(win, [i,j], SCREEN.grid[i][j])

win.addch(PLAYER.position[0],PLAYER.position[1], PLAYER.char)

while key != 27:
    win.border(0)

    if key == KEY_LEFT:
        PLAYER.position = move_char(win, PLAYER.position, PLAYER.char, "left")

    if key == KEY_RIGHT:
        PLAYER.position = move_char(win, PLAYER.position, PLAYER.char, "right")

    if key == KEY_UP:
        PLAYER.position = move_char(win, PLAYER.position, PLAYER.char, "up")

    if key == KEY_DOWN:
        PLAYER.position = move_char(win, PLAYER.position, PLAYER.char, "down")

    win.addstr(0,0, str(PLAYER.position[0]))
    win.addstr(0,1, str(","))
    win.addstr(0,2, str(PLAYER.position[1]))

    key = win.getch()



curses.endwin()
