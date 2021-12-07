
def is_valid(a, b, c):
    # print('is_valid {} {} {}'.format(a, b, c))
    return (a + b) > c and (b + c) > a and (c + a) > b


with open('03.input') as f:
    triangles = f.read().split('\n')

valid_count = 0

for t1, t2, t3 in zip(*[iter(triangles)] * 3):
    t1 = list(map(int, t1.split()))
    t2 = list(map(int, t2.split()))
    t3 = list(map(int, t3.split()))

    if is_valid(t1[0], t2[0], t3[0]):
        valid_count = valid_count + 1
    if is_valid(t1[1], t2[1], t3[1]):
        valid_count = valid_count + 1
    if is_valid(t1[2], t2[2], t3[2]):
        valid_count = valid_count + 1

print(valid_count)
