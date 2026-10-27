class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = {}
        left = 0
        max_len = 0
        cur_len = 0
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            cur_len += 1
            while freq[s[i]] > 2:
                freq[s[left]] -= 1
                left += 1
                cur_len -= 1

            if cur_len > max_len:
                max_len = cur_len

        return max_len



        