import re

meta_pattern = re.compile(r'\((\d+)x(\d+)\)')


def decompress(encoded):
    decoded = []

    repeat_len = -1
    repeat_amt = -1
    i = 0
    while i < len(encoded):
        char = encoded[i]
        # print('  checking ' + char)
        # print('  {} {}'.format(i, char))

        if repeat_len != -1:
            repeat_chunk = encoded[i:i + repeat_len]
            for j in range(repeat_amt):
                decoded.append(repeat_chunk)
            i = i + repeat_len
            repeat_len = -1
            repeat_amt = -1
        elif char == '(':
            index = encoded.find(')', i)
            meta = encoded[i:index + 1]
            matches = meta_pattern.match(meta)
            repeat_len = int(matches.group(1))
            repeat_amt = int(matches.group(2))
            i = index + 1
        else:
            decoded.append(char)
            i += 1

    return ''.join(decoded)


lines = open('09.input').read().split('\n')
line = lines[0]

print(line)
decode = decompress(line)
print(decode)
print(len(decode))
