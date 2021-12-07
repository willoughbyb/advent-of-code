from collections import Counter

with open('06.input') as f:
    input = f.read().split('\n')

cipher = []
counts = []

sample = input[0]
for i in range(len(sample)):
    cipher.append([])
    counts.append(None)

for line in input:
    for i in range(len(line)):
        char = line[i]
        cipher[i].append(char)

for i in range(len(cipher)):
    counts[i] = Counter(cipher[i])

plain = []
for i in range(len(counts)):
    plain.append(counts[i].most_common(1)[0][0])

print(''.join(plain))
