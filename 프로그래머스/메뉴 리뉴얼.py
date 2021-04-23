import collections
import itertools
from typing import List

'''
answer 변수 생성
[course 반복문]
[combination 메서드 따로 작성]
Counter 해서 가장 많이 나온 것을 answer에 추가 
'''
def solution(orders: List, course: List):
    answer = []


    for course_size in course:
        dict = collections.defaultdict(int)
        for order in orders:
            # combinations = list(itertools.combinations(sorted(order), c))
            combinations = getCombination(course_size, sorted(order))
            for combi in combinations:
                dict[''.join(combi)] += 1

        answer += list(filter(lambda x: dict[x]==max(dict.values()) and dict[x] > 1, dict))

    return sorted(answer)

def getCombination(course_size, order):
    result = []

    def dfs(elements: List, start, k):
        if k==0:
            result.append(elements[:])

        for i in range(start, len(order)):
            elements.append(order[i])
            dfs(elements, i+1, k-1)
            elements.pop()

    dfs([], 0, course_size)
    return result

print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
# print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
