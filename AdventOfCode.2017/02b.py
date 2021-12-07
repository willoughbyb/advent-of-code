
lines = open('02.input').read().split('\n')

checksum = 0
for line in lines:
    nums = list(map(int, line.split()))

    for i in range(len(nums)):
        a = nums[i]
        for j in range(len(nums)):
            if i == j:
                continue

            if nums[i] % nums[j] == 0:
                checksum += nums[i] / nums[j]
                break
print(checksum)
