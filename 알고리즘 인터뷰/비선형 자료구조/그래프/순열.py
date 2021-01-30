from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, path):
            if index == len(path)-1:
                result.append(path)
                return

            for i in range(len(nums)):
                for j in nums[i]:
                    dfs(i+1, path+j)

        if not nums:
            return []

        result = []
        return result

print(Solution().permute([1,2,3]))