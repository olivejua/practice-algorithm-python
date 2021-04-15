import collections


def solution(clothes):

    answer = 1

    count = collections.Counter(kind for name, kind in clothes)

    for i in count.values():
        answer *= (i + 1)

    return answer - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
