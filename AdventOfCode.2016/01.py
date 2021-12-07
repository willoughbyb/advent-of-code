from collections import Counter
from collections import defaultdict

facings = {}
facings['N'] = ('W', 'E')
facings['W'] = ('S', 'N')
facings['S'] = ('E', 'W')
facings['E'] = ('N', 'S')

location = {'x': 0, 'y': 0}
direction = 'N'
location_history = []


def do_move(dir, len):
    for i in range(len):
        if dir == 'N':
            location['y'] = location['y'] + 1
        elif dir == 'W':
            location['x'] = location['x'] - 1
        elif dir == 'S':
            location['y'] = location['y'] - 1
        elif dir == 'E':
            location['x'] = location['x'] + 1

        location_history.append((location['x'], location['y']))


def get_first_duplicate_location():
    locations = [k for k, v in Counter(location_history).items() if v > 1]
    return locations[0]


with open('01.input') as f:
    steps = f.read()

steps = steps.split(', ')
for step in steps:
    turn_index = 0 if step[0] == 'L' else 1
    length = int(step[1:])

    new_direction = facings[direction][turn_index]
    do_move(new_direction, length)
    # print('{} {} {} {} - {}'.format(direction, step[0], new_direction, length, location))
    direction = new_direction

print('destination {}'.format(location))
distance = abs(location['x']) + abs(location['y'])
print('distance {}'.format(distance))
print(location_history)
loc = get_first_duplicate_location()
print('dup location {}'.format(loc))
distance2 = abs(loc[0]) + abs(loc[1])
print('dup distance {}'.format(distance2))
