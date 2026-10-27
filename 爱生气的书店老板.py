class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        """
        nums_pry = sum(customers[: minutes])
        for i in range(len(customers) - minutes + 1):
            left_w = customers[i]
            right_w = customers[i + minutes - 1]
            nums_cur = nums_pry - left_w + right_w

            if nums_cur >= nums_pry:
                nums_pry = nums_cur

        return nums_pry
        """
        ord_sum = 0
        for i in range(len(customers)):
            ord_sum += customers[i] * (grumpy[i] - 1) * -1

        ang_sum = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                ang_sum += customers[i]

        res_sum = ang_sum

        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                ang_sum += customers[i]

            if grumpy[i - minutes] == 1:
                ang_sum -= customers[i - minutes]

            res_sum = max(res_sum, ang_sum)

        return res_sum + ord_sum
