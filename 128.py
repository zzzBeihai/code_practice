class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))
        ans = 1
        i = 0
        n = len(nums)

        while i < n - 1:
            if nums[i + 1] != nums[i] + 1:
                i += 1
                continue

            start = i

            while i < n - 1 and nums[i + 1] == nums[i] + 1:
                i += 1

            ans = max(ans, i - start + 1)

        return ans