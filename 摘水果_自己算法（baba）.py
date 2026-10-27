class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        left = 0
        right = k
        total = 0
        pos = []
        for i in range(len(fruits)):
            pos.append(fruits[i][0])  # 存所有水果坐标

        # 第一次初始化 total
        for i in range(len(fruits)):
            if startPos + right > fruits[-1][0]:
                right = fruits[-1][0] - startPos
            if startPos - left <= fruits[i][0] <= startPos + right:
                total += fruits[i][1]

        ans = total

        for i in range(k):
            # 移除右边：必须用 pos.index() 找下标！
            if startPos + right in pos:
                idx = pos.index(startPos + right)
                total -= fruits[idx][1]

            left += 1
            right = k - 2 * left

            if right + startPos > fruits[-1][0]:
                right = fruits[-1][0] - startPos
            if right < 0:  # 防止负数越界
                right = 0
            if right < left:
                left = k - 2 * right
                if left < 0:
                    left = 0

            # 加入左边：必须用 pos.index() 找下标！
            if startPos - left in pos:
                idx = pos.index(startPos - left)
                total += fruits[idx][1]
                if startPos - left == 0:
                    break

            ans = max(total, ans)

        return ans

        """
        left = 0
        right = k
        total = 0
        pos = []
        for i in range (len(fruits)):
            pos.append(fruits[i][0])
            if startPos + right > fruits[-1][0]:
                right = fruits[-1][0] - startPos
            if startPos - left <= fruits[i][0] <= startPos + right:
                total += fruits[i][1]
        ans = total
        for i in range (k):
            if startPos + right in pos:
                total -= fruits[startPos + right][1]
            left += 1
            right = k - 2 * left
            if right + startPos > fruits[-1][0]:
                right = fruits[-1][0] - startPos
            if right < left:
                left = k - 2 * right
            if startPos - left in pos:
                total += fruits[startPos - left][1]
                if startPos - left == 0:
                    break
            ans = max(total, ans)
        return ans
        """