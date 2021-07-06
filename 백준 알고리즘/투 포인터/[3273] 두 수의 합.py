import sys

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()
answer = 0

i, j = 0, (n-1)
while i < j:
    if nums[i]+nums[j] < x:
        i += 1
    elif nums[i]+nums[j] > x:
        j -= 1
    else:
        answer += 1
        i += 1
        j -= 1

print(answer)