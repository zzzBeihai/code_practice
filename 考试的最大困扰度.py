class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        freq = {}
        left = 0
        cur_len = max_len = 0
        for i in range(len(answerKey)):
            freq[answerKey[i]] = freq.get(answerKey[i], 0) + 1
            cur_len += 1

            while max(freq.values()) + k < cur_len:
                freq[answerKey[i]] -= 1
                freq[answerKey[left]] -= 1
                left += 1
                cur_len -= 1

            max_len = max(max_len, cur_len)

        return max_len
