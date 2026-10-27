class Solution:

    """
    def minArrivalsToDiscard(self, arrivals: list[int], w: int, m: int) -> int:

        freq = {}
        for i in range(w):
            freq[arrivals[i]] = freq.get(arrivals[i], 0) + 1
            if freq[arrivals[i]] >= m:
                result = freq[arrivals[i]] - m

        for i in range(len(arrivals) - w):
            freq[arrivals[i]] += freq.get(arrivals[i], 0) - 1
            freq[arrivals[i + m]] += freq.get(arrivals[i + m], 0) + 1
            if freq[arrivals[i]] >= m:
                result = freq[arrivals[i]] - m
    """



