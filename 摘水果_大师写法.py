from bisect import bisect_left
class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        left = bisect_left(fruits, [startPos - k])  # 向左最远能到 fruits[left][0]
        right = bisect_left(fruits, [startPos + 1])  # 位置 <= startPos 的最大下标 + 1
        ans = s = sum(f[1] for f in fruits[left: right])  # 从 fruits[left][0] 到 startPos 的水果数
        # 枚举最右走到 fruits[right][0]
        while right < len(fruits) and fruits[right][0] <= startPos + k:
            s += fruits[right][1]
            while fruits[right][0] * 2 - fruits[left][0] - startPos > k and \
                  fruits[right][0] - fruits[left][0] * 2 + startPos > k:
                s -= fruits[left][1]  # fruits[left][0] 太远了
                left += 1
            ans = max(ans, s)  # 更新答案最大值
            right += 1  # 继续枚举下一个最右位置
        return ans