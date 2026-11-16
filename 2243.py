class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            t = []
            for i in range(0, len(s), k):
                total = sum(map(int, s[i: i + k]))
                t.append(str(total))
            s = ''.join(t)
        return s