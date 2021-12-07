

keypad = (
    "00100",
    "02340",
    "56789",
    "0ABC0",
    "00D00",
)

location = {'row': 2, 'col': 0}


def get_key(directions):
    row = location['row']
    col = location['col']

    # print('get_key {}'.format(location))
    for dir in directions:
        if dir == 'U' and row > 0 and keypad[row - 1][col] != '0':
            row = row - 1
        elif dir == 'L' and col > 0 and keypad[row][col - 1] != '0':
            col = col - 1
        elif dir == 'D' and row < 4 and keypad[row + 1][col] != '0':
            row = row + 1
        elif dir == 'R' and col < 4 and keypad[row][col + 1] != '0':
            col = col + 1

        # print('{} {} {} - {}'.format(dir, row, col, key))

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
