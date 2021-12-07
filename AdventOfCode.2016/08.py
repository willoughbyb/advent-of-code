import re
from collections import deque


def print_screen():
    for line in screen:
        [print('#' if char else '.', end="") for char in line]
        print()


def count_screen():
    total = 0
    for line in screen:
        for col in line:
            if col == 1:
                total += 1

    return total


def do_rect(width, height):
    print('do_rect {} {}'.format(width, height))
    for row in range(height):
        for col in range(width):
            screen[row][col] = 1


def do_rotate_column(column, amount):
    print('do_rcol {} {}'.format(column, amount))

    column_values = [x[column] for x in screen]
    column_values = shift_array(column_values, amount)

    for i in range(len(screen)):
        screen[i][column] = column_values[i]


def do_rotate_row(row, amount):
    print('do_rrow {} {}'.format(row, amount))

    row_values = screen[row]
    row_values = shift_array(row_values, amount)
    screen[row] = row_values


def shift_array(array, amount):
    # print('shift_array {}'.format(amount))
    que = deque(array)
    for i in range(amount):
        val = que.pop()
        que.appendleft(val)

    return list(que)


# 50 x 6 box
screen = [[0] * 50 for i in range(6)]

actions = {
    'rect': do_rect,
    'rotate row': do_rotate_row,
    'rotate column': do_rotate_column
}

pattern = re.compile(r"^(rect|rotate row|rotate column)\D*(\d+)\D*(\d+)$")

lines = open('08.input').read().split('\n')
for line in lines:
    match = pattern.match(line)
    command = match.group(1)
    arg1 = int(match.group(2))
    arg2 = int(match.group(3))

    actions[command](arg1, arg2)

print_screen()
print(count_screen())
