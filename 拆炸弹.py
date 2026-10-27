class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        num = len(code) * [0]
        if k  == 0:
            return num

        total = 0

        if k > 0:
            for i in range(k):
                total += code[(i + 1) % len(code)]

            num[0] = total

            for i in range(1, len(code)):
                total -= code[i % len(code)]
                total += code[(i + k) % len(code)]

                num[i] = total

        if k < 0:
            k = k * -1
            for i in range(k):
                total += code[(-i - 1) % len(code)]

            num[0] = total

            for i in range(1, len(code)):
                total -= code[(i - 1 - k) % len(code)]
                total += code[(i - 1) % len(code)]

                num[i] = total

        return num







