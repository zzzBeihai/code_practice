class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # 1. 统计总字符数（用total字典，和窗口freq完全分离，避免覆盖）
        total = {}
        for i in range(len(s)):
            total[s[i]] = total.get(s[i], 0) + 1

        a_num = total.get("a", 0)
        b_num = total.get("b", 0)
        c_num = total.get("c", 0)

        # 特判：任意字符总数不足k，直接返回-1
        if a_num < k or b_num < k or c_num < k:
            return -1

        # 2. 滑动窗口：freq只存窗口内计数
        freq = {"a": 0, "b": 0, "c": 0}
        left = 0
        max_len = 0  # 最长保留窗口长度

        for right, x in enumerate(s):
            # 右边界入窗口：x是字符，直接更新freq
            freq[x] = freq.get(x, 0) + 1

            # 核心：窗口外字符不足k → 缩窗口
            # 条件：总a - 窗口a < k 或 总b - 窗口b < k 或 总c - 窗口c < k
            while (total.get("a", 0) - freq.get("a", 0) < k or
                   total.get("b", 0) - freq.get("b", 0) < k or
                   total.get("c", 0) - freq.get("c", 0) < k):
                # 左边界出窗口：用s[left]取字符，更新freq
                left_ch = s[left]
                freq[left_ch] = freq.get(left_ch, 0) - 1
                left += 1

            # 更新最长保留窗口
            max_len = max(max_len, right - left + 1)

        # 最少取走的字符数 = 总长度 - 最长保留窗口
        return len(s) - max_len

        """
        left = 0
        freq = {}
        length = 0
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1

        a_num = freq.get("a", 0)
        b_num = freq.get("b", 0)
        c_num = freq.get("c", 0)

        for right, x in enumerate(s):
            freq[s[x]] = freq.get(x) - 1
            while freq.get("a", 0) < a_num - k and freq.get("b", 0) < b_num - k or freq.get("c", 0) < c_num - k:
                left += 1
                freq[s[left]] = freq.get(left) - 1

            length = (length, right - left + 1)

        return length
        """


