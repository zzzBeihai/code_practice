from math import gcd,lcm
class Solution:
    def maxLength(self, nums: list[int]) -> int:
        max_m = lcm(*nums) * max(nums)
        ans = 0
        for i in range(len(nums)):
            m, l, g = 1, 1, 0
            for j in range(i, len(nums)):
                x = nums[j]
                m *= x
                l = lcm(l, x)
                g = gcd(g, x)
                if m == l * g:
                    ans = max(ans, j - i + 1)
                if m > max_m:
                    break
        return ans