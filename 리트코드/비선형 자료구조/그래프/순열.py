from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_elements = []

        def dfs(elements):
            if not elements:
                result.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                prev_elements.append(e)

                dfs(next_elements)

                prev_elements.pop()

        dfs(nums)
        return result

print(Solution().permute([1,2,3,4,5]))