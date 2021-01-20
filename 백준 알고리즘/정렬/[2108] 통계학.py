n = '2143'
nums = list(map(int, n))

i = 1
while i < len(nums):
    j = i
    while 0 < j and nums[j-1] < nums[j]:
        nums[j], nums[j-1] = nums[j-1], nums[j]
        j -= 1
    i += 1

print(nums)