with open('05.input') as f:
    lines = f.read().split('\n')

instructions = list(map(int, lines))

step_counter = 0
index = 0

try:
    while True:
        input = instructions[index]

        if input >= 3:
            instructions[index] -= 1
        else:
            instructions[index] += 1
        index += input
        step_counter += 1
except IndexError:
    print('done')

print(step_counter)
