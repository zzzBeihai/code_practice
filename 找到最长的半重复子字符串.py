class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        freq = []
        mid = 0
        left = 0
        right = 0
        max_len = cur_len = 0
        i = 0
        for right in range (1, len(s)):
            cur_len += 1
            if s[right] == s[right-1]:
                i += 1
                mid = right - 1
                freq.append(mid)
            if i > 2:
                left = freq[0]
                left += 1
                i -= 1
                del freq[0]
                cur_len = right - left + 1

            max_len = max(max_len, cur_len)

        return max_len