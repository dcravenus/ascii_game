import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

WIN_HEIGHT = 7
WIN_WIDTH = 7

PLAYER_CHAR = 'X'
WALL_CHAR = '█'

row1 = ['EMPTY', 'EMPTY', 'WALL', 'WALL', 'WALL']
row2 = ['WALL', 'EMPTY', 'EMPTY', 'WALL', 'WALL']
row3 = ['WALL', 'EMPTY', 'EMPTY', 'WALL', 'WALL']
row4 = ['WALL', 'EMPTY', 'WALL', 'WALL', 'WALL']
row5 = ['WALL', 'EMPTY', 'WALL', 'WALL', 'WALL']
grid = [row1, row2, row3, row4, row5]


def remove_char(win,location):
    win.addch(location[0],location[1],' ')

def move_left(win, pt, char):
    new_x = pt[1]-1
    if new_x < 1:
        new_x = WIN_WIDTH-2
    if grid[pt[0]-1][new_x-1] != "WALL":
        remove_char(win, pt)
        pt[1] = new_x
        win.addch(pt[0], pt[1], char)

def move_right(win, pt, char):
    new_x = pt[1]+1
    if new_x > WIN_WIDTH-2:
        new_x = 1
    if grid[pt[0]-1][new_x-1] != "WALL":
        remove_char(win, pt)
        pt[1] = new_x
        win.addch(pt[0], pt[1], char)

def move_up(win, pt, char):
    new_y = pt[0]-1
    if new_y < 1:
        new_y = WIN_HEIGHT-2
    if grid[new_y-1][pt[1]-1] != "WALL":
        remove_char(win, pt)
        pt[0] = new_y
        win.addch(pt[0], pt[1], char)

def move_down(win, pt, char):
    new_y = pt[0]+1
    if new_y > WIN_HEIGHT-2:
        new_y = 1
    if grid[new_y-1][pt[1]-1] != "WALL":
        remove_char(win, pt)
        pt[0] = new_y
        win.addch(pt[0], pt[1], char)

def draw_grid_obj(win, pt, obj):
    char = " "
    if obj == "PLAYER":
        char = PLAYER_CHAR
    if obj == "WALL":
        char = WALL_CHAR
    if obj == "EMPTY":
        char = " "
    win.addch(pt[0]+1, pt[1]+1, char)

curses.initscr()
win = curses.newwin(WIN_HEIGHT, WIN_WIDTH, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)

location = [1,1]
win.addch(location[0],location[1], PLAYER_CHAR)

key = 0

for i in range(WIN_HEIGHT-2):
    for j in range(WIN_WIDTH-2):
        draw_grid_obj(win, [i,j], grid[i][j])

while key != 27:

    if key == KEY_LEFT:
        move_left(win, location, PLAYER_CHAR)

    if key == KEY_RIGHT:
        move_right(win, location, PLAYER_CHAR)

    if key == KEY_UP:
        move_up(win, location, PLAYER_CHAR)

    if key == KEY_DOWN:
        move_down(win, location, PLAYER_CHAR)

    key = win.getch()


curses.endwin()
