
def is_valid(passphrase):
    phrases = passphrase.split()
    phrase_anagrams = set([''.join(sorted(p)) for p in phrases])
    if (len(phrases) != len(phrase_anagrams)):
        return False

    return True


with open('04.input') as f:
    lines = f.read().split('\n')

total = 0
for passphrase in lines:
    print(passphrase)
    if is_valid(passphrase) == True:
        total += 1
        print('  valid')

print(total)
