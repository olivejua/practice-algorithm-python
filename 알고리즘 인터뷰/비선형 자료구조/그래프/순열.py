from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(path: List[int], rest: List[int]):
            if len(rest) <= 1:
                result.append(path+rest)
                return

            for n in rest:
                copy = rest[:]
                copy.remove(n)
                path.append(n)
                dfs(path, copy)
                path.remove(n)

        dfs([], nums)
        return result

    def permute2(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
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