
def is_valid(a, b, c):
    # print('is_valid {} {} {}'.format(a, b, c))
    return (a + b) > c and (b + c) > a and (c + a) > b


with open('03.input') as f:
    triangles = f.read().split('\n')

valid_count = 0
for triangle in triangles:
    points = triangle.split()
    points = list(map(int, points))
    if is_valid(points[0], points[1], points[2]):
        valid_count = valid_count + 1

print(valid_count)
