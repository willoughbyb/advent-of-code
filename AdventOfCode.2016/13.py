
SIZE = 20
map = [[0] * SIZE for i in range(SIZE)]
favorite_number = 10

start_location = (1, 1)
target_location = (7, 4)


def magic_number(x, y):
    return (x * x) + (3 * x) + (2 * x * y) + y + (y * y)


def fill_map():
    for i in range(SIZE):
        for j in range(SIZE):
            magic_string = "{0:b}".format(magic_number(j, i) + favorite_number)
            count = len([char for char in magic_string if char == '1'])
            if count % 2 == 1:
                map[i][j] = 1

            if j == target_location[0] and i == target_location[1]:
                map[i][j] = 2


def print_map():
    for line in map:
        for char in line:
            val = '. '
            if char == 1:
                val = '# '
            elif char == 2:
                val = 'X '
            print(val, end='')
        print()


fill_map()
print_map()
location = start_location
history = []
