from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(index, path, target):
            if target < 0:
                return
            elif target==0:
                result.append(path[:])
                return

            for i in range(index, len(candidates)):
                target -= candidates[i]
                path.append(candidates[i])

                # print(i, path, target)
                dfs(i, path, target)

                target += candidates[i]
                path.pop()

        dfs(0, [], target)
        return result

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(index, path, csum):
            if target < csum:
                return
            elif csum==target:
                result.append(path[:])
                return

            for i in range(index, len(candidates)):
                # print(i, path, target)
                dfs(i, path + [candidates[i]], csum + candidates[i])

        dfs(0, [], 0)
        return result

print(Solution().combinationSum2([2,3,6,7], 7))
print(Solution().combinationSum2([2,3,5], 8))