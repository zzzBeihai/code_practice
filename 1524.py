class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        sums = [0] * (len(arr) + 1)
        for i, x in enumerate(arr):
            sums[i + 1] = (sums[i] + x) % 2

        cnt = [0] * 2
        ans = 0
        for s in sums:
            ans += cnt[s ^ 1]
            cnt[s] += 1
        return ans % 1_000_000_007