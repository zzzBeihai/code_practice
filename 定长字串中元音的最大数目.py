class Solution:
    def max_vowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_num = 0
        for i in range(len(s) - k + 1):
            cur_num = 0
            new_s = s[i:i + k]
            for h in new_s:
                if h in vowels:
                    cur_num += 1
            if cur_num > max_num:
                max_num = cur_num
        return max_num

# 复杂度高，大数组超时
