from typing import List


def solution1(nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 힙 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


def solution3(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])

print(solution1([1, 2, 3, 4]))
print(solution1([6, 2, 6, 5, 1, 2]))
print(solution3([1, 2, 3, 4]))
print(solution3([6, 2, 6, 5, 1, 2]))
