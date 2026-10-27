class Solution:

    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        """
        num_current = set(nums[:k])
        total_sum = sum(num_current)
        judge = True
        if len(num_current) != k:
            judge = False
        for i in range(len(nums)-k):
            if nums[i:i+k].count(nums[i]) == 1:
                num_current.discard(nums[i])

            num_current.add(nums[i+k])

            if len(num_current) == k:
                judge = True
                total = sum(num_current)
                if total > total_sum:
                    total_sum = total
            else:
                judge = False


        if not judge:
                return 0

        return total_sum
        """
        






