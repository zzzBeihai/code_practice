class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        res1 = cost1 * need1 + cost2 * need2
        if need1 > need2:
            need1, need2 = need2, need1
            cost2 = cost1
        res2 = costBoth * need2
        res3 = costBoth * need1 + cost2 * (need2 - need1)
        return min(res1, res2, res3)