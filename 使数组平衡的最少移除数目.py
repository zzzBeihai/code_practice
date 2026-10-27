class Solution:
    def minRemoval(self, nums: list[int], k: int) -> int:
        nums.sort()
        max_save = 0
        left = 0
        for i, mx in enumerate(nums):
            while nums[left] * k < mx:
                left += 1
            max_save = max(max_save, i - left + 1)

        return len(nums) - max_save