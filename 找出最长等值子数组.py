class Solution:
    def longestEqualSubarray(self, nums: list[int], k: int) -> int:
        left = 0
        freq = {}
        max_freq = 0
        for right, x in enumerate(nums):
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            max_freq = max(max_freq, freq[nums[right]])
            while  (right - left +1) - max_freq > k :
                freq[nums[left]] = freq.get(nums[left], 0) - 1
                left += 1
        return  max_freq