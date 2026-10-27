class Solution:
    def minOperations(self, nums: list[int]) -> int:
        sorted_unique_nums = sorted(set(nums))
        res = n = len(nums)
        j = 0
        for i, left in enumerate(sorted_unique_nums):
            right = left + n - 1
            while j < len(sorted_unique_nums) and sorted_unique_nums[j] <= right:
                res = min(res, n - (j - i + 1))
                j += 1
        return res