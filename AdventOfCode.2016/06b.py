from collections import Counter

with open('06.input') as f:
    input = f.read().split('\n')

cipher = []
counts = []

sample = input[0]
for i in range(len(sample)):
    cipher.append([])
    counts.append(None)


def get_least_common(dict):
    count = 99999
    value = ''
    for ele in dict.items():
        if ele[1] < count:
            count = ele[1]
            value = ele[0]

    return value


for line in input:
    for i in range(len(line)):
        char = line[i]
        cipher[i].append(char)

for i in range(len(cipher)):
    counts[i] = Counter(cipher[i])

plain = []
for i in range(len(counts)):
    least_common = get_least_common(dict(counts[i]))
    plain.append(least_common)

print(''.join(plain))
