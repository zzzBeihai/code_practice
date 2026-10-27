class Solution:
    def maxSum(self, nums: list[int], m: int, k: int) -> int:
        max_sum = 0
        current_sum = 0
        freq = {}

        for i in range(k):
            num = nums[i]
            current_sum += num
            freq[num] = freq.get(num, 0) + 1

        if len(freq) >= m:
            max_sum = current_sum

        for i in range(len(nums)-k):
            left_num = nums[i]
            current_sum -= left_num
            freq[left_num] = freq.get(left_num, 0) - 1
            if freq[left_num] == 0:
                del freq[left_num]

            right_num = nums[i+k]
            current_sum += right_num
            freq[right_num] = freq.get(right_num, 0) + 1

            if current_sum > max_sum and len(freq) >= m:
                max_sum = current_sum

        return max_sum





