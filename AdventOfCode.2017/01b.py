import re

with open('01.input') as f:
    lines = f.read().split('\n')

for line in lines:
    total = 0
    length = len(line)
    inc = int(length / 2)

    print('{} len:{} inc:{}'.format(line, length, inc))
    for i in range(length):
        char = line[i]
        ni = (i + inc) % length
        nchar = line[ni]
        # print('  i:{} ni:{} "{}" "{}"'.format(i, ni, char, nchar))

        if char == nchar:
            total += int(char)

    print(total)
