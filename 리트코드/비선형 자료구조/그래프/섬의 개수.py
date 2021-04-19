from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row: int, col: int):
            if row < 0 or row == len(grid) or \
                    col < 0 or col == len(grid[0]) or \
                    grid[row][col] != '1':
                return

            grid[row][col] = '0'

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        number = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    number += 1
                    print(grid)

        return number


class Solution_mine:
    def numIslands(self, grid: List[List[str]]) -> int:
        number = 0

        def dfs(row: int, col: int):
            if grid[row][col] == "0":
                return

            grid[row][col] = "0"

            if 0 < row:  # left
                dfs(row - 1, col)
            if row < len(grid) - 1:  # right
                dfs(row + 1, col)
            if 0 < col:  # up
                dfs(row, col - 1)
            if col < len(grid[row]) - 1:  # down
                dfs(row, col + 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    number += 1
                    dfs(i, j)
                    print(grid)

        return number


# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]

# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]

grid = [["1","1","1"],["0","1","0"],["1","1","1"]]

print(Solution.numIslands(None, grid))