import re

hypernet_pat = re.compile(r"\[(\w+)\]")
ipchunk_pat = re.compile(r"(\w+)")
exp = re.compile(r"(\w)(\w)\2\1")


def has_abba(word):
    has = exp.search(word)
    # print('has_abba {} {} '.format(word, has))
    if has != None and has.group(1) == has.group(2):
        return None
    return has


with open('07.input') as f:
    lines = f.read().split('\n')

total = 0
for line in lines:
    print('{}'.format(line))
    hypernets = hypernet_pat.findall(line)
    print('h: {}'.format(hypernets))

    ipchunks = ipchunk_pat.findall(line)
    for h in hypernets:
        ipchunks.remove(h)

    print('i: {}'.format(ipchunks))

    valid = True
    for h in hypernets:
        if has_abba(h):
            valid = False

    if valid == False:
        continue

    valid = False
    for ipchunk in ipchunks:
        if has_abba(ipchunk):
            valid = True

    if valid == True:
        total += 1

print(total)
