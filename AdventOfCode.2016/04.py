import re
from collections import Counter

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def parse_code(code):
    data = {
        'original': code,
        'sector': int(code[-10:-7]),
        'checksum': code[-6:-1]
    }

    code_normalized = code[0:-10].translate({ord(c): None for c in '-'})
    data['counts'] = Counter(code_normalized)

    decrypt = []
    for char in code[0:-10]:
        if char in alphabet:
            decrypt.append(
                alphabet[(alphabet.index(char) + data['sector']) % 26])
        elif char == '-':
            decrypt.append(' ')
        else:
            decrypt.append(char)

    data['decrypt'] = ''.join(decrypt)

    return data


def is_checksum_valid(data):
    last_count = 99999
    last_char = ' '

    for char in data['checksum']:
        count = data['counts'][char]
        if count == 0:
            return False

        if count > last_count:
            return False
        elif count == last_count and ord(last_char) > ord(char):
            return False

        last_count = count
        last_char = char

    return True


with open('04.input') as f:
    codes = f.read().split('\n')

check = re.compile('\-\d{3}\[\w{5}\]$')

sector_count = 0
sector_total = 0
for c in codes:
    if check.match(c) == False:
        print(c)

    code = parse_code(c)
    is_valid = is_checksum_valid(code)
    # print('{} - {} {}'.format(str(is_valid)[0:1], code['checksum'], code['sector']))
    if is_valid:
        print('{} {} {}'.format(code['checksum'], code['sector'], code['decrypt']))
        sector_count = sector_count + 1
        sector_total = sector_total + code['sector']

print('valid: {}'.format(sector_count))
print('total: {}'.format(sector_total))
