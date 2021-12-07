
lines = open('02.input').read().split('\n')

checksum = 0;
for line in lines:
    print(line)
    nums = list(map(int, line.split()))
    print(nums)
    checksum += max(nums) - min(nums)
print(checksum)
