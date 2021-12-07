import hashlib
import re

r_first = re.compile(r'(\w)\1\1')

salt = 'ahsbgdzn'
keys = []

overall = 0
counter = 0


def stretch(string):
    for j in range(2017):
        string = hashlib.md5(string.encode('utf-8')).hexdigest()

    return string


while len(keys) < 64:
    print('\r{}\t{}          '.format(overall, len(keys)), end='')
    # enc = hashlib.md5(get_string(overall)).hexdigest()
    enc = stretch(salt + str(overall))
    match = r_first.search(enc)
    if match == None:
        overall += 1
        continue

    # print('{}\t{}'.format(overall, enc))
    counter = 1
    r_second = re.compile(''.join([match.group(1)] * 5))
    while counter <= 1000:
        enc = stretch(salt + str(overall + counter))
        match = r_second.search(enc)
        if match != None:
            # print('  2: {}'.format(enc))
            keys.append(enc)
            break
        counter += 1

    overall += 1

print(overall - 1)
