class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        freq = {}
        left = 0
        cur_len = max_len = 0
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            cur_len += 1

            while freq[nums[i]] > k:
                freq[nums[left]] -= 1
                left += 1
                cur_len -= 1

            max_len = max(max_len, cur_len)

        return max_len
