import re

hypernet_pat = re.compile(r"\[(\w+)\]")
ipchunk_pat = re.compile(r"(\w+)")
aba_pat = re.compile(r"(\w)(\w)\1")


def get_abas(word):
    results = []

    sresult = aba_pat.search(word)
    while sresult != None:
        results.append(sresult.group(0))
        sresult = aba_pat.search(word, sresult.start() + 1)

    return results


def has_bab(pat, word):
    has = re.search(pat, word)
    print('    has_bab {} {} {}'.format(pat, word, has))
    return has


with open('07.input') as f:
    lines = f.read().split('\n')

total = 0
for line in lines:
    hypernets = hypernet_pat.findall(line)
    ipchunks = ipchunk_pat.findall(line)
    for h in hypernets:
        ipchunks.remove(h)

    print('l:{}\nh:{}\ni:{}'.format(line, hypernets, ipchunks))

    valid = False
    for ipchunk in ipchunks:
        abas = get_abas(ipchunk)

        for aba in abas:
            bab_pattern = aba[1] + aba[0] + aba[1]
            print('  {} {} -> {}'.format(ipchunk, aba, bab_pattern))
            for hypernet in hypernets:
                bab_result = has_bab(bab_pattern, hypernet)
                if bab_result != None:
                    valid = True

    if valid == True:
        total += 1

    print()

print(total)
