
spiral = []

# tuple layer
#   0 - index
#   1 - array of values


def get_layer(index, previous):
    max_val = 1

    x = index
    y = -(index - 1)

    side_length = (index * 2) + 1
    line_length = (side_length * 4) - 4
    boundary = int(line_length / 2)

    values = []
    i = 0
    dir = 'N'
    while i < line_length:
        value = 0
        if len(previous[1]) > 0:
            value += previous[1][-1]

        if i > 0:
            value += values[-1]

        values.append(value)
        i += 1

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


    if len(values) == 0:
        values = [1]

    return (index, values, (x, y), side_length, line_length)


# input = 265149
input = 1

last_layer = (0, [1], (0, 0))
for i in range(1, 3):
    layer = get_layer(i, last_layer)
    print(layer)
    last_layer = layer
