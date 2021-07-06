import sys

f = sys.stdin.readline

n = int(f())
nums = list(map(int, f().split()))

nums.sort()
print(nums)

i, j = 0, n-1
min_num = nums[j]

answer = []
while i < j:
    two_sum = nums[i] + nums[j]

    if abs(two_sum) < min_num:
        min_num = abs(two_sum)
        answer = [nums[i], nums[j]]

    if two_sum > 0:
        j -= 1
    elif two_sum < 0:
        i += 1
    else:
        break

print(' '.join(map(str, answer)))