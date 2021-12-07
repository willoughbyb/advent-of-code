

def get_largest_index():
    max_value = max(banks, key=lambda bank: len(bank))
    return banks.index(max_value)


def redistribute(values, index):
    while len(values) > 0:
        val = values.pop()
        index += 1
        if index >= len(banks):
            index = 0

        banks[index].append(val)


with open('06.input') as f:
    lines = f.read().split('\n')

input = list(map(int, lines[0].split()))

banks = []
bank_history = []
print(input)
for i in range(len(input)):
    banks.append([1] * input[i])

first = 0
last = 0
cycle_count = 0
while len(bank_history) == len(set(bank_history)):
    largest_index = get_largest_index()
    values = banks[largest_index]
    banks[largest_index] = []
    redistribute(values, largest_index)
    cycle_count += 1

    entry = tuple([len(x) for x in banks])
    bank_history.append(entry)


print(cycle_count)

dup_entry = bank_history[-1]
print(dup_entry)

second_cycle_count = 0
while True:
    largest_index = get_largest_index()
    values = banks[largest_index]
    banks[largest_index] = []
    redistribute(values, largest_index)
    second_cycle_count += 1

    entry = tuple([len(x) for x in banks])
    if dup_entry == entry:
        break


print(second_cycle_count)
