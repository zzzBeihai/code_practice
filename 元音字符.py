class Solution:
    def voweStrings (self, words: list[str], left: int, right: int) -> int:
        vowels = set("aeiou")
        ans = 0
        for i in range(left, right + 1):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                ans += 1
        return ans

solution = Solution()
test_words = ["apple", "banana", "orange", "umbrella", "echo", "test"]
left_idx = 1
right_idx = 4

result = solution.voweStrings(test_words, left_idx, right_idx)
print(f"qualified words: {result}")