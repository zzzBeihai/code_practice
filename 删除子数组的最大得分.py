from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        prefix = [0] * (len(nums) + 1)
        # 计算某下标前的所有数字和并存储
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]

            last_pos = defaultdict(int)
            # 这个字典里调用时如果没这个元素也不报错，会返回0
            left = 0
            max_sum = 0

        for right, num in enumerate(nums):
            if num in last_pos:
                left = max(left, last_pos[num] + 1)

            last_pos[num] = right
            current_sum = prefix[right + 1] - prefix[left]
            max_sum = max(max_sum, current_sum)

        return max_sum







