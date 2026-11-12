class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        left, right = 0, 1
        ans = 1

        while right < len(nums):
            # 相等元素不构成严格单调
            if nums[left] == nums[right]:
                left = right
                right += 1
                continue

            # 当前窗口可以继续递增或递减
            if right + 1 < len(nums) and (
                nums[left] < nums[right] < nums[right + 1]
                or
                nums[left] > nums[right] > nums[right + 1]
            ):
                right += 1
            else:
                # 当前窗口仍然有效，先更新答案
                ans = max(ans, right - left + 1)

                # 从当前元素开始新的窗口
                left = right
                right += 1

        return ans