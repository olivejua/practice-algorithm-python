from typing import List

"""
동서남북으로 탐색하며 섬이 몇개인지 찾아라 (재귀호출 사용) 
"""
class Solution:
    def dfs(self, grid: List[List[str]], i: int, j:int):
        # 더이상 땅이 아닌 경우 종료
        if i < 0 or len(grid) <= i or \
            j < 0 or len(grid[0]) <= j or \
            grid[i][j] != '1':
            return

        grid[i][j] = '0'
        
        # 동서남북 탐색
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)


    def numIslands(self, grid: List[List[str]]) -> int:
        # 예외 처리
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1

        return count