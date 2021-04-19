from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(elements, index, k):
            if k == 0:
                result.append(elements[:])
                return

            for i in range(index, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()

        dfs([], 1, k)
        return result

print(Solution().combine(5,3))