"""
문제)
    시간 복잡도가 O(nlogn)인 정렬 알고리즘으로 풀 수 있습니다.
    예를 들면 병합 정렬, 힙 정렬 등이 있지만, 어려운 알고리즘이므로 지금은 언어에 내장된 정렬 함수를 쓰는 것을 추천드립니다.
예제 입력)
    5
    5
    4
    3
    2
    1
예제 출력)
    1
    2
    3
    4
    5

배열로 병합 정렬
"""

def merge(left, right):
    v = list()
    i, j = 0, 0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            v.append(left[i])
            i += 1
        else:
            v.append(right[j])
            j += 1

    if i==len(left):
        v = v + right[j:len(right)]
    if j==len(right):
        v = v + left[i:len(left)]
    return v


def merged_sort(v):
    if len(v) <= 1:
        return v
    mid = len(v) // 2
    left = merged_sort(v[:mid])
    right = merged_sort(v[mid:])
    return merge(left, right)


v = [int(input()) for i in range(int(input()))]

m = merged_sort(v)
print(*m, sep="\n")

print("\n".join(map(str, sorted(v))))