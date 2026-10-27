class Solution:
    def maximizeWin(self, prizePositions: list[int], k: int) -> int:
        """prizePositions.sort(reverse=True)
        right = len(prizePositions)
        if 2 * k + 1 > len(prizePositions):
            total = (sum(prizePositions[0: k]) + sum(prizePositions[right - k: right])
                     - sum(prizePositions[right - k: k]))
        else:
            total = sum(prizePositions[0:2 * k + 1])
        return total"""

