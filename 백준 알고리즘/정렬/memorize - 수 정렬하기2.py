"""
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다.
이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

"""
import sys
from typing import List

# 정렬하며 병합하기
def mergeTwoLists(left: List[int], right: List[int]) -> List[int]:
    result = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    if len(left) == l:
        result = result + right[r:]
    elif len(right) == r:
        result = result + left[l:]

    return result

# 반으로 나누기
def sortList(A: List[int]) -> List[int]:
    if len(A) == 1:
        return A

    mid = len(A)//2
    left = sortList(A[:mid])
    right = sortList(A[mid:])

    return mergeTwoLists(left, right)


A = [int(sys.stdin.readline()) for i in range(int(sys.stdin.readline()))]

m = sortList(A)
print(*m, sep='\n')