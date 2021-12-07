import hashlib


def md5(val):
    return hashlib.md5(val.encode('utf-8')).hexdigest()


with open('05.input') as f:
    codes = f.read().split('\n')

code = codes[0]
password = ['_'] * 8
index = 0

while True:
    string = code + str(index)
    hash = md5(string)

    if hash[0:5] == '00000' and hash[5:6].isdigit():
        pos = int(hash[5:6])
        val = hash[6:7]

        if pos < 8 and password[pos] == '_':
            password[pos] = val
            print('{} {} {}'.format(hash, string, ''.join(password)))

        # print('  {} {} {}'.format(pos, val, ''.join(password)))

    index = index + 1

    exists = '_' in password
    if exists == False:
        break

print(''.join(password))
