
def get_register(key):
    if key not in registers.keys():
        registers[key] = 0
    return registers[key]


def set_register(key, val):
    registers[key] = val


def get_operation(op):
    if op == 'inc':
        return '+'
    elif op == 'dec':
        return '-'
    else:
        return 'error'


with open('08.input') as f:
    lines = f.read().split('\n')

registers = {}

max_val = 0
for instruction in lines:
    print(instruction)
    operation, condition = instruction.split(' if ')

    conditions = condition.split()
    cmd = '{} {} {}'.format(get_register(
        conditions[0]), conditions[1], conditions[2])
    result = eval(cmd)
    if result == False:
        continue

    operations = operation.split()
    cmd = '{} {} {}'.format(
        get_register(operations[0]), get_operation(operations[1]), operations[2])
    result = eval(cmd)
    registers[operations[0]] = result

    cur_max = max(registers.values())
    if cur_max > max_val:
        max_val = cur_max

print(max_val)
