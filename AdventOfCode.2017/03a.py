
spiral = []


def get_layer(max_val):
    squares = []

    i = 0
    cur_val = 1
    while cur_val <= max_val:
        side_length = (i * 2) + 1
        line_length = (side_length * 4) - 4

        if i > 0:
            cur_val = cur_val + line_length

        i += 1

    return (i, side_length, line_length, cur_val)


def get_coord(layer, input):
    x = layer[0] - 1
    y = -(layer[0] - 2)

    line_width = layer[1]
    boundary = int(line_width / 2)

    cur_val = layer[3] - layer[2] + 1

    dir = 'N'
    while cur_val < input:
        if dir == 'N':
            if y < boundary:
                y += 1
            if y == boundary:
                dir = 'W'
        elif dir == 'W':
            if x > -boundary:
                x -= 1
            if x == -boundary:
                dir = 'S'
        elif dir == 'S':
            if y > -boundary:
                y -= 1
            if y == -boundary:
                dir = 'E'
        elif dir == 'E':
            if x < boundary:
                x += 1
            if x == boundary:
                dir = 'N'

        cur_val += 1
        # print('({}, {}) = {}'.format(x, y, cur_val))

    return (x, y)


def get_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


input = 265149

layer = get_layer(input)
print(layer)
coord = get_coord(layer, input)
print(coord)
distance = get_distance((0, 0), coord)
print(distance)
