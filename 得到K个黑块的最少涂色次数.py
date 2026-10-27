class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        num_b = blocks[: k].count("B")
        c_result = result = k-num_b
        if num_b == k:
            result = 0
        for i in range(len(blocks)-k+1):
            if blocks[i] == "W":
                result -= 1
            if blocks[i+k] == "W":
                result += 1

            if c_result >= result:
                c_result = result

        return c_result








