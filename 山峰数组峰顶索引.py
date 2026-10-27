class Solution:
    def peak_index_in_mountain_array(self, arr: list[int]) -> int:
        for i in range(len(arr)):
            if arr[i] > arr[i - 1]:
                continue
            return i - 1

        return len(arr) - 1
