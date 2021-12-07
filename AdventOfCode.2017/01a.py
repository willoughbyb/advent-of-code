import re

with open('01.input') as f:
    lines = f.read().split('\n')

for line in lines:
    total = 0

    for i in range(len(line)):
        char = line[i]
        if i < len(line) - 1:
            nchar = line[i + 1]
        elif i == len(line) - 1:
            nchar = line[0]

        if char == nchar:
            total += int(char)

    print('{} {}'.format(line, total))
