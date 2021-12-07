
keypad = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

location = {'row': 1, 'col': 1}


def get_key(directions):
    row = location['row']
    col = location['col']

    # print('get_key {}'.format(location))
    for dir in directions:
        if dir == 'U':
            row = row - 1
        elif dir == 'L':
            col = col - 1
        elif dir == 'D':
            row = row + 1
        elif dir == 'R':
            col = col + 1

        if row < 0:
            row = 0
        elif row > 2:
            row = 2

        if col < 0:
            col = 0
        elif col > 2:
            col = 2

        # print('{} {} {}'.format(dir, row, col))

    location['row'] = row
    location['col'] = col

    return keypad[row][col]


with open('02.input') as f:
    steps = f.read()

steps = steps.split('\n')
keys = []
for step in steps:
    key = get_key(step)
    keys.append(key)

key_string = ''.join(map(str, keys))
print(key_string)
