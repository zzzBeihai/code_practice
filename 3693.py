from functools import cache
class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(i: int) -> int:
            if i == 0:
                return 0
            # costs[i-1] 与 j 无关，可以提到循环外面
            return min(dfs(j) + (i - j) * (i - j) for j in range(max(i - 3, 0), i)) + costs[i - 1]
        return dfs(n)