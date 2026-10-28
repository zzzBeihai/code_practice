class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        vis = set()
        ans = 10086

        def dfs(i: int , j: int, xor: int) -> None:
            nonlocal ans
            if ans == 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or (i, j, xor) in vis:
                return
            vis.add((i, j, xor))
            xor ^= grid[i][j]
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                ans = min(ans, xor)
                return
            dfs(i + 1, j, xor)
            dfs(i, j + 1, xor)

        dfs(0, 0, 0)
        return ans
