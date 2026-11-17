class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))  # 把 s 排序，作为 dict 的 key
            if sorted_s not in d:  # 首次遇到 sorted_s
                d[sorted_s] = []  # 创建列表
            d[sorted_s].append(s)  # 排序后相同的字符串，保存到同一组中
        return list(d.values())  # 哈希表的所有 value 就是分组结果