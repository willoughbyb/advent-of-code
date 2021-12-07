
with open('12.input') as f:
    lines = f.read().split('\n')

registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

i = 0
while i < len(lines):
    # print('{}\t{}'.format(i, lines[i]))
    instructions = lines[i].split()
    if instructions[0] == 'cpy':
        try:
            value = int(instructions[1])
        except:
            value = registers[instructions[1]]
        registers[instructions[2]] = value
    elif instructions[0] == 'inc':
        registers[instructions[1]] += 1
    elif instructions[0] == 'dec':
        registers[instructions[1]] -= 1
    elif instructions[0] == 'jnz':
        try:
            value = int(instructions[1])
        except:
            value = registers[instructions[1]]

        if value != 0:
            i += int(instructions[2])
            continue
    i += 1

print(registers['a'])
