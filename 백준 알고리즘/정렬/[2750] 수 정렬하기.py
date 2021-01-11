# 삽입정렬
import heapq
# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

def solution1():
    n = int(input())

    nums = []
    for _ in range(n):
        nums.append(int(input()))

        i = len(nums)-1
        while 0 < i and nums[i-1] > nums[i]:
            nums[i-1], nums[i] = nums[i], nums[i-1]
            i -= 1

    for num in nums:
        print(num)

# 삽입정렬
def solution2():
    n = int(input())
    nums = []

    for _ in range(n):
        nums.append(int(input()))

    for i in range(1, len(nums)):
        while (0 < i) and (nums[i] < nums[i-1]):
            nums[i], nums[i-1] = nums[i-1], nums[i]
            i -= 1

# 우선순위 큐
def solution3():
    print('solution3')
    n = int(input())
    heap = []

    for _ in range(n):
        heapq.heappush(heap, int(input()))

    for _ in range(n):
        print(heapq.heappop(heap))

# 내장함수
def solution4():
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))

    for num in sorted(nums):
        print(num)

# 파이썬 다운 방식
print(*sorted(map(int, [*open(0)][1:])))