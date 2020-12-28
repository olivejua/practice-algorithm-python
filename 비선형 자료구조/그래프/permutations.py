import itertools
from typing import List


"""
주어진 숫자 조합의 모든 경우의 수를 
"""
class Solution:
    def permute_s1(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                results.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)

                prev_elements.pop()


        dfs(nums)
        return results

    def permute_s2(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, itertools.permutations(nums)))