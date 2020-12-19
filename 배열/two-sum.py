from typing import List

# 브루트 포스 방식 O(n**2)
def solution1(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


print(solution1([2, 7, 11, 15], 9))


# in을 이용한 탐색 O(1)
def solution2(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i+1:]:
            return nums.index(n), nums[i+1:].index(complement) + (i+1)


print(solution2([2, 7, 11, 15], 9))


# 첫 번째 수를 뺀 결과 키 조회
def solution3(nums: List[int], target: int) -> List[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target-num in nums_map and i != nums_map[target-num]:
            return nums.index(num), nums_map[target-num]

print(solution3([2, 7, 11, 15], 9))


# 조회 구조 개선
def solution4(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    # 하나의 for 문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num], i]
        nums_map[num] = i

print(solution4([2, 7, 11, 15], 9))
