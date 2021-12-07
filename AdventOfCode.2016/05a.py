import hashlib


def md5(val):
    return hashlib.md5(val.encode('utf-8')).hexdigest()


with open('05.input') as f:
    codes = f.read().split('\n')

password = []
for code in codes:
    index = 0

    while True:
        string = code + str(index)
        hash = md5(string)

        if hash[0:5] == '00000':
            print('{} {}'.format(hash, string))
            password.append(hash[5:6])

        index = index + 1

        if len(password) >= 8:
            break


password = ''.join(password)
print(password)
