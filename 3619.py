class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> int:
            res = grid[i][j]
            grid[i][j] = 0  # 标记 (i,j) 访问过
            for x, y in (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    res += dfs(x, y)
            return res

        ans = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x and dfs(i, j) % k == 0:
                    ans += 1
        return ans
