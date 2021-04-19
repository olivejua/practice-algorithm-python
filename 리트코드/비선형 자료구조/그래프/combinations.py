import itertools
from typing import List


"""
조합의 수
"""
class Solution:
    def combine_s1(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k==0:
                results.append(elements[:])

            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()


        dfs([], 1, k)
        return results

    def combine_s2(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n+1), k))