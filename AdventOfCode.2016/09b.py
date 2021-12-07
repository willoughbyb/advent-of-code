import re

meta_pattern = re.compile(r'\((\d+)x(\d+)\)')


def parse_operations(line):
    operations = []

    line = re.sub('[A-Z]+', '_', line)
    items = line.split('_')
    print(items)


    return operations


lines = open('09.input.test').read().split('\n')
line = lines[0]

for line in lines:
    print(line)

    operations = parse_operations(line)
    [print(o) for o in operations]
