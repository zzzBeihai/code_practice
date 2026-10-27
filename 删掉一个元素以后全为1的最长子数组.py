class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        freq = {}
        left = 0
        max_len = 0
        cur_len = 0
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            cur_len += 1
            while freq.get(0, 0) == 2:
                freq[nums[left]] = freq.get(nums[left]) - 1
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len

        return max_len - 1




