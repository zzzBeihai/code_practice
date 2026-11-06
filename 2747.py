class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key = lambda item: item[1])
        order = sorted(range(len(queries)), key = lambda i: queries[i])

        freq = [0] * (n + 1)
        ans = [0] * len(queries)

        active = left = right = 0
        m = len(logs)

        for query_index in order:
            q = queries[query_index]

            while right < m and logs[right][1] <= q:
                server_id = logs[right][0]

                if freq[server_id] == 0:
                    active += 1

                freq[server_id] += 1
                right += 1

            while left < right and logs[left][1] < q - x:
                server_id = logs[left][0]

                freq[server_id] -= 1

                if freq[server_id] == 0:
                    active -= 1

                left += 1

            ans[query_index] = n - active

        return ans