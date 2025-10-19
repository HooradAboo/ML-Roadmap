import curses
from math import ceil
import time

BOARD_SIZE = (10, 10)        # Width and Height
SPEED = 0.5


def draw(stdscr, snake):
    stdscr.clear()

    board_width, board_height = BOARD_SIZE[0], BOARD_SIZE[1]
    snake_x, snake_y = snake[0], snake[1]

    for x in range(0, board_width+2):
        stdscr.addstr(0, x, '#')
        stdscr.addstr(board_height+1, x, '#')

    for y in range(1, board_height+1):
        stdscr.addstr(y, 0, '#')
        stdscr.addstr(y, board_width+1, '#')
    
    if (0 < snake_x < board_width+1) and (0 < snake_y < board_height+1):
        stdscr.addstr(snake_y, snake_x, 'O')

        stdscr.refresh()

def move(stdscr, snake, snake_direction):
    head_x = snake[-1][0]
    head_y = snake[-1][1]
    if (0 < head_x + snake_direction[0] < BOARD_SIZE[0]+1) and (0 < head_y + snake_direction[1] < BOARD_SIZE[1]+1):
        head_x += snake_direction[0]
        head_y += snake_direction[1]
        snake.append((head_x, head_y))
    draw(stdscr, snake[-1])


def main(stdscr):
    curses.curs_set(0)          # hide cursor
    stdscr.nodelay(True)        # make getch() non-blocking
    stdscr.clear()
    stdscr.refresh()

    head_x, head_y = ceil(BOARD_SIZE[0] / 2), ceil(BOARD_SIZE[1] / 2)
    snake = [(head_x, head_y)]
    snake_direction = (1, 0)    # (dx, dy) -> (1, 0) = right

    draw(stdscr, snake[0])

    last_step = time.time()
    while(True):
        key = stdscr.getch()

        if time.time() - last_step > SPEED:
            last_step = time.time()
            move(stdscr, snake, snake_direction)
            continue

        if key == -1:
            time.sleep(0.02)    # small idle
            continue

        
    
        if key in (ord('q'), ord('Q')):
            break

        if key in (ord('w'), ord('W')) and snake_direction != (0, 1):      # up
            last_step = time.time()
            snake_direction = (0, -1)
        elif key in (ord('s'), ord('S')) and snake_direction != (0, -1):   # down
            last_step = time.time()
            snake_direction = (0, 1)
        elif key in (ord('d'), ord('D')) and snake_direction != (-1, 0):   # right
            last_step = time.time()
            snake_direction = (1, 0)
        elif key in (ord('a'), ord('A')) and snake_direction != (1, 0):    # left
            last_step = time.time()
            snake_direction = (-1, 0)
        
        
        move(stdscr, snake, snake_direction)

        

    stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)