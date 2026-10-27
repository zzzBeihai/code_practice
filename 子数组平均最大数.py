class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_total = total = sum(nums[:k])
        n = len(nums)

        for i in range(k,n):
            total = total - nums[i - k] + nums[i]
            max_total = max(max_total, total)

        return max_total / k

