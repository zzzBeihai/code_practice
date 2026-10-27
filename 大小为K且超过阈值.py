class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        num = 0
        for i in range(len(arr)-k+1):
            total = sum(arr[i:i+k])
            if total >= k * threshold:
                num += 1

        return num

